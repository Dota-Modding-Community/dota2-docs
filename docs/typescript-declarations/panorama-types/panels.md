# Panorama panels



33 panel interfaces and 11 panel type aliases.

## Contents

<details><summary>Interfaces</summary>

- [AbilityImage](#abilityimage)
- [AnimatedImageStrip](#animatedimagestrip)
- [AvatarImage](#avatarimage)
- [Button](#button)
- [CarouselPanel](#carouselpanel)
- [CircularProgressBar](#circularprogressbar)
- [ContextMenuScriptPanel](#contextmenuscriptpanel)
- [CountdownPanel](#countdownpanel)
- [DropDown](#dropdown)
- [EconItemPanel](#econitempanel)
- [HeroImage](#heroimage)
- [HeroMovie](#heromovie)
- [HTMLPanel](#htmlpanel)
- [HUDOverlayMap](#hudoverlaymap)
- [ImagePanel](#imagepanel)
- [ItemImage](#itemimage)
- [LabelPanel](#labelpanel)
- [LeagueImage](#leagueimage)
- [MoviePanel](#moviepanel)
- [NumberEntry](#numberentry)
- [Panel](#panel)
- [PanelBase](#panelbase)
- [PanoramaPanelNameMap](#panoramapanelnamemap)
- [ParticleScenePanel](#particlescenepanel)
- [ProgressBar](#progressbar)
- [ProgressBarWithMiddle](#progressbarwithmiddle)
- [RadioButton](#radiobutton)
- [ScenePanel](#scenepanel)
- [SliderPanel](#sliderpanel)
- [TextButton](#textbutton)
- [TextEntry](#textentry)
- [ToggleButton](#togglebutton)
- [UserName](#username)

</details>
<details><summary>Type aliases</summary>

- [AccountLinkHTML](#accountlinkhtml)
- [HeroSetList](#herosetlist)
- [HTML](#html)
- [HUDShopTextEntry](#hudshoptextentry)
- [PanelEvent](#panelevent)
- [ScalingFunction](#scalingfunction)
- [SettingsCheckbox](#settingscheckbox)
- [SlottedSlider](#slottedslider)
- [StoreCustomControls](#storecustomcontrols)
- [UserRichPresence](#userrichpresence)
- [WeekendTourneyTrophyScene](#weekendtourneytrophyscene)

</details>

## Interfaces

### AbilityImage

Extends `ImagePanel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `abilityname` | `string` |  |
| `contextEntityIndex` | `AbilityEntityIndex` |  |

### AnimatedImageStrip

Extends `ImagePanel`

**Methods**

| Method | Description |
| --- | --- |
| `StartAnimating(): void` |  |
| `StopAnimating(): void` |  |

### AvatarImage

Extends `UserName`

**Methods**

| Method | Description |
| --- | --- |
| `SetAccountID(accountid: number): void` |  |

### Button

Extends `Panel`

_No members._

### CarouselPanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `GetFocusIndex(): number` |  |
| `GetFocusChild(): Panel` |  |
| `SetSelectedChild(selected: Panel): void` |  |

### CircularProgressBar

Extends `PanelBase`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `value` | `number` |  |
| `min` | `number` |  |
| `max` | `number` |  |

### ContextMenuScriptPanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `GetContentsPanel(): Panel` |  |

### CountdownPanel

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `startTime` | `string \| number` | get(): string; set(): number; |
| `endTime` | `string \| number` | get(): string; set(): number; |
| `updateInterval` | `number` | **Default:** 1 |
| `timeDialogVariable` | `string` | **Default:** 'countdown_time' |

### DropDown

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `HasOption(id: string): boolean` |  |
| `AddOption(panel: Panel): void` |  |
| `RemoveOption(id: string): void` |  |
| `RemoveAllOptions(): void` |  |
| `GetSelected(): Panel` |  |
| `SetSelected(id: string): void` |  |
| `AccessDropDownMenu(): Panel` |  |
| `FindDropDownMenuChild(string: string): Panel` |  |
| `SetSelectedIndex(index: number): void` |  |

### EconItemPanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `SetItemByDefinition(itemDef: number): void` | **Example:**<br><br>`// Wyvern Hatchling, Ice style`<br>`panel.SetItemByDefinition(11321);` |
| `SetItemByDefinitionAndStyle(itemDef: number, style: number): void` | **Example:**<br><br>`// Wyvern Hatchling, Gold style`<br>`panel.SetItemByDefinition(11321, 2);` |

### HeroImage

Extends `ImagePanel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `heroid` | `HeroID` |  |
| `heroname` | `string` |  |
| `heroimagestyle` | `'icon' \| 'portrait' \| 'landscape'` |  |

### HeroMovie

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `heroid` | `HeroID` |  |
| `heroname` | `string` |  |
| `persona` | `any` |  |

### HTMLPanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `SetURL(url: string): void` |  |
| `SetIgnoreCursor(value: boolean): void` |  |
| `RunJavascript(js: string): void` |  |

### HUDOverlayMap

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `mapscale` | `number` |  |
| `maptexture` | `string` |  |
| `mapscroll` | `boolean` |  |
| `fixedoffsetenabled` | `boolean` |  |

**Methods**

| Method | Description |
| --- | --- |
| `SetFixedOffset(x: number, y: number): void` |  |
| `SetFixedBackgroundTexturePosition(size: number, x: number, y: number): void` |  |

### ImagePanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `SetImage(path: string): void` | Sets the source of this Image.<br><br>**Example:**<br><br>`image.SetImage("file://{images}/custom_image.png");`<br>`image.SetImage("s2r://panorama/images/hud/reborn/icon_glyph_on_psd.vtex");` |
| `SetScaling(scale: ScalingFunction): void` |  |
| `SetImageFromPanel(sourcePanel: Panel, unknown1: boolean): void` |  |

### ItemImage

Extends `ImagePanel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `itemname` | `string` |  |
| `contextEntityIndex` | `ItemEntityIndex` |  |

### LabelPanel

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |
| `html` | `boolean` |  |

**Methods**

| Method | Description |
| --- | --- |
| `SetLocString(token: string): void` |  |
| `SetAlreadyLocalizedText(token: string): void` |  |

### LeagueImage

Extends `ImagePanel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `leagueid` | `number` |  |

### MoviePanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `SetMovie(source: string): void` |  |
| `SetControls(controls: 'none' \| 'minimal' \| 'full'): void` |  |
| `SetTitle(title: string): void` | Changes video title that is shown with 'full' controls. |
| `Play(): void` |  |
| `Pause(): void` |  |
| `Stop(): void` |  |
| `SetRepeat(repeat: boolean): void` |  |
| `SetPlaybackVolume(volume: number): void` | **Parameters:**<br><br>- volume A number within 0..1 range.<br> |
| `BAdjustingVolume(): boolean` |  |

### NumberEntry

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `value` | `number` |  |
| `min` | `number` | **Default:** 0 |
| `max` | `number` | **Default:** 1000000 |
| `increment` | `number` | **Default:** 1 |

### Panel

Extends `PanelBase`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `style` | `VCSSStyleDeclaration` |  |
| `scrolloffset_x` | `number` |  |
| `scrolloffset_y` | `number` |  |
| `actualxoffset` | `number` |  |
| `actualyoffset` | `number` |  |
| `actuallayoutwidth` | `number` |  |
| `actuallayoutheight` | `number` |  |
| `desiredlayoutwidth` | `number` |  |
| `desiredlayoutheight` | `number` |  |
| `contentwidth` | `number` |  |
| `contentheight` | `number` |  |
| `actualuiscale_y` | `number` |  |
| `actualuiscale_x` | `number` |  |
| `layoutfile` | `string` |  |
| `id` | `string` |  |
| `selectionpos_x` | `number \| null` | get(): number \\| null; set(): number \\| 'auto' \\| null; |
| `selectionpos_y` | `number \| null` |  |
| `tabindex` | `number \| null` | get(): number \\| null; set(): number \\| 'auto' \\| null; |
| `hittestchildren` | `boolean` |  |
| `hittest` | `boolean` |  |
| `inputnamespace` | `string` |  |
| `defaultfocus` | `string` |  |
| `checked` | `boolean` |  |
| `enabled` | `boolean` |  |
| `visible` | `boolean` |  |

**Methods**

| Method | Description |
| --- | --- |
| `IsValid(): boolean` |  |
| `AddClass(name: string): void` |  |
| `RemoveClass(name: string): void` |  |
| `BAscendantHasClass(name: string): boolean` |  |
| `BHasClass(name: string): boolean` |  |
| `SetHasClass(name: string, active: boolean): void` |  |
| `ToggleClass(name: string): void` |  |
| `SwitchClass(name: string, replacement: string): void` |  |
| `TriggerClass(name: string): void` |  |
| `ClearPanelEvent(event: PanelEvent): void` |  |
| `SetDraggable(draggable: boolean): void` |  |
| `IsDraggable(): boolean` |  |
| `IsSizeValid(): boolean` |  |
| `GetChildCount(): number` |  |
| `GetChild(index: number): Panel \| null` |  |
| `GetChildIndex(child: Panel): number` |  |
| `Children(): Panel[]` |  |
| `FindChildrenWithClassTraverse(classname: string): Panel[]` |  |
| `GetParent(): Panel \| null` |  |
| `SetParent(parent: Panel): void` |  |
| `FindChild(childId: string): Panel \| null` |  |
| `FindChildTraverse(childId: string): Panel \| null` |  |
| `FindChildInLayoutFile(childId: string): Panel \| null` |  |
| `FindPanelInLayoutFile(id: string): Panel \| null` |  |
| `FindAncestor(id: string): Panel \| null` |  |
| `RemoveAndDeleteChildren(): void` |  |
| `MoveChildBefore(child: PanelBase, beforeChild: PanelBase): void` |  |
| `MoveChildAfter(child: PanelBase, afterChild: PanelBase): void` |  |
| `GetPositionWithinWindow(): { x: number; y: number }` |  |
| `GetPositionWithinAncestor(unknown: Panel): { x: number; y: number }` |  |
| `ApplyStyles(bool: boolean): void` | Sets whether to update panel with style changes |
| `ClearPropertyFromCode(unknown: string): void` |  |
| `DeleteAsync(time: number): void` |  |
| `BIsTransparent(): boolean` |  |
| `BAcceptsInput(): boolean` |  |
| `BAcceptsFocus(): boolean` |  |
| `SetFocus(): void` |  |
| `UpdateFocusInContext(): void` | ?? |
| `BHasHoverStyle(): boolean` | ?? |
| `SetAcceptsFocus(value: boolean): void` |  |
| `SetDisableFocusOnMouseDown(value: boolean): void` | ?? |
| `BHasKeyFocus(): boolean` | ?? |
| `SetScrollParentToFitWhenFocused(value: boolean): void` |  |
| `BScrollParentToFitWhenFocused(): boolean` | ?? |
| `IsSelected(): boolean` |  |
| `BHasDescendantKeyFocus(): boolean` |  |
| `BLoadLayout(path: string, overrideExisting: boolean, partialLayout: boolean): boolean` |  |
| `BLoadLayoutSnippet(snippetName: string): boolean` |  |
| `BHasLayoutSnippet(snippetName: string): boolean` |  |
| `SetTopOfInputContext(): void` |  |
| `SetDialogVariable(name: string, value: string): void` | ???? |
| `SetDialogVariableInt(name: string, value: number): void` |  |
| `SetDialogVariableTime(name: string, value: number): void` |  |
| `SetDialogVariableLocString(name: string, token: string): void` |  |
| `SetDialogVariablePluralLocStringInt(name: string, token: string, value: number): void` |  |
| `ScrollToTop(): void` |  |
| `ScrollToBottom(): void` |  |
| `ScrollToLeftEdge(): void` |  |
| `ScrollToRightEdge(): void` |  |
| `ScrollParentToMakePanelFit(scrollBehaviour: number, unknown: boolean): void` | Scroll behaviour is an enum? |
| `BCanSeeInParentScroll(): boolean` |  |
| `GetAttributeInt(name: string, defaultValue: number): number` |  |
| `GetAttributeString(name: string, defaultValue: string): string` |  |
| `GetAttributeUInt32(name: string, defaultValue: number): number` |  |
| `SetAttributeInt(name: string, value: number): void` |  |
| `SetAttributeString(name: string, value: string): void` |  |
| `SetAttributeUInt32(name: string, value: number): void` |  |
| `SetInputNamespace(namespace: string): void` |  |
| `RegisterForReadyEvents(callback: (event: object) => void): void` | ?? |
| `BReadyForDisplay(): boolean` | ???? |
| `SetReadyForDisplay(value: boolean): void` |  |
| `SetPositionInPixels(x: number, y: number, z: number): void` | ??? |
| `Data<T = object>(): T` |  |
| `SetSendScrollPositionChangedEvents(value: boolean): void` |  |

### PanelBase

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` |  |
| `paneltype` | `string` |  |
| `rememberchildfocus` | `boolean` |  |

**Methods**

| Method | Description |
| --- | --- |
| `SetPanelEvent(event: PanelEvent, handler: () => void): void` |  |
| `RunScriptInPanelContext(script: string): void` |  |

### PanoramaPanelNameMap

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `Panel` | `Panel` |  |
| `Label` | `LabelPanel` |  |
| `Image` | `ImagePanel` |  |
| `DOTAAbilityImage` | `AbilityImage` |  |
| `DOTAItemImage` | `ItemImage` |  |
| `DOTAHeroImage` | `HeroImage` |  |
| `DOTACountryFlagImage` | `ImagePanel` |  |
| `DOTALeagueImage` | `LeagueImage` |  |
| `EconItemImage` | `ImagePanel` |  |
| `AnimatedImageStrip` | `ImagePanel` |  |
| `DOTAEmoticon` | `ImagePanel` |  |
| `Movie` | `MoviePanel` |  |
| `DOTAHeroMovie` | `HeroMovie` |  |
| `DOTAScenePanel` | `ScenePanel` |  |
| `DOTAParticleScenePanel` | `ParticleScenePanel` |  |
| `DOTAEconItem` | `EconItemPanel` |  |
| `ProgressBar` | `ProgressBar` |  |
| `CircularProgressBar` | `CircularProgressBar` |  |
| `ProgressBarWithMiddle` | `ProgressBarWithMiddle` |  |
| `DOTAUserName` | `UserName` |  |
| `DOTAUserRichPresence` | `UserRichPresence` |  |
| `DOTAAvatarImage` | `AvatarImage` |  |
| `Countdown` | `CountdownPanel` |  |
| `Button` | `Button` |  |
| `TextButton` | `TextButton` |  |
| `ToggleButton` | `ToggleButton` |  |
| `DOTASettingsCheckbox` | `SettingsCheckbox` |  |
| `RadioButton` | `RadioButton` |  |
| `TextEntry` | `TextEntry` |  |
| `DOTAHUDShopTextEntry` | `HUDShopTextEntry` |  |
| `NumberEntry` | `NumberEntry` |  |
| `Slider` | `SliderPanel` |  |
| `SlottedSlider` | `SlottedSlider` |  |
| `DropDown` | `DropDown` |  |
| `ContextMenuScript` | `ContextMenuScriptPanel` |  |
| `Carousel` | `CarouselPanel` |  |
| `DOTAHeroSetList` | `HeroSetList` |  |
| `CarouselNav` | `Panel` |  |
| `DOTAHUDOverlayMap` | `HUDOverlayMap` |  |
| `DOTAMinimap` | `Panel` |  |
| `HTML` | `HTML` |  |
| `DOTAAccountLinkHTML` | `AccountLinkHTML` |  |
| `DOTAHTMLPanel` | `HTMLPanel` |  |
| `DOTAStoreCustomControls` | `StoreCustomControls` |  |
| `CustomLayoutPanel` | `Panel` |  |

### ParticleScenePanel

Extends `ScenePanel`

**Methods**

| Method | Description |
| --- | --- |
| `StartParticles(): void` |  |
| `StopParticlesImmediately(b: boolean): void` |  |
| `StopParticlesWithEndcaps(): void` |  |
| `SetControlPoint(cp: number, x: number, y: number, z: number): void` |  |

### ProgressBar

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `value` | `number` |  |
| `min` | `number` |  |
| `max` | `number` |  |
| `hasNotches` | `boolean` |  |
| `valuePerNotch` | `boolean` |  |

### ProgressBarWithMiddle

Extends `Panel`

**See:** https://github.com/SteamDatabase/GameTracking-Dota2/search?q=ProgressBarWithMiddle
 

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `lowervalue` | `number` |  |
| `uppervalue` | `number` |  |
| `min` | `number` |  |
| `max` | `number` |  |

### RadioButton

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `GetSelectedButton(): RadioButton` |  |

### ScenePanel

Extends `Panel`

**Methods**

| Method | Description |
| --- | --- |
| `FireEntityInput(entityName: string, inputName: string, value: string): void` |  |
| `PlayEntitySoundEvent(arg1: any, arg2: any): number` |  |
| `SetUnit(unitName: string, environment: string, drawBackground: boolean): void` |  |
| `GetPanoramaSurfacePanel(): Panel \| null` |  |
| `SetRotateParams(yawMin: number, yawMax: number, pitchMin: number, pitchMax: number): void` |  |
| `SpawnHeroInScenePanelByPlayerSlot(match_id: string, slot: number, entityName: string): boolean` |  |
| `SpawnHeroInScenePanelByHeroId(heroID: number, entityName: string, econId: number): boolean` |  |
| `SetScenePanelToPlayerHero(heroName: string, player: PlayerID): boolean` |  |
| `SetScenePanelToLocalHero(heroId: HeroID): boolean` |  |
| `SetPostProcessFade(value: number): void` |  |
| `SetCustomPostProcessMaterial(material: string): void` | **Example:**<br><br>`scenePanel.SetCustomPostProcessMaterial("materials/dev/deferred_post_process_graphic_ui.vmat")` |
| `SpawnHeroInScenePanelByPlayerSlotWithFullBodyView(heroName: string, player: PlayerID): boolean` |  |
| `LerpToCameraEntity(entityName: string, duration: number): void` |  |
| `ReloadScene(): void` |  |
| `ClearScene(unknown1: boolean): void` |  |
| `SetAnimgraphParameterOnEntityInt(entityName: string, name: string, value: number): void` |  |
| `SetAnimgraphParameterOnEntityFloat(entityName: string, name: string, value: number): void` |  |
| `SetAnimgraphParameterOnEntityEnum(entityName: string, name: string, value: string): void` |  |

### SliderPanel

Extends `PanelBase`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `value` | `number` |  |
| `min` | `number` |  |
| `max` | `number` |  |
| `default` | `number` |  |
| `increment` | `number` |  |
| `mousedown` | `boolean` |  |

**Methods**

| Method | Description |
| --- | --- |
| `SetDirection(value: any): void` |  |
| `SetRequiresSelection(value: boolean): void` | ?? |
| `SetShowDefaultValue(value: boolean): void` |  |
| `SetValueNoEvents(value: number): void` |  |

### TextButton

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |

### TextEntry

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |

**Methods**

| Method | Description |
| --- | --- |
| `RaiseChangeEvents(bool: boolean): void` |  |
| `SelectAll(): void` |  |
| `ClearSelection(): void` |  |
| `GetMaxCharCount(): number` |  |
| `SetMaxChars(value: number): void` |  |
| `GetCursorOffset(): number` |  |
| `SetCursorOffset(value: number): void` |  |

### ToggleButton

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |

**Methods**

| Method | Description |
| --- | --- |
| `SetSelected(value: boolean): void` |  |

### UserName

Extends `Panel`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `steamid` | `string` | 64-bit Steam ID number. |
| `accountid` | `string` | 32-bit Steam ID number. |

## Type aliases

### AccountLinkHTML

```ts
type AccountLinkHTML = HTMLPanel;
```

### HeroSetList

```ts
type HeroSetList = CarouselPanel;
```

### HTML

```ts
type HTML = HTMLPanel;
```

### HUDShopTextEntry

```ts
type HUDShopTextEntry = TextEntry;
```

### PanelEvent

```ts
type PanelEvent =
    | 'onactivate'
    | 'oncancel'
    | 'oncontextmenu'
    | 'ondblclick'
    | 'ondeselect'
    | 'oneconsetloaded'
    | 'onfilled'
    | 'onfindmatchend'
    | 'onfindmatchstart'
    | 'onfocus'
    | 'onblur'
    | 'ondescendantfocus'
    | 'ondescendantblur'
    | 'oninputsubmit'
    | 'onload'
    | 'onmouseactivate'
    | 'onmouseout'
    | 'onmouseover'
    | 'onmovedown'
    | 'onmoveleft'
    | 'onmoveright'
    | 'onmoveup'
    | 'onnotfilled'
    | 'onpagesetupsuccess'
    | 'onpopupsdismissed'
    | 'onselect'
    | 'ontabforward'
    | 'ontabbackward'
    | 'ontextentrychange'
    | 'ontextentrysubmit'
    | 'onscrolledtobottom'
    | 'onscrolledtorightedge'
    | 'ontooltiploaded'
    | 'onvaluechanged';
```

### ScalingFunction

```ts
type ScalingFunction =
    | 'none'
    | 'stretch' // the default
    | 'stretchx'
    | 'stretchy'
    | 'stretch-to-fit-preserve-aspect'
    | 'stretch-to-fit-x-preserve-aspect'
    | 'stretch-to-fit-y-preserve-aspect'
    | 'stretch-to-cover-preserve-aspect';
```

### SettingsCheckbox

```ts
type SettingsCheckbox = ToggleButton;
```

### SlottedSlider

```ts
type SlottedSlider = SliderPanel;
```

### StoreCustomControls

```ts
type StoreCustomControls = HTMLPanel;
```

### UserRichPresence

```ts
type UserRichPresence = UserName;
```

### WeekendTourneyTrophyScene

```ts
type WeekendTourneyTrophyScene = ScenePanel;
```
