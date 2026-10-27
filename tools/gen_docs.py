#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Generate static Markdown documentation for dota-data and TypeScriptDeclarations.

Usage:
    uv run tools/gen_docs.py
    uv run tools/gen_docs.py --out docs --root .
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = ROOT
DEFAULT_OUT = ROOT / "docs"


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------


def fence(text: str, language: str = "") -> str:
    text = text.strip("\n")
    marker = "```"
    if marker in text:
        marker = "~~~"
    return f"{marker}{language}\n{text}\n{marker}"


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def cell(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("|", "\\|")
    text = text.replace("\n", "<br>")
    return text.strip()


def code(value: Any) -> str:
    text = normalize_ws("" if value is None else str(value))
    if "`" in text:
        return f"`` {text} ``"
    return f"`{text}`"


def code_cell(value: Any) -> str:
    return code(str(value))


def table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        escaped_row = []
        for value in row:
            text = "" if value is None else str(value)
            text = text.replace("\r\n", "\n").replace("\r", "\n")
            text = text.replace("\n", "<br>")
            # Escape all pipes for table compatibility
            text = text.replace("|", "\\|")
            escaped_row.append(text.strip())
        lines.append("| " + " | ".join(escaped_row) + " |")
    return "\n".join(lines)


def slug(text: str) -> str:
    value = text.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "-", value)
    return value


def toc(title: str, names: list[str]) -> str:
    if len(names) < 2:
        return ""
    lines = [f"<details><summary>{title}</summary>", ""]
    for name in names:
        lines.append(f"- [{name}](#{slug(name)})")
    lines += ["", "</details>", ""]
    return "\n".join(lines)


def contents(*sections: str) -> list[str]:
    body = [section.rstrip() for section in sections if section]
    if not body:
        return []
    return ["## Contents", "", *body, ""]


def generated_note(source: str) -> str:
    return ""


def page(title: str, source: str, intro: str = "") -> str:
    parts = [f"# {title}", "", generated_note(source), ""]
    if intro:
        parts += [intro, ""]
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# JSDoc parsing / rendering
# ---------------------------------------------------------------------------


def parse_jsdoc(comment: str | None) -> dict[str, Any]:
    if not comment:
        return {"description": "", "tags": []}

    content = comment.strip()
    if content.startswith("/**"):
        content = content[2:]
    if content.endswith("*/"):
        content = content[:-2]

    description: list[str] = []
    tags: list[dict[str, str]] = []
    for raw_line in content.splitlines():
        line = re.sub(r"^\s*\*\s?", "", raw_line)
        match = re.match(r"@(\w+)\s*(.*)", line)
        if match:
            tags.append({"name": match.group(1), "text": match.group(2)})
        elif tags:
            tags[-1]["text"] += "\n" + line
        else:
            description.append(line)

    for tag in tags:
        tag["text"] = tag["text"].strip("\n")

    return {"description": "\n".join(description).strip(), "tags": tags}


def render_jsdoc(jsdoc: dict[str, Any], compact: bool = False) -> str:
    parts: list[str] = []
    description = jsdoc.get("description", "").strip()
    if description:
        parts.append(description)

    tags: list[dict[str, str]] = jsdoc.get("tags", [])
    availability = [
        tag["name"] for tag in tags if tag["name"] in ("both", "client", "server")
    ]
    if availability:
        parts.append(
            "**Availability:** " + ", ".join(f"`{value}`" for value in availability)
        )

    for tag in tags:
        if tag["name"] == "deprecated":
            parts.append("**Deprecated:** " + (tag["text"] or "Yes"))
        elif tag["name"] == "compileMembersOnly":
            parts.append(
                "**Compile members only:** values are inlined at compile time."
            )

    parameters = [
        tag
        for tag in tags
        if tag["name"] in ("param", "arg", "argument", "property", "prop")
    ]
    if parameters:
        parts.append("**Parameters:**")
        parts.extend(f"- {tag['text']}" for tag in parameters)

    returns = [tag for tag in tags if tag["name"] in ("returns", "return")]
    if returns:
        parts.append("**Returns:** " + "; ".join(tag["text"] for tag in returns))

    templates = [tag for tag in tags if tag["name"] == "template"]
    if templates:
        parts.append("**Type parameters:**")
        parts.extend(f"- {tag['text']}" for tag in templates)

    defaults = [tag for tag in tags if tag["name"] == "default"]
    if defaults:
        parts.append("**Default:** " + "; ".join(tag["text"] for tag in defaults))

    handled = {
        "both",
        "client",
        "server",
        "deprecated",
        "compileMembersOnly",
        "param",
        "arg",
        "argument",
        "property",
        "prop",
        "returns",
        "return",
        "template",
        "default",
        "example",
        "noSelfInFile",
        "noSelf",
    }
    for tag in tags:
        if tag["name"] in handled:
            continue
        label = (
            re.sub(r"(?<!^)(?=[A-Z])", " ", tag["name"]).replace("_", " ").capitalize()
        )
        if tag["text"]:
            parts.append(f"**{label}:** {tag['text']}")
        else:
            parts.append(f"**{label}**")

    for tag in tags:
        if tag["name"] == "example" and tag["text"].strip():
            example = tag["text"].strip("\n")
            parts.append("**Example:**")
            if compact:
                parts.append(
                    "<br>".join(
                        code(line) for line in example.splitlines() if line.strip()
                    )
                )
            else:
                parts.append(fence(example, "ts"))

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Lightweight TypeScript declaration parser
# ---------------------------------------------------------------------------


DECL_RE = re.compile(
    r"(?P<prefix>(?:(?:export|declare|abstract|const)\s+)*)"
    r"(?P<kind>interface|class|enum|namespace|type|function|const|let|var)\s+"
    r"(?P<name>[A-Za-z_$][\w$]*)"
)

AGGREGATE_KINDS = {"interface", "class", "enum", "namespace"}


def _scan_end(
    text: str, start: int, aggregate: bool
) -> tuple[int, int | None, int | None]:
    """Return (end, body_start, body_end) for a declaration starting at start."""
    i = start
    n = len(text)
    depth = 0
    state: str | None = None

    while i < n:
        char = text[i]
        if state == "line":
            if char == "\n":
                state = None
        elif state == "block":
            if text.startswith("*/", i):
                state = None
                i += 1
        elif state in ("'", '"', "`"):
            if char == "\\":
                i += 1
            elif char == state:
                state = None
        else:
            if text.startswith("//", i):
                state = "line"
                i += 1
            elif text.startswith("/*", i):
                state = "block"
                i += 1
            elif char in ("'", '"', "`"):
                state = char
            elif char in "([":
                depth += 1
            elif char in ")]":
                depth -= 1
            elif char == "{":
                if aggregate and depth == 0:
                    body_start = i
                    body_end = _find_matching_brace(text, i)
                    if body_end == -1:
                        return n - 1, body_start, None
                    return body_end, body_start, body_end
                depth += 1
            elif char == "}":
                depth -= 1
            elif char == ";" and depth == 0:
                return i, None, None
        i += 1

    return n - 1, None, None


def _find_matching_brace(text: str, open_index: int) -> int:
    i = open_index
    n = len(text)
    depth = 0
    state: str | None = None
    while i < n:
        char = text[i]
        if state == "line":
            if char == "\n":
                state = None
        elif state == "block":
            if text.startswith("*/", i):
                state = None
                i += 1
        elif state in ("'", '"', "`"):
            if char == "\\":
                i += 1
            elif char == state:
                state = None
        else:
            if text.startswith("//", i):
                state = "line"
                i += 1
            elif text.startswith("/*", i):
                state = "block"
                i += 1
            elif char in ("'", '"', "`"):
                state = char
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1


def _split_statements(body: str, delimiter: str = ";") -> list[str]:
    statements: list[str] = []
    buffer: list[str] = []
    i = 0
    n = len(body)
    depth = 0
    state: str | None = None

    while i < n:
        char = body[i]
        if state == "line":
            buffer.append(char)
            if char == "\n":
                state = None
        elif state == "block":
            buffer.append(char)
            if body.startswith("*/", i):
                buffer.append("/")
                i += 1
                state = None
        elif state in ("'", '"', "`"):
            buffer.append(char)
            if char == "\\":
                if i + 1 < n:
                    buffer.append(body[i + 1])
                    i += 1
            elif char == state:
                state = None
        else:
            if body.startswith("//", i):
                state = "line"
                buffer.append("//")
                i += 1
            elif body.startswith("/*", i):
                state = "block"
                buffer.append("/*")
                i += 1
            elif char in ("'", '"', "`"):
                state = char
                buffer.append(char)
            elif char in "([{":
                depth += 1
                buffer.append(char)
            elif char in ")]}":
                depth -= 1
                buffer.append(char)
            elif char == delimiter and depth == 0:
                statements.append("".join(buffer))
                buffer = []
            else:
                buffer.append(char)
        i += 1

    if "".join(buffer).strip():
        statements.append("".join(buffer))
    return statements


LEADING_COMMENTS_RE = re.compile(
    r"^\s*((?:(?:/\*.*?\*/)|(?://[^\n]*(?:\n|$)))*)\s*(.*)$",
    re.S,
)


def _strip_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//[^\n]*", "", text)
    return text


def parse_members(body: str | None) -> list[dict[str, Any]]:
    if not body:
        return []

    members: list[dict[str, Any]] = []
    for statement in _split_statements(body):
        match = LEADING_COMMENTS_RE.match(statement)
        if not match:
            continue
        comments, content = match.group(1), match.group(2).strip()
        if not content:
            continue

        jsdoc_comment = None
        block_match = re.search(r"/\*\*.*?\*/", comments, re.S)
        if block_match:
            jsdoc_comment = block_match.group(0)
        jsdoc = parse_jsdoc(jsdoc_comment)
        if not jsdoc["description"] and not jsdoc["tags"]:
            line_comments = [
                re.sub(r"^//\s?", "", line).strip()
                for line in comments.splitlines()
                if line.strip().startswith("//")
            ]
            line_comments = [line for line in line_comments if line]
            if line_comments:
                jsdoc["description"] = "\n".join(line_comments)

        content = _strip_comments(content).strip()
        if content.endswith(";"):
            content = content[:-1].rstrip()
        if not content:
            continue

        content_one_line = normalize_ws(content)
        property_match = re.match(
            r"^(?:readonly\s+)?([A-Za-z_$][\w$]*)\s*(\?)?\s*:\s*(.+)$",
            content_one_line,
            re.S,
        )
        if property_match and "(" not in content_one_line.split(":", 1)[0]:
            members.append(
                {
                    "kind": "property",
                    "name": property_match.group(1),
                    "optional": bool(property_match.group(2)),
                    "type": property_match.group(3).strip(),
                    "signature": content_one_line,
                    "jsdoc": jsdoc,
                }
            )
            continue

        method_match = re.match(
            r"^(?:readonly\s+)?(?:get\s+|set\s+)?([A-Za-z_$][\w$]*)"
            r"\s*(?:<.*?>)?\s*\(",
            content_one_line,
            re.S,
        )
        if method_match:
            members.append(
                {
                    "kind": "method",
                    "name": method_match.group(1),
                    "signature": content_one_line,
                    "jsdoc": jsdoc,
                }
            )
            continue

        members.append(
            {
                "kind": "other",
                "name": content_one_line.split(":", 1)[0][:80],
                "signature": content_one_line,
                "jsdoc": jsdoc,
            }
        )

    return members


def parse_enum_members(body: str | None) -> list[dict[str, str]]:
    if not body:
        return []

    members: list[dict[str, str]] = []
    for item in _split_statements(body, ","):
        match = LEADING_COMMENTS_RE.match(item)
        if not match:
            continue
        content = _strip_comments(match.group(2)).strip()
        if not content:
            continue
        content = content.strip(",").strip()
        member_match = re.match(r"([A-Za-z_$][\w$]*)\s*(?:=\s*(.*))?$", content, re.S)
        if not member_match:
            continue
        members.append(
            {
                "name": member_match.group(1),
                "value": (member_match.group(2) or "").strip(),
            }
        )
    return members


def scan_declarations(text: str) -> list[dict[str, Any]]:
    declarations: list[dict[str, Any]] = []
    position = 0
    n = len(text)
    pending_jsdoc: dict[str, Any] = {"description": "", "tags": []}

    while position < n:
        if text[position].isspace():
            position += 1
            continue

        if text.startswith("///", position):
            newline = text.find("\n", position)
            position = n if newline == -1 else newline + 1
            continue

        if text.startswith("//", position):
            newline = text.find("\n", position)
            position = n if newline == -1 else newline + 1
            continue

        if text.startswith("/*", position):
            end = text.find("*/", position + 2)
            if end == -1:
                break
            comment = text[position : end + 2]
            if comment.startswith("/**"):
                pending_jsdoc = parse_jsdoc(comment)
            position = end + 2
            continue

        match = DECL_RE.match(text, position)
        if not match:
            newline = text.find("\n", position)
            position = n if newline == -1 else newline + 1
            pending_jsdoc = {"description": "", "tags": []}
            continue

        kind = match.group("kind")
        name = match.group("name")
        end, body_start, body_end = _scan_end(text, position, kind in AGGREGATE_KINDS)
        if end < position:
            end = position

        if body_start is not None and body_end is not None:
            header = text[position:body_start].strip()
            body = text[body_start + 1 : body_end]
        else:
            header = text[position : end + 1].strip()
            if header.endswith(";"):
                header = header[:-1].rstrip()
            body = None

        declaration: dict[str, Any] = {
            "kind": kind,
            "name": name,
            "header": header,
            "text": text[position : end + 1].strip(),
            "body": body,
            "jsdoc": pending_jsdoc,
            "members": [],
            "extends": [],
        }

        if kind in ("interface", "class"):
            declaration["members"] = parse_members(body)
            extends_match = re.search(r"\bextends\s+([^{]+)", header)
            if extends_match:
                declaration["extends"] = [
                    part.strip()
                    for part in extends_match.group(1).split(",")
                    if part.strip()
                ]
        elif kind == "enum":
            declaration["members"] = parse_enum_members(body)
        elif kind == "namespace":
            declaration["body"] = body
        elif kind in ("const", "let", "var"):
            const_match = re.match(
                r".*?\b(?:const|let|var)\s+[A-Za-z_$][\w$]*\s*:\s*(.*)$",
                header,
                re.S,
            )
            declaration["type"] = const_match.group(1).strip() if const_match else ""
        elif kind == "type":
            type_match = re.match(
                r".*?\btype\s+[A-Za-z_$][\w$]*\s*=\s*(.*)$",
                header,
                re.S,
            )
            declaration["rhs"] = type_match.group(1).strip() if type_match else ""

        declarations.append(declaration)
        pending_jsdoc = {"description": "", "tags": []}
        position = end + 1

    return declarations


def merge_duplicate_interfaces(
    declarations: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    by_key: dict[tuple[str, str], dict[str, Any]] = {}

    for declaration in declarations:
        key = (declaration["kind"], declaration["name"])
        if declaration["kind"] in ("interface", "class") and key in by_key:
            existing = by_key[key]
            existing["members"].extend(declaration["members"])
            if not existing["jsdoc"].get("description") and declaration["jsdoc"].get(
                "description"
            ):
                existing["jsdoc"] = declaration["jsdoc"]
            continue
        if declaration["kind"] == "namespace" and key in by_key:
            existing = by_key[key]
            body = "\n".join(
                part.strip("\n")
                for part in (existing.get("body"), declaration.get("body"))
                if part
            )
            existing["body"] = body
            existing["text"] = f"declare namespace {existing['name']} {{\n{body}\n}}"
            continue
        by_key[key] = declaration
        merged.append(declaration)

    return merged


# ---------------------------------------------------------------------------
# Rendering declarations
# ---------------------------------------------------------------------------


def render_function(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    lines += [fence(declaration["text"], "ts"), ""]
    jsdoc = render_jsdoc(declaration["jsdoc"])
    if jsdoc:
        lines += [jsdoc, ""]
    return "\n".join(lines)


def render_type_alias(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    lines += [fence(declaration["text"], "ts"), ""]
    jsdoc = render_jsdoc(declaration["jsdoc"])
    if jsdoc:
        lines += [jsdoc, ""]
    return "\n".join(lines)


def render_enum(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    jsdoc = render_jsdoc(declaration["jsdoc"])
    if jsdoc:
        lines += [jsdoc, ""]
    if declaration["members"]:
        rows = [
            [code_cell(member["name"]), code_cell(member["value"])]
            for member in declaration["members"]
        ]
        lines += [table(["Member", "Value"], rows), ""]
    else:
        lines += ["_No members._", ""]
    return "\n".join(lines)


def render_namespace(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    jsdoc = render_jsdoc(declaration["jsdoc"])
    if jsdoc:
        lines += [jsdoc, ""]
    lines += [fence(declaration["text"], "ts"), ""]
    return "\n".join(lines)


def render_interface(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    meta: list[str] = []
    if declaration["extends"]:
        meta.append(
            "Extends " + ", ".join(f"`{value}`" for value in declaration["extends"])
        )
    if meta:
        lines += [" · ".join(meta), ""]

    jsdoc = render_jsdoc(declaration["jsdoc"])
    if jsdoc:
        lines += [jsdoc, ""]

    members = [
        member for member in declaration["members"] if member["name"] != "__kind__"
    ]
    properties = [member for member in members if member["kind"] == "property"]
    methods = [member for member in members if member["kind"] == "method"]
    others = [member for member in members if member["kind"] == "other"]

    if properties:
        rows = []
        for member in properties:
            label = member["name"] + ("?" if member.get("optional") else "")
            rows.append(
                [
                    code_cell(label),
                    code_cell(member["type"]),
                    cell(render_jsdoc(member["jsdoc"], compact=True)),
                ]
            )
        lines += [
            "**Properties**",
            "",
            table(["Property", "Type", "Description"], rows),
            "",
        ]

    if methods:
        rows = []
        for member in methods:
            rows.append(
                [
                    code_cell(member["signature"]),
                    cell(render_jsdoc(member["jsdoc"], compact=True)),
                ]
            )
        lines += ["**Methods**", "", table(["Method", "Description"], rows), ""]

    if others:
        rows = [
            [
                code_cell(member["signature"]),
                cell(render_jsdoc(member["jsdoc"], compact=True)),
            ]
            for member in others
        ]
        lines += ["**Other members**", "", table(["Member", "Description"], rows), ""]

    if not members:
        lines += ["_No members._", ""]

    return "\n".join(lines)


def render_constants(declarations: list[dict[str, Any]]) -> str:
    if not declarations:
        return ""
    rows = []
    for declaration in declarations:
        rows.append(
            [
                code_cell(declaration["name"]),
                code_cell(declaration.get("type", "")),
                cell(render_jsdoc(declaration["jsdoc"], compact=True)),
            ]
        )
    return table(["Name", "Type / value", "Description"], rows)


# ---------------------------------------------------------------------------
# Data dump renderers
# ---------------------------------------------------------------------------


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def types_text(types: Any) -> str:
    if types is None:
        return ""
    if isinstance(types, str):
        return types
    return " | ".join(str(value) for value in types)


def args_text(args: Any) -> str:
    parts = []
    for argument in args or []:
        name = argument.get("name", "arg")
        types = argument.get("types", argument.get("type"))
        parts.append(f"{name}: {types_text(types)}")
    return ", ".join(parts)


def vscript_signature(function: dict[str, Any]) -> str:
    returns = function.get("returns") or []
    return_types = (
        ", ".join(str(value) for value in returns)
        if isinstance(returns, list)
        else str(returns)
    )
    return f"{function['name']}({args_text(function.get('args'))}): {return_types or 'nil'}"


def render_vscript_function(function: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {function['name']}", ""]
    lines += [code(vscript_signature(function)), ""]
    meta = []
    if function.get("available"):
        meta.append(f"Availability: `{function['available']}`")
    if function.get("deprecated"):
        meta.append(f"**Deprecated:** {function['deprecated']}")
    if meta:
        lines += [" · ".join(meta), ""]
    if function.get("description"):
        lines += [function["description"], ""]
    return "\n".join(lines)


def render_vscript_class(declaration: dict[str, Any], level: int = 3) -> str:
    lines = [f"{'#' * level} {declaration['name']}", ""]
    meta = []
    if (
        declaration.get("clientName")
        and declaration["clientName"] != declaration["name"]
    ):
        meta.append(f"Client name: `{declaration['clientName']}`")
    if declaration.get("extend"):
        meta.append(f"Extends `{declaration['extend']}`")
    if declaration.get("available"):
        meta.append(f"Availability: `{declaration['available']}`")
    if meta:
        lines += [" · ".join(meta), ""]
    if declaration.get("description"):
        lines += [declaration["description"], ""]

    members = declaration.get("members", [])
    fields = [member for member in members if member.get("kind") == "field"]
    functions = [member for member in members if member.get("kind") == "function"]

    if fields:
        rows = [
            [
                code_cell(field["name"]),
                code_cell(types_text(field.get("types"))),
                cell(field.get("description", "")),
            ]
            for field in fields
        ]
        lines += ["**Fields**", "", table(["Field", "Type", "Description"], rows), ""]

    if functions:
        rows = []
        for function in functions:
            description = function.get("description", "")
            if function.get("deprecated"):
                description = (
                    f"**Deprecated:** {function['deprecated']}\n\n{description}".strip()
                )
            rows.append(
                [
                    code_cell(vscript_signature(function)),
                    cell(function.get("available", "")),
                    cell(description),
                ]
            )
        lines += [
            "**Methods**",
            "",
            table(["Method", "Available", "Description"], rows),
            "",
        ]

    if not members:
        lines += ["_No members._", ""]

    return "\n".join(lines)


def generate_vscripts_api(out: Path) -> None:
    data = load_json(DATA_DIR / "vscripts" / "api.json")
    classes = sorted(
        [entry for entry in data if entry.get("kind") == "class"],
        key=lambda entry: entry["name"].casefold(),
    )
    functions = sorted(
        [entry for entry in data if entry.get("kind") == "function"],
        key=lambda entry: entry["name"].casefold(),
    )

    lines = [
        page(
            "VScripts API",
            "dota-data/files/vscripts/api.json",
            f"Server and client Lua API. {len(classes)} classes and {len(functions)} global functions.",
        ),
        *contents(
            toc("Classes", [entry["name"] for entry in classes]),
            toc("Global functions", [entry["name"] for entry in functions]),
        ),
        "## Global functions",
        "",
    ]
    lines += [render_vscript_function(function) for function in functions]
    lines += ["## Classes", ""]
    lines += [render_vscript_class(declaration) for declaration in classes]
    write(out / "dota-data" / "vscripts-api.md", "\n".join(lines))


def generate_vscripts_api_types(out: Path) -> None:
    data = load_json(DATA_DIR / "vscripts" / "api-types.json")
    primitives = sorted(
        [entry for entry in data if entry.get("kind") == "primitive"],
        key=lambda entry: entry["name"].casefold(),
    )
    nominals = sorted(
        [entry for entry in data if entry.get("kind") == "nominal"],
        key=lambda entry: entry["name"].casefold(),
    )
    objects = sorted(
        [entry for entry in data if entry.get("kind") == "object"],
        key=lambda entry: entry["name"].casefold(),
    )

    lines = [
        page(
            "VScripts API types",
            "dota-data/files/vscripts/api-types.json",
            f"{len(primitives)} primitive, {len(nominals)} nominal and {len(objects)} object types.",
        ),
        "## Primitive types",
        "",
        table(
            ["Name", "Description"],
            [
                [code_cell(entry["name"]), cell(entry.get("description", ""))]
                for entry in primitives
            ],
        ),
        "",
        "## Nominal types",
        "",
        table(
            ["Name", "Base type", "Description"],
            [
                [
                    code_cell(entry["name"]),
                    code_cell(entry.get("baseType", "")),
                    cell(entry.get("description", "")),
                ]
                for entry in nominals
            ],
        ),
        "",
        "## Object types",
        "",
        toc("Object types", [entry["name"] for entry in objects]),
    ]

    for entry in objects:
        lines += [f"### {entry['name']}", ""]
        if entry.get("description"):
            lines += [entry["description"], ""]
        fields = entry.get("fields", [])
        if fields:
            rows = [
                [
                    code_cell(field["name"]),
                    code_cell(types_text(field.get("types"))),
                    cell(field.get("description", "")),
                ]
                for field in fields
            ]
            lines += [table(["Field", "Type", "Description"], rows), ""]
        else:
            lines += ["_No fields._", ""]

    write(out / "dota-data" / "vscripts-api-types.md", "\n".join(lines))


def generate_vscripts_enums(out: Path) -> None:
    data = load_json(DATA_DIR / "vscripts" / "enums.json")
    constants = sorted(
        [entry for entry in data if entry.get("kind") == "constant"],
        key=lambda entry: entry["name"].casefold(),
    )
    enums = sorted(
        [entry for entry in data if entry.get("kind") == "enum"],
        key=lambda entry: entry["name"].casefold(),
    )

    lines = [
        page(
            "VScripts enums and constants",
            "dota-data/files/vscripts/enums.json",
            f"{len(enums)} enums and {len(constants)} constants.",
        ),
        "## Constants",
        "",
        table(
            ["Name", "Value", "Available"],
            [
                [
                    code_cell(entry["name"]),
                    code_cell(entry.get("value", "")),
                    cell(entry.get("available", "")),
                ]
                for entry in constants
            ],
        ),
        "",
        "## Enums",
        "",
        toc("Enums", [entry["name"] for entry in enums]),
    ]

    for entry in enums:
        lines += [f"### {entry['name']}", ""]
        if entry.get("available"):
            lines += [f"Availability: `{entry['available']}`", ""]
        if entry.get("description"):
            lines += [entry["description"], ""]
        rows = [
            [code_cell(member["name"]), code_cell(member.get("value", ""))]
            for member in entry.get("members", [])
        ]
        lines += [table(["Member", "Value"], rows), ""]

    write(out / "dota-data" / "vscripts-enums.md", "\n".join(lines))


def generate_game_events(out: Path) -> None:
    events = sorted(
        load_json(DATA_DIR / "events.json"),
        key=lambda entry: entry["name"].casefold(),
    )

    lines = [
        page(
            "Game events",
            "dota-data/files/events.json",
            f"{len(events)} game events generated from the Dota 2 VPKs.",
        ),
        toc("Events", [event["name"] for event in events]),
    ]

    for event in events:
        lines += [f"### {event['name']}", ""]
        meta = []
        if event.get("sourceFile"):
            meta.append(f"Source: `{event['sourceFile']}`")
        if "local" in event:
            meta.append(f"Local: `{str(event['local']).lower()}`")
        if meta:
            lines += [" · ".join(meta), ""]
        if event.get("description"):
            lines += [event["description"], ""]
        fields = event.get("fields", [])
        if fields:
            rows = [
                [
                    code_cell(field["name"]),
                    code_cell(field.get("type", "")),
                    cell(field.get("description", "")),
                ]
                for field in fields
            ]
            lines += [table(["Field", "Type", "Description"], rows), ""]
        else:
            lines += ["_No fields._", ""]

    write(out / "dota-data" / "game-events.md", "\n".join(lines))


def generate_engine_enums(out: Path) -> None:
    enums = load_json(DATA_DIR / "engine-enums.json")
    enums = sorted(enums, key=lambda entry: entry["name"].casefold())

    lines = [
        page(
            "Engine enums",
            "dota-data/files/engine-enums.json",
            f"{len(enums)} enums extracted from the Dota 2 engine.",
        ),
        toc("Enums", [entry["name"] for entry in enums]),
    ]

    for entry in enums:
        lines += [f"### {entry['name']}", ""]
        if entry.get("description"):
            lines += [entry["description"], ""]
        members = entry.get("members", [])
        headers = ["Member"]
        keys = ["name"]
        if any("shortName" in member for member in members):
            headers.append("Short name")
            keys.append("shortName")
        if any("value" in member for member in members):
            headers.append("Value")
            keys.append("value")
        rows = [[code_cell(member.get(key, "")) for key in keys] for member in members]
        lines += [table(headers, rows), ""]

    write(out / "dota-data" / "engine-enums.md", "\n".join(lines))


def generate_panorama_css(out: Path) -> None:
    properties = load_json(DATA_DIR / "panorama" / "css.json")

    lines = [
        page(
            "Panorama CSS properties",
            "dota-data/files/panorama/css.json",
            f"{len(properties)} supported Panorama CSS properties.",
        ),
        toc("Properties", list(properties)),
    ]

    for name, value in properties.items():
        lines += [f"### `{name}`", ""]
        if value.get("description"):
            lines += [value["description"], ""]
        examples = value.get("examples") or []
        for example in examples:
            lines += [fence(example, "css"), ""]

    write(out / "dota-data" / "panorama-css.md", "\n".join(lines))


def generate_panorama_enums(out: Path) -> None:
    enums = sorted(
        load_json(DATA_DIR / "panorama" / "enums.json"),
        key=lambda entry: entry["name"].casefold(),
    )

    lines = [
        page(
            "Panorama enums",
            "dota-data/files/panorama/enums.json",
            f"{len(enums)} Panorama and Steam enums.",
        ),
        toc("Enums", [entry["name"] for entry in enums]),
    ]

    for entry in enums:
        lines += [f"### {entry['name']}", ""]
        if entry.get("description"):
            lines += [entry["description"], ""]
        rows = [
            [code_cell(member["name"]), code_cell(member.get("value", ""))]
            for member in entry.get("members", [])
        ]
        lines += [table(["Member", "Value"], rows), ""]

    write(out / "dota-data" / "panorama-enums.md", "\n".join(lines))


def generate_panorama_events(out: Path) -> None:
    events = load_json(DATA_DIR / "panorama" / "events.json")

    lines = [
        page(
            "Panorama events",
            "dota-data/files/panorama/events.json",
            f"{len(events)} Panorama panel events.",
        ),
        toc("Events", list(events)),
    ]

    for name, value in events.items():
        lines += [f"### {name}", ""]
        if value.get("panelEvent"):
            lines += ["Panel event: `true`", ""]
        if value.get("description"):
            lines += [value["description"], ""]
        args = value.get("args") or []
        if args:
            rows = [
                [
                    code_cell(argument.get("name", "")),
                    code_cell(types_text(argument.get("type", argument.get("types")))),
                ]
                for argument in args
            ]
            lines += [table(["Argument", "Type"], rows), ""]

    write(out / "dota-data" / "panorama-events.md", "\n".join(lines))


# ---------------------------------------------------------------------------
# Declaration file renderers
# ---------------------------------------------------------------------------


def declarations_by_kind(
    declarations: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for declaration in declarations:
        result.setdefault(declaration["kind"], []).append(declaration)
    return result


def sorted_declarations(declarations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(declarations, key=lambda declaration: declaration["name"].casefold())


def generate_api_declarations(out: Path) -> None:
    path = PACKAGES_DIR / "dota-lua-types" / "types" / "api.generated.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    interfaces = sorted_declarations(groups.get("interface", []))
    functions = sorted_declarations(groups.get("function", []))
    types = sorted_declarations(groups.get("type", []))
    consts = sorted_declarations(groups.get("const", []))
    namespaces = sorted_declarations(groups.get("namespace", []))

    data_class_names: set[str] = set()
    data_api_path = DATA_DIR / "vscripts" / "api.json"
    if data_api_path.exists():
        data_class_names = {
            entry["name"]
            for entry in load_json(data_api_path)
            if entry.get("kind") == "class"
        }

    if not data_class_names:
        for constant in consts:
            match = re.search(
                r"DotaConstructor<([A-Za-z_$][\w$]*)>", constant.get("type", "")
            )
            if match:
                data_class_names.add(match.group(1))

    classes = [
        declaration
        for declaration in interfaces
        if declaration["name"] in data_class_names
    ]
    additional_interfaces = [
        declaration
        for declaration in interfaces
        if declaration["name"] not in data_class_names
    ]

    lines = [
        page(
            "Dota Lua API declarations",
            "TypeScriptDeclarations/packages/dota-lua-types/types/api.generated.d.ts",
            f"{len(classes)} classes, {len(additional_interfaces)} additional interfaces, "
            f"{len(functions)} global functions and {len(types)} type aliases.",
        ),
        *contents(
            toc("Classes", [declaration["name"] for declaration in classes]),
            toc(
                "Additional interfaces",
                [declaration["name"] for declaration in additional_interfaces],
            ),
            toc("Global functions", [declaration["name"] for declaration in functions]),
        ),
        "## Global functions",
        "",
    ]
    lines += [render_function(declaration) for declaration in functions]
    lines += ["## Classes", ""]
    lines += [render_interface(declaration) for declaration in classes]

    if additional_interfaces:
        lines += ["## Additional interfaces", ""]
        lines += [
            render_interface(declaration) for declaration in additional_interfaces
        ]

    if types:
        lines += ["## Type aliases", ""]
        lines += [render_type_alias(declaration) for declaration in types]

    if namespaces:
        lines += ["## Namespaces", ""]
        lines += [render_namespace(declaration) for declaration in namespaces]

    if consts:
        lines += [
            "## Global constants",
            "",
            "These include generated constructor globals for classes.",
            "",
            render_constants(consts),
            "",
        ]

    write(
        out / "typescript-declarations" / "dota-lua-types" / "api.md", "\n".join(lines)
    )


def generate_api_types_declarations(out: Path) -> None:
    path = PACKAGES_DIR / "dota-lua-types" / "types" / "api-types.generated.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    types = sorted_declarations(groups.get("type", []))
    interfaces = sorted_declarations(groups.get("interface", []))

    lines = [
        page(
            "Dota Lua API types",
            "TypeScriptDeclarations/packages/dota-lua-types/types/api-types.generated.d.ts",
            f"{len(types)} type aliases and {len(interfaces)} interfaces. Primitive Lua types come from `lua-types`.",
        ),
        *contents(
            toc("Type aliases", [declaration["name"] for declaration in types]),
            toc("Interfaces", [declaration["name"] for declaration in interfaces]),
        ),
    ]

    if types:
        lines += ["## Type aliases", ""]
        lines += [render_type_alias(declaration) for declaration in types]

    if interfaces:
        lines += ["## Interfaces", ""]
        lines += [render_interface(declaration) for declaration in interfaces]

    write(
        out / "typescript-declarations" / "dota-lua-types" / "api-types.md",
        "\n".join(lines),
    )


def generate_enum_declarations(
    out: Path, package: str, source: str, title: str, destination: str
) -> None:
    path = PACKAGES_DIR / package / "types" / source
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    enums = sorted_declarations(groups.get("enum", []))
    consts = sorted_declarations(groups.get("const", []))
    aliases = sorted_declarations(groups.get("type", []))

    lines = [
        page(
            title,
            f"TypeScriptDeclarations/packages/{package}/types/{source}",
            f"{len(enums)} enums, {len(aliases)} compatibility aliases and {len(consts)} constants.",
        ),
        *contents(
            toc("Enums", [declaration["name"] for declaration in enums]),
            toc(
                "Compatibility aliases",
                [declaration["name"] for declaration in aliases],
            ),
        ),
    ]

    if consts:
        lines += ["## Constants", "", render_constants(consts), ""]

    if enums:
        lines += ["## Enums", ""]
        lines += [render_enum(declaration) for declaration in enums]

    if aliases:
        lines += ["## Compatibility aliases", ""]
        rows = [
            [
                f'<a name="{slug(declaration["name"])}"></a>{code_cell(declaration["name"])}',
                code_cell(declaration.get("rhs", "")),
                cell(render_jsdoc(declaration["jsdoc"], compact=True)),
            ]
            for declaration in aliases
        ]
        lines += [table(["Alias", "Target", "Description"], rows), ""]

    write(out / "typescript-declarations" / package / destination, "\n".join(lines))


def generate_game_event_declarations(out: Path, package: str, destination: str) -> None:
    path = PACKAGES_DIR / package / "types" / "events.generated.d.ts"
    declarations = scan_declarations(path.read_text(encoding="utf-8-sig"))

    event_map = next(
        (
            declaration
            for declaration in declarations
            if declaration["name"] == "GameEventDeclarations"
        ),
        None,
    )
    interfaces = {
        declaration["name"]: declaration
        for declaration in declarations
        if declaration["kind"] == "interface"
        and declaration["name"] != "GameEventDeclarations"
    }

    entries: list[tuple[str, dict[str, Any], dict[str, Any] | None]] = []
    if event_map:
        for member in event_map["members"]:
            event_interface = interfaces.get(member.get("type", ""))
            entries.append((member["name"], member, event_interface))

    entries.sort(key=lambda entry: entry[0].casefold())

    lines = [
        page(
            "Dota game event declarations",
            f"TypeScriptDeclarations/packages/{package}/types/events.generated.d.ts",
            f"{len(entries)} typed game events.",
        ),
        toc("Events", [entry[0] for entry in entries]),
    ]

    for name, member, event_interface in entries:
        lines += [f"### {name}", ""]
        event_type = member.get("type", "")
        if event_type:
            lines += [f"Type: `{event_type}`", ""]
        description = member["jsdoc"].get("description", "")
        if description:
            lines += [description, ""]
        fields = event_interface["members"] if event_interface else []
        if fields:
            rows = []
            for field in fields:
                label = field["name"] + ("?" if field.get("optional") else "")
                rows.append(
                    [
                        code_cell(label),
                        code_cell(field.get("type", field.get("signature", ""))),
                        cell(render_jsdoc(field["jsdoc"], compact=True)),
                    ]
                )
            lines += [table(["Field", "Type", "Description"], rows), ""]
        else:
            lines += ["_No typed fields._", ""]

    write(out / "typescript-declarations" / package / destination, "\n".join(lines))


def generate_common_declarations(
    out: Path,
    package: str,
    source: str,
    title: str,
    destination: str,
    intro: str = "Shared declarations used by the generated type definitions.",
) -> None:
    path = PACKAGES_DIR / package / "types" / source
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    types = sorted_declarations(groups.get("type", []))
    interfaces = sorted_declarations(groups.get("interface", []))
    consts = sorted_declarations(groups.get("const", []))
    namespaces = sorted_declarations(groups.get("namespace", []))

    lines = [
        page(
            title,
            f"TypeScriptDeclarations/packages/{package}/types/{source}",
            intro,
        ),
        *contents(
            toc("Types", [declaration["name"] for declaration in types]),
            toc("Interfaces", [declaration["name"] for declaration in interfaces]),
            toc("Namespaces", [declaration["name"] for declaration in namespaces]),
        ),
    ]

    if consts:
        lines += ["## Constants", "", render_constants(consts), ""]
    if types:
        lines += ["## Type aliases", ""]
        lines += [render_type_alias(declaration) for declaration in types]
    if interfaces:
        lines += ["## Interfaces", ""]
        lines += [render_interface(declaration) for declaration in interfaces]
    if namespaces:
        lines += ["## Namespaces", ""]
        lines += [render_namespace(declaration) for declaration in namespaces]

    write(out / "typescript-declarations" / package / destination, "\n".join(lines))


def generate_panorama_api(out: Path) -> None:
    path = PACKAGES_DIR / "panorama-types" / "types" / "api.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    interfaces = sorted_declarations(groups.get("interface", []))
    types = sorted_declarations(groups.get("type", []))
    namespaces = sorted_declarations(groups.get("namespace", []))

    lines = [
        page(
            "Panorama API declarations",
            "TypeScriptDeclarations/packages/panorama-types/types/api.d.ts",
            f"{len(interfaces)} interfaces, {len(types)} type aliases and {len(namespaces)} namespaces.",
        ),
        *contents(
            toc("Interfaces", [declaration["name"] for declaration in interfaces]),
            toc("Namespaces", [declaration["name"] for declaration in namespaces]),
        ),
    ]

    if interfaces:
        lines += ["## Interfaces", ""]
        lines += [render_interface(declaration) for declaration in interfaces]
    if types:
        lines += ["## Type aliases", ""]
        lines += [render_type_alias(declaration) for declaration in types]
    if namespaces:
        lines += ["## Namespaces", ""]
        lines += [render_namespace(declaration) for declaration in namespaces]

    write(
        out / "typescript-declarations" / "panorama-types" / "api.md", "\n".join(lines)
    )


def generate_panels_declarations(out: Path) -> None:
    path = PACKAGES_DIR / "panorama-types" / "types" / "panels.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )
    groups = declarations_by_kind(declarations)

    interfaces = sorted_declarations(groups.get("interface", []))
    types = sorted_declarations(groups.get("type", []))

    lines = [
        page(
            "Panorama panels",
            "TypeScriptDeclarations/packages/panorama-types/types/panels.d.ts",
            f"{len(interfaces)} panel interfaces and {len(types)} panel type aliases.",
        ),
        *contents(
            toc("Interfaces", [declaration["name"] for declaration in interfaces]),
            toc("Type aliases", [declaration["name"] for declaration in types]),
        ),
    ]

    if interfaces:
        lines += ["## Interfaces", ""]
        lines += [render_interface(declaration) for declaration in interfaces]
    if types:
        lines += ["## Type aliases", ""]
        lines += [render_type_alias(declaration) for declaration in types]

    write(
        out / "typescript-declarations" / "panorama-types" / "panels.md",
        "\n".join(lines),
    )


def generate_css_declarations(out: Path) -> None:
    path = PACKAGES_DIR / "panorama-types" / "types" / "css.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )

    style_declaration = next(
        (
            declaration
            for declaration in declarations
            if declaration["name"] == "VCSSStyleDeclaration"
        ),
        None,
    )
    other_declarations = [
        declaration
        for declaration in declarations
        if declaration["name"] != "VCSSStyleDeclaration"
    ]
    other_groups = declarations_by_kind(other_declarations)

    lines = [
        page(
            "Panorama CSS declarations",
            "TypeScriptDeclarations/packages/panorama-types/types/css.d.ts",
            "Typed Panorama style properties and helper declarations.",
        ),
    ]

    if style_declaration:
        properties = [
            member
            for member in style_declaration["members"]
            if member["kind"] == "property"
        ]
        properties.sort(key=lambda member: member["name"].casefold())
        lines += ["## VCSSStyleDeclaration", ""]
        lines += [toc("CSS properties", [member["name"] for member in properties])]
        for property_declaration in properties:
            lines += [f"### {property_declaration['name']}", ""]
            jsdoc = render_jsdoc(property_declaration["jsdoc"])
            if jsdoc:
                lines += [jsdoc, ""]
            lines += [f"Type: `{property_declaration['type']}`", ""]

    for kind, title in (
        ("interface", "Other interfaces"),
        ("type", "Type aliases"),
        ("enum", "Enums"),
    ):
        group = sorted_declarations(other_groups.get(kind, []))
        if not group:
            continue
        lines += [f"## {title}", ""]
        if kind == "type":
            lines += [render_type_alias(declaration) for declaration in group]
        elif kind == "enum":
            lines += [render_enum(declaration) for declaration in group]
        else:
            lines += [render_interface(declaration) for declaration in group]

    write(
        out / "typescript-declarations" / "panorama-types" / "css.md", "\n".join(lines)
    )


def generate_panorama_events_declarations(out: Path) -> None:
    path = PACKAGES_DIR / "panorama-types" / "types" / "panorama-events.d.ts"
    declarations = merge_duplicate_interfaces(
        scan_declarations(path.read_text(encoding="utf-8-sig"))
    )

    event_declaration = next(
        (
            declaration
            for declaration in declarations
            if declaration["name"] == "PanoramaEvent"
        ),
        None,
    )
    others = [
        declaration
        for declaration in declarations
        if declaration["name"] != "PanoramaEvent"
    ]
    other_groups = declarations_by_kind(others)

    lines = [
        page(
            "Panorama event declarations",
            "TypeScriptDeclarations/packages/panorama-types/types/panorama-events.d.ts",
            "Events available on Panorama panels.",
        ),
    ]

    if event_declaration:
        methods = [
            member
            for member in event_declaration["members"]
            if member["kind"] == "method"
        ]
        methods.sort(key=lambda member: member["name"].casefold())
        lines += [
            "## PanoramaEvent",
            "",
            toc("Events", [member["name"] for member in methods]),
        ]
        for method in methods:
            lines += [f"### {method['name']}", ""]
            lines += [fence(method["signature"], "ts"), ""]
            jsdoc = render_jsdoc(method["jsdoc"])
            if jsdoc:
                lines += [jsdoc, ""]

    for kind, title in (
        ("interface", "Other interfaces"),
        ("type", "Type aliases"),
    ):
        group = sorted_declarations(other_groups.get(kind, []))
        if not group:
            continue
        lines += [f"## {title}", ""]
        if kind == "type":
            lines += [render_type_alias(declaration) for declaration in group]
        else:
            lines += [render_interface(declaration) for declaration in group]

    write(
        out / "typescript-declarations" / "panorama-types" / "panorama-events.md",
        "\n".join(lines),
    )


# ---------------------------------------------------------------------------
# Indexes
# ---------------------------------------------------------------------------


def generate_indexes(out: Path) -> None:
    dota_data_pages = [
        (
            "VScripts API",
            "vscripts-api.md",
            "Server/client Lua classes and global functions.",
        ),
        (
            "VScripts API types",
            "vscripts-api-types.md",
            "Primitive, nominal and object types.",
        ),
        (
            "VScripts enums and constants",
            "vscripts-enums.md",
            "Lua enums and global constants.",
        ),
        ("Game events", "game-events.md", "Engine game events and their fields."),
        ("Engine enums", "engine-enums.md", "C++ engine enums."),
        ("Panorama CSS", "panorama-css.md", "Supported Panorama CSS properties."),
        ("Panorama enums", "panorama-enums.md", "Panorama and Steam enums."),
        ("Panorama events", "panorama-events.md", "Panorama panel events."),
    ]

    lines = [
        "# dota-data",
        "",
    ]
    for title, filename, description in dota_data_pages:
        lines.append(
            f"- [{title}](dota-data/{filename.replace('.md', '')}) - {description}"
        )
    lines.append("")
    write(out / "dota-data" / "README.md", "\n".join(lines))

    declaration_pages = [
        (
            "dota-lua-types",
            "Dota Lua declarations",
            [
                ("API", "api.md", "Lua classes and global functions."),
                ("API types", "api-types.md", "Nominal types and object shapes."),
                (
                    "Enums",
                    "enums.md",
                    "Lua enums, constants and compatibility aliases.",
                ),
                ("Normalized enums", "enums-normalized.md", "Normalized enum aliases."),
                ("Game events", "game-events.md", "Typed game events."),
                ("Common", "common.md", "Shared type helpers."),
                ("JSON", "json.md", "The `json` library types."),
            ],
        ),
        (
            "panorama-types",
            "Panorama declarations",
            [
                ("API", "api.md", "Panorama script API."),
                ("Panels", "panels.md", "Panel interfaces and panel types."),
                ("CSS", "css.md", "Typed Panorama CSS properties."),
                ("Panorama events", "panorama-events.md", "Panel event declarations."),
                ("Game events", "game-events.md", "Typed game events."),
                ("Enums", "enums.md", "Panorama enums and compatibility aliases."),
                ("Normalized enums", "enums-normalized.md", "Normalized enum aliases."),
                ("Stack trace API", "stack-trace-api.md", "Stack trace types."),
                ("Common", "common.md", "Shared type helpers."),
            ],
        ),
    ]

    lines = [
        "# TypeScriptDeclarations",
        "",
    ]
    for package, title, pages in declaration_pages:
        lines += [f"## {package}", ""]
        for page_title, filename, description in pages:
            lines.append(
                f"- [{page_title}](typescript-declarations/{package}/{filename.replace('.md', '')}) - {description}"
            )
        lines.append("")
    write(out / "typescript-declarations" / "README.md", "\n".join(lines))

    lines = [
        "# Dota 2 documentation",
    ]
    write(out / "README.md", "\n".join(lines))


def generate_docsify_sidebar(out: Path) -> None:
    dota_data_pages = [
        ("VScripts API", "dota-data/vscripts-api.md"),
        ("VScripts API types", "dota-data/vscripts-api-types.md"),
        ("VScripts enums and constants", "dota-data/vscripts-enums.md"),
        ("Game events", "dota-data/game-events.md"),
        ("Engine enums", "dota-data/engine-enums.md"),
        ("Panorama CSS", "dota-data/panorama-css.md"),
        ("Panorama enums", "dota-data/panorama-enums.md"),
        ("Panorama events", "dota-data/panorama-events.md"),
    ]

    declaration_pages = [
        (
            "dota-lua-types",
            [
                ("API", "typescript-declarations/dota-lua-types/api.md"),
                ("API types", "typescript-declarations/dota-lua-types/api-types.md"),
                ("Enums", "typescript-declarations/dota-lua-types/enums.md"),
                (
                    "Normalized enums",
                    "typescript-declarations/dota-lua-types/enums-normalized.md",
                ),
                (
                    "Game events",
                    "typescript-declarations/dota-lua-types/game-events.md",
                ),
                ("Common", "typescript-declarations/dota-lua-types/common.md"),
                ("JSON", "typescript-declarations/dota-lua-types/json.md"),
            ],
        ),
        (
            "panorama-types",
            [
                ("API", "typescript-declarations/panorama-types/api.md"),
                ("Panels", "typescript-declarations/panorama-types/panels.md"),
                ("CSS", "typescript-declarations/panorama-types/css.md"),
                (
                    "Panorama events",
                    "typescript-declarations/panorama-types/panorama-events.md",
                ),
                (
                    "Game events",
                    "typescript-declarations/panorama-types/game-events.md",
                ),
                ("Enums", "typescript-declarations/panorama-types/enums.md"),
                (
                    "Normalized enums",
                    "typescript-declarations/panorama-types/enums-normalized.md",
                ),
                (
                    "Stack trace API",
                    "typescript-declarations/panorama-types/stack-trace-api.md",
                ),
                ("Common", "typescript-declarations/panorama-types/common.md"),
            ],
        ),
    ]

    lines = [
        "* [Home](/)",
        "* [dota-data](/dota-data/README.md)",
    ]
    for title, path in dota_data_pages:
        lines.append(f"  * [{title}]({path})")
    lines.append("* [TypeScriptDeclarations](/typescript-declarations/README.md)")
    for package, pages in declaration_pages:
        lines.append(f"  * [{package}](/typescript-declarations/{package}/README.md)")
        for title, path in pages:
            lines.append(f"    * [{title}]({path})")

    write(out / "_sidebar.md", "\n".join(lines))


def generate_docsify_navbar(out: Path) -> None:
    lines = [
        "* [Home](/)",
        "* [dota-data](/dota-data/)",
        "* [TypeScriptDeclarations](/typescript-declarations/)",
    ]
    write(out / "_navbar.md", "\n".join(lines))


def generate_single_readme(out: Path) -> None:
    import os

    md_files = []
    for root, dirs, files in os.walk(out):
        for f in files:
            if f.endswith(".md") and f != "README.md":
                if f in ("_navbar.md", "_sidebar.md"):
                    continue
                md_files.append(Path(root) / f)
    md_files = sorted(md_files)

    lines = []
    lines.append("# Dota 2 Documentation")
    lines.append("")
    for p in md_files:
        rel = p.relative_to(out).as_posix()
        lines.append(f"- [{rel}](./{rel})")
    lines.append("")

    write(out / "README.md", "\n".join(lines))

    # remove per-directory readmes
    for extra in [
        out / "dota-data" / "README.md",
        out / "typescript-declarations" / "README.md",
    ]:
        try:
            if extra.exists():
                extra.unlink()
        except Exception:
            pass
    for pkg in ["dota-lua-types", "panorama-types"]:
        try:
            p = out / "typescript-declarations" / pkg / "README.md"
            if p.exists():
                p.unlink()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=None, help="Output directory")
    parser.add_argument(
        "--root", type=Path, default=DEFAULT_ROOT, help="Repository root"
    )
    args = parser.parse_args()

    global ROOT, DATA_DIR, PACKAGES_DIR
    ROOT = args.root.resolve()
    DATA_DIR = ROOT / "dota-data" / "files"
    PACKAGES_DIR = ROOT / "TypeScriptDeclarations" / "packages"

    out = (args.out if args.out is not None else ROOT / "docs").resolve()
    out.mkdir(parents=True, exist_ok=True)

    generate_vscripts_api(out)
    generate_vscripts_api_types(out)
    generate_vscripts_enums(out)
    generate_game_events(out)
    generate_engine_enums(out)
    generate_panorama_css(out)
    generate_panorama_enums(out)
    generate_panorama_events(out)

    generate_api_declarations(out)
    generate_api_types_declarations(out)
    generate_enum_declarations(
        out, "dota-lua-types", "enums.generated.d.ts", "Dota Lua enums", "enums.md"
    )
    generate_enum_declarations(
        out,
        "dota-lua-types",
        "enums-normalized.generated.d.ts",
        "Dota Lua normalized enums",
        "enums-normalized.md",
    )
    generate_game_event_declarations(out, "dota-lua-types", "game-events.md")
    generate_common_declarations(
        out,
        "dota-lua-types",
        "common.d.ts",
        "Dota Lua common declarations",
        "common.md",
    )
    generate_common_declarations(
        out,
        "dota-lua-types",
        "json.d.ts",
        "json library declarations",
        "json.md",
        "Types for the bundled `json` library.",
    )

    generate_panorama_api(out)
    generate_panels_declarations(out)
    generate_css_declarations(out)
    generate_panorama_events_declarations(out)
    generate_game_event_declarations(out, "panorama-types", "game-events.md")
    generate_enum_declarations(
        out, "panorama-types", "enums.generated.d.ts", "Panorama enums", "enums.md"
    )
    generate_enum_declarations(
        out,
        "panorama-types",
        "enums-normalized.generated.d.ts",
        "Panorama normalized enums",
        "enums-normalized.md",
    )
    generate_common_declarations(
        out,
        "panorama-types",
        "stack-trace-api.d.ts",
        "Panorama stack trace API",
        "stack-trace-api.md",
        "Types for the V8 stack trace API.",
    )
    generate_common_declarations(
        out,
        "panorama-types",
        "common.d.ts",
        "Panorama common declarations",
        "common.md",
    )

    generate_indexes(out)
    generate_docsify_sidebar(out)
    generate_docsify_navbar(out)
    generate_single_readme(out)

    print(f"Generated documentation in {out}")


if __name__ == "__main__":
    main()
