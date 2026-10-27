# Panorama event declarations



Events available on Panorama panels.

## PanoramaEvent

<details><summary>Events</summary>

- [AddStyle](#addstyle)
- [AddStyleAfterDelay](#addstyleafterdelay)
- [AddStyleToEachChild](#addstyletoeachchild)
- [AddTimedStyle](#addtimedstyle)
- [AsyncEvent](#asyncevent)
- [BrowserGoToURL](#browsergotourl)
- [DismissAllContextMenus](#dismissallcontextmenus)
- [DOTADisplayDashboardTip](#dotadisplaydashboardtip)
- [DOTAGlobalSceneFireEntityInput](#dotaglobalscenefireentityinput)
- [DOTAGlobalSceneSetCameraEntity](#dotaglobalscenesetcameraentity)
- [DOTAGlobalSceneSetRootEntity](#dotaglobalscenesetrootentity)
- [DOTAHideAbilityTooltip](#dotahideabilitytooltip)
- [DOTAHideBuffTooltip](#dotahidebufftooltip)
- [DOTAHideDroppedItemTooltip](#dotahidedroppeditemtooltip)
- [DOTAHideEconItemTooltip](#dotahideeconitemtooltip)
- [DOTAHideProfileCardBattleCupTooltip](#dotahideprofilecardbattlecuptooltip)
- [DOTAHideProfileCardTooltip](#dotahideprofilecardtooltip)
- [DOTAHideRankTierTooltip](#dotahideranktiertooltip)
- [DOTAHideRuneTooltip](#dotahiderunetooltip)
- [DOTAHideTextTooltip](#dotahidetexttooltip)
- [DOTAHideTI10EventGameTooltip](#dotahideti10eventgametooltip)
- [DOTAHideTitleImageTextTooltip](#dotahidetitleimagetexttooltip)
- [DOTAHideTitleTextTooltip](#dotahidetitletexttooltip)
- [DOTAHUDBuffClicked](#dotahudbuffclicked)
- [DOTAHUDGameDisconnect](#dotahudgamedisconnect)
- [DOTAHUDHideDamageArmorTooltip](#dotahudhidedamagearmortooltip)
- [DOTAHUDHideGoldTooltip](#dotahudhidegoldtooltip)
- [DOTAHUDHideScoreboard](#dotahudhidescoreboard)
- [DOTAHUDShopOpened](#dotahudshopopened)
- [DOTAHUDShowDamageArmorTooltip](#dotahudshowdamagearmortooltip)
- [DOTAHUDShowDashboard](#dotahudshowdashboard)
- [DOTAHUDShowGoldTooltip](#dotahudshowgoldtooltip)
- [DOTAHUDShowScoreboard](#dotahudshowscoreboard)
- [DOTAHUDToggleScoreboard](#dotahudtogglescoreboard)
- [DOTAHUDToggleShop](#dotahudtoggleshop)
- [DOTASceneFireEntityInput](#dotascenefireentityinput)
- [DOTAScenePanelCameraLerpFinished](#dotascenepanelcameralerpfinished)
- [DOTAScenePanelDumpState](#dotascenepaneldumpstate)
- [DOTAScenePanelEntityClicked](#dotascenepanelentityclicked)
- [DOTAScenePanelEntityMouseOut](#dotascenepanelentitymouseout)
- [DOTAScenePanelEntityMouseOver](#dotascenepanelentitymouseover)
- [DOTAScenePanelResetRotation](#dotascenepanelresetrotation)
- [DOTAScenePanelSceneLoaded](#dotascenepanelsceneloaded)
- [DOTAScenePanelSceneUnloaded](#dotascenepanelsceneunloaded)
- [DOTAScenePanelSetRotationSpeed](#dotascenepanelsetrotationspeed)
- [DOTAScenePanelSimulateWorld](#dotascenepanelsimulateworld)
- [DOTASceneSetCameraEntity](#dotascenesetcameraentity)
- [DOTAShopCancelSearch](#dotashopcancelsearch)
- [DOTAShowAbilityInventoryItemTooltip](#dotashowabilityinventoryitemtooltip)
- [DOTAShowAbilityShopItemTooltip](#dotashowabilityshopitemtooltip)
- [DOTAShowAbilityTooltip](#dotashowabilitytooltip)
- [DOTAShowAbilityTooltipForEntityIndex](#dotashowabilitytooltipforentityindex)
- [DOTAShowAbilityTooltipForGuide](#dotashowabilitytooltipforguide)
- [DOTAShowAbilityTooltipForHero](#dotashowabilitytooltipforhero)
- [DOTAShowAbilityTooltipForLevel](#dotashowabilitytooltipforlevel)
- [DOTAShowBuffTooltip](#dotashowbufftooltip)
- [DOTAShowDroppedItemTooltip](#dotashowdroppeditemtooltip)
- [DOTAShowEconItemTooltip](#dotashoweconitemtooltip)
- [DOTAShowHomePage](#dotashowhomepage)
- [DOTAShowMatchDetails](#dotashowmatchdetails)
- [DOTAShowProfileCardBattleCupTooltip](#dotashowprofilecardbattlecuptooltip)
- [DOTAShowProfileCardTooltip](#dotashowprofilecardtooltip)
- [DOTAShowRankTierTooltip](#dotashowranktiertooltip)
- [DOTAShowReferencePage](#dotashowreferencepage)
- [DOTAShowReferencePageStyled](#dotashowreferencepagestyled)
- [DOTAShowRuneTooltip](#dotashowrunetooltip)
- [DOTAShowSettingsPopup](#dotashowsettingspopup)
- [DOTAShowTextTooltip](#dotashowtexttooltip)
- [DOTAShowTextTooltipStyled](#dotashowtexttooltipstyled)
- [DOTAShowTitleImageTextTooltip](#dotashowtitleimagetexttooltip)
- [DOTAShowTitleImageTextTooltipStyled](#dotashowtitleimagetexttooltipstyled)
- [DOTAShowTitleTextTooltip](#dotashowtitletexttooltip)
- [DOTAShowTitleTextTooltipStyled](#dotashowtitletexttooltipstyled)
- [DragDrop](#dragdrop)
- [DragEnd](#dragend)
- [DragEnter](#dragenter)
- [DragLeave](#dragleave)
- [DragStart](#dragstart)
- [DropInputFocus](#dropinputfocus)
- [ExternalBrowserGoToURL](#externalbrowsergotourl)
- [FireCustomGameEvent_Str](#firecustomgameevent_str)
- [IfHasClassEvent](#ifhasclassevent)
- [IfHoverOtherEvent](#ifhoverotherevent)
- [IfNotHasClassEvent](#ifnothasclassevent)
- [IfNotHoverOtherEvent](#ifnothoverotherevent)
- [MovePanelDown](#movepaneldown)
- [MovePanelLeft](#movepanelleft)
- [MovePanelRight](#movepanelright)
- [MovePanelUp](#movepanelup)
- [PageDown](#pagedown)
- [PageLeft](#pageleft)
- [PagePanelDown](#pagepaneldown)
- [PagePanelLeft](#pagepanelleft)
- [PagePanelRight](#pagepanelright)
- [PagePanelUp](#pagepanelup)
- [PageRight](#pageright)
- [PageUp](#pageup)
- [PlaySoundEffect](#playsoundeffect)
- [RemoveStyle](#removestyle)
- [RemoveStyleAfterDelay](#removestyleafterdelay)
- [RemoveStyleFromEachChild](#removestylefromeachchild)
- [ScrollDown](#scrolldown)
- [ScrollLeft](#scrollleft)
- [ScrollPanelDown](#scrollpaneldown)
- [ScrollPanelLeft](#scrollpanelleft)
- [ScrollPanelRight](#scrollpanelright)
- [ScrollPanelUp](#scrollpanelup)
- [ScrollRight](#scrollright)
- [ScrollToBottom](#scrolltobottom)
- [ScrollToTop](#scrolltotop)
- [ScrollUp](#scrollup)
- [SetChildPanelsSelected](#setchildpanelsselected)
- [SetInputFocus](#setinputfocus)
- [SetPanelEnabled](#setpanelenabled)
- [SetPanelSelected](#setpanelselected)
- [SwitchStyle](#switchstyle)
- [TogglePanelSelected](#togglepanelselected)
- [ToggleStyle](#togglestyle)
- [TriggerStyle](#triggerstyle)
- [UIHideCustomLayoutParametersTooltip](#uihidecustomlayoutparameterstooltip)
- [UIHideCustomLayoutTooltip](#uihidecustomlayouttooltip)
- [UIHideCustomLayoutTooltip](#uihidecustomlayouttooltip)
- [UIHideTextTooltip](#uihidetexttooltip)
- [UIPopupButtonClicked](#uipopupbuttonclicked)
- [UIShowCustomLayoutParametersTooltip](#uishowcustomlayoutparameterstooltip)
- [UIShowCustomLayoutPopup](#uishowcustomlayoutpopup)
- [UIShowCustomLayoutTooltip](#uishowcustomlayouttooltip)
- [UIShowTextTooltip](#uishowtexttooltip)
- [UIShowTextTooltip](#uishowtexttooltip)

</details>

### AddStyle

```ts
AddStyle(className: string): void
```

Add a CSS class to a panel.

### AddStyleAfterDelay

```ts
AddStyleAfterDelay(className: string, preDelay: number): void
```

Add a CSS class to a panel after a specified delay.

### AddStyleToEachChild

```ts
AddStyleToEachChild(className: string): void
```

Add a CSS class to all children of this panel.

### AddTimedStyle

```ts
AddTimedStyle(className: string, duration: number, preDelay: number): void
```

Add a class for a specified duration, with optional pre-delay; clears existing timers when called with same class.

### AsyncEvent

```ts
AsyncEvent(delay: number, event: string): void
```

Fire another event after a delay (in seconds, the event is provided in string and parsed by javascript engine).

### BrowserGoToURL

```ts
BrowserGoToURL(url: string): void
```

Built in browser goto the provided url. (will return to the dashboard)

### DismissAllContextMenus

```ts
DismissAllContextMenus(): void
```

Dismiss all context menus

### DOTADisplayDashboardTip

```ts
DOTADisplayDashboardTip(str: string, panelName?: string): void
```

Tip to display, panel to attach to (default 'DefaultTipAttachment')

### DOTAGlobalSceneFireEntityInput

```ts
DOTAGlobalSceneFireEntityInput(entityName: string, eventName: string, eventParam: string | number): void
```

### DOTAGlobalSceneSetCameraEntity

```ts
DOTAGlobalSceneSetCameraEntity(sceneId: string, entityName: string, delay: number): void
```

### DOTAGlobalSceneSetRootEntity

```ts
DOTAGlobalSceneSetRootEntity(sceneId: string, entityName: string): void
```

### DOTAHideAbilityTooltip

```ts
DOTAHideAbilityTooltip(): void
```

Hide the ability tooltip

### DOTAHideBuffTooltip

```ts
DOTAHideBuffTooltip(): void
```

Hide the buff tooltip

### DOTAHideDroppedItemTooltip

```ts
DOTAHideDroppedItemTooltip(): void
```

Hide the dropped item tooltip

### DOTAHideEconItemTooltip

```ts
DOTAHideEconItemTooltip(): void
```

Hide the econ item tooltip.

### DOTAHideProfileCardBattleCupTooltip

```ts
DOTAHideProfileCardBattleCupTooltip(): void
```

Hide the profile card / battle cup tooltip.

### DOTAHideProfileCardTooltip

```ts
DOTAHideProfileCardTooltip(panel: PanelBase): void
```

Hide the profile card tooltip.

### DOTAHideRankTierTooltip

```ts
DOTAHideRankTierTooltip(): void
```

Hide the rank tier tooltip.

### DOTAHideRuneTooltip

```ts
DOTAHideRuneTooltip(): void
```

Hide the rune tooltip.

### DOTAHideTextTooltip

```ts
DOTAHideTextTooltip(): void
```

Hide the text tooltip.

### DOTAHideTI10EventGameTooltip

```ts
DOTAHideTI10EventGameTooltip(): void
```

Hide the ti10 event game tooltip.

### DOTAHideTitleImageTextTooltip

```ts
DOTAHideTitleImageTextTooltip(): void
```

Hide the title image text tooltip.

### DOTAHideTitleTextTooltip

```ts
DOTAHideTitleTextTooltip(): void
```

Hide the title text tooltip.

### DOTAHUDBuffClicked

```ts
DOTAHUDBuffClicked(): void
```

Buff icon is clicked

### DOTAHUDGameDisconnect

```ts
DOTAHUDGameDisconnect(): void
```

Click the disconnect icon

### DOTAHUDHideDamageArmorTooltip

```ts
DOTAHUDHideDamageArmorTooltip(): void
```

hide the damage armor tooltip

### DOTAHUDHideGoldTooltip

```ts
DOTAHUDHideGoldTooltip(): void
```

Hide gold tooltip

### DOTAHUDHideScoreboard

```ts
DOTAHUDHideScoreboard(): void
```

### DOTAHUDShopOpened

```ts
DOTAHUDShopOpened(shopType: DOTA_SHOP_TYPE, opened: boolean): void
```

### DOTAHUDShowDamageArmorTooltip

```ts
DOTAHUDShowDamageArmorTooltip(): void
```

display the damage armor tooltip

### DOTAHUDShowDashboard

```ts
DOTAHUDShowDashboard(): void
```

Go back to dashboard

### DOTAHUDShowGoldTooltip

```ts
DOTAHUDShowGoldTooltip(): void
```

Show gold tooltip

### DOTAHUDShowScoreboard

```ts
DOTAHUDShowScoreboard(): void
```

### DOTAHUDToggleScoreboard

```ts
DOTAHUDToggleScoreboard(): void
```

### DOTAHUDToggleShop

```ts
DOTAHUDToggleShop(): void
```

### DOTASceneFireEntityInput

```ts
DOTASceneFireEntityInput( panel: PanelBase, entityName: string, eventName: string, eventParam: string | number, ): void
```

### DOTAScenePanelCameraLerpFinished

```ts
DOTAScenePanelCameraLerpFinished(panel: PanelBase): void
```

### DOTAScenePanelDumpState

```ts
DOTAScenePanelDumpState(): void
```

### DOTAScenePanelEntityClicked

```ts
DOTAScenePanelEntityClicked(entityName: string): void
```

### DOTAScenePanelEntityMouseOut

```ts
DOTAScenePanelEntityMouseOut(entityName: string): void
```

### DOTAScenePanelEntityMouseOver

```ts
DOTAScenePanelEntityMouseOver(entityName: string): void
```

### DOTAScenePanelResetRotation

```ts
DOTAScenePanelResetRotation(): void
```

### DOTAScenePanelSceneLoaded

```ts
DOTAScenePanelSceneLoaded(panel: PanelBase): void
```

### DOTAScenePanelSceneUnloaded

```ts
DOTAScenePanelSceneUnloaded(panel: PanelBase): void
```

### DOTAScenePanelSetRotationSpeed

```ts
DOTAScenePanelSetRotationSpeed(speed: number): void
```

### DOTAScenePanelSimulateWorld

```ts
DOTAScenePanelSimulateWorld(num: number): void
```

### DOTASceneSetCameraEntity

```ts
DOTASceneSetCameraEntity(entityName: string, delay: number): void
```

### DOTAShopCancelSearch

```ts
DOTAShopCancelSearch(): void
```

### DOTAShowAbilityInventoryItemTooltip

```ts
DOTAShowAbilityInventoryItemTooltip(entityIndex: EntityIndex, inventorySlot: number): void
```

Show tooltip for an item in the entityIndex NPC's inventory.

### DOTAShowAbilityShopItemTooltip

```ts
DOTAShowAbilityShopItemTooltip( panel: PanelBase, abilityName: string, guideName: string, entityIndex: EntityIndex, ): void
```

Show tooltip for an item in the entityIndex NPC's shop.

### DOTAShowAbilityTooltip

```ts
DOTAShowAbilityTooltip(abilityName: string): void
```

Show an ability tooltip.

### DOTAShowAbilityTooltipForEntityIndex

```ts
DOTAShowAbilityTooltipForEntityIndex(abilityName: string, entityIndex: EntityIndex): void
```

Show an ability tooltip. Level information comes from the entity specified by the entityIndex.

### DOTAShowAbilityTooltipForGuide

```ts
DOTAShowAbilityTooltipForGuide(abilityName: string, guideName: string): void
```

Show an ability tooltip annotated with a particular guide's info.

### DOTAShowAbilityTooltipForHero

```ts
DOTAShowAbilityTooltipForHero(abilityName: string, heroid: EntityIndex, bOnEnemy: boolean): void
```

Show an ability tooltip for the specified hero.

### DOTAShowAbilityTooltipForLevel

```ts
DOTAShowAbilityTooltipForLevel(abilityName: string, level: number): void
```

Show an ability tooltip for a specific level.

### DOTAShowBuffTooltip

```ts
DOTAShowBuffTooltip(entityIndex: EntityIndex, buffSerial: BuffID, bOnEnemy: boolean): void
```

Show a buff tooltip for the specified entityIndex + buff serial.

### DOTAShowDroppedItemTooltip

```ts
DOTAShowDroppedItemTooltip(x: number, y: number, abilityName: string, playerId: PlayerID, unknown: boolean): void
```

Show the dropped item tooltip

### DOTAShowEconItemTooltip

```ts
DOTAShowEconItemTooltip(itemDef: string, styleIndex: number, heroID: number): void
```

Show the econ item tooltip for a given item, style, and hero. Use 0 for the default style, and -1 for the default hero.

### DOTAShowHomePage

```ts
DOTAShowHomePage(): void
```

### DOTAShowMatchDetails

```ts
DOTAShowMatchDetails(matchId: number): void
```

Show the match details screen for the provided match id.

### DOTAShowProfileCardBattleCupTooltip

```ts
DOTAShowProfileCardBattleCupTooltip(steamID: number): void
```

Show the battle cup portion of the user's profile card, if it exists

### DOTAShowProfileCardTooltip

```ts
DOTAShowProfileCardTooltip(steamID: number, useProName: boolean): void
```

Show a user's profile card. Use pro name determines whether to use their professional team name if applicable.

### DOTAShowRankTierTooltip

```ts
DOTAShowRankTierTooltip(steamID: number): void
```

Show the rank tier tooltip for a user

### DOTAShowReferencePage

```ts
DOTAShowReferencePage(xmlPath: string): void
```

### DOTAShowReferencePageStyled

```ts
DOTAShowReferencePageStyled(xmlPath: string, styleClass: string): void
```

### DOTAShowRuneTooltip

```ts
DOTAShowRuneTooltip(X: number, Y: number, RuneType: number): void
```

Show a rune tooltip in the X Y location for the rune type

### DOTAShowSettingsPopup

```ts
DOTAShowSettingsPopup(): void
```

Show the settings popup panel

### DOTAShowTextTooltip

```ts
DOTAShowTextTooltip(text: string): void
```

Show a tooltip with the given text.

### DOTAShowTextTooltipStyled

```ts
DOTAShowTextTooltipStyled(text: string, style: string): void
```

Show a tooltip with the given text. Also apply a CSS class named "style" to allow custom styling.

### DOTAShowTitleImageTextTooltip

```ts
DOTAShowTitleImageTextTooltip(title: string, imagePath: string, text: string): void
```

Show a tooltip with the given title, image, and text.

### DOTAShowTitleImageTextTooltipStyled

```ts
DOTAShowTitleImageTextTooltipStyled( panel: PanelBase, title: string, imagePath: string, text: string, style: string, ): void
```

Show a tooltip with the given title, image, and text. Also apply a CSS class named "style" to allow custom styling.

### DOTAShowTitleTextTooltip

```ts
DOTAShowTitleTextTooltip(title: string, text: string): void
```

Show a tooltip with the given title and text.

### DOTAShowTitleTextTooltipStyled

```ts
DOTAShowTitleTextTooltipStyled(title: string, text: string, style: string): void
```

Show a tooltip with the given title and text. Also apply a CSS class named "style" to allow custom styling.

### DragDrop

```ts
DragDrop(displayPanel: PanelBase): void
```

### DragEnd

```ts
DragEnd(displayPanel: PanelBase): void
```

### DragEnter

```ts
DragEnter(displayPanel: PanelBase): void
```

### DragLeave

```ts
DragLeave(displayPanel: PanelBase): void
```

### DragStart

```ts
DragStart(settings: DragSettings): void
```

Drag events

### DropInputFocus

```ts
DropInputFocus(): void
```

Drop focus entirely from the window containing this panel.

### ExternalBrowserGoToURL

```ts
ExternalBrowserGoToURL(url: string): void
```

Open your default browser and goto url.

### FireCustomGameEvent_Str

```ts
FireCustomGameEvent_Str(eventName: string, data: string | number): void
```

Fire a game event clientside?

### IfHasClassEvent

```ts
IfHasClassEvent(className: string, event: string): void
```

Fire another event if this panel has a given class.

### IfHoverOtherEvent

```ts
IfHoverOtherEvent(otherPanelID: string, event: string): void
```

Fire another event if this panel is hovered over.

### IfNotHasClassEvent

```ts
IfNotHasClassEvent(className: string, event: string): void
```

Fire another event if this panel does not have a given class.

### IfNotHoverOtherEvent

```ts
IfNotHoverOtherEvent(otherPanelID: string, event: string): void
```

Fire another event if this panel is not hovered over.

### MovePanelDown

```ts
MovePanelDown(repeatCount: number): void
```

Move down from the panel. By default, this will change the focus position, but other panel types may implement this differently.

### MovePanelLeft

```ts
MovePanelLeft(repeatCount: number): void
```

Move left from the panel. By default, this will change the focus position, but other panel types may implement this differently.

### MovePanelRight

```ts
MovePanelRight(repeatCount: number): void
```

Move right from the panel. By default, this will change the focus position, but other panel types may implement this differently.

### MovePanelUp

```ts
MovePanelUp(repeatCount: number): void
```

Move up from the panel. By default, this will change the focus position, but other panel types may implement this differently.

### PageDown

```ts
PageDown(): void
```

Scroll the panel down by one page.

### PageLeft

```ts
PageLeft(): void
```

Scroll the panel left by one page.

### PagePanelDown

```ts
PagePanelDown(panel: PanelBase): void
```

Scroll the panel down by one page.

### PagePanelLeft

```ts
PagePanelLeft(panel: PanelBase): void
```

Scroll the panel left by one page.

### PagePanelRight

```ts
PagePanelRight(panel: PanelBase): void
```

Scroll the panel right by one page.

### PagePanelUp

```ts
PagePanelUp(panel: PanelBase): void
```

Scroll the panel up by one page.

### PageRight

```ts
PageRight(): void
```

Scroll the panel right by one page.

### PageUp

```ts
PageUp(): void
```

Scroll the panel up by one page.

### PlaySoundEffect

```ts
PlaySoundEffect(sound: string): void
```

Play a sound effect.

### RemoveStyle

```ts
RemoveStyle(className: string): void
```

Remove a CSS class from a panel.

### RemoveStyleAfterDelay

```ts
RemoveStyleAfterDelay(className: string, preDelay: number): void
```

Remove a CSS class from a panel after a specified delay.

### RemoveStyleFromEachChild

```ts
RemoveStyleFromEachChild(className: string): void
```

Remove a CSS class from all children of this panel.

### ScrollDown

```ts
ScrollDown(): void
```

Scroll the panel down by one line.

### ScrollLeft

```ts
ScrollLeft(): void
```

Scroll the panel left by one line.

### ScrollPanelDown

```ts
ScrollPanelDown(panel: PanelBase): void
```

Scroll the panel down by one line.

### ScrollPanelLeft

```ts
ScrollPanelLeft(panel: PanelBase): void
```

Scroll the panel left by one line.

### ScrollPanelRight

```ts
ScrollPanelRight(panel: PanelBase): void
```

Scroll the panel right by one line.

### ScrollPanelUp

```ts
ScrollPanelUp(panel: PanelBase): void
```

Scroll the panel up by one line.

### ScrollRight

```ts
ScrollRight(): void
```

Scroll the panel right by one line.

### ScrollToBottom

```ts
ScrollToBottom(): void
```

Scroll this panel to the bottom.

### ScrollToTop

```ts
ScrollToTop(): void
```

Scroll this panel to the top.

### ScrollUp

```ts
ScrollUp(): void
```

Scroll the panel up by one line.

### SetChildPanelsSelected

```ts
SetChildPanelsSelected(selected: boolean): void
```

Set whether any child panels are :selected.

### SetInputFocus

```ts
SetInputFocus(panel: PanelBase): void
```

Set focus to this panel.

### SetPanelEnabled

```ts
SetPanelEnabled(enabled: boolean): void
```

Sets whether the given panel is enabled

### SetPanelSelected

```ts
SetPanelSelected(selected: boolean): void
```

Set whether this panel is :selected.

### SwitchStyle

```ts
SwitchStyle(slot: string, className: string): void
```

Switch which class the panel has for a given attribute slot. Allows easily changing between multiple states.

### TogglePanelSelected

```ts
TogglePanelSelected(panel: PanelBase): void
```

Toggle whether this panel is :selected.

### ToggleStyle

```ts
ToggleStyle(className: string): void
```

Toggle whether a panel has the given CSS class.

### TriggerStyle

```ts
TriggerStyle(className: string): void
```

Remove then immediately add back a CSS class from a panel. Useful to re-trigger events like animations or sound effects.

### UIHideCustomLayoutParametersTooltip

```ts
UIHideCustomLayoutParametersTooltip(toolipId: string): void
```

Hide custom layout parameters tooltip.

### UIHideCustomLayoutTooltip

```ts
UIHideCustomLayoutTooltip(toolipId: string): void
```

Hide custom layout tooltip

### UIHideCustomLayoutTooltip

```ts
UIHideCustomLayoutTooltip(toolipId: string): void
```

### UIHideTextTooltip

```ts
UIHideTextTooltip(): void
```

### UIPopupButtonClicked

```ts
UIPopupButtonClicked(panel: PanelBase): void
```

Popup button is clicked

### UIShowCustomLayoutParametersTooltip

```ts
UIShowCustomLayoutParametersTooltip(toolipId: string, xmlFile: string, parameters: string): void
```

Show custom layout parameters tooltip, layout is the xml file, the parameters are contacted with & symbol.

### UIShowCustomLayoutPopup

```ts
UIShowCustomLayoutPopup(id: string, xmlPath: string): void
```

### UIShowCustomLayoutTooltip

```ts
UIShowCustomLayoutTooltip(toolipId: string, xmlFile: string): void
```

Show custom layout tooltip, layout is the xml file.

### UIShowTextTooltip

```ts
UIShowTextTooltip(text: string): void
```

### UIShowTextTooltip

```ts
UIShowTextTooltip(text: string): void
```
