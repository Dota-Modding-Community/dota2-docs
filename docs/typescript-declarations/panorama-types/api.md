# Panorama API declarations



29 interfaces, 4 type aliases and 2 namespaces.

## Contents

<details><summary>Interfaces</summary>

- [AsyncWebRequestData](#asyncwebrequestdata)
- [AsyncWebRequestResponse](#asyncwebrequestresponse)
- [CDOTA_PanoramaScript_CustomNetTables](#cdota_panoramascript_customnettables)
- [CDOTA_PanoramaScript_EventData](#cdota_panoramascript_eventdata)
- [CDOTA_PanoramaScript_GameEvents](#cdota_panoramascript_gameevents)
- [CDOTA_PanoramaScript_GameUI](#cdota_panoramascript_gameui)
- [CDOTA_PanoramaScript_LocalInventory](#cdota_panoramascript_localinventory)
- [ContextualTip](#contextualtip)
- [CPanoramaScript_SteamFriends](#cpanoramascript_steamfriends)
- [CPanoramaScript_SteamUGC](#cpanoramascript_steamugc)
- [CPanoramaScript_SteamUtils](#cpanoramascript_steamutils)
- [CPanoramaScript_VRUtils](#cpanoramascript_vrutils)
- [CScriptBindingPR_Abilities](#cscriptbindingpr_abilities)
- [CScriptBindingPR_Buffs](#cscriptbindingpr_buffs)
- [CScriptBindingPR_Entities](#cscriptbindingpr_entities)
- [CScriptBindingPR_Game](#cscriptbindingpr_game)
- [CScriptBindingPR_Items](#cscriptbindingpr_items)
- [CScriptBindingPR_Particles](#cscriptbindingpr_particles)
- [CScriptBindingPR_Players](#cscriptbindingpr_players)
- [CustomGameEventDeclarations](#customgameeventdeclarations)
- [CustomNetTableDeclarations](#customnettabledeclarations)
- [CustomUIConfig](#customuiconfig)
- [DollarStatic](#dollarstatic)
- [DragSettings](#dragsettings)
- [MapInfo](#mapinfo)
- [PlayerInfo](#playerinfo)
- [PrepareUnitOrdersArgument](#prepareunitordersargument)
- [ScreenEntity](#screenentity)
- [TeamDetails](#teamdetails)

</details>
<details><summary>Namespaces</summary>

- [GameEvents](#gameevents)
- [PanoramaEvents](#panoramaevents)

</details>

## Interfaces

### AsyncWebRequestData

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `type?` | `string` |  |
| `timeout?` | `number` |  |
| `headers?` | `object` |  |
| `data?` | `object` |  |

**Other members**

| Member | Description |
| --- | --- |
| `success?(response: any, result: 'success', statusText: string): void` |  |
| `error?(data: AsyncWebRequestResponse, result: 'error', statusText: string): void` |  |
| `complete?(data: AsyncWebRequestResponse, result: 'success' \| 'error'): void` |  |

### AsyncWebRequestResponse

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `statusText` | `string` |  |
| `responseText` | `string \| null` |  |
| `status` | `number` |  |

### CDOTA_PanoramaScript_CustomNetTables

**Methods**

| Method | Description |
| --- | --- |
| `GetTableValue< TName extends keyof CustomNetTableDeclarations, T extends CustomNetTableDeclarations[TName], K extends keyof T, >( pTableName: TName, pKeyName: K, ): NetworkedData<T[K]> \| null` | Get a key from a custom net table |
| `GetAllTableValues<TName extends keyof CustomNetTableDeclarations, T extends CustomNetTableDeclarations[TName]>( pTableName: TName, ): { [K in keyof T]: { key: K; value: NetworkedData<T[K]> } }[keyof T][]` | Get all values from a custom net table |
| `SubscribeNetTableListener< TName extends keyof CustomNetTableDeclarations, T extends CustomNetTableDeclarations[TName], >( tableName: TName, callback: (tableName: TName, key: keyof T, value: NetworkedData<T[keyof T]>) => void, ): NetTableListenerID` | Register a callback when a particular custom net table changes |
| `UnsubscribeNetTableListener(nCallbackHandle: NetTableListenerID): void` | Unsubscribe from a game event |

### CDOTA_PanoramaScript_EventData

**Methods**

| Method | Description |
| --- | --- |
| `GetEventActionScore(unEventID: number, unActionID: number): number` | Get the score of an EventAction. |
| `GetPeriodicResourceUsed(unPeriodicResourceID: number): number` | Get a periodic resource value used. |
| `GetPeriodicResourceMax(unPeriodicResourceID: number): number` | Get a periodic resource value max. |
| `IsFirstRunThisEvent(): boolean` | Is this the first time we've launched this season? |

### CDOTA_PanoramaScript_GameEvents

**Methods**

| Method | Description |
| --- | --- |
| `Subscribe<T extends string \| object>( pEventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations \| keyof GameEventDeclarations, funcVal: (event: NetworkedData<GameEvents.InferGameEventType<T, object>>) => void, ): GameEventListenerID` | Subscribe to a game event.<br><br>**Type parameters:**<br><br>- T Either a name of the event (inferred automatically) or the type of a custom event.<br><br>**Example:**<br><br>`// Custom event with separate definition`<br>`interface CustomGameEventDeclarations {`<br>`custom_event: { field: string };`<br>`}`<br>`GameEvents.Subscribe("custom_event", event => $.Msg(event.field));`<br><br>**Example:**<br><br>`// Custom event with inline type definition`<br>`GameEvents.Subscribe<{ field: string }>("custom_event", event => $.Msg(event.field));`<br><br>**Example:**<br><br>`// Builtin event`<br>`GameEvents.Subscribe("npc_spawned", event => $.Msg(event.entindex));` |
| `Unsubscribe(nCallbackHandle: GameEventListenerID): void` | Unsubscribe from a game event.<br><br>**Parameters:**<br><br>- nCallbackHandle Return value of `GameEvents.Subscribe`.<br> |
| `SendCustomGameEventToServer<T extends string \| object>( pEventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, eventData: GameEvents.InferCustomGameEventType<T, never>, ): void` | Send a custom game event.<br><br>**Example:**<br><br>`// Separate definition`<br>`interface CustomGameEventDeclarations {`<br>`custom_event: { field: string };`<br>`}`<br>`GameEvents.SendCustomGameEventToServer("custom_event", { field: "foo" });`<br><br>**Example:**<br><br>`// Inline type definition`<br>`GameEvents.SendCustomGameEventToServer<{ field: string }>("custom_event", { field: "foo" });` |
| `SendCustomGameEventToAllClients<T extends string \| object>( pEventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, eventData: GameEvents.InferCustomGameEventType<T, never>, ): void` | Send a custom game event to the server, which will send it to all clients. |
| `SendCustomGameEventToClient<T extends string \| object>( pEventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, playerIndex: PlayerID, eventData: GameEvents.InferCustomGameEventType<T, never>, ): void` | Send a custom game event to the server, which will send it to all clients. |
| `SendEventClientSide<TName extends keyof GameEventDeclarations>( pEventName: TName, eventData: GameEventDeclarations[TName], ): void` | Send a client-side event using gameeventmanager. |

### CDOTA_PanoramaScript_GameUI

**Methods**

| Method | Description |
| --- | --- |
| `SetDefaultUIEnabled(nElementType: number, bVisible: boolean): void` | Control whether the default UI is enabled |
| `SavePersistentEventGameData(unknown: any): void` | Save persistent data used by an event game |
| `LoadPersistentEventGameData(...unknown: any[]): void` | Load persistent data used by an event game |
| `CustomUIConfig(): CustomUIConfig` | Get the current UI configuration |
| `PingMinimapAtLocation(vec3: [number, number, number]): void` | Create a minimap ping at the given location |
| `SetMouseCallback(callbackFn: (event: MouseEvent, value: MouseButton \| MouseScrollDirection) => boolean): void` | Install a mouse input filter |
| `EnableAliMode(bEnable: boolean, nPort: number, offsetVal: number, flScale: number): void` |  |
| `GetCursorPosition(): [number, number]` | Get the current mouse position. |
| `FindScreenEntities(screenPos: [number, number]): ScreenEntity[]` | Return the entity index of the entity under the given screen position. |
| `GetScreenWorldPosition(screenPos: [number, number]): [number, number, number] \| null` | Get the world position of the screen position, or null if the cursor is out of the world. |
| `WasMousePressed(nButtonNum: MouseButton): boolean` | Install a mouse input filter |
| `WasMouseDoublePressed(nButtonNum: MouseButton): boolean` | Install a mouse input filter |
| `IsMouseDown(nButtonNum: MouseButton): boolean` | Install a mouse input filter |
| `IsShiftDown(): boolean` | Is the shift button pressed? |
| `IsAltDown(): boolean` | Is the alt button pressed? |
| `IsControlDown(): boolean` | Is the control button pressed? |
| `GetClickBehaviors(): CLICK_BEHAVIORS` | Get the current UI click interaction mode. |
| `SelectUnit(nEntityIndex: EntityIndex, bAddToGroup: boolean): void` | Select a unit, adding it to the group or replacing the current selection. |
| `GetCameraLookAtPosition(): [number, number, number]` | Get the current look at position. |
| `GetCameraPosition(): [number, number, number]` | Get the current camera position. |
| `GetCameraLookAtPositionHeightOffset(): number` | Get the current look at position height offset. |
| `SetCameraPitchMin(flPitchMin: number): void` | Set the minimum camera pitch angle. |
| `SetCameraPitchMax(flPitchMax: number): void` | Set the maximum camera pitch angle. |
| `SetCameraYaw(flCameraYaw: number): void` | Set the camera's yaw. |
| `GetCameraYaw(): number` | Get the camera's yaw. |
| `SetCameraLookAtPositionHeightOffset(flCameraLookAtHeightOffset: number): void` | Offset the camera's look at point. |
| `SetCameraPositionFromLateralLookAtPosition(x: number, y: number): void` | Set the camera from a lateral position. |
| `SetCameraTerrainAdjustmentEnabled(bEnabled: boolean): void` | Set whether the camera should automatically adjust to average terrain height. |
| `SetCameraDistance(flDistance: number): void` | Set the camera distance from the look at point. |
| `SetRenderBottomInsetOverride(nInset: number): void` | Set the gap between the bottom of the screen and the game rendering viewport. (Value expressed as pixels in a normalized 1024x768 viewport.) |
| `SetRenderTopInsetOverride(nInset: number): void` | Set the gap between the top of the screen and the game rendering viewport. (Value expressed as pixels in a normalized 1024x768 viewport.) |
| `SetCameraTarget(nTargetEntIndex: EntityIndex): void` | Set the camera target for the local player, or -1 to clear. |
| `SetCameraTargetPosition(vec3: [number, number, number], flLerp: number): void` | Set the camera target as position for the local player over specified lerp. |
| `MoveCameraToEntity(nTargetEntIndex: EntityIndex): void` | Moves the camera to an entity, but doesn't lock the camera on that entity. |
| `WorldToScreenXYClamped(vec3: [number, number, number]): [number, number, 0]` | Converts the specified x,y,z world co-ordinate into an x,y screen coordinate. Will clamp position to always be in front of camera.  Position returned as 0->1.0 |
| `GetPlayerScoreboardScore(pszScoreboardName: string): number` | Get the current players scoreboard score for the specified zone. |
| `SendCustomHUDError(pszErrorText: string, pszErrorSound: string): void` | Send a custom client side error message with passed string and soundevent. |
| `ReplaceDOTAAbilitySpecialValues(abilityName: string, text: string): string \| null` | Given a passed ability, replace the special value variables in the passed localized text.<br>Returns `null` if `abilityName` is invalid. |
| `GetUnitLocToken(name: string): string` | Returns the localization token to use for a particular unit, given the unit's name. |
| `GetUnitNameLocalized(name: string): string` | Get the localized version of a unit's name. |
| `ConstructNumberString(n: number): string` | Creates a localized version of the number |
| `AreTipsAvailable(): boolean` | Query to check if Tips are available for the local player |
| `IsPlayerTippable(iPlayerID: number): boolean` | Query to see if the local player can tip a specific player |
| `TipPlayer(iPlayerID: number): void` | Tip a player |
| `DisplayCustomContextualTip(tip: ContextualTip): void` | Display a custom contextual tip (wizard tip) with specific loc string and duration |
| `SetupDOTATalentNameLabel(panel: LabelPanel, sAbilityName: string): void` | Set the text of a passed label for a DOTA Talent using ability values. |
| `IsAbilityDOTATalent(pszAbilityName: string): boolean` | Returns true if the passed ability is a talent. |

### CDOTA_PanoramaScript_LocalInventory

**Methods**

| Method | Description |
| --- | --- |
| `HasItemByDefinition(nDefIndex: number): boolean` | Does the player have an inventory item of a given item definition index? |

### ContextualTip

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `TipAnnotation?` | `string` |  |
| `DisplayDuration?` | `number` |  |
| `PanoramaClasses?` | `string[]` |  |
| `PanoramaSnippet?` | `string` |  |
| `ReferencedAbilities?` | `string[]` |  |
| `ReferencedUnits` | `string[]` |  |
| `Variant?` | `number` |  |
| `ForceAnnotation?` | `boolean` |  |
| `IntParameter?` | `number` |  |
| `IntParameter2?` | `number` |  |
| `FloatParameter?` | `number` |  |
| `FloatParameter2?` | `number` |  |
| `StringParameter?` | `string` |  |
| `StringParameter2?` | `string` |  |

### CPanoramaScript_SteamFriends

**Methods**

| Method | Description |
| --- | --- |
| `RequestPersonaName(pchSteamID: string, funcVal: any): string` | Requests the user's persona name |
| `SetLargeAvatarImage(...unknown: any[]): void` | Sets the avatar image on the image panel |

### CPanoramaScript_SteamUGC

**Methods**

| Method | Description |
| --- | --- |
| `SubscribeItem(pPublishedFileID: string, funcVal: any): void` | Subscribe to a piece of UGC |
| `UnsubscribeItem(pPublishedFileID: string, funcVal: any): void` | Unsubscribe to a piece of UGC |
| `GetSubscriptionInfo(pPublishedFileID: string): any` | Get a key from a custom net table |
| `SetUserItemVote(pPublishedFileID: string, bVoteUp: boolean, funcVal: any): any` | Vote on a piece of UGC |
| `GetUserItemVote(pPublishedFileID: string, funcVal: any): any` | Get the user's vote on a peice of UGC |
| `AddToFavorites(pPublishedFileID: string, funcVal: any): any` | Add an item to the user's favorites list |
| `RemoveFromFavorites(pPublishedFileID: string, funcVal: any): any` | Remove an item from the user's favorites list |
| `CreateQueryAllUGCRequest(eQueryType: number, eMatchingeMatchingUGCTypeFileType: number, unPage: number): any` | Create a request to query Steam for all UGC |
| `CreateQueryUGCDetailsRequest(pPublishedFileIDs: string[]): any` | Creqte a request to query Steam for specific UGC |
| `AddRequiredTagToQuery(handle: number, pchTag: string): any` | Adds a required tag to the query |
| `AddExcludedTagToQuery(handle: number, pchTag: string): any` | Adds an excluded tag to the query |
| `ConfigureQuery(handle: number, jsObject: any): any` | Adds a required tag to the query |
| `SendUGCQuery(handle: number, funcVal: any): any` | Sends the prepared query |
| `RegisterDownloadItemResultCallback(pPublishedFileID: string, funcVal: any): any` | Register a callback to be called when the item is downloaded |

### CPanoramaScript_SteamUtils

**Methods**

| Method | Description |
| --- | --- |
| `GetConnectedUniverse(): number` | Returns the connected universe |
| `GetAppID(): number` | Returns the appid of the current app |

### CPanoramaScript_VRUtils

**Methods**

| Method | Description |
| --- | --- |
| `GetVRAppPropertyData(nAppID: number): any` | Get application properties for a VR app with the specified appID |
| `LaunchSteamApp(nAppID: number, pszLaunchSource: string): void` | Launches a Steam Application using OpenVR. |

### CScriptBindingPR_Abilities

**Methods**

| Method | Description |
| --- | --- |
| `GetAbilityName(nEntityIndex: AbilityEntityIndex): string` |  |
| `GetAbilityTextureName(nEntityIndex: AbilityEntityIndex): string` |  |
| `GetAssociatedPrimaryAbilities(nEntityIndex: AbilityEntityIndex): AbilityEntityIndex[]` |  |
| `GetAssociatedSecondaryAbilities(nEntityIndex: AbilityEntityIndex): AbilityEntityIndex[]` |  |
| `GetHotkeyOverride(nEntityIndex: AbilityEntityIndex): string` |  |
| `GetIntrinsicModifierName(nEntityIndex: AbilityEntityIndex): string` |  |
| `GetSharedCooldownName(nEntityIndex: AbilityEntityIndex): string` |  |
| `AbilityReady(nEntityIndex: AbilityEntityIndex): number` |  |
| `CanAbilityBeUpgraded(nEntityIndex: AbilityEntityIndex): AbilityLearnResult_t` |  |
| `CanBeExecuted(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `GetAbilityDamage(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityDamageType(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityTargetFlags(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityTargetTeam(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityTargetType(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityType(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetBehavior(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCastRange(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetChannelledManaCostPerSecond(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCurrentCharges(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCurrentAbilityCharges(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetEffectiveLevel(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetHeroLevelRequiredToUpgrade(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetLevel(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetManaCost(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetMaxLevel(nEntityIndex: AbilityEntityIndex): number` |  |
| `AttemptToUpgrade(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `CanLearn(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `GetAutoCastState(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `GetToggleState(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `HasScepterUpgradeTooltip(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsActivated(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsActivatedChanging(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsAttributeBonus(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsAutocast(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsCooldownReady(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsDisplayedAbility(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsHidden(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsHiddenWhenStolen(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsInAbilityPhase(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsItem(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsMarkedAsDirty(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsMuted(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsOnCastbar(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsOnLearnbar(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsOwnersGoldEnough(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsOwnersGoldEnoughForUpgrade(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsOwnersManaEnough(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsPassive(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsRecipe(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsSharedWithTeammates(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsStealable(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsStolen(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `IsToggle(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `UsesAbilityCharges(nEntityIndex: AbilityEntityIndex): boolean` |  |
| `GetAOERadius(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetBackswingTime(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCastPoint(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetChannelStartTime(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetChannelTime(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCooldown(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCooldownLength(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCooldownTime(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetCooldownTimeRemaining(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetDuration(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetUpgradeBlend(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetAbilityChargeRestoreTimeRemaining(nEntityIndex: AbilityEntityIndex): number` |  |
| `GetLocalPlayerActiveAbility(): AbilityEntityIndex` | Get the local player's current active ability. (Pre-cast targetting state.) |
| `GetCaster(nAbilityIndex: AbilityEntityIndex): EntityIndex` |  |
| `GetCustomValueFor(nAbilityIndex: AbilityEntityIndex, pszAbilityVarName: string): number` |  |
| `GetLevelSpecialValueFor(nAbilityIndex: AbilityEntityIndex, szName: string, nLevel: number): number` |  |
| `GetSpecialValueFor(nAbilityIndex: AbilityEntityIndex, szName: string): number` |  |
| `IsCosmetic(nAbilityIndex: AbilityEntityIndex, nTargetEntityIndex: EntityIndex): boolean` |  |
| `ExecuteAbility(nAbilityEntIndex: AbilityEntityIndex, nCasterEntIndex: EntityIndex, bIsQuickCast: boolean): boolean` | Attempt to execute the specified ability (Equivalent to clicking the ability in the HUD action bar) |
| `CreateDoubleTapCastOrder(nAbilityEntIndex: AbilityEntityIndex, nCasterEntIndex: EntityIndex): void` | Attempt to double-tap (self-cast) the specified ability (Equivalent to double-clicking the ability in the HUD action bar) |
| `PingAbility(nAbilityIndex: AbilityEntityIndex): void` | Ping the specified ability (Equivalent to alt-clicking the ability in the HUD action bar) |
| `GetKeybind(nAbilityEntIndex: AbilityEntityIndex): string` | Returns the keybind (as a string) for the specified ability. |
| `GetMaxAbilityCharges(nAbilityEntIndex: number): number` | Get the max ability charge count. |

### CScriptBindingPR_Buffs

**Methods**

| Method | Description |
| --- | --- |
| `GetName(nEntityIndex: EntityIndex, nBuffIndex: BuffID): string` | Returns the name of the modifier. |
| `GetClass(nEntityIndex: EntityIndex, nBuffIndex: BuffID): string` | Returns the classname of the modifier. |
| `GetTexture(nEntityIndex: EntityIndex, nBuffIndex: BuffID): string` | Returns the modifier icon texture. |
| `GetDuration(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the total duration of the modifier. |
| `GetDieTime(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the time at which the modifier will expire. |
| `GetRemainingTime(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the time until the modifier expires. |
| `GetElapsedTime(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the time elapsed since the creation of the modifier. |
| `GetCreationTime(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the time at which the modifier was created. |
| `GetStackCount(nEntityIndex: EntityIndex, nBuffIndex: BuffID): number` | Returns the keybind (as a string) for the specified ability. |
| `IsDebuff(nEntityIndex: EntityIndex, nBuffIndex: BuffID): boolean` | Returns true if the modifier is a debuff (red icon), false otherwise. |
| `IsHidden(nEntityIndex: EntityIndex, nBuffIndex: BuffID): boolean` | Returns the keybind (as a string) for the specified ability. |
| `GetCaster(nEntityIndex: EntityIndex, nBuffIndex: BuffID): EntityIndex` | Returns the entity that created the modifier (possibly on another entity). |
| `GetParent(nEntityIndex: EntityIndex, nBuffIndex: BuffID): EntityIndex` | Returns the entity to which the modifier is applied. |
| `GetAbility(nEntityIndex: EntityIndex, nBuffIndex: BuffID): AbilityEntityIndex` | Returns the ability associated with the modifier. |

### CScriptBindingPR_Entities

**Methods**

| Method | Description |
| --- | --- |
| `GetAbsOrigin(nEntityIndex: EntityIndex): [number, number, number]` | Get the world origin of the entity. |
| `GetAbsAngles(nEntityIndex: EntityIndex): [number, number, number]` | Get the world angles of the entity. |
| `GetForward(nEntityIndex: EntityIndex): [number, number, number]` | Get the forward vector of the entity. |
| `GetRight(nEntityIndex: EntityIndex): [number, number, number]` | Get the right vector of the entity. |
| `GetUp(nEntityIndex: EntityIndex): [number, number, number]` | Get the up vector of the entity. |
| `GetAllBuildingEntities(): EntityIndex[]` | Get all the building entities. |
| `GetAllHeroEntities(): EntityIndex[]` | Get all the hero entities. |
| `GetAllEntitiesByName(pszName: string): EntityIndex[]` | Get all the entities with a given name. |
| `GetAllEntitiesByClassname(pszName: string): EntityIndex[]` | Get all the entities with a given classname. |
| `GetAllCreatureEntities(): EntityIndex[]` | Get all the creature entities. |
| `GetAllEntities(): EntityIndex[]` | Get all the entities. |
| `GetPlayerOwnerID(nEntityIndex: EntityIndex): PlayerID` | Get the ID of the player owning the given entity. |
| `CanBeDominated(nEntityIndex: EntityIndex): boolean` |  |
| `HasAttackCapability(nEntityIndex: EntityIndex): boolean` |  |
| `HasCastableAbilities(nEntityIndex: EntityIndex): boolean` |  |
| `HasFlyingVision(nEntityIndex: EntityIndex): boolean` |  |
| `HasFlyMovementCapability(nEntityIndex: EntityIndex): boolean` |  |
| `HasGroundMovementCapability(nEntityIndex: EntityIndex): boolean` |  |
| `HasMovementCapability(nEntityIndex: EntityIndex): boolean` |  |
| `HasScepter(nEntityIndex: EntityIndex): boolean` |  |
| `HasUpgradeableAbilities(nEntityIndex: EntityIndex): boolean` |  |
| `HasUpgradeableAbilitiesThatArentMaxed(nEntityIndex: EntityIndex): boolean` |  |
| `IsAlive(nEntityIndex: EntityIndex): boolean` |  |
| `IsAncient(nEntityIndex: EntityIndex): boolean` |  |
| `IsAttackImmune(nEntityIndex: EntityIndex): boolean` |  |
| `IsBarracks(nEntityIndex: EntityIndex): boolean` |  |
| `IsBlind(nEntityIndex: EntityIndex): boolean` |  |
| `IsBoss(nEntityIndex: EntityIndex): boolean` |  |
| `IsBossCreature(nEntityIndex: EntityIndex): boolean` |  |
| `IsRoshan(nEntityIndex: EntityIndex): boolean` |  |
| `IsBuilding(nEntityIndex: EntityIndex): boolean` |  |
| `IsCommandRestricted(nEntityIndex: EntityIndex): boolean` |  |
| `IsConsideredHero(nEntityIndex: EntityIndex): boolean` |  |
| `IsControllableByAnyPlayer(nEntityIndex: EntityIndex): boolean` |  |
| `IsCourier(nEntityIndex: EntityIndex): boolean` |  |
| `IsCreature(nEntityIndex: EntityIndex): boolean` |  |
| `IsCreep(nEntityIndex: EntityIndex): boolean` |  |
| `IsCreepHero(nEntityIndex: EntityIndex): boolean` |  |
| `IsDeniable(nEntityIndex: EntityIndex): boolean` |  |
| `IsDominated(nEntityIndex: EntityIndex): boolean` |  |
| `IsEnemy(nEntityIndex: EntityIndex): boolean` |  |
| `IsEvadeDisabled(nEntityIndex: EntityIndex): boolean` |  |
| `IsFort(nEntityIndex: EntityIndex): boolean` |  |
| `IsFrozen(nEntityIndex: EntityIndex): boolean` |  |
| `IsGeneratedByEconItem(nEntityIndex: EntityIndex): boolean` |  |
| `IsHallofFame(nEntityIndex: EntityIndex): boolean` |  |
| `IsDisarmed(nEntityIndex: EntityIndex): boolean` |  |
| `IsHero(nEntityIndex: EntityIndex): boolean` |  |
| `IsHexed(nEntityIndex: EntityIndex): boolean` |  |
| `IsIllusion(nEntityIndex: EntityIndex): boolean` |  |
| `IsInRangeOfFountain(nEntityIndex: EntityIndex): boolean` |  |
| `IsInventoryEnabled(nEntityIndex: EntityIndex): boolean` |  |
| `IsInvisible(nEntityIndex: EntityIndex): boolean` |  |
| `IsInvulnerable(nEntityIndex: EntityIndex): boolean` |  |
| `IsLaneCreep(nEntityIndex: EntityIndex): boolean` |  |
| `IsLowAttackPriority(nEntityIndex: EntityIndex): boolean` |  |
| `IsMagicImmune(nEntityIndex: EntityIndex): boolean` |  |
| `IsMuted(nEntityIndex: EntityIndex): boolean` |  |
| `IsNeutralUnitType(nEntityIndex: EntityIndex): boolean` |  |
| `IsNightmared(nEntityIndex: EntityIndex): boolean` |  |
| `IsOther(nEntityIndex: EntityIndex): boolean` |  |
| `IsOutOfGame(nEntityIndex: EntityIndex): boolean` |  |
| `IsOwnedByAnyPlayer(nEntityIndex: EntityIndex): boolean` |  |
| `IsPhantom(nEntityIndex: EntityIndex): boolean` |  |
| `IsRangedAttacker(nEntityIndex: EntityIndex): boolean` |  |
| `IsRealHero(nEntityIndex: EntityIndex): boolean` |  |
| `IsRooted(nEntityIndex: EntityIndex): boolean` |  |
| `IsSelectable(nEntityIndex: EntityIndex): boolean` |  |
| `IsShop(nEntityIndex: EntityIndex): boolean` |  |
| `IsSilenced(nEntityIndex: EntityIndex): boolean` |  |
| `IsSpeciallyDeniable(nEntityIndex: EntityIndex): boolean` |  |
| `IsStunned(nEntityIndex: EntityIndex): boolean` |  |
| `IsSummoned(nEntityIndex: EntityIndex): boolean` |  |
| `IsTower(nEntityIndex: EntityIndex): boolean` |  |
| `IsUnselectable(nEntityIndex: EntityIndex): boolean` |  |
| `IsWard(nEntityIndex: EntityIndex): boolean` |  |
| `IsZombie(nEntityIndex: EntityIndex): boolean` |  |
| `NoHealthBar(nEntityIndex: EntityIndex): boolean` |  |
| `NoTeamMoveTo(nEntityIndex: EntityIndex): boolean` |  |
| `NoTeamSelect(nEntityIndex: EntityIndex): boolean` |  |
| `NotOnMinimap(nEntityIndex: EntityIndex): boolean` |  |
| `NotOnMinimapForEnemies(nEntityIndex: EntityIndex): boolean` |  |
| `NoUnitCollision(nEntityIndex: EntityIndex): boolean` |  |
| `PassivesDisabled(nEntityIndex: EntityIndex): boolean` |  |
| `ProvidesVision(nEntityIndex: EntityIndex): boolean` |  |
| `UsesHeroAbilityNumbers(nEntityIndex: EntityIndex): boolean` |  |
| `IsMoving(nEntityIndex: EntityIndex): boolean` |  |
| `GetAbilityCount(nEntityIndex: EntityIndex): number` |  |
| `GetCombatClassAttack(nEntityIndex: EntityIndex): number` |  |
| `GetCombatClassDefend(nEntityIndex: EntityIndex): number` |  |
| `GetCurrentVisionRange(nEntityIndex: EntityIndex): number` |  |
| `GetDamageBonus(nEntityIndex: EntityIndex): number` |  |
| `GetDamageMax(nEntityIndex: EntityIndex): number` |  |
| `GetDamageMin(nEntityIndex: EntityIndex): number` |  |
| `GetDayTimeVisionRange(nEntityIndex: EntityIndex): number` |  |
| `GetHealth(nEntityIndex: EntityIndex): number` |  |
| `GetHealthPercent(nEntityIndex: EntityIndex): number` |  |
| `GetHealthThinkRegen(nEntityIndex: EntityIndex): number` |  |
| `GetLevel(nEntityIndex: EntityIndex): number` |  |
| `GetMaxHealth(nEntityIndex: EntityIndex): number` |  |
| `GetNightTimeVisionRange(nEntityIndex: EntityIndex): number` |  |
| `GetStates(nEntityIndex: EntityIndex): modifierstate[]` |  |
| `GetTotalPurchasedUpgradeGoldCost(nEntityIndex: EntityIndex): number` |  |
| `GetTeamNumber(nEntityIndex: EntityIndex): DOTATeam_t` |  |
| `GetHealthBarOffset(nEntityIndex: EntityIndex): number` |  |
| `GetAttackRange(nEntityIndex: EntityIndex): number` |  |
| `GetAttackSpeed(nEntityIndex: EntityIndex): number` |  |
| `GetAttacksPerSecond(nEntityIndex: EntityIndex): number` |  |
| `GetBaseAttackTime(nEntityIndex: EntityIndex): number` |  |
| `GetBaseMagicalResistanceValue(nEntityIndex: EntityIndex): number` |  |
| `GetBaseMoveSpeed(nEntityIndex: EntityIndex): number` |  |
| `GetBonusPhysicalArmor(nEntityIndex: EntityIndex): number` |  |
| `GetCollisionPadding(nEntityIndex: EntityIndex): number` |  |
| `GetEffectiveInvisibilityLevel(nEntityIndex: EntityIndex): number` |  |
| `GetHasteFactor(nEntityIndex: EntityIndex): number` |  |
| `GetHullRadius(nEntityIndex: EntityIndex): number` |  |
| `GetIdealSpeed(nEntityIndex: EntityIndex): number` |  |
| `GetIncreasedAttackSpeed(nEntityIndex: EntityIndex): number` |  |
| `GetMana(nEntityIndex: EntityIndex): number` |  |
| `GetManaThinkRegen(nEntityIndex: EntityIndex): number` |  |
| `GetMaxMana(nEntityIndex: EntityIndex): number` |  |
| `GetMagicalArmorValue(nEntityIndex: EntityIndex): number` |  |
| `GetPaddedCollisionRadius(nEntityIndex: EntityIndex): number` |  |
| `GetPercentInvisible(nEntityIndex: EntityIndex): number` |  |
| `GetPhysicalArmorValue(nEntityIndex: EntityIndex): number` |  |
| `GetProjectileCollisionSize(nEntityIndex: EntityIndex): number` |  |
| `GetRingRadius(nEntityIndex: EntityIndex): number` | Returns the radius of the bounding ring of the unit. |
| `GetSecondsPerAttack(nEntityIndex: EntityIndex): number` |  |
| `ManaFraction(nEntityIndex: EntityIndex): number` |  |
| `GetClassNameAsCStr(nEntityIndex: EntityIndex): string` |  |
| `GetDisplayedUnitName(nEntityIndex: EntityIndex): string` |  |
| `GetSelectionGroup(nEntityIndex: EntityIndex): string` |  |
| `GetSoundSet(nEntityIndex: EntityIndex): string` |  |
| `GetUnitLabel(nEntityIndex: EntityIndex): string` |  |
| `GetUnitName(nEntityIndex: EntityIndex): string` |  |
| `GetTotalDamageTaken(nEntityIndex: EntityIndex): number` |  |
| `IsControllableByPlayer(nEntityIndex: EntityIndex, nPlayerIndex: PlayerID): boolean` |  |
| `GetChosenTarget(nEntityIndex: EntityIndex): number` |  |
| `HasItemInInventory(nEntityIndex: EntityIndex, pItemName: string): boolean` |  |
| `GetRangeToUnit(nEntityIndex: EntityIndex, nEntityIndex2: EntityIndex): number` |  |
| `IsEntityInRange(nEntityIndex: EntityIndex, nEntityIndex2: EntityIndex, flRange: number): boolean` |  |
| `GetMoveSpeedModifier(nEntityIndex: EntityIndex, flBaseSpeed: number): number` |  |
| `CanAcceptTargetToAttack(nEntityIndex: EntityIndex, nEntityIndex2: EntityIndex): boolean` |  |
| `InState(nEntityIndex: EntityIndex, nState: modifierstate): boolean` |  |
| `GetArmorForDamageType(nEntityIndex: EntityIndex, iDamageType: DAMAGE_TYPES): number` |  |
| `GetArmorReductionForDamageType(nEntityIndex: EntityIndex, iDamageType: DAMAGE_TYPES): number` |  |
| `IsInRangeOfShop(nEntityIndex: EntityIndex, iShopType: number, bSpecific: boolean): boolean` |  |
| `GetNumItemsInStash(nEntityIndex: EntityIndex): number` |  |
| `GetNumItemsInInventory(nEntityIndex: EntityIndex): number` |  |
| `GetItemInSlot(nEntityIndex: EntityIndex, nSlotIndex: number): ItemEntityIndex` |  |
| `GetAbility(nEntityIndex: EntityIndex, nSlotIndex: number): AbilityEntityIndex` |  |
| `GetAbilityByName(nEntityIndex: EntityIndex, pszAbilityName: string): AbilityEntityIndex` |  |
| `GetNumBuffs(nEntityIndex: EntityIndex): number` |  |
| `GetBuff(nEntityIndex: EntityIndex, nBufIndex: number): BuffID` |  |
| `GetAbilityPoints(nEntityIndex: EntityIndex): number` |  |
| `GetCurrentXP(nEntityIndex: EntityIndex): number` |  |
| `GetNeededXPToLevel(nEntityIndex: EntityIndex): number` |  |
| `GetSelectionEntities(nEntityIndex: EntityIndex): EntityIndex[]` | Get the currently selected entities |
| `IsValidEntity(nEntityIndex: EntityIndex): boolean` | Is this a valid entity index? |
| `IsItemPhysical(nEntityIndex: EntityIndex): boolean` | Is this entity an item container in the world? |
| `GetContainedItem(nEntityIndex: EntityIndex): ItemEntityIndex` | Get the item contained in this physical item container. |
| `SetMinimapIcon(nEntityIndex: number, pszMinimapIcon: string): void` | Set the minimap icon on this client. |

### CScriptBindingPR_Game

**Methods**

| Method | Description |
| --- | --- |
| `Time(): number` |  |
| `GetGameTime(): number` |  |
| `GetGameFrameTime(): number` |  |
| `GetDOTATime(bIncludePreGame: boolean, bIncludeNegativeTime: boolean): number` |  |
| `IsGamePaused(): boolean` |  |
| `IsDayTime(): boolean` |  |
| `IsInToolsMode(): boolean` |  |
| `IsInBanPhase(): boolean` |  |
| `GetConvarBool(name: string): boolean` |  |
| `GetConvarInt(name: string): number` |  |
| `GetConvarFloat(name: string): number` |  |
| `GetGameWinner(): DOTATeam_t` | Return the team id of the winning team. |
| `GetStateTransitionTime(): number` |  |
| `GetCustomGameDifficulty(): number` | Get the difficulty setting of the game. |
| `IsHUDFlipped(): boolean` | Returns true if the user has enabled flipped HUD |
| `GetScreenWidth(): number` | Returns the width of the display. |
| `GetScreenHeight(): number` | Returns the height of the display. |
| `WorldToScreenX(x: number, y: number, z: number): number` | Converts the specified x,y,z world co-ordinate into an x screen coordinate. Returns -1 if behind the camera |
| `WorldToScreenY(x: number, y: number, z: number): number` | Converts the specified x,y,z world co-ordinate into a y screen coordinate. Returns -1 if behind the camera |
| `ScreenXYToWorld(nX: number, nY: number): [number, number, number]` | Converts the specified x, y screen coordinates into a x, y, z world coordinates. |
| `GetKeybindForAbility(iSlot: number): string` | Returns the keybind (as a string) for the requested ability slot. |
| `GetKeybindForInventorySlot(iSlot: number): string` | Returns the keybind (as a string) for the requested inventory slot. |
| `GetKeybindForCommand(nCommand: DOTAKeybindCommand_t): string` | Returns the keybind (as a string). |
| `GetNianFightTimeLeft(): number` |  |
| `Diretide2020ShouldShowGameInfo(): boolean` |  |
| `Diretide2020SetShowGameInfo(bShowGameInfo: boolean): void` |  |
| `Diretide2020GetGameplayTipNumber(): number` |  |
| `Diretide2020SetGameplayTipNumber(nGameplayTipNumber: number): void` |  |
| `GetState(): DOTA_GameState` |  |
| `GameStateIs(nState: DOTA_GameState): boolean` |  |
| `GameStateIsBefore(nState: DOTA_GameState): boolean` |  |
| `GameStateIsAfter(nState: DOTA_GameState): boolean` |  |
| `AddCommand( pszCommandName: string, callback: (name: string, ...args: string[]) => void, pszDescription: string, nFlags: number, ): void` |  |
| `GetLocalPlayerID(): PlayerID` |  |
| `PlayerJoinTeam(nTeamID: DOTATeam_t): void` | Assign the local player to the specified team |
| `AutoAssignPlayersToTeams(): void` | Assign the currently unassigned players to teams |
| `ShufflePlayerTeamAssignments(): void` | Shuffle the team assignments of all of the players currently assigned to a team. |
| `SetRemainingSetupTime(flSeconds: number): void` | Set the remaining seconds in team setup before the game starts. -1 to stop the countdown timer |
| `SetAutoLaunchDelay(flSeconds: number): void` | Set the amount of time in seconds that will be set as the remaining time when all players are assigned to a team. |
| `SetAutoLaunchEnabled(bEnable: boolean): void` | Enable or disable automatically starting the game once all players are assigned to a team |
| `GetAutoLaunchEnabled(): boolean` | Return true of false indicating if automatically starting the game is enabled. |
| `SetTeamSelectionLocked(bLockTeams: boolean): void` | Lock the team selection preventing players from swiching teams. |
| `GetTeamSelectionLocked(): boolean` | Returns true or false to indicate if team selection is locked |
| `GetAllTeamIDs(): DOTATeam_t[]` | Get all team IDs |
| `GetAllPlayerIDs(): PlayerID[]` | Get all player IDs |
| `GetUnassignedPlayerIDs(): PlayerID[]` | Get unassigned player IDs |
| `GetPlayerUltimateStateOrTime(nPlayerID: PlayerID): number` | Get info about the player hero ultimate ability |
| `IsPlayerMuted(nPlayerID: PlayerID): boolean` | Whether the local player has muted text and voice chat for the specified player id |
| `SetPlayerMuted(nPlayerID: PlayerID, bMuted: boolean): void` | Set whether the local player has muted text and voice chat for the specified player id |
| `GetTeamDetails(nTeam: number): TeamDetails` | Get detailed information for the given team |
| `GetLocalPlayerInfo(): PlayerInfo` | Get details for the local player |
| `GetPlayerItems(nPlayerID: PlayerID): ItemEntityIndex[]` | Get info about the player items. |
| `GetPlayerInfo(nPlayerID: PlayerID): PlayerInfo` | Get info about the given player |
| `GetPlayerIDsOnTeam(nTeam: DOTATeam_t): PlayerID[]` | Get player IDs for the given team |
| `ServerCmd(pMsg: string): void` |  |
| `SetDotaRefractHeroes(bEnabled: boolean): void` |  |
| `FinishGame(): void` |  |
| `LeaveCurrentGame(): void` |  |
| `Disconnect(): void` |  |
| `FindEventMatch(): void` |  |
| `EmitSound(pSoundEventName: string): number` | Emit a sound for the local player. Returns an integer handle that can be passed to StopSound. (Returns 0 on failure.) |
| `StopSound(nHandle: number): void` | Stop a current playing sound on the local player. Takes handle from a call to EmitSound. |
| `IsShopOpen(): boolean` | Ask whether the in game shop is open. |
| `SetCustomShopEntityString(pszCustomShopEntityString: string): void` | Set custom shop context. |
| `GetMapInfo(): MapInfo` | Return information about the current map. |
| `PrepareUnitOrders(args: PrepareUnitOrdersArgument): void` | Orders from the local player. |
| `DropItemAtCursor(nControlledUnitEnt: EntityIndex, nItemEnt: ItemEntityIndex): void` | Order a unit to drop the specified item at the current cursor location. |
| `Length2D(vec1: [number, number, number], vec2: [number, number, number]): number` | Calculate 2D length. |
| `Normalized(vec: [number, number, number]): [number, number, number]` | Returns normalized vector. |
| `EnterAbilityLearnMode(): void` |  |
| `EndAbilityLearnMode(): void` |  |
| `IsInAbilityLearnMode(): boolean` |  |
| `CreateCustomKeyBind(keyName: string, commandName: string): void` | Registers a keybind that can be listened to with Game.AddCommand |
| `NemesticeGetGameplayTipNumber(): number` |  |
| `NemesticeSetGameplayTipNumber(nGameplayTipNumber: number): void` |  |
| `NemesticeShouldShowGameInfo(): boolean` |  |
| `NemesticeSetShowGameInfo(bShowGameInfo: boolean): void` |  |
| `Winter2022ShouldShowGameInfo(): boolean` |  |
| `Winter2022SetShowGameInfo(bShowGameInfo: boolean): void` |  |
| `Winter2022GetGameplayTipNumber(): number` |  |
| `Winter2022SetGameplayTipNumber(nGameplayTipNumber: number): void` |  |
| `ForceCustomUILoad(): void` |  |
| `CutToDefaultCamera(): void` |  |
| `PlayDataDrivenCamera(pszCameraName: string): number` |  |
| `SetJoyFocusPanel(pPanelArg?: Panel): void` |  |
| `PushJoyFocusPanel(pPanelArg?: Panel): void` |  |
| `PopJoyFocusPanel(): void` |  |
| `IsPlayerMutedVoice(nPlayerID: number): boolean` | Whether the local player has muted voice chat for the specified player id |
| `SetPlayerMutedVoice(nPlayerID: number, bMutedVoice: boolean): void` | Set whether the local player has muted voice chat for the specified player id |
| `IsPlayerMutedText(nPlayerID: number): boolean` | Whether the local player has muted text chat for the specified player id |
| `SetPlayerMutedText(nPlayerID: number, bMutedText: boolean): void` | Set whether the local player has muted text chat for the specified player id |

### CScriptBindingPR_Items

**Methods**

| Method | Description |
| --- | --- |
| `ShouldDisplayCharges(nEntityIndex: ItemEntityIndex): boolean` |  |
| `AlwaysDisplayCharges(nEntityIndex: ItemEntityIndex): boolean` |  |
| `ShowSecondaryCharges(nEntityIndex: ItemEntityIndex): boolean` |  |
| `CanBeSoldByLocalPlayer(nEntityIndex: ItemEntityIndex): boolean` |  |
| `CanDoubleTapCast(nEntityIndex: ItemEntityIndex): boolean` |  |
| `ForceHideCharges(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsAlertableItem(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsCastOnPickup(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsDisassemblable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsDroppable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsInnatelyDisassemblable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsKillable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsMuted(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsPermanent(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsPurchasable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsRecipe(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsRecipeGenerated(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsSellable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `IsStackable(nEntityIndex: ItemEntityIndex): boolean` |  |
| `ProRatesChargesWhenSelling(nEntityIndex: ItemEntityIndex): boolean` |  |
| `RequiresCharges(nEntityIndex: ItemEntityIndex): boolean` |  |
| `CanBeExecuted(nEntityIndex: ItemEntityIndex): number` |  |
| `GetCost(nEntityIndex: ItemEntityIndex): number` |  |
| `GetCurrentCharges(nEntityIndex: ItemEntityIndex): number` |  |
| `GetSecondaryCharges(nEntityIndex: ItemEntityIndex): number` |  |
| `GetDisplayedCharges(nEntityIndex: ItemEntityIndex): number` |  |
| `GetInitialCharges(nEntityIndex: ItemEntityIndex): number` |  |
| `GetItemColor(nEntityIndex: ItemEntityIndex): number` |  |
| `GetShareability(nEntityIndex: ItemEntityIndex): EShareAbility` |  |
| `GetAbilityTextureSF(nEntityIndex: ItemEntityIndex): string` |  |
| `GetAssembledTime(nEntityIndex: ItemEntityIndex): number` |  |
| `GetPurchaseTime(nEntityIndex: ItemEntityIndex): number` |  |
| `GetPurchaser(nItemID: ItemEntityIndex): EntityIndex` |  |
| `LocalPlayerDisassembleItem(nItem: ItemEntityIndex): boolean` | Attempt to have the local player disassemble the specified item. Returns false if the order wasn't issued. |
| `LocalPlayerDropItemFromStash(nItem: ItemEntityIndex): boolean` | Attempt to have the local player drop the specified item from its stash. Returns false if the order wasn't issued. |
| `LocalPlayerItemAlertAllies(nItem: ItemEntityIndex): boolean` | Attempt to have the local player alert allies about the specified item. Returns false if the order wasn't issued. |
| `LocalPlayerMoveItemToStash(nItem: ItemEntityIndex): boolean` | Attempt to have the local player move the specified item to its stash. Returns false if the order wasn't issued. |
| `LocalPlayerSellItem(nItem: ItemEntityIndex): boolean` | Attempt to have the local player sell the specified item. Returns false if the order wasn't issued. |

### CScriptBindingPR_Particles

**Methods**

| Method | Description |
| --- | --- |
| `CreateParticle(particleName: string, particleAttach: ParticleAttachment_t, owningEntity: EntityIndex): ParticleID` | Create a particle from a file with an attachment and an owning entity. |
| `ReleaseParticleIndex(particle: ParticleID): void` | Release the index of a particle, will make the particle in-accessible from script. This allows another particle<br>to reuse the freed particle index. |
| `DestroyParticleEffect(particle: ParticleID, immediate: boolean): void` | Destroy a particle. Setting the immediate boolean to true will prevent the endcap from playing. |
| `SetParticleControl(particle: ParticleID, controlPoint: number, value: [number, number, number]): void` | Set a particle's control point to a vector value. |
| `SetParticleControlForward(particle: ParticleID, controlPoint: number, value: [number, number, number]): void` | [OBSOLETE - Use SetParticleControlTransformForward] Set the orientation on a control point on a particle system |
| `SetParticleControlTransform( particle: ParticleID, controlPoint: number, origin: [number, number, number], angles: [number, number, number], ): void` | Set the position and orientation on a control point on a particle system. |
| `SetParticleControlTransformForward( particle: ParticleID, controlPoint: number, origin: [number, number, number], forward: [number, number, number], ): void` | Set the position and orientation (derived from a forward direction) on a control point on a particle system |
| `SetParticleAlwaysSimulate(particle: ParticleID): void` | Unknown use, any info welcome. |
| `SetParticleControlEnt( particle: ParticleID, controlPoint: number, entity: EntityIndex, particleAttach: ParticleAttachment_t, attachmentName: string, offset: [number, number, number], unknown: boolean, ): void` | Set a particle's control point to an entity's attachment.<br><br>**Example:**<br><br>`Particles.SetParticleControlEnt(particle, 0, entity, ParticleAttachment_t.PATTACH_POINT_FOLLOW, "attach_hitloc", [0, 0, 0], true);` |

### CScriptBindingPR_Players

**Methods**

| Method | Description |
| --- | --- |
| `GetMaxPlayers(): number` | Get the maximum number of players in the game. |
| `GetMaxTeamPlayers(): number` | Get the maximum number of players on teams. |
| `GetLocalPlayer(): PlayerID` | Get the local player ID. |
| `IsValidPlayerID(iPlayerID: PlayerID): boolean` | Is the nth player a valid player? |
| `GetPlayerName(iPlayerID: PlayerID): string` | Return the name of a player. |
| `GetPlayerHeroEntityIndex(iPlayerID: PlayerID): EntityIndex` | Get the entity index of the hero controlled by this player. |
| `GetSelectedEntities(iPlayerID: PlayerID): EntityIndex[]` | Get the entities this player has selected. |
| `GetQueryUnit(iPlayerID: PlayerID): EntityIndex` | Get the entities this player is querying. |
| `GetLocalPlayerPortraitUnit(): EntityIndex` | Get local player current portrait unit. (ie. Player's hero or primary selected unit.) |
| `CanPlayerBuyback(iPlayerID: PlayerID): boolean` | Can the player buy back? |
| `HasCustomGameTicketForPlayerID(iPlayerID: PlayerID): boolean` | Does this player have a custom game ticket? |
| `GetAssists(iPlayerID: PlayerID): number` | The number of assists credited to a player. |
| `GetClaimedDenies(iPlayerID: PlayerID): number` |  |
| `GetClaimedMisses(iPlayerID: PlayerID): number` |  |
| `GetDeaths(iPlayerID: PlayerID): number` | The number of deaths a player has suffered. |
| `GetDenies(iPlayerID: PlayerID): number` | The number of denies credited to a player. |
| `GetGold(iPlayerID: PlayerID): number` | The amount of gold a player has. |
| `GetKills(iPlayerID: PlayerID): number` | The number of kills credited to a player. |
| `GetLastBuybackTime(iPlayerID: PlayerID): number` |  |
| `GetLastHitMultikill(iPlayerID: PlayerID): number` |  |
| `GetLastHits(iPlayerID: PlayerID): number` | The number of last hits credited to a player. |
| `GetLastHitStreak(iPlayerID: PlayerID): number` |  |
| `GetLevel(iPlayerID: PlayerID): number` | The current level of a player. |
| `GetMisses(iPlayerID: PlayerID): number` |  |
| `GetNearbyCreepDeaths(iPlayerID: PlayerID): number` |  |
| `GetReliableGold(iPlayerID: PlayerID): number` | Total reliable gold for this player. |
| `GetRespawnSeconds(iPlayerID: PlayerID): number` |  |
| `GetStreak(iPlayerID: PlayerID): number` |  |
| `GetTotalEarnedGold(iPlayerID: PlayerID): number` | Total gold earned in this game by this player. |
| `GetTotalEarnedXP(iPlayerID: PlayerID): number` | Total xp earned in this game by this player. |
| `GetUnreliableGold(iPlayerID: PlayerID): number` | Total unreliable gold for this player. |
| `GetTeam(iPlayerID: PlayerID): DOTATeam_t` | Get the team this player is on. |
| `GetSelectedHeroID(iPlayerID: PlayerID): HeroID` | Get the player's selected hero id. |
| `GetGoldPerMin(iPlayerID: PlayerID): number` | Average gold earned per minute for this player. |
| `GetXPPerMin(iPlayerID: PlayerID): number` | Average xp earned per minute for this player. |
| `GetPlayerSelectedHero(iPlayerID: PlayerID): string` | Return the name of the hero a player is controlling. |
| `GetPlayerColor(iPlayerID: PlayerID): number` | Get the player color. |
| `IsSpectator(iPlayerID: PlayerID): boolean` | Is this player a spectator. |
| `PlayerPortraitClicked(nClickedPlayerID: PlayerID, bHoldingCtrl: boolean, bHoldingAlt: boolean): void` | Player portrait click event. |
| `PlayerPortraitDoubleClicked(nClickedPlayerID: PlayerID, bHoldingCtrl: boolean, bHoldingAlt: boolean): void` | Player portrait double click event. |
| `BuffClicked(nEntity: EntityIndex, nBuffSerial: number, bAlert: boolean): void` |  |
| `IsLocalPlayerLiveSpectating(): boolean` | Is the local player live spectating? |
| `IsLocalPlayerInPerspectiveCamera(): boolean` | If player is in perspective camera, returns true. Else, false |
| `GetPerspectivePlayerEntityIndex(): EntityIndex` | If player is in perspective mode, returns the followed players entity index.  Else, -1. |
| `GetPerspectivePlayerId(): PlayerID` | If player is in perspective mode, returns the followed players id.  Else, -1. |

### CustomGameEventDeclarations

The type used for validation of custom events.

This type may be augmented via interface merging.

_No members._

### CustomNetTableDeclarations

The type used for validation of custom net tables.

This type may be augmented via interface merging.

_No members._

### CustomUIConfig

The type of `Game.CustomUIConfig()`.

If you need to declare that a given property exists in `Game.CustomUIConfig()`,
this type may be augmented via interface merging.

_No members._

### DollarStatic

**Methods**

| Method | Description |
| --- | --- |
| `FindChildInContext(selector: string): Panel` |  |
| `CreatePanel<K extends keyof PanoramaPanelNameMap>( type: K, root: PanelBase, id: string, properties?: Record<string, any>, ): PanoramaPanelNameMap[K]` |  |
| `CreatePanel(type: string, root: PanelBase, id: string, properties?: Record<string, any>): Panel` |  |
| `CreatePanelWithProperties<K extends keyof PanoramaPanelNameMap>( type: K, root: PanelBase, id: string, properties: Record<string, any>, ): PanoramaPanelNameMap[K]` | **Deprecated:**      <br><br>**Parameters:**<br><br>- properties An object with XML-style properties added to the created panel.<br><br>**Example:**<br><br>`$.CreatePanelWithProperties("Label", $.GetContextPanel(), "id", {`<br>`class: "MyClass",`<br>`text: "Button",`<br>`onactivate: "$.Msg('Button Pressed')",`<br>`});` |
| `CreatePanelWithProperties(type: string, root: PanelBase, id: string, properties: Record<string, any>): Panel` |  |
| `Msg(...args: any[]): void` | Log a message |
| `AssertHelper(...args: any[]): void` | Trigger an assert.<br>Prints a message with a stack trace to the console. |
| `Warning(...args: any[]): void` | Log a warning message to specified channel. |
| `GetContextPanel(): Panel` |  |
| `Schedule(time: number, callback: () => void): ScheduleID` |  |
| `CancelScheduled(scheduledEvent: ScheduleID): void` |  |
| `DispatchEvent<E extends PanoramaEvents.PanoramaEventName \| string>( eventName: E extends PanoramaEvents.PanoramaEventName ? E : string, ...args: PanoramaEvents.InferPanoramaEventParams<E, any[]> ): void` |  |
| `DispatchEventAsync<E extends PanoramaEvents.PanoramaEventName \| string>( eventName: E extends PanoramaEvents.PanoramaEventName ? E : string, ...args: PanoramaEvents.InferPanoramaEventParams<E, any[]> ): void` |  |
| `Language(): string` |  |
| `Localize(token: string, parent?: PanelBase): string` | Localize a string. Optionally accepts Quantity, Precision, and Panel arguments. |
| `Localize(token: string, value: number, parent?: PanelBase): string` |  |
| `LocalizePlural(token: string, value: number, parent?: PanelBase): string` | **Deprecated:** |
| `RegisterEventHandler<E extends PanoramaEvents.PanoramaEventName \| string>( eventName: E extends PanoramaEvents.PanoramaEventName ? E : string, panel: PanelBase \| string, callback: PanoramaEvents.InferPanoramaCallback<E>, ): void` |  |
| `RegisterForUnhandledEvent<E extends PanoramaEvents.PanoramaEventName \| string>( eventName: E extends PanoramaEvents.PanoramaEventName ? E : string, callback: PanoramaEvents.InferPanoramaCallback<E>, ): UnhandledEventListenerID` |  |
| `UnregisterForUnhandledEvent(event: string, handle: UnhandledEventListenerID): void` |  |
| `Each<T>(list: T[], callback: (item: T, index: number) => void): void` |  |
| `Each<T>(map: { [key: string]: T }, callback: (value: T, key: string) => void): void` |  |
| `Each<T>(map: { [key: number]: T }, callback: (value: T, key: number) => void): void` |  |
| `FrameTime(): number` | Gets the time this frame started, in seconds since panorama was initialized |
| `AsyncWebRequest(url: string, data: AsyncWebRequestData): void` | **Deprecated:** Yes |
| `RegisterKeyBind<T extends PanelBase = Panel>( panel: T \| string, key: string, callback: (source: 'keyboard' \| 'gamepad', presses: number, panel: T) => void, ): void` | Register a key binding.<br><br>**Parameters:**<br><br>- panel Panel or input context to bind on. Using an empty string crashes the game when the key is pressed out of Panorama context.<br><br>- key A key name, with keyboard names starting with `key_`. Can be a comma-delimited list to register multiple keys at once.<br> |
| `DbgIsReloadingScript(): boolean` | Call during JS startup code to check if script is being reloaded. |
| `LogChannel(...unknown: any[]): void` | Create a logging channel. |
| `HTMLEscape(string: string): string` | Convert a string to HTML-safe |
| `BImageFileExists(path: string): boolean` | Return true if a file exists.  Path will usually start with 'file://{images}' |

**Other members**

| Member | Description |
| --- | --- |
| `(selector: string): Panel` |  |

### DragSettings

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `displayPanel` | `Panel` |  |
| `offsetX` | `number` |  |
| `offsetY` | `number` |  |
| `removePositionBeforeDrop` | `boolean` |  |

### MapInfo

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `map_name` | `string` |  |
| `map_display_name` | `string` |  |

### PlayerInfo

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |
| `player_name` | `string` |  |
| `player_connection_state` | `DOTAConnectionState_t` |  |
| `player_steamid` | `string` |  |
| `player_kills` | `number` |  |
| `player_deaths` | `number` |  |
| `player_assists` | `number` |  |
| `player_selected_hero_id` | `HeroID` |  |
| `player_selected_hero` | `string` |  |
| `player_selected_hero_entity_index` | `EntityIndex` |  |
| `possible_hero_selection` | `string` |  |
| `player_level` | `number` |  |
| `player_respawn_seconds` | `number` |  |
| `player_gold` | `number` |  |
| `player_team_id` | `DOTATeam_t` |  |
| `player_is_local` | `boolean` |  |
| `player_has_host_privileges` | `boolean` |  |

### PrepareUnitOrdersArgument

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `OrderType` | `dotaunitorder_t` |  |
| `TargetIndex?` | `number` |  |
| `Position?` | `[number, number, number]` |  |
| `AbilityIndex?` | `number` |  |
| `OrderIssuer?` | `PlayerOrderIssuer_t` |  |
| `UnitIndex?` | `number` |  |
| `QueueBehavior?` | `OrderQueueBehavior_t` |  |
| `ShowEffects?` | `boolean` |  |

### ScreenEntity

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entityIndex` | `EntityIndex` |  |
| `accurateCollision` | `boolean` |  |

### TeamDetails

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `team_id` | `DOTATeam_t` |  |
| `team_name` | `string` |  |
| `team_max_players` | `number` |  |
| `team_score` | `number` |  |
| `team_num_players` | `number` |  |

## Type aliases

### MouseButton

```ts
type MouseButton = 0 | 1 | 2 | 3 | 4 | 5 | 6;
```

0 - Left
1 - Right
2 - Middle
3 - Mouse 4
4 - Mouse 5
5 - Scroll up
6 - Scroll down

### MouseEvent

```ts
type MouseEvent = 'pressed' | 'doublepressed' | 'released' | 'wheeled';
```

### MouseScrollDirection

```ts
type MouseScrollDirection = 1 | -1;
```

1 - Up
-1 - Down

### NetworkedData

```ts
type NetworkedData<T> = T extends string | number
    ? T
    : T extends boolean
    ? 0 | 1
    : T extends (infer U)[]
    ? { [key: number]: NetworkedData<U> }
    : T extends Function // eslint-disable-line @typescript-eslint/ban-types
    ? undefined
    : T extends object
    ? { [K in keyof T]: NetworkedData<T[K]> }
    : never;
```

## Namespaces

### GameEvents

```ts
declare namespace GameEvents {
    type InferCustomGameEventType<T extends string | object, TUntyped> = T extends keyof CustomGameEventDeclarations
        ? CustomGameEventDeclarations[T]
        : T extends string
        ? TUntyped
        : T;

    type InferGameEventType<T extends string | object, TUntyped> = T extends keyof GameEventDeclarations
        ? GameEventDeclarations[T]
        : InferCustomGameEventType<T, TUntyped>;
}
```

### PanoramaEvents

```ts
declare namespace PanoramaEvents {
    type PanoramaEventName = keyof PanoramaEvent;
    type InferPanoramaEventParams<T extends string, TUntyped> = T extends PanoramaEventName
        ? PanoramaEvent[T] extends (...args: infer P) => void
            ? P | [PanelBase, ...P]
            : TUntyped
        : TUntyped;
    type InferPanoramaCallback<T extends string> = T extends PanoramaEventName
        ? PanoramaEvent[T] extends (...args: infer P) => void
            ? ((...args: P) => void) | ((...args: [PanelBase, ...P]) => void)
            : (...args: any[]) => void
        : (...args: any[]) => void;
}
```
