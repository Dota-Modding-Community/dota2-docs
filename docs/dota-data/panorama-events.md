# Panorama events



89 Panorama panel events.

<details><summary>Events</summary>

- [AddStyle](#addstyle)
- [AddStyleAfterDelay](#addstyleafterdelay)
- [AddStyleToEachChild](#addstyletoeachchild)
- [AddTimedStyle](#addtimedstyle)
- [AsyncEvent](#asyncevent)
- [DOTADisplayDashboardTip](#dotadisplaydashboardtip)
- [DOTAHideAbilityTooltip](#dotahideabilitytooltip)
- [DOTAHideBuffTooltip](#dotahidebufftooltip)
- [DOTAHideDroppedItemTooltip](#dotahidedroppeditemtooltip)
- [DOTAHideEconItemTooltip](#dotahideeconitemtooltip)
- [DOTAHideFacetTooltip](#dotahidefacettooltip)
- [DOTAHideProfileCardTooltip](#dotahideprofilecardtooltip)
- [DOTAHideRankTierTooltip](#dotahideranktiertooltip)
- [DOTAHideRuneTooltip](#dotahiderunetooltip)
- [DOTAHideTextTooltip](#dotahidetexttooltip)
- [DOTAHideTI10EventGameTooltip](#dotahideti10eventgametooltip)
- [DOTAHideTitleImageTextTooltip](#dotahidetitleimagetexttooltip)
- [DOTAHideTitleTextTooltip](#dotahidetitletexttooltip)
- [DOTALiveStreamUpcoming](#dotalivestreamupcoming)
- [DOTALiveStreamVideoLive](#dotalivestreamvideolive)
- [DOTALiveStreamVideoPlaying](#dotalivestreamvideoplaying)
- [DOTAShowAbilityInventoryItemTooltip](#dotashowabilityinventoryitemtooltip)
- [DOTAShowAbilityLevelUpTooltipForEntityIndex](#dotashowabilityleveluptooltipforentityindex)
- [DOTAShowAbilityShopItemTooltip](#dotashowabilityshopitemtooltip)
- [DOTAShowAbilityTooltip](#dotashowabilitytooltip)
- [DOTAShowAbilityTooltipForEntityIndex](#dotashowabilitytooltipforentityindex)
- [DOTAShowAbilityTooltipForFacet](#dotashowabilitytooltipforfacet)
- [DOTAShowAbilityTooltipForGuide](#dotashowabilitytooltipforguide)
- [DOTAShowAbilityTooltipForHero](#dotashowabilitytooltipforhero)
- [DOTAShowAbilityTooltipForLevel](#dotashowabilitytooltipforlevel)
- [DOTAShowBuffTooltip](#dotashowbufftooltip)
- [DOTAShowEconItemTooltip](#dotashoweconitemtooltip)
- [DOTAShowFacetTooltip](#dotashowfacettooltip)
- [DOTAShowProfileCardTooltip](#dotashowprofilecardtooltip)
- [DOTAShowProfileCardTooltipForPartyMember](#dotashowprofilecardtooltipforpartymember)
- [DOTAShowRankTierTooltip](#dotashowranktiertooltip)
- [DOTAShowRuneTooltip](#dotashowrunetooltip)
- [DOTAShowTextTooltip](#dotashowtexttooltip)
- [DOTAShowTextTooltipStyled](#dotashowtexttooltipstyled)
- [DOTAShowTI10EventGameTooltip](#dotashowti10eventgametooltip)
- [DOTAShowTitleImageTextTooltip](#dotashowtitleimagetexttooltip)
- [DOTAShowTitleImageTextTooltipStyled](#dotashowtitleimagetexttooltipstyled)
- [DOTAShowTitleTextTooltip](#dotashowtitletexttooltip)
- [DOTAShowTitleTextTooltipStyled](#dotashowtitletexttooltipstyled)
- [DropInputFocus](#dropinputfocus)
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
- [DismissAllContextMenus](#dismissallcontextmenus)
- [BrowserGoToURL](#browsergotourl)
- [ExternalBrowserGoToURL](#externalbrowsergotourl)
- [UIHideCustomLayoutTooltip](#uihidecustomlayouttooltip)
- [UIShowCustomLayoutParametersTooltip](#uishowcustomlayoutparameterstooltip)
- [DOTAHUDGameDisconnect](#dotahudgamedisconnect)
- [DOTAShowMatchDetails](#dotashowmatchdetails)

</details>

### AddStyle

Panel event: `true`

Add a CSS class to a panel.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### AddStyleAfterDelay

Panel event: `true`

Add a CSS class to a panel after a specified delay.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |
| `preDelay` | `float` |

### AddStyleToEachChild

Panel event: `true`

Add a CSS class to all children of this panel.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### AddTimedStyle

Panel event: `true`

Add a class for a specified duration, with optional pre-delay; clears existing timers when called with same class.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |
| `duration` | `float` |
| `preDelay` | `float` |

### AsyncEvent

Fire another event after a delay (in seconds).

| Argument | Type |
| --- | --- |
| `delay` | `float` |
| `eventToFire` | `event` |

### DOTADisplayDashboardTip

Tip to display, panel to attach to (default 'DefaultTipAttachment')

| Argument | Type |
| --- | --- |
| `string` | `string` |
| `optional` | `string` |

### DOTAHideAbilityTooltip

Panel event: `true`

Hide the ability tooltip

### DOTAHideBuffTooltip

Panel event: `true`

Hide the buff tooltip

### DOTAHideDroppedItemTooltip

Panel event: `true`

Hide the dropped item tooltip

### DOTAHideEconItemTooltip

Panel event: `true`

Hide the econ item tooltip.

### DOTAHideFacetTooltip

Panel event: `true`

Hides the variant tooltip

### DOTAHideProfileCardTooltip

Panel event: `true`

Hide the profile card tooltip.

### DOTAHideRankTierTooltip

Panel event: `true`

Hide the rank tier tooltip.

### DOTAHideRuneTooltip

Panel event: `true`

Hide the rune tooltip

### DOTAHideTextTooltip

Panel event: `true`

Hide the text tooltip

### DOTAHideTI10EventGameTooltip

Panel event: `true`

Hide the ti10 event game tooltip

### DOTAHideTitleImageTextTooltip

Panel event: `true`

Hide the title image text tooltip.

### DOTAHideTitleTextTooltip

Panel event: `true`

Hide the title text tooltip.

### DOTALiveStreamUpcoming

Panel event: `true`

Notify change in RTime32 we expect the stream to start

| Argument | Type |
| --- | --- |
| `time` | `uint32` |

### DOTALiveStreamVideoLive

Panel event: `true`

Notify change in stream state (we detected the stream going live)

| Argument | Type |
| --- | --- |
| `isLive` | `bool` |

### DOTALiveStreamVideoPlaying

Panel event: `true`

Notify change in video state (is it pointing at a live stream page or not)

| Argument | Type |
| --- | --- |
| `isShowingVideo` | `bool` |

### DOTAShowAbilityInventoryItemTooltip

Panel event: `true`

Show tooltip for an item in the entityIndex NPC's inventory.

| Argument | Type |
| --- | --- |
| `entityIndex` | `int32` |
| `inventorySlot` | `int32` |

### DOTAShowAbilityLevelUpTooltipForEntityIndex

Panel event: `true`

Show a tooltip describing what will happen when an ability levels. Current level information comes from the entity specified by the entityIndex.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `entityIndex` | `int32` |

### DOTAShowAbilityShopItemTooltip

Panel event: `true`

Show tooltip for an item in the entityIndex NPC's shop.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `guideName` | `string` |
| `entityIndex` | `int32` |
| `parentId` | `AbilityID_t` |

### DOTAShowAbilityTooltip

Panel event: `true`

Show an ability tooltip.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |

### DOTAShowAbilityTooltipForEntityIndex

Panel event: `true`

Show an ability tooltip. Level information comes from the entity specified by the entityIndex.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `entityIndex` | `int32` |

### DOTAShowAbilityTooltipForFacet

Panel event: `true`

Show an ability tooltip for a specific facet.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `facetName` | `CUtlStringToken` |
| `showVideo` | `bool` |

### DOTAShowAbilityTooltipForGuide

Panel event: `true`

Show an ability tooltip annotated with a particular guide's info.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `guideName` | `string` |
| `arg3` | `HeroID_t` |
| `arg4` | `bool` |

### DOTAShowAbilityTooltipForHero

Panel event: `true`

Show an ability tooltip for the specified hero.

| Argument | Type |
| --- | --- |
| `abilityName` | `string` |
| `heroid` | `HeroID_t` |
| `heroVariant` | `HeroFacetID_t` |
| `arg4` | `bool` |
| `arg5` | `bool` |

### DOTAShowAbilityTooltipForLevel

Panel event: `true`

Show an ability tooltip for a specific level.

| Argument | Type |
| --- | --- |
| `level` | `string` |
| `arg2` | `int32` |

### DOTAShowBuffTooltip

Panel event: `true`

Show a buff tooltip for the specified entityIndex + buff serial.

| Argument | Type |
| --- | --- |
| `entityIndex` | `int32` |
| `buffSerial` | `int32` |
| `onEnemy` | `bool` |

### DOTAShowEconItemTooltip

Panel event: `true`

Show the econ item tooltip for a given item, style, and hero. Use 0 for the default style, and 0 for the default hero.

| Argument | Type |
| --- | --- |
| `itemDef` | `item_definition_index_t` |
| `styleIndex` | `style_index_t` |
| `heroId` | `HeroID_t` |

### DOTAShowFacetTooltip

Panel event: `true`

Shows a variant tooltip for the given hero facet key

| Argument | Type |
| --- | --- |
| `facetKey` | `HeroFacetKey_t` |

### DOTAShowProfileCardTooltip

Panel event: `true`

Show a user's profile card. Use pro name determines whether to use their professional team name if applicable.

| Argument | Type |
| --- | --- |
| `steamId` | `uint64` |
| `useProName` | `bool` |

### DOTAShowProfileCardTooltipForPartyMember

Panel event: `true`

Show a user's profile card including their hero ban choices. Use pro name determines whether to use their professional team name if applicable.

| Argument | Type |
| --- | --- |
| `steamId` | `uint64` |
| `useProName` | `bool` |

### DOTAShowRankTierTooltip

Panel event: `true`

Show the rank tier tooltip for a user

| Argument | Type |
| --- | --- |
| `steamId` | `uint64` |

### DOTAShowRuneTooltip

Panel event: `true`

Show a rune tooltip in the X Y location for the rune type

| Argument | Type |
| --- | --- |
| `x` | `int32` |
| `y` | `int32` |
| `runeType` | `int32` |

### DOTAShowTextTooltip

Panel event: `true`

Show a tooltip with the given text.

| Argument | Type |
| --- | --- |
| `text` | `string` |

### DOTAShowTextTooltipStyled

Panel event: `true`

Show a tooltip with the given text. Also apply a CSS class named "style" to allow custom styling.

| Argument | Type |
| --- | --- |
| `text` | `string` |
| `style` | `panoramasymbol` |

### DOTAShowTI10EventGameTooltip

Panel event: `true`

Show a ti10 event game tooltip

| Argument | Type |
| --- | --- |
| `ti10EventGameTooltipInfoT` | `struct` |

### DOTAShowTitleImageTextTooltip

Panel event: `true`

Show a tooltip with the given title, image, and text.

| Argument | Type |
| --- | --- |
| `title` | `string` |
| `imagePath` | `string` |
| `text` | `string` |

### DOTAShowTitleImageTextTooltipStyled

Panel event: `true`

Show a tooltip with the given title, image, and text. Also apply a CSS class named "style" to allow custom styling.

| Argument | Type |
| --- | --- |
| `title` | `string` |
| `imagePath` | `string` |
| `text` | `string` |
| `style` | `panoramasymbol` |

### DOTAShowTitleTextTooltip

Panel event: `true`

Show a tooltip with the given title and text.

| Argument | Type |
| --- | --- |
| `title` | `string` |
| `text` | `string` |

### DOTAShowTitleTextTooltipStyled

Panel event: `true`

Show a tooltip with the given title and text. Also apply a CSS class named "style" to allow custom styling.

| Argument | Type |
| --- | --- |
| `title` | `string` |
| `text` | `string` |
| `style` | `panoramasymbol` |

### DropInputFocus

Panel event: `true`

Drop focus entirely from the window containing this panel.

### IfHasClassEvent

Panel event: `true`

Fire another event if this panel has a given class.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |
| `eventToFire` | `event` |

### IfHoverOtherEvent

Panel event: `true`

Fire another event if currently hovering over a panel with the given ID.

| Argument | Type |
| --- | --- |
| `otherPanelId` | `string` |
| `eventToFire` | `event` |

### IfNotHasClassEvent

Panel event: `true`

Fire another event if this panel does not have a given class.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |
| `eventToFire` | `event` |

### IfNotHoverOtherEvent

Panel event: `true`

Fire another event if not currently hovering over a panel with the given ID.

| Argument | Type |
| --- | --- |
| `otherPanelId` | `string` |
| `eventToFire` | `event` |

### MovePanelDown

Panel event: `true`

Move down from the panel. By default, this will change the focus position, but other panel types may implement this differently.

| Argument | Type |
| --- | --- |
| `repeatCount` | `int32` |

### MovePanelLeft

Panel event: `true`

Move left from the panel. By default, this will change the focus position, but other panel types may implement this differently.

| Argument | Type |
| --- | --- |
| `repeatCount` | `int32` |

### MovePanelRight

Panel event: `true`

Move right from the panel. By default, this will change the focus position, but other panel types may implement this differently.

| Argument | Type |
| --- | --- |
| `repeatCount` | `int32` |

### MovePanelUp

Panel event: `true`

Move up from the panel. By default, this will change the focus position, but other panel types may implement this differently.

| Argument | Type |
| --- | --- |
| `repeatCount` | `int32` |

### PageDown

Scroll the panel down by one page.

### PageLeft

Scroll the panel left by one page.

### PagePanelDown

Panel event: `true`

Scroll the panel down by one page.

### PagePanelLeft

Panel event: `true`

Scroll the panel left by one page.

### PagePanelRight

Panel event: `true`

Scroll the panel left by one page.

### PagePanelUp

Panel event: `true`

Scroll the panel up by one page.

### PageRight

Scroll the panel right by one page.

### PageUp

Scroll the panel up by one page.

### RemoveStyle

Panel event: `true`

Remove a CSS class from a panel.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### RemoveStyleAfterDelay

Panel event: `true`

Remove a CSS class from a panel after a specified delay.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |
| `preDelay` | `float` |

### RemoveStyleFromEachChild

Panel event: `true`

Remove a CSS class from all children of this panel.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### ScrollDown

Scroll the panel down by one line.

### ScrollLeft

Scroll the panel left by one line.

### ScrollPanelDown

Panel event: `true`

Scroll the panel down by one line.

### ScrollPanelLeft

Panel event: `true`

Scroll the panel left by one line.

### ScrollPanelRight

Panel event: `true`

Scroll the panel right by one line.

### ScrollPanelUp

Panel event: `true`

Scroll the panel up by one line.

### ScrollRight

Scroll the panel right by one line.

### ScrollToBottom

Panel event: `true`

Scroll this panel to the bottom.

### ScrollToTop

Panel event: `true`

Scroll this panel to the top.

### ScrollUp

Scroll the panel up by one line.

### SetChildPanelsSelected

Panel event: `true`

Set whether any child panels are :selected.

| Argument | Type |
| --- | --- |
| `selected` | `bool` |

### SetInputFocus

Panel event: `true`

Set focus to this panel.

### SetPanelEnabled

Panel event: `true`

Sets whether the given panel is enabled

| Argument | Type |
| --- | --- |
| `enabled` | `bool` |

### SetPanelSelected

Panel event: `true`

Set whether this panel is :selected.

| Argument | Type |
| --- | --- |
| `selected` | `bool` |

### SwitchStyle

Panel event: `true`

Switch which class the panel has for a given attribute slot. Allows easily changing between multiple states.

| Argument | Type |
| --- | --- |
| `slot` | `panoramasymbol` |
| `class` | `panoramasymbol` |

### TogglePanelSelected

Panel event: `true`

Toggle whether this panel is :selected.

### ToggleStyle

Panel event: `true`

Toggle whether a panel has the given CSS class.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### TriggerStyle

Panel event: `true`

Remove then immediately add back a CSS class from a panel. Useful to re-trigger events like animations or sound effects.

| Argument | Type |
| --- | --- |
| `class` | `panoramasymbol` |

### DismissAllContextMenus

### BrowserGoToURL

| Argument | Type |
| --- | --- |
| `url` | `string` |

### ExternalBrowserGoToURL

| Argument | Type |
| --- | --- |
| `url` | `string` |

### UIHideCustomLayoutTooltip

Panel event: `true`

| Argument | Type |
| --- | --- |
| `name` | `string` |

### UIShowCustomLayoutParametersTooltip

Panel event: `true`

| Argument | Type |
| --- | --- |
| `name` | `string` |
| `layoutPath` | `string` |
| `parameters` | `string` |

### DOTAHUDGameDisconnect

### DOTAShowMatchDetails

| Argument | Type |
| --- | --- |
| `matchId` | `int32` |
