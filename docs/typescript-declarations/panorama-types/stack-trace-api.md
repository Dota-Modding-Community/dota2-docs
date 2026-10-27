# Panorama stack trace API



Types for the V8 stack trace API.

## Contents

<details><summary>Interfaces</summary>

- [ErrorCallSite](#errorcallsite)
- [ErrorConstructor](#errorconstructor)

</details>

## Interfaces

### ErrorCallSite

**Methods**

| Method | Description |
| --- | --- |
| `getThis(): any` | Value of "this" |
| `getTypeName(): string \| null` | Type of "this" as a string.<br>This is the name of the function stored in the constructor field of<br>"this", if available.  Otherwise the object's [[Class]] internal<br>property. |
| `getFunction(): Function \| undefined` | Current function |
| `getFunctionName(): string \| null` | Name of the current function, typically its name property.<br>If a name property is not available an attempt will be made to try<br>to infer a name from the function's context. |
| `getMethodName(): string \| null` | Name of the property [of "this" or one of its prototypes] that holds<br>the current function |
| `getFileName(): string \| null` | Name of the script [if this function was defined in a script] |
| `getLineNumber(): number \| null` | Current line number [if this function was defined in a script] |
| `getColumnNumber(): number \| null` | Current column number [if this function was defined in a script] |
| `getEvalOrigin(): string \| undefined` | A call site object representing the location where eval was called<br>[if this function was created using a call to eval] |
| `isToplevel(): boolean` | Is this a toplevel invocation, that is, is "this" the global object? |
| `isEval(): boolean` | Does this call take place in code defined by a call to eval? |
| `isNative(): boolean` | Is this call in native V8 code? |
| `isConstructor(): boolean` | Is this a constructor call? |

### ErrorConstructor

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `prepareStackTrace?` | `(err: Error, stackTraces: ErrorCallSite[]) => any` | Optional override for formatting stack traces<br><br>**See:** https://github.com/v8/v8/wiki/Stack%20Trace%20API#customizing-stack-traces<br> |
| `stackTraceLimit` | `number` |  |

**Methods**

| Method | Description |
| --- | --- |
| `captureStackTrace(targetObject: object, constructorOpt?: Function): void` | Create .stack property on a target object |
