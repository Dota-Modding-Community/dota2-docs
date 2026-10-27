# Dota Lua API declarations



95 classes, 3 additional interfaces, 244 global functions and 2 type aliases.

## Contents

<details><summary>Classes</summary>

- [CBaseAnimatingActivity](#cbaseanimatingactivity)
- [CBaseAnimatingOverlay](#cbaseanimatingoverlay)
- [CBaseAnimGraph](#cbaseanimgraph)
- [CBaseCombatCharacter](#cbasecombatcharacter)
- [CBaseEntity](#cbaseentity)
- [CBaseModelEntity](#cbasemodelentity)
- [CBasePlayerController](#cbaseplayercontroller)
- [CBasePlayerPawn](#cbaseplayerpawn)
- [CBaseTrigger](#cbasetrigger)
- [CBodyComponent](#cbodycomponent)
- [CCustomGameEventManager](#ccustomgameeventmanager)
- [CCustomNetTableManager](#ccustomnettablemanager)
- [CDebugOverlayScriptHelper](#cdebugoverlayscripthelper)
- [CDOTA_Ability_Aghanim_Spear](#cdota_ability_aghanim_spear)
- [CDOTA_Ability_Animation_Attack](#cdota_ability_animation_attack)
- [CDOTA_Ability_Animation_TailSpin](#cdota_ability_animation_tailspin)
- [CDOTA_Ability_DataDriven](#cdota_ability_datadriven)
- [CDOTA_Ability_Lua](#cdota_ability_lua)
- [CDOTA_Ability_Nian_Dive](#cdota_ability_nian_dive)
- [CDOTA_Ability_Nian_Leap](#cdota_ability_nian_leap)
- [CDOTA_Ability_Nian_Roar](#cdota_ability_nian_roar)
- [CDOTA_BaseNPC](#cdota_basenpc)
- [CDOTA_BaseNPC_Building](#cdota_basenpc_building)
- [CDOTA_BaseNPC_Creature](#cdota_basenpc_creature)
- [CDOTA_BaseNPC_Hero](#cdota_basenpc_hero)
- [CDOTA_BaseNPC_LotusPool](#cdota_basenpc_lotuspool)
- [CDOTA_BaseNPC_NeutralItemStash](#cdota_basenpc_neutralitemstash)
- [CDOTA_BaseNPC_Shop](#cdota_basenpc_shop)
- [CDOTA_BaseNPC_Trap_Ward](#cdota_basenpc_trap_ward)
- [CDOTA_BaseNPC_Watch_Tower](#cdota_basenpc_watch_tower)
- [CDOTA_Buff](#cdota_buff)
- [CDOTA_CustomUIManager](#cdota_customuimanager)
- [CDOTA_Item](#cdota_item)
- [CDOTA_Item_BagOfGold](#cdota_item_bagofgold)
- [CDOTA_Item_DataDriven](#cdota_item_datadriven)
- [CDOTA_Item_EmptyBottle](#cdota_item_emptybottle)
- [CDOTA_Item_Lua](#cdota_item_lua)
- [CDOTA_Item_Physical](#cdota_item_physical)
- [CDOTA_ItemSpawner](#cdota_itemspawner)
- [CDOTA_MapTree](#cdota_maptree)
- [CDOTA_Modifier_Lua](#cdota_modifier_lua)
- [CDOTA_Modifier_Lua_Horizontal_Motion](#cdota_modifier_lua_horizontal_motion)
- [CDOTA_Modifier_Lua_Motion_Both](#cdota_modifier_lua_motion_both)
- [CDOTA_Modifier_Lua_Vertical_Motion](#cdota_modifier_lua_vertical_motion)
- [CDOTA_NeutralSpawner](#cdota_neutralspawner)
- [CDOTA_PlayerResource](#cdota_playerresource)
- [CDOTA_ShopTrigger](#cdota_shoptrigger)
- [CDOTA_SimpleObstruction](#cdota_simpleobstruction)
- [CDOTA_Unit_Courier](#cdota_unit_courier)
- [CDOTA_Unit_CustomGameAnnouncer](#cdota_unit_customgameannouncer)
- [CDOTA_Unit_CustomGameAnnouncerAghanim](#cdota_unit_customgameannounceraghanim)
- [CDOTA_Unit_Nian](#cdota_unit_nian)
- [CDOTA_Unit_Scout](#cdota_unit_scout)
- [CDOTABaseAbility](#cdotabaseability)
- [CDOTABaseGameMode](#cdotabasegamemode)
- [CDOTAGameManager](#cdotagamemanager)
- [CDOTAGameRules](#cdotagamerules)
- [CDOTAPlayerController](#cdotaplayercontroller)
- [CDotaQuest](#cdotaquest)
- [CDotaSubquestBase](#cdotasubquestbase)
- [CDOTATutorial](#cdotatutorial)
- [CDotaTutorialNPCBlocker](#cdotatutorialnpcblocker)
- [CDOTAVoteSystem](#cdotavotesystem)
- [CEntities](#centities)
- [CEntityInstance](#centityinstance)
- [CEntityScriptFramework](#centityscriptframework)
- [CEnvEntityMaker](#cenventitymaker)
- [CFoWBlockerRegion](#cfowblockerregion)
- [CInfoData](#cinfodata)
- [CInfoPlayerStartDota](#cinfoplayerstartdota)
- [CInfoWorldLayer](#cinfoworldlayer)
- [CLogicRelay](#clogicrelay)
- [CLogicScript](#clogicscript)
- [CMarkupVolumeTagged](#cmarkupvolumetagged)
- [CNativeOutputs](#cnativeoutputs)
- [Convars](#convars)
- [CParticleSystem](#cparticlesystem)
- [CPhysicsProp](#cphysicsprop)
- [CPointClientUIWorldPanel](#cpointclientuiworldpanel)
- [CPointEntity](#cpointentity)
- [CPointTemplate](#cpointtemplate)
- [CPointWorldText](#cpointworldtext)
- [CSceneEntity](#csceneentity)
- [CScriptHeroList](#cscriptherolist)
- [CScriptHTTPRequest](#cscripthttprequest)
- [CScriptKeyValues](#cscriptkeyvalues)
- [CScriptParticleManager](#cscriptparticlemanager)
- [CScriptPrecacheContext](#cscriptprecachecontext)
- [CScriptUniformRandomStream](#cscriptuniformrandomstream)
- [CTakeDamageInfo](#ctakedamageinfo)
- [GlobalSys](#globalsys)
- [GridNav](#gridnav)
- [ProjectileManager](#projectilemanager)
- [SteamInfo](#steaminfo)
- [Uint64](#uint64)

</details>
<details><summary>Additional interfaces</summary>

- [CustomGameEventDeclarations](#customgameeventdeclarations)
- [CustomNetTableDeclarations](#customnettabledeclarations)
- [GameEventProvidedProperties](#gameeventprovidedproperties)

</details>
<details><summary>Global functions</summary>

- [AddFOWViewer](#addfowviewer)
- [AngleDiff](#anglediff)
- [AnglesToVector](#anglestovector)
- [AppendToLogFile](#appendtologfile)
- [ApplyDamage](#applydamage)
- [AxisAngleToQuaternion](#axisangletoquaternion)
- [CalcClosestPointOnEntityOBB](#calcclosestpointonentityobb)
- [CalcDistanceBetweenEntityOBB](#calcdistancebetweenentityobb)
- [CalcDistanceToLineSegment2D](#calcdistancetolinesegment2d)
- [CancelEntityIOEvents](#cancelentityioevents)
- [CenterCameraOnUnit](#centercameraonunit)
- [ClearTeamCustomHealthbarColor](#clearteamcustomhealthbarcolor)
- [CreateDamageInfo](#createdamageinfo)
- [CreateEffect](#createeffect)
- [CreateHeroForPlayer](#createheroforplayer)
- [CreateHTTPRequest](#createhttprequest)
- [CreateHTTPRequestScriptVM](#createhttprequestscriptvm)
- [CreateIllusions](#createillusions)
- [CreateItem](#createitem)
- [CreateItemOnPositionForLaunch](#createitemonpositionforlaunch)
- [CreateItemOnPositionSync](#createitemonpositionsync)
- [CreateModifierThinker](#createmodifierthinker)
- [CreateRune](#createrune)
- [CreateSceneEntity](#createsceneentity)
- [CreateTempTree](#createtemptree)
- [CreateTempTreeWithModel](#createtemptreewithmodel)
- [CreateTrigger](#createtrigger)
- [CreateTriggerRadiusApproximate](#createtriggerradiusapproximate)
- [CreateUniformRandomStream](#createuniformrandomstream)
- [CreateUnitByName](#createunitbyname)
- [CreateUnitByNameAsync](#createunitbynameasync)
- [CreateUnitFromTable](#createunitfromtable)
- [CrossVectors](#crossvectors)
- [cvar_getf](#cvar_getf)
- [cvar_setf](#cvar_setf)
- [DebugBreak](#debugbreak)
- [DebugChangeTeam](#debugchangeteam)
- [DebugCreateHeroWithVariant](#debugcreateherowithvariant)
- [DebugCreateUnit](#debugcreateunit)
- [DebugDrawBox](#debugdrawbox)
- [DebugDrawBoxDirection](#debugdrawboxdirection)
- [DebugDrawCircle](#debugdrawcircle)
- [DebugDrawClear](#debugdrawclear)
- [DebugDrawLine](#debugdrawline)
- [DebugDrawLine_vCol](#debugdrawline_vcol)
- [DebugDrawScreenTextLine](#debugdrawscreentextline)
- [DebugDrawSphere](#debugdrawsphere)
- [DebugDrawText](#debugdrawtext)
- [DebugScreenTextPretty](#debugscreentextpretty)
- [DeepPrintTable](#deepprinttable)
- [DestroyDamageInfo](#destroydamageinfo)
- [DisconnectClient](#disconnectclient)
- [DoCleaveAttack](#docleaveattack)
- [DoEntFire](#doentfire)
- [DoEntFireByInstanceHandle](#doentfirebyinstancehandle)
- [DoIncludeScript](#doincludescript)
- [DoScriptAssert](#doscriptassert)
- [DOTA_SpawnMapAtPosition](#dota_spawnmapatposition)
- [DOTA_SpawnMapAtPosition](#dota_spawnmapatposition)
- [DotProduct](#dotproduct)
- [DoUniqueString](#douniquestring)
- [DropNeutralItemAtPositionForHero](#dropneutralitematpositionforhero)
- [DropNeutralItemAtPositionForHeroWithOffset](#dropneutralitematpositionforherowithoffset)
- [Dynamic_Wrap](#dynamic_wrap)
- [EmitAnnouncerSound](#emitannouncersound)
- [EmitAnnouncerSoundForPlayer](#emitannouncersoundforplayer)
- [EmitAnnouncerSoundForTeam](#emitannouncersoundforteam)
- [EmitAnnouncerSoundForTeamOnLocation](#emitannouncersoundforteamonlocation)
- [EmitGlobalSound](#emitglobalsound)
- [EmitSoundOn](#emitsoundon)
- [EmitSoundOnClient](#emitsoundonclient)
- [EmitSoundOnEntityForPlayer](#emitsoundonentityforplayer)
- [EmitSoundOnLocationForAllies](#emitsoundonlocationforallies)
- [EmitSoundOnLocationForPlayer](#emitsoundonlocationforplayer)
- [EmitSoundOnLocationWithCaster](#emitsoundonlocationwithcaster)
- [EntIndexToHScript](#entindextohscript)
- [ExecuteOrderFromTable](#executeorderfromtable)
- [ExponentialDecay](#exponentialdecay)
- [FindClearRandomPositionAroundUnit](#findclearrandompositionaroundunit)
- [FindClearSpaceForUnit](#findclearspaceforunit)
- [FindSpawnEntityForTeam](#findspawnentityforteam)
- [FindUnitsInLine](#findunitsinline)
- [FindUnitsInRadius](#findunitsinradius)
- [FireEntityIOInputNameOnly](#fireentityioinputnameonly)
- [FireEntityIOInputString](#fireentityioinputstring)
- [FireEntityIOInputVec](#fireentityioinputvec)
- [FireGameEvent](#firegameevent)
- [FireGameEventLocal](#firegameeventlocal)
- [FrameTime](#frametime)
- [GetAbilityKeyValuesByName](#getabilitykeyvaluesbyname)
- [GetAbilityTextureNameForAbility](#getabilitytexturenameforability)
- [GetActiveSpawnGroupHandle](#getactivespawngrouphandle)
- [GetClearSpaceForUnit](#getclearspaceforunit)
- [GetDedicatedServerKey](#getdedicatedserverkey)
- [GetDedicatedServerKeyV2](#getdedicatedserverkeyv2)
- [GetDedicatedServerKeyV3](#getdedicatedserverkeyv3)
- [GetEntityIndexForTreeId](#getentityindexfortreeid)
- [GetFrameCount](#getframecount)
- [GetGroundHeight](#getgroundheight)
- [GetGroundPosition](#getgroundposition)
- [GetItemCost](#getitemcost)
- [GetItemDefOwnedCount](#getitemdefownedcount)
- [GetItemDefQuantity](#getitemdefquantity)
- [GetListenServerHost](#getlistenserverhost)
- [GetLobbyEventGameDetails](#getlobbyeventgamedetails)
- [GetLocalPlayerID](#getlocalplayerid)
- [GetLocalPlayerTeam](#getlocalplayerteam)
- [GetMapName](#getmapname)
- [GetMaxOutputDelay](#getmaxoutputdelay)
- [GetPhysAngularVelocity](#getphysangularvelocity)
- [GetPhysVelocity](#getphysvelocity)
- [GetPotentialNeutralItemDrop](#getpotentialneutralitemdrop)
- [GetSystemDate](#getsystemdate)
- [GetSystemTime](#getsystemtime)
- [GetSystemTimeMS](#getsystemtimems)
- [GetTargetAOELocation](#gettargetaoelocation)
- [GetTargetLinearLocation](#gettargetlinearlocation)
- [GetTeamHeroKills](#getteamherokills)
- [GetTeamName](#getteamname)
- [GetTreeIdForEntityIndex](#gettreeidforentityindex)
- [GetUnitKeyValuesByName](#getunitkeyvaluesbyname)
- [GetWorldMaxX](#getworldmaxx)
- [GetWorldMaxY](#getworldmaxy)
- [GetWorldMinX](#getworldminx)
- [GetWorldMinY](#getworldminy)
- [GetXPNeededToReachNextLevel](#getxpneededtoreachnextlevel)
- [HeroMaxLevel](#heromaxlevel)
- [InitLogFile](#initlogfile)
- [IsClient](#isclient)
- [IsDedicatedServer](#isdedicatedserver)
- [IsDotaAltPressed](#isdotaaltpressed)
- [IsDotaCtrlPressed](#isdotactrlpressed)
- [IsInToolsMode](#isintoolsmode)
- [IsLocationVisible](#islocationvisible)
- [IsMangoTree](#ismangotree)
- [IsMarkedForDeletion](#ismarkedfordeletion)
- [IsServer](#isserver)
- [IsUnitInValidPosition](#isunitinvalidposition)
- [IsValidEntity](#isvalidentity)
- [LerpVectors](#lerpvectors)
- [LimitPathingSearchDepth](#limitpathingsearchdepth)
- [LinkLuaModifier](#linkluamodifier)
- [ListenToGameEvent](#listentogameevent)
- [ListenToGameEvent](#listentogameevent)
- [LoadKeyValues](#loadkeyvalues)
- [LoadKeyValuesFromString](#loadkeyvaluesfromstring)
- [LocalTime](#localtime)
- [MakeStringToken](#makestringtoken)
- [ManuallyTriggerSpawnGroupCompletion](#manuallytriggerspawngroupcompletion)
- [MinimapEvent](#minimapevent)
- [Msg](#msg)
- [PauseGame](#pausegame)
- [Plat_FloatTime](#plat_floattime)
- [PlayerInstanceFromIndex](#playerinstancefromindex)
- [PrecacheEntityFromTable](#precacheentityfromtable)
- [PrecacheEntityListFromTable](#precacheentitylistfromtable)
- [PrecacheItemByNameAsync](#precacheitembynameasync)
- [PrecacheItemByNameSync](#precacheitembynamesync)
- [PrecacheModel](#precachemodel)
- [PrecacheResource](#precacheresource)
- [PrecacheUnitByNameAsync](#precacheunitbynameasync)
- [PrecacheUnitByNameSync](#precacheunitbynamesync)
- [PrecacheUnitFromTableAsync](#precacheunitfromtableasync)
- [PrecacheUnitFromTableSync](#precacheunitfromtablesync)
- [PrintLinkedConsoleMessage](#printlinkedconsolemessage)
- [QSlerp](#qslerp)
- [RandomFloat](#randomfloat)
- [RandomFloatWrapper](#randomfloatwrapper)
- [RandomInt](#randomint)
- [RandomVector](#randomvector)
- [RecordNeutralItemEarned](#recordneutralitemearned)
- [RegisterCustomAnimationScriptForModel](#registercustomanimationscriptformodel)
- [RegisterSpawnGroupFilterProxy](#registerspawngroupfilterproxy)
- [ReloadMOTD](#reloadmotd)
- [RemoveFOWViewer](#removefowviewer)
- [RemoveSpawnGroupFilterProxy](#removespawngroupfilterproxy)
- [ResolveNPCPositions](#resolvenpcpositions)
- [RollPercentage](#rollpercentage)
- [RollPseudoRandomPercentage](#rollpseudorandompercentage)
- [RotateOrientation](#rotateorientation)
- [RotatePosition](#rotateposition)
- [RotateQuaternionByAxisAngle](#rotatequaternionbyaxisangle)
- [RotationDelta](#rotationdelta)
- [RotationDeltaAsAngularVelocity](#rotationdeltaasangularvelocity)
- [Say](#say)
- [ScreenShake](#screenshake)
- [Script_RandomFloat](#script_randomfloat)
- [Script_RemapValClamped](#script_remapvalclamped)
- [SendOverheadEventMessage](#sendoverheadeventmessage)
- [SendToConsole](#sendtoconsole)
- [SendToServerConsole](#sendtoserverconsole)
- [SetOpvarFloatAll](#setopvarfloatall)
- [SetOpvarFloatPlayer](#setopvarfloatplayer)
- [SetPhysAngularVelocity](#setphysangularvelocity)
- [SetQuestName](#setquestname)
- [SetQuestPhase](#setquestphase)
- [SetRenderingEnabled](#setrenderingenabled)
- [SetTeamCustomHealthbarColor](#setteamcustomhealthbarcolor)
- [ShowCustomHeaderMessage](#showcustomheadermessage)
- [ShowGenericPopup](#showgenericpopup)
- [ShowGenericPopupToPlayer](#showgenericpopuptoplayer)
- [ShowMessage](#showmessage)
- [SpawnDOTAShopTriggerRadiusApproximate](#spawndotashoptriggerradiusapproximate)
- [SpawnEffigyOfUnitOrModel](#spawneffigyofunitormodel)
- [SpawnEntityFromTableAsynchronous](#spawnentityfromtableasynchronous)
- [SpawnEntityFromTableSynchronous](#spawnentityfromtablesynchronous)
- [SpawnEntityGroupFromTable](#spawnentitygroupfromtable)
- [SpawnEntityListFromTableAsynchronous](#spawnentitylistfromtableasynchronous)
- [SpawnEntityListFromTableSynchronous](#spawnentitylistfromtablesynchronous)
- [SpawnMangoTree](#spawnmangotree)
- [SplineQuaternions](#splinequaternions)
- [SplineVectors](#splinevectors)
- [StartSoundEvent](#startsoundevent)
- [StartSoundEventFromPosition](#startsoundeventfromposition)
- [StartSoundEventFromPositionReliable](#startsoundeventfrompositionreliable)
- [StartSoundEventFromPositionUnreliable](#startsoundeventfrompositionunreliable)
- [StartSoundEventReliable](#startsoundeventreliable)
- [StartSoundEventUnreliable](#startsoundeventunreliable)
- [StopEffect](#stopeffect)
- [StopGlobalSound](#stopglobalsound)
- [StopListeningToAllGameEvents](#stoplisteningtoallgameevents)
- [StopListeningToGameEvent](#stoplisteningtogameevent)
- [StopSoundEvent](#stopsoundevent)
- [StopSoundOn](#stopsoundon)
- [Time](#time)
- [TraceCollideable](#tracecollideable)
- [TraceHull](#tracehull)
- [TraceLine](#traceline)
- [UnitFilter](#unitfilter)
- [UnloadSpawnGroup](#unloadspawngroup)
- [UnloadSpawnGroupByHandle](#unloadspawngroupbyhandle)
- [UpdateEventPoints](#updateeventpoints)
- [UserIDToControllerHScript](#useridtocontrollerhscript)
- [UTIL_MessageText](#util_messagetext)
- [UTIL_MessageText_WithContext](#util_messagetext_withcontext)
- [UTIL_MessageTextAll](#util_messagetextall)
- [UTIL_MessageTextAll_WithContext](#util_messagetextall_withcontext)
- [UTIL_Remove](#util_remove)
- [UTIL_RemoveImmediate](#util_removeimmediate)
- [UTIL_ResetMessageText](#util_resetmessagetext)
- [UTIL_ResetMessageTextAll](#util_resetmessagetextall)
- [VectorAngles](#vectorangles)
- [VectorToAngles](#vectortoangles)
- [Warning](#warning)

</details>

## Global functions

### AddFOWViewer

```ts
declare function AddFOWViewer(
    teamId: DOTATeam_t,
    location: Vector,
    radius: number,
    duration: number,
    obstructedVision: boolean,
): ViewerID;
```

Add temporary vision for a given team.

### AngleDiff

```ts
declare function AngleDiff(arg1: number, arg2: number): number;
```

Returns the number of degrees difference between two yaw angles.

**Availability:** `both`

### AnglesToVector

```ts
declare function AnglesToVector(arg1: QAngle): Vector;
```

Generate a vector given a QAngles.

**Availability:** `both`

### AppendToLogFile

```ts
declare function AppendToLogFile(arg1: string, arg2: string): void;
```

**Availability:** `both`

**Deprecated:** AppendToLogFile is deprecated. Print to the console for logging
            instead.

### ApplyDamage

```ts
declare function ApplyDamage(options: ApplyDamageOptions): number;
```

Damage an npc.

### AxisAngleToQuaternion

```ts
declare function AxisAngleToQuaternion(arg1: Vector, arg2: number): never;
```

Constructs a quaternion representing a rotation by angle around the specified
vector axis.

**Availability:** `both`

### CalcClosestPointOnEntityOBB

```ts
declare function CalcClosestPointOnEntityOBB(arg1: object, arg2: Vector): Vector;
```

Compute the closest point on the OBB of an entity.

**Availability:** `both`

### CalcDistanceBetweenEntityOBB

```ts
declare function CalcDistanceBetweenEntityOBB(arg1: object, arg2: object): number;
```

Compute the distance between two entity OBB. A negative return value indicates
an input error. A return value of zero indicates that the OBBs are overlapping.

**Availability:** `both`

### CalcDistanceToLineSegment2D

```ts
declare function CalcDistanceToLineSegment2D(arg1: Vector, arg2: Vector, arg3: Vector): number;
```

**Availability:** `both`

### CancelEntityIOEvents

```ts
declare function CancelEntityIOEvents(arg1: number): void;
```

Create all I/O events for a particular entity.

**Availability:** `both`

### CenterCameraOnUnit

```ts
declare function CenterCameraOnUnit(playerId: PlayerID, unit: CBaseEntity | undefined): void;
```

Centers each players' camera on a unit.

### ClearTeamCustomHealthbarColor

```ts
declare function ClearTeamCustomHealthbarColor(team: DOTATeam_t): void;
```

### CreateDamageInfo

```ts
declare function CreateDamageInfo(
    arg1: object,
    arg2: object,
    arg3: Vector,
    arg4: Vector,
    arg5: number,
    arg6: number,
): CTakeDamageInfo;
```

Allocate a damageinfo object, used as an argument to TakeDamage(). Call
DestroyDamageInfo( hInfo ) to free the object.

### CreateEffect

```ts
declare function CreateEffect(arg1: object): boolean;
```

Pass table - Inputs: entity, effect.

**Availability:** `both`

### CreateHeroForPlayer

```ts
declare function CreateHeroForPlayer(heroName: string, player: CDOTAPlayerController): CDOTA_BaseNPC_Hero;
```

Creates a DOTA hero by its dota_npc_units.txt name and sets it as the given
player's controlled hero.

### CreateHTTPRequest

```ts
declare function CreateHTTPRequest(method: string, url: string): CScriptHTTPRequest;
```

Create an HTTP request.

**Availability:** `both`

### CreateHTTPRequestScriptVM

```ts
declare function CreateHTTPRequestScriptVM(method: string, url: string): CScriptHTTPRequest;
```

Create an HTTP request.

**Availability:** `both`

### CreateIllusions

```ts
declare function CreateIllusions(
    owner: CBaseEntity,
    heroToCopy: CDOTA_BaseNPC_Hero,
    modifierKeys: CreateIllusionsModifierKeys,
    numIllusions: number,
    padding: number,
    scramblePosition: boolean,
    findClearSpace: boolean,
): CDOTA_BaseNPC_Hero[];
```

Create illusions of the passed hero that belong to passed unit using passed
modifier data.

### CreateItem

```ts
declare function CreateItem(
    itemName: string,
    owner: CDOTAPlayerController | undefined,
    purchaser: CDOTA_BaseNPC_Hero | undefined,
): CDOTA_Item | undefined;
```

Create a DOTA item.

### CreateItemOnPositionForLaunch

```ts
declare function CreateItemOnPositionForLaunch(location: Vector, item: CDOTA_Item | undefined): CDOTA_Item_Physical;
```

Create a physical item at a given location, can start in air (but doesn't clear
a space).

### CreateItemOnPositionSync

```ts
declare function CreateItemOnPositionSync(location: Vector, item: CDOTA_Item | undefined): CDOTA_Item_Physical;
```

Create a physical item at a given location.

### CreateModifierThinker

```ts
declare function CreateModifierThinker(
    caster: CDOTA_BaseNPC | undefined,
    ability: CDOTABaseAbility | undefined,
    modifierName: string,
    paramTable: object | undefined,
    origin: Vector,
    teamNumber: DOTATeam_t,
    phantomBlocker: boolean,
): CDOTA_BaseNPC;
```

Create a modifier not associated with an NPC.

### CreateRune

```ts
declare function CreateRune(location: Vector, runeType: DOTA_RUNES): CBaseAnimatingActivity;
```

Create a rune of the specified type.

### CreateSceneEntity

```ts
declare function CreateSceneEntity(arg1: string): CBaseAnimatingActivity;
```

Create a scene entity to play the specified scene.

### CreateTempTree

```ts
declare function CreateTempTree(location: Vector, duration: number): CBaseAnimatingActivity;
```

Create a temporary tree, uses a default tree model.

### CreateTempTreeWithModel

```ts
declare function CreateTempTreeWithModel(location: Vector, duration: number, modelName: string): CBaseAnimatingActivity;
```

Create a temporary tree, specifying the tree model name.

### CreateTrigger

```ts
declare function CreateTrigger(arg1: Vector, arg2: Vector, arg3: Vector): CBaseTrigger;
```

Creates and returns an AABB trigger.

### CreateTriggerRadiusApproximate

```ts
declare function CreateTriggerRadiusApproximate(vecOrigin: Vector, radius: number): CBaseTrigger;
```

Creates and returns an AABB trigger thats bigger than the radius provided.

### CreateUniformRandomStream

```ts
declare function CreateUniformRandomStream(seed: number): CScriptUniformRandomStream;
```

Creates a separate random number stream.

**Availability:** `both`

### CreateUnitByName

```ts
declare function CreateUnitByName(
    unitName: string,
    location: Vector,
    findClearSpace: boolean,
    npcOwner: CBaseEntity | undefined,
    entityOwner: CBaseEntity | undefined,
    team: DOTATeam_t,
): CDOTA_BaseNPC;
```

Creates a unit by its dota_npc_units.txt name.

The spawned unit will not be controllable by default. You can use
unit.SetControllableByPlayer() to change this.

Warning: mass synchronous unit spawning may be slow. Prefer
CreateUnitByNameAsync unless synchronous access is required.

**Parameters:**

- entityOwner This entity will be returned by GetOwner() and
                   GetOwnerEntity(). GetPlayerOwner() and GetPlayerOwnerID()
                   will be automatically inferred from this entity. Can be
                   changed after spawn using SetOwner(entity). When spawning
                   heroes, passing CDOTAPlayerController makes hero use owned
                   wearables.
 

### CreateUnitByNameAsync

```ts
declare function CreateUnitByNameAsync(
    unitName: string,
    location: Vector,
    findClearSpace: boolean,
    npcOwner: CBaseEntity | undefined,
    entityOwner: CBaseEntity | undefined,
    team: DOTATeam_t,
    callback: (unit: CDOTA_BaseNPC) => void,
): SpawnGroupHandle;
```

Creates a unit by its dota_npc_units.txt name.

The spawned unit will not be controllable by default. You can use
unit.SetControllableByPlayer() to change this.

**Parameters:**

- entityOwner This entity will be returned by GetOwner() and
                   GetOwnerEntity(). GetPlayerOwner() and GetPlayerOwnerID()
                   will be automatically inferred from this entity. Can be
                   changed after spawn using SetOwner(entity). When spawning
                   heroes, passing CDOTAPlayerController makes hero use owned
                   wearables.
 

### CreateUnitFromTable

```ts
declare function CreateUnitFromTable(options: CreateUnitFromTableOptions, location: Vector): CDOTA_BaseNPC;
```

Creates a DOTA unit by its dota_npc_units.txt name from a table of entity key
values and a position to spawn at.

### CrossVectors

```ts
declare function CrossVectors(arg1: Vector, arg2: Vector): Vector;
```

Cross product between two vectors.

**Availability:** `both`

### cvar_getf

```ts
declare function cvar_getf(arg1: string): number;
```

Gets the value of the given cvar, as a float.

**Availability:** `both`

### cvar_setf

```ts
declare function cvar_setf(arg1: string, arg2: number): boolean;
```

Sets the value of the given cvar, as a float.

**Availability:** `both`

### DebugBreak

```ts
declare function DebugBreak(): void;
```

Breaks in the debugger.

**Availability:** `both`

### DebugChangeTeam

```ts
declare function DebugChangeTeam(arg1: object): void;
```

Changes the team of the hero.

### DebugCreateHeroWithVariant

```ts
declare function DebugCreateHeroWithVariant(
    arg1: object,
    arg2: string,
    arg3: number,
    arg4: number,
    arg5: boolean,
    arg6: object,
): number;
```

Creates a unit with a specified hero variant, controllable by the specified
player.

### DebugCreateUnit

```ts
declare function DebugCreateUnit(
    playerOwner: CDOTAPlayerController,
    unitName: string,
    team: DOTATeam_t,
    arg4: boolean,
    callback: (unit: CDOTA_BaseNPC) => void,
): number;
```

Creates a test unit controllable by the specified player.

### DebugDrawBox

```ts
declare function DebugDrawBox(
    arg1: Vector,
    arg2: Vector,
    arg3: Vector,
    arg4: number,
    arg5: number,
    arg6: number,
    arg7: number,
    arg8: number,
): void;
```

Draw a debug overlay box.

**Availability:** `both`

### DebugDrawBoxDirection

```ts
declare function DebugDrawBoxDirection(
    cent: Vector,
    min: Vector,
    max: Vector,
    forward: Vector,
    rgb: Vector,
    a: number,
    duration: number,
): void;
```

Draw a debug forward box.

**Availability:** `both`

### DebugDrawCircle

```ts
declare function DebugDrawCircle(
    center: Vector,
    rgb: Vector,
    a: number,
    rad: number,
    ztest: boolean,
    duration: number,
): void;
```

Draw a debug circle.

**Availability:** `both`

### DebugDrawClear

```ts
declare function DebugDrawClear(): void;
```

Try to clear all the debug overlay info.

**Availability:** `both`

### DebugDrawLine

```ts
declare function DebugDrawLine(
    origin: Vector,
    target: Vector,
    r: number,
    g: number,
    b: number,
    ztest: boolean,
    duration: number,
): void;
```

Draw a debug overlay line.

**Availability:** `both`

### DebugDrawLine_vCol

```ts
declare function DebugDrawLine_vCol(arg1: Vector, arg2: Vector, arg3: Vector, arg4: boolean, arg5: number): void;
```

Draw a debug line using color vec.

**Availability:** `both`

### DebugDrawScreenTextLine

```ts
declare function DebugDrawScreenTextLine(
    x: number,
    y: number,
    lineOffset: number,
    text: string,
    r: number,
    g: number,
    b: number,
    a: number,
    duration: number,
): void;
```

Draw text with a line offset.

**Availability:** `both`

### DebugDrawSphere

```ts
declare function DebugDrawSphere(
    center: Vector,
    rgb: Vector,
    a: number,
    rad: number,
    ztest: boolean,
    duration: number,
): void;
```

Draw a debug sphere.

**Availability:** `both`

### DebugDrawText

```ts
declare function DebugDrawText(origin: Vector, text: string, viewCheck: boolean, duration: number): void;
```

Draw text in 3d.

**Availability:** `both`

### DebugScreenTextPretty

```ts
declare function DebugScreenTextPretty(
    x: number,
    y: number,
    lineOffset: number,
    text: string,
    r: number,
    g: number,
    b: number,
    a: number,
    duration: number,
    font: string,
    size: number,
    bold: boolean,
): void;
```

Draw pretty debug text.

**Availability:** `both`

### DeepPrintTable

```ts
declare function DeepPrintTable(table?: Record<any, any>): void;
```

Print out a table (and subtables) to the console.

**Availability:** `both`

### DestroyDamageInfo

```ts
declare function DestroyDamageInfo(damageInfo: CTakeDamageInfo): void;
```

Free a damageinfo object that was created with CreateDamageInfo().

### DisconnectClient

```ts
declare function DisconnectClient(arg1: number, arg2: boolean): void;
```

Kick a specific player from the game.

### DoCleaveAttack

```ts
declare function DoCleaveAttack(
    attacker: CDOTA_BaseNPC,
    target: CDOTA_BaseNPC,
    ability: CDOTABaseAbility | undefined,
    damage: number,
    startRadius: number,
    endRadius: number,
    distance: number,
    effectName: string,
): number;
```

### DoEntFire

```ts
declare function DoEntFire(arg1: string, arg2: string, arg3: string, arg4: number, arg5: object, arg6: object): void;
```

Generate and entity i/o event.

### DoEntFireByInstanceHandle

```ts
declare function DoEntFireByInstanceHandle(
    arg1: object,
    arg2: string,
    arg3: string,
    arg4: number,
    arg5: object,
    arg6: object,
): void;
```

Generate and entity i/o event.

### DoIncludeScript

```ts
declare function DoIncludeScript(arg1: string, arg2: object): boolean;
```

Execute a script (internal).

**Availability:** `both`

### DoScriptAssert

```ts
declare function DoScriptAssert(arg1: boolean, arg2: string): void;
```

Asserts the passed in value. Prints out a message and brings up the assert
dialog.

**Availability:** `both`

### DOTA_SpawnMapAtPosition

```ts
declare function DOTA_SpawnMapAtPosition(
    mapName: string,
    location: Vector,
    deferCompletion: boolean,
    onReadyToSpawn: (spawnGroupHandle: SpawnGroupHandle) => void,
    onSpawnComplete: (spawnGroupHandle: SpawnGroupHandle) => void,
    context: undefined,
): SpawnGroupHandle;
```

Spawn a .vmap at the target location.

**Parameters:**

- mapName A map name without extension, relative to "maps" directory.

- location The value of x and y must be multiple the grid size 64.

                To avoid GridNav conflicts, tiles on these coordinates on the
                base map must be empty.

- deferCompletion If true, to finish map loading you need to call
                       ManuallyTriggerSpawnGroupCompletion(spawnGroupHandle).

- onReadyToSpawn Called only when deferCompletion is true.
 

### DOTA_SpawnMapAtPosition

```ts
declare function DOTA_SpawnMapAtPosition<TContext extends {}>(
    mapName: string,
    location: Vector,
    deferCompletion: boolean,
    onReadyToSpawn: (this: TContext, spawnGroupHandle: SpawnGroupHandle) => void,
    onSpawnComplete: (this: TContext, spawnGroupHandle: SpawnGroupHandle) => void,
    context: TContext,
): SpawnGroupHandle;
```

### DotProduct

```ts
declare function DotProduct(arg1: Vector, arg2: Vector): number;
```

### DoUniqueString

```ts
declare function DoUniqueString(seed: string): string;
```

Generate a string guaranteed to be unique across the life of the script VM,
with an optional root string. Useful for adding data to tables when not sure
what keys are already in use in that table.

**Availability:** `both`

### DropNeutralItemAtPositionForHero

```ts
declare function DropNeutralItemAtPositionForHero(
    itemName: string,
    location: Vector,
    unit: CDOTA_BaseNPC,
    tier: number,
    arg5: boolean,
): CDOTA_Item_Physical;
```

Drop a neutral item for the team of the hero at the given tier.

**Parameters:**

- itemName Can be any item name, it does not have to be neutral.

- tier Zero-based tier number.
 

### DropNeutralItemAtPositionForHeroWithOffset

```ts
declare function DropNeutralItemAtPositionForHeroWithOffset(
    arg1: string,
    arg2: Vector,
    arg3: object,
    arg4: number,
    arg5: boolean,
    arg6: Vector,
): object;
```

Drop a neutral item for the team of the hero at the given tier.

### Dynamic_Wrap

```ts
declare function Dynamic_Wrap<
    T extends object,
    K extends {
        [P in keyof T]: ((...args: any[]) => any) extends T[P] // At least one of union's values is a function
            ? [T[P]] extends [((this: infer TThis, ...args: any[]) => any) | null | undefined] // Box type to make it not distributive
                ? {} extends TThis // Has no specified this
                    ? P
                    : TThis extends T // Has this specified as T
                    ? P
                    : never
                : never
            : never;
    }[keyof T],
>(context: T, name: K): T[K];
```

A function to re-lookup a function by name every time.

**Availability:** `both`

### EmitAnnouncerSound

```ts
declare function EmitAnnouncerSound(soundName: string): void;
```

Emit an announcer sound for all players.

### EmitAnnouncerSoundForPlayer

```ts
declare function EmitAnnouncerSoundForPlayer(soundName: string, playerId: PlayerID): void;
```

Emit an announcer sound for a player.

### EmitAnnouncerSoundForTeam

```ts
declare function EmitAnnouncerSoundForTeam(soundName: string, team: DOTATeam_t): void;
```

Emit an announcer sound for a team.

### EmitAnnouncerSoundForTeamOnLocation

```ts
declare function EmitAnnouncerSoundForTeamOnLocation(soundName: string, team: DOTATeam_t, location: Vector): void;
```

Emit an announcer sound for a team at a specific location.

### EmitGlobalSound

```ts
declare function EmitGlobalSound(soundName: string): void;
```

Play named sound for all players.

### EmitSoundOn

```ts
declare function EmitSoundOn(soundName: string, entity: CBaseEntity): void;
```

Play named sound on Entity.

**Availability:** `both`

### EmitSoundOnClient

```ts
declare function EmitSoundOnClient(soundName: string, arg2: object): void;
```

Play named sound only on the client for the passed in player.

**Availability:** `both`

### EmitSoundOnEntityForPlayer

```ts
declare function EmitSoundOnEntityForPlayer(arg1: string, arg2: object, arg3: number): void;
```

Emit a sound on an entity for only a specific player.

### EmitSoundOnLocationForAllies

```ts
declare function EmitSoundOnLocationForAllies(location: Vector, soundName: string, caster: CBaseEntity): void;
```

Emit a sound on a location from a unit, only for players allied with that unit.

### EmitSoundOnLocationForPlayer

```ts
declare function EmitSoundOnLocationForPlayer(arg1: string, arg2: Vector, arg3: number): void;
```

Emit a sound on a location for only a specific player.

### EmitSoundOnLocationWithCaster

```ts
declare function EmitSoundOnLocationWithCaster(location: Vector, soundName: string, caster: CDOTA_BaseNPC): void;
```

Emit a sound on a location from a unit.

### EntIndexToHScript

```ts
declare function EntIndexToHScript(entityIndex: EntityIndex): CBaseEntity | undefined;
```

Turn an entity index integer to an HScript representing that entity's script
instance.

**Availability:** `both`

### ExecuteOrderFromTable

```ts
declare function ExecuteOrderFromTable(order: ExecuteOrderOptions): void;
```

Issue an order from a script table.

### ExponentialDecay

```ts
declare function ExponentialDecay(arg1: number, arg2: number, arg3: number): number;
```

Smooth curve decreasing slower as it approaches zero.

**Availability:** `both`

### FindClearRandomPositionAroundUnit

```ts
declare function FindClearRandomPositionAroundUnit(arg1: object, arg2: object, arg3: number): boolean;
```

Finds a clear random position around a given target unit, using the target
unit's padded collision radius.

### FindClearSpaceForUnit

```ts
declare function FindClearSpaceForUnit(unit: CDOTA_BaseNPC, location: Vector, arg3: boolean): boolean;
```

Place a unit somewhere not already occupied.

### FindSpawnEntityForTeam

```ts
declare function FindSpawnEntityForTeam(team: DOTATeam_t): CBaseEntity | undefined;
```

Find a spawn point for the given team.

### FindUnitsInLine

```ts
declare function FindUnitsInLine(
    team: DOTATeam_t,
    startPos: Vector,
    endPos: Vector,
    cacheUnit: CBaseEntity | undefined,
    width: number,
    teamFilter: DOTA_UNIT_TARGET_TEAM,
    typeFilter: DOTA_UNIT_TARGET_TYPE,
    flagFilter: DOTA_UNIT_TARGET_FLAGS,
): CDOTA_BaseNPC[];
```

Find units that intersect the given line with the given flags.

### FindUnitsInRadius

```ts
declare function FindUnitsInRadius(
    team: DOTATeam_t,
    location: Vector,
    cacheUnit: CBaseEntity | undefined,
    radius: number,
    teamFilter: DOTA_UNIT_TARGET_TEAM,
    typeFilter: DOTA_UNIT_TARGET_TYPE,
    flagFilter: DOTA_UNIT_TARGET_FLAGS,
    order: FindOrder,
    canGrowCache: boolean,
): CDOTA_BaseNPC[];
```

Finds the units in a given radius with the given flags.

### FireEntityIOInputNameOnly

```ts
declare function FireEntityIOInputNameOnly(arg1: number, arg2: string): void;
```

Fire Entity's Action Input w/no data.

**Availability:** `both`

### FireEntityIOInputString

```ts
declare function FireEntityIOInputString(arg1: number, arg2: string, arg3: string): void;
```

Fire Entity's Action Input with passed String - you own the memory.

**Availability:** `both`

### FireEntityIOInputVec

```ts
declare function FireEntityIOInputVec(arg1: number, arg2: string, arg3: Vector): void;
```

Fire Entity's Action Input with passed Vector - you own the memory.

**Availability:** `both`

### FireGameEvent

```ts
declare function FireGameEvent<TName extends keyof GameEventDeclarations>(
    eventName: TName,
    eventData: GameEventDeclarations[TName],
): void;
```

Fire a game event.

**Availability:** `both`

### FireGameEventLocal

```ts
declare function FireGameEventLocal<TName extends keyof GameEventDeclarations>(
    eventName: TName,
    eventData: GameEventDeclarations[TName],
): void;
```

Fire a game event without broadcasting to the client.

**Availability:** `both`

### FrameTime

```ts
declare function FrameTime(): number;
```

Get the time spent on the server in the last frame.

**Availability:** `both`

### GetAbilityKeyValuesByName

```ts
declare function GetAbilityKeyValuesByName(arg1: string): object;
```

Get ability data by ability name.

**Availability:** `both`

### GetAbilityTextureNameForAbility

```ts
declare function GetAbilityTextureNameForAbility(abilityName: string): string;
```

Gets the ability texture name for an ability.

**Availability:** `both`

### GetActiveSpawnGroupHandle

```ts
declare function GetActiveSpawnGroupHandle(): SpawnGroupHandle;
```

Returns the currently active spawn group handle.

**Availability:** `both`

### GetClearSpaceForUnit

```ts
declare function GetClearSpaceForUnit(arg1: object, arg2: Vector): Vector;
```

Returns a location for the unit that is not already occupied.

### GetDedicatedServerKey

```ts
declare function GetDedicatedServerKey(version: string): string;
```

**Deprecated:** This function is unsafe. Prefer using `GetDedicatedServerKeyV2`
            instead.
 

### GetDedicatedServerKeyV2

```ts
declare function GetDedicatedServerKeyV2(version: string): string;
```

### GetDedicatedServerKeyV3

```ts
declare function GetDedicatedServerKeyV3(version: string): string;
```

### GetEntityIndexForTreeId

```ts
declare function GetEntityIndexForTreeId(treeId: number): EntityIndex;
```

Get the enity index for a tree id specified as the entindex_target of a
DOTA_UNIT_ORDER_CAST_TARGET_TREE.

### GetFrameCount

```ts
declare function GetFrameCount(): number;
```

Returns the engines current frame count.

**Availability:** `both`

### GetGroundHeight

```ts
declare function GetGroundHeight(location: Vector, unitHull: CDOTA_BaseNPC | undefined): number;
```

### GetGroundPosition

```ts
declare function GetGroundPosition(location: Vector, unitHull: CDOTA_BaseNPC | undefined): Vector;
```

Returns the supplied position moved to the ground. Second parameter is an NPC
for measuring movement collision hull offset.

### GetItemCost

```ts
declare function GetItemCost(arg1: string): number;
```

Get the cost of an item by name.

### GetItemDefOwnedCount

```ts
declare function GetItemDefOwnedCount(arg1: number, arg2: number): number;
```

### GetItemDefQuantity

```ts
declare function GetItemDefQuantity(arg1: number, arg2: number): number;
```

### GetListenServerHost

```ts
declare function GetListenServerHost(): CDOTAPlayerController;
```

Get the local player on a listen server.

**Availability:** `both`

### GetLobbyEventGameDetails

```ts
declare function GetLobbyEventGameDetails(): object;
```

### GetLocalPlayerID

```ts
declare function GetLocalPlayerID(): PlayerID;
```

Get the local player ID.

**Availability:** `client`

### GetLocalPlayerTeam

```ts
declare function GetLocalPlayerTeam(arg1: number): DOTATeam_t;
```

Get the local player team.

**Availability:** `client`

### GetMapName

```ts
declare function GetMapName(): string;
```

Get the name of the map.

**Availability:** `both`

### GetMaxOutputDelay

```ts
declare function GetMaxOutputDelay(arg1: number, arg2: string): number;
```

Get the longest delay for all events attached to an output.

**Availability:** `both`

### GetPhysAngularVelocity

```ts
declare function GetPhysAngularVelocity(arg1: object): Vector;
```

Get Angular Velocity for VPHYS or normal object. Returns a vector of the axis
of rotation, multiplied by the degrees of rotation per second.

**Availability:** `both`

### GetPhysVelocity

```ts
declare function GetPhysVelocity(arg1: object): Vector;
```

Get Velocity for VPHYS or normal object.

**Availability:** `both`

### GetPotentialNeutralItemDrop

```ts
declare function GetPotentialNeutralItemDrop(tier: number, team: DOTATeam_t): string;
```

Given the item tier and the team, roll for the name of a valid neutral item
drop, considering previous drops and consumables.

### GetSystemDate

```ts
declare function GetSystemDate(): string;
```

Get the current real world date.

### GetSystemTime

```ts
declare function GetSystemTime(): string;
```

Get the current real world time.

### GetSystemTimeMS

```ts
declare function GetSystemTimeMS(): number;
```

Get system time in milliseconds.

### GetTargetAOELocation

```ts
declare function GetTargetAOELocation(
    arg1: number,
    arg2: number,
    arg3: number,
    arg4: Vector,
    arg5: number,
    arg6: number,
    arg7: number,
): Vector;
```

### GetTargetLinearLocation

```ts
declare function GetTargetLinearLocation(
    arg1: number,
    arg2: number,
    arg3: number,
    arg4: Vector,
    arg5: number,
    arg6: number,
    arg7: number,
): Vector;
```

### GetTeamHeroKills

```ts
declare function GetTeamHeroKills(team: DOTATeam_t): number;
```

### GetTeamName

```ts
declare function GetTeamName(team: DOTATeam_t): string;
```

### GetTreeIdForEntityIndex

```ts
declare function GetTreeIdForEntityIndex(entityIndex: EntityIndex): number;
```

Given and entity index of a tree, get the tree id for use for use with with
unit orders.

### GetUnitKeyValuesByName

```ts
declare function GetUnitKeyValuesByName(arg1: string): object;
```

Get unit data by ability name.

**Availability:** `both`

### GetWorldMaxX

```ts
declare function GetWorldMaxX(): number;
```

Gets the world's maximum X position.

### GetWorldMaxY

```ts
declare function GetWorldMaxY(): number;
```

Gets the world's maximum Y position.

### GetWorldMinX

```ts
declare function GetWorldMinX(): number;
```

Gets the world's minimum X position.

### GetWorldMinY

```ts
declare function GetWorldMinY(): number;
```

Gets the world's minimum Y position.

### GetXPNeededToReachNextLevel

```ts
declare function GetXPNeededToReachNextLevel(level: number): number;
```

Get amount of XP required to reach the next level.

### HeroMaxLevel

```ts
declare function HeroMaxLevel(arg1: object): void;
```

Max out a hero's level and give them all appropriate abilities and talents.

### InitLogFile

```ts
declare function InitLogFile(arg1: string, arg2: string): void;
```

**Availability:** `both`

**Deprecated:** InitLogFile is deprecated. Print to the console for logging instead.

### IsClient

```ts
declare function IsClient(): boolean;
```

Returns true if this is lua running from the client.dll.

**Availability:** `both`

### IsDedicatedServer

```ts
declare function IsDedicatedServer(): boolean;
```

Returns true if this server is a dedicated server.

**Availability:** `both`

### IsDotaAltPressed

```ts
declare function IsDotaAltPressed(): boolean;
```

Returns true if whatever alt is remapped to is pressed.

**Availability:** `client`

### IsDotaCtrlPressed

```ts
declare function IsDotaCtrlPressed(): boolean;
```

Returns true if whatever ctrl is remapped to is pressed.

**Availability:** `client`

### IsInToolsMode

```ts
declare function IsInToolsMode(): boolean;
```

Returns true if this is lua running within tools mode.

**Availability:** `both`

### IsLocationVisible

```ts
declare function IsLocationVisible(team: DOTATeam_t, location: Vector): boolean;
```

Ask fog of war if a location is visible to a certain team.

### IsMangoTree

```ts
declare function IsMangoTree(entity: CBaseEntity): entity is CBaseAnimatingActivity;
```

Is this entity a mango tree? (hEntity).

### IsMarkedForDeletion

```ts
declare function IsMarkedForDeletion(entity: CBaseEntity): boolean;
```

Returns true if the entity is valid and marked for deletion.

**Availability:** `both`

### IsServer

```ts
declare function IsServer(): boolean;
```

Returns true if this is lua running from the server.dll.

**Availability:** `both`

### IsUnitInValidPosition

```ts
declare function IsUnitInValidPosition(unit: CBaseEntity): boolean;
```

Returns true if the unit is in a valid position in the gridnav.

### IsValidEntity

```ts
declare function IsValidEntity(entity: object | undefined): entity is CBaseEntity;
```

Checks to see if the given hScript is a valid entity.

**Availability:** `both`

### LerpVectors

```ts
declare function LerpVectors(arg1: Vector, arg2: Vector, arg3: number): Vector;
```

Lerp between two vectors by a float factor returning new vector.

**Availability:** `both`

### LimitPathingSearchDepth

```ts
declare function LimitPathingSearchDepth(arg1: number): void;
```

Set the limit on the pathfinding search space.

### LinkLuaModifier

```ts
declare function LinkLuaModifier(className: string, filePath: string, luaModifierType: LuaModifierType): void;
```

Link a lua-defined modifier with the associated class.

**Availability:** `both`

### ListenToGameEvent

```ts
declare function ListenToGameEvent<TName extends keyof GameEventDeclarations>(
    eventName: TName,
    listener: (event: GameEventProvidedProperties & GameEventDeclarations[TName]) => void,
    context: undefined,
): EventListenerID;
```

Register as a listener for a game event from script.

**Availability:** `both`

### ListenToGameEvent

```ts
declare function ListenToGameEvent<TName extends keyof GameEventDeclarations, TContext extends {}>(
    eventName: TName,
    listener: (this: TContext, event: GameEventProvidedProperties & GameEventDeclarations[TName]) => void,
    context: TContext,
): EventListenerID;
```

### LoadKeyValues

```ts
declare function LoadKeyValues(filePath: string): object;
```

Creates a table from the specified keyvalues text file.

**Availability:** `both`

### LoadKeyValuesFromString

```ts
declare function LoadKeyValuesFromString(kvString: string): object;
```

Creates a table from the specified keyvalues string.

**Availability:** `both`

### LocalTime

```ts
declare function LocalTime(): LocalTime;
```

Get the current local time.

**Availability:** `both`

### MakeStringToken

```ts
declare function MakeStringToken(arg1: string): number;
```

Checks to see if the given hScript is a valid entity.

**Availability:** `both`

### ManuallyTriggerSpawnGroupCompletion

```ts
declare function ManuallyTriggerSpawnGroupCompletion(handle: SpawnGroupHandle): void;
```

Triggers the creation of entities in a manually-completed spawn group.

**Availability:** `both`

### MinimapEvent

```ts
declare function MinimapEvent(
    team: DOTATeam_t,
    entity: CBaseEntity,
    xCoord: number,
    yCoord: number,
    eventType: DOTAMinimapEvent_t,
    eventDuration: number,
): void;
```

Start a minimap event.

### Msg

```ts
declare function Msg(message: string): void;
```

Print a message.

**Availability:** `both`

### PauseGame

```ts
declare function PauseGame(paused: boolean): void;
```

Pause or unpause the game.

### Plat_FloatTime

```ts
declare function Plat_FloatTime(): number;
```

Get the current float time from the engine.

**Availability:** `both`

### PlayerInstanceFromIndex

```ts
declare function PlayerInstanceFromIndex(entityIndex: EntityIndex): CDOTAPlayerController | undefined;
```

Get a script instance of a player by index.

**Availability:** `both`

### PrecacheEntityFromTable

```ts
declare function PrecacheEntityFromTable(arg1: string, arg2: object, context: CScriptPrecacheContext): void;
```

Precache an entity from KeyValues in table.

**Availability:** `both`

### PrecacheEntityListFromTable

```ts
declare function PrecacheEntityListFromTable(arg1: object, context: CScriptPrecacheContext): void;
```

Precache a list of entity KeyValues tables.

**Availability:** `both`

### PrecacheItemByNameAsync

```ts
declare function PrecacheItemByNameAsync(itemName: string, callback: (precacheId: number) => void): void;
```

Asynchronously precaches a DOTA item by its dota_npc_items.txt name, provides a
callback when it's finished.

### PrecacheItemByNameSync

```ts
declare function PrecacheItemByNameSync(itemName: string, context: CScriptPrecacheContext): void;
```

Precaches a DOTA item by its dota_npc_items.txt name.

### PrecacheModel

```ts
declare function PrecacheModel(modelName: string, context: CScriptPrecacheContext): void;
```

Manually precache a single model.

### PrecacheResource

```ts
declare function PrecacheResource(arg1: string, arg2: string, context: CScriptPrecacheContext): void;
```

Manually precache a single resource.

### PrecacheUnitByNameAsync

```ts
declare function PrecacheUnitByNameAsync(
    unitName: string,
    callback: (precacheId: number) => void,
    playerId?: PlayerID,
): void;
```

Asynchronously precaches a DOTA unit by its dota_npc_units.txt name, provides a
callback when it's finished.

### PrecacheUnitByNameSync

```ts
declare function PrecacheUnitByNameSync(unitName: string, context: CScriptPrecacheContext, playerId?: PlayerID): void;
```

Precaches a DOTA unit by its dota_npc_units.txt name.

### PrecacheUnitFromTableAsync

```ts
declare function PrecacheUnitFromTableAsync(arg1: object, callback: (precacheId: number) => void): void;
```

Precaches a DOTA unit from a table of entity key values.

### PrecacheUnitFromTableSync

```ts
declare function PrecacheUnitFromTableSync(arg1: object, context: CScriptPrecacheContext): void;
```

Precaches a DOTA unit from a table of entity key values.

### PrintLinkedConsoleMessage

```ts
declare function PrintLinkedConsoleMessage(message: string, tooltip: string): void;
```

Print a console message with a linked console command.

**Availability:** `both`

### QSlerp

```ts
declare function QSlerp(from_angle: QAngle, to_angle: QAngle, time: number): QAngle;
```

Spherical lerp of angle from->to based on time.

**Availability:** `both`

### RandomFloat

```ts
declare function RandomFloat(min: number, max: number): number;
```

Get a random float within a range.

### RandomFloatWrapper

```ts
declare function RandomFloatWrapper(arg1: number, arg2: number): number;
```

Generate a random floating point number within a range, inclusive.

**Availability:** `both`

### RandomInt

```ts
declare function RandomInt(min: number, max: number): number;
```

Get a random int within a range.

**Availability:** `both`

### RandomVector

```ts
declare function RandomVector(length: number): Vector;
```

Get a random 2D vector of the given length.

### RecordNeutralItemEarned

```ts
declare function RecordNeutralItemEarned(arg1: object, arg2: object, arg3: number): void;
```

Record in player resources that a new neutral item has been created, if it
hasn't already been, and show a toast.

### RegisterCustomAnimationScriptForModel

```ts
declare function RegisterCustomAnimationScriptForModel(arg1: string, arg2: string): void;
```

Register a custom animation script to run when a model loads.

### RegisterSpawnGroupFilterProxy

```ts
declare function RegisterSpawnGroupFilterProxy(arg1: string): void;
```

Create a C proxy for a script-based spawn group filter.

**Availability:** `both`

### ReloadMOTD

```ts
declare function ReloadMOTD(): void;
```

Reloads the MotD file.

**Availability:** `both`

### RemoveFOWViewer

```ts
declare function RemoveFOWViewer(teamId: DOTATeam_t, viewerId: ViewerID): void;
```

Remove temporary vision for a given team.

### RemoveSpawnGroupFilterProxy

```ts
declare function RemoveSpawnGroupFilterProxy(arg1: string): void;
```

Remove the C proxy for a script-based spawn group filter.

**Availability:** `both`

### ResolveNPCPositions

```ts
declare function ResolveNPCPositions(location: Vector, radius: number): void;
```

Check and fix units that have been assigned a position inside collision radius
of other NPCs.

### RollPercentage

```ts
declare function RollPercentage(successPercentage: number): boolean;
```

Rolls a number from 1 to 100 and returns true if the roll is less than or equal
to the number specified.

### RollPseudoRandomPercentage

```ts
declare function RollPseudoRandomPercentage(chance: number, pseudoRandomId: PseudoRandom, unit: CDOTA_BaseNPC): boolean;
```

**Parameters:**

- pseudoRandomId Any number can be specified. Using
                      DOTA_PSEUDO_RANDOM_NONE makes it act as a pure RNG.
 

### RotateOrientation

```ts
declare function RotateOrientation(arg1: QAngle, arg2: QAngle): QAngle;
```

Rotate a QAngle by another QAngle.

**Availability:** `both`

### RotatePosition

```ts
declare function RotatePosition(arg1: Vector, arg2: QAngle, arg3: Vector): Vector;
```

Rotate a Vector around a point.

**Availability:** `both`

### RotateQuaternionByAxisAngle

```ts
declare function RotateQuaternionByAxisAngle(arg1: never, arg2: Vector, arg3: number): never;
```

Rotates a quaternion by the specified angle around the specified vector axis.

**Availability:** `both`

### RotationDelta

```ts
declare function RotationDelta(arg1: QAngle, arg2: QAngle): QAngle;
```

Find the delta between two QAngles.

**Availability:** `both`

### RotationDeltaAsAngularVelocity

```ts
declare function RotationDeltaAsAngularVelocity(arg1: QAngle, arg2: QAngle): Vector;
```

Converts delta QAngle to an angular velocity Vector.

**Availability:** `both`

### Say

```ts
declare function Say(entity: CBaseEntity | undefined, message: string, teamOnly: boolean): void;
```

Have Entity say string, and teamOnly or not.

### ScreenShake

```ts
declare function ScreenShake(
    center: Vector,
    amplitude: number,
    frequency: number,
    duration: number,
    radius: number,
    command: 0 | 1,
    airShake: boolean,
): void;
```

Start a screenshake.

**Availability:** `both`

**Parameters:**

- command SHAKE_START = 0, SHAKE_STOP = 1

### Script_RandomFloat

```ts
declare function Script_RandomFloat(arg1: number, arg2: number): number;
```

Get a random float within a range.

**Availability:** `both`

### Script_RemapValClamped

```ts
declare function Script_RemapValClamped(arg1: number, arg2: number, arg3: number, arg4: number, arg5: number): number;
```

RemapValClamped.

### SendOverheadEventMessage

```ts
declare function SendOverheadEventMessage(
    sendToPlayer: CDOTAPlayerController | undefined,
    messageType: DOTA_OVERHEAD_ALERT,
    targetEntity: CDOTA_BaseNPC,
    value: number,
    sourcePlayer: CDOTAPlayerController | undefined,
): void;
```

### SendToConsole

```ts
declare function SendToConsole(arg1: string): void;
```

Send a string to the console as a client command.

**Availability:** `both`

### SendToServerConsole

```ts
declare function SendToServerConsole(arg1: string): void;
```

Send a string to the console as a server command.

### SetOpvarFloatAll

```ts
declare function SetOpvarFloatAll(arg1: string, arg2: string, arg3: string, arg4: number): void;
```

Sets an opvar value for all players.

**Availability:** `both`

### SetOpvarFloatPlayer

```ts
declare function SetOpvarFloatPlayer(arg1: string, arg2: string, arg3: string, arg4: number, arg5: object): void;
```

Sets an opvar value for a single player.

**Availability:** `both`

### SetPhysAngularVelocity

```ts
declare function SetPhysAngularVelocity(arg1: object, arg2: Vector): void;
```

Set Angular Velocity for VPHYS or normal object, from a vector of the axis of
rotation, multiplied by the degrees of rotation per second.

**Availability:** `both`

### SetQuestName

```ts
declare function SetQuestName(arg1: string): void;
```

Set the current quest name.

**Availability:** `both`

### SetQuestPhase

```ts
declare function SetQuestPhase(arg1: number): void;
```

Set the current quest phase.

**Availability:** `both`

### SetRenderingEnabled

```ts
declare function SetRenderingEnabled(arg1: number, arg2: boolean): void;
```

Set rendering on/off for an ehandle.

**Availability:** `both`

**Deprecated:** Instantly crashes the game.

### SetTeamCustomHealthbarColor

```ts
declare function SetTeamCustomHealthbarColor(team: DOTATeam_t, r: number, g: number, b: number): void;
```

### ShowCustomHeaderMessage

```ts
declare function ShowCustomHeaderMessage(message: string, playerId: PlayerID, value: number, time: number): void;
```

Supports localized strings - %s1 = PlayerName, %s2 = Value, %s3 = TeamName.

### ShowGenericPopup

```ts
declare function ShowGenericPopup(arg1: string, arg2: string, arg3: string, arg4: string, arg5: number): void;
```

Show a generic popup dialog for all players.

### ShowGenericPopupToPlayer

```ts
declare function ShowGenericPopupToPlayer(
    arg1: object,
    arg2: string,
    arg3: string,
    arg4: string,
    arg5: string,
    arg6: number,
): void;
```

Show a generic popup dialog to a specific player.

### ShowMessage

```ts
declare function ShowMessage(arg1: string): void;
```

Print a hud message on all clients.

### SpawnDOTAShopTriggerRadiusApproximate

```ts
declare function SpawnDOTAShopTriggerRadiusApproximate(origin: Vector, radius: number): CDOTA_ShopTrigger;
```

### SpawnEffigyOfUnitOrModel

```ts
declare function SpawnEffigyOfUnitOrModel(
    arg1: string,
    arg2: number,
    arg3: Vector,
    arg4: Vector,
    arg5: number,
    arg6: number,
    arg7: number,
): object;
```

Spawn an effigy of the target unit.

### SpawnEntityFromTableAsynchronous

```ts
declare function SpawnEntityFromTableAsynchronous(arg1: string, arg2: object, arg3: object, arg4: object): void;
```

Asynchronously spawns a single entity from a table.

**Availability:** `both`

### SpawnEntityFromTableSynchronous

```ts
declare function SpawnEntityFromTableSynchronous(baseclass: string, data: object): CBaseEntity;
```

Synchronously spawns a single entity from a table.

**Availability:** `both`

### SpawnEntityGroupFromTable

```ts
declare function SpawnEntityGroupFromTable(arg1: object, arg2: boolean, arg3: object): boolean;
```

Hierarchically spawn an entity group from a set of spawn tables.

**Availability:** `both`

### SpawnEntityListFromTableAsynchronous

```ts
declare function SpawnEntityListFromTableAsynchronous(arg1: object, arg2: object): number;
```

Asynchronously spawn an entity group from a list of spawn tables. A callback
will be triggered when the spawning is complete.

**Availability:** `both`

### SpawnEntityListFromTableSynchronous

```ts
declare function SpawnEntityListFromTableSynchronous(arg1: object): object;
```

Synchronously spawn an entity group from a list of spawn tables.

**Availability:** `both`

### SpawnMangoTree

```ts
declare function SpawnMangoTree(
    pos: Vector,
    team: number,
    duration: number,
    mangoInterval: number,
    initialMangoes: number,
): object;
```

Spawn a mango tree.

### SplineQuaternions

```ts
declare function SplineQuaternions(arg1: never, arg2: never, arg3: number): never;
```

Very basic interpolation of v0 to v1 over t on [0,1].

**Availability:** `both`

### SplineVectors

```ts
declare function SplineVectors(arg1: Vector, arg2: Vector, arg3: number): Vector;
```

Very basic interpolation of v0 to v1 over t on [0,1].

**Availability:** `both`

### StartSoundEvent

```ts
declare function StartSoundEvent(arg1: string, arg2: object): void;
```

Start a sound event.

**Availability:** `both`

### StartSoundEventFromPosition

```ts
declare function StartSoundEventFromPosition(soundName: string, position: Vector): void;
```

Start a sound event from position.

**Availability:** `both`

### StartSoundEventFromPositionReliable

```ts
declare function StartSoundEventFromPositionReliable(soundName: string, position: Vector): void;
```

Start a sound event from position with reliable delivery.

**Availability:** `both`

### StartSoundEventFromPositionUnreliable

```ts
declare function StartSoundEventFromPositionUnreliable(soundName: string, position: Vector): void;
```

Start a sound event from position with optional delivery.

**Availability:** `both`

### StartSoundEventReliable

```ts
declare function StartSoundEventReliable(arg1: string, arg2: object): void;
```

Start a sound event with reliable delivery.

**Availability:** `both`

### StartSoundEventUnreliable

```ts
declare function StartSoundEventUnreliable(arg1: string, arg2: object): void;
```

Start a sound event with optional delivery.

**Availability:** `both`

### StopEffect

```ts
declare function StopEffect(arg1: object, arg2: string): void;
```

Pass entity and effect name.

**Availability:** `both`

### StopGlobalSound

```ts
declare function StopGlobalSound(arg1: string): void;
```

Stop named sound for all players.

### StopListeningToAllGameEvents

```ts
declare function StopListeningToAllGameEvents(arg1: object): void;
```

Stop listening to all game events within a specific context.

**Availability:** `both`

### StopListeningToGameEvent

```ts
declare function StopListeningToGameEvent(listenerId: EventListenerID): boolean;
```

Stop listening to a particular game event.

**Availability:** `both`

### StopSoundEvent

```ts
declare function StopSoundEvent(arg1: string, arg2: object): void;
```

Stops a sound event with optional delivery.

**Availability:** `both`

### StopSoundOn

```ts
declare function StopSoundOn(arg1: string, arg2: object): void;
```

Stop named sound on Entity.

**Availability:** `both`

### Time

```ts
declare function Time(): number;
```

Get the current server time.

**Availability:** `both`

### TraceCollideable

```ts
declare function TraceCollideable(query: TraceCollideableInputs): query is TraceCollideableOutputs;
```

**Availability:** `both`

### TraceHull

```ts
declare function TraceHull(query: TraceHullInputs): query is TraceHullOutputs;
```

**Availability:** `both`

### TraceLine

```ts
declare function TraceLine(query: TraceLineInputs): query is TraceLineOutputs;
```

**Availability:** `both`

### UnitFilter

```ts
declare function UnitFilter(
    npc: CDOTA_BaseNPC,
    teamFilter: DOTA_UNIT_TARGET_TEAM,
    typeFilter: DOTA_UNIT_TARGET_TYPE,
    flagFilter: DOTA_UNIT_TARGET_FLAGS,
    team: DOTATeam_t,
): UnitFilterResult;
```

Check if a unit passes a set of filters.

**Availability:** `both`

### UnloadSpawnGroup

```ts
declare function UnloadSpawnGroup(arg1: string): void;
```

Unload a spawn group by name.

**Availability:** `both`

### UnloadSpawnGroupByHandle

```ts
declare function UnloadSpawnGroupByHandle(handle: SpawnGroupHandle): void;
```

Unload a spawn group by handle.

**Availability:** `both`

### UpdateEventPoints

```ts
declare function UpdateEventPoints(eventPointData: object): void;
```

### UserIDToControllerHScript

```ts
declare function UserIDToControllerHScript(arg1: number): object;
```

Turn a userid integer (typically, fields named 'userid' in game events) to an
HScript representing the associated player controller's script instance.

**Availability:** `both`

### UTIL_MessageText

```ts
declare function UTIL_MessageText(
    arg1: number,
    arg2: string,
    arg3: number,
    arg4: number,
    arg5: number,
    arg6: number,
): void;
```

Sends colored text to one client.

### UTIL_MessageText_WithContext

```ts
declare function UTIL_MessageText_WithContext(
    arg1: number,
    arg2: string,
    arg3: number,
    arg4: number,
    arg5: number,
    arg6: number,
    arg7: object,
): void;
```

Sends colored text to one client. (Valid context keys: player_id, value,
team_id).

### UTIL_MessageTextAll

```ts
declare function UTIL_MessageTextAll(arg1: string, arg2: number, arg3: number, arg4: number, arg5: number): void;
```

Sends colored text to all clients.

### UTIL_MessageTextAll_WithContext

```ts
declare function UTIL_MessageTextAll_WithContext(
    arg1: string,
    arg2: number,
    arg3: number,
    arg4: number,
    arg5: number,
    arg6: object,
): void;
```

Sends colored text to all clients. (Valid context keys: player_id, value,
team_id).

### UTIL_Remove

```ts
declare function UTIL_Remove(entity: CBaseEntity | undefined): void;
```

Removes the specified entity.

**Availability:** `both`

### UTIL_RemoveImmediate

```ts
declare function UTIL_RemoveImmediate(entity: CBaseEntity | undefined): void;
```

Immediately removes the specified entity.

**Availability:** `both`

### UTIL_ResetMessageText

```ts
declare function UTIL_ResetMessageText(arg1: number): void;
```

Clear all message text on one client.

### UTIL_ResetMessageTextAll

```ts
declare function UTIL_ResetMessageTextAll(): void;
```

Clear all message text from all clients.

### VectorAngles

```ts
declare function VectorAngles(arg1: Vector): QAngle;
```

### VectorToAngles

```ts
declare function VectorToAngles(arg1: Vector): QAngle;
```

Get Qangles (with no roll) for a Vector.

**Availability:** `both`

### Warning

```ts
declare function Warning(message: string): void;
```

Print a warning.

**Availability:** `both`

## Classes

### CBaseAnimatingActivity

Extends `CBaseModelEntity`

**Methods**

| Method | Description |
| --- | --- |
| `ActiveSequenceDuration(): number` | Returns the duration in seconds of the active sequence. |
| `GetCycle(): number` | Get the cycle of the animation. |
| `GetSequence(): string` | Returns the name of the active sequence. |
| `IsSequenceFinished(): boolean` | Ask whether the main sequence is done playing. |
| `ResetSequence(sequenceName: string): void` | Sets the active sequence by name, resetting the current cycle. |
| `SequenceDuration(sequenceName: string): number` | Returns the duration in seconds of the given sequence name. |
| `SetCycle(cycle: number): void` | Set the cycle of the animation. |
| `SetPoseParameter(name: string, value: number): number` | Set the specified pose parameter to the specified value. |
| `SetSequence(sequenceName: string): void` | Sets the active sequence by name, keeping the current cycle. |
| `StopAnimation(): void` | Stop the current animation by setting playback rate to 0.0. |

### CBaseAnimatingOverlay

Extends `CBaseAnimatingActivity`

_No members._

### CBaseAnimGraph

Extends `CBaseModelEntity`

_No members._

### CBaseCombatCharacter

Extends `CBaseAnimatingOverlay`

_No members._

### CBaseEntity

Extends `CEntityInstance`

**Methods**

| Method | Description |
| --- | --- |
| `AddEffects(flags: EntityEffects): void` | Adds the render effect flag. |
| `ApplyAbsVelocityImpulse(vecImpulse: Vector): void` | Apply a Velocity Impulse. |
| `ApplyLocalAngularVelocityImpulse(angImpulse: Vector): void` | Apply an Ang Velocity Impulse. |
| `Attribute_GetFloatValue(name: string, defaultValue: number): number` | Get float value for an entity attribute. |
| `Attribute_GetIntValue(name: string, defaultValue: number): number` | Get int value for an entity attribute. |
| `Attribute_SetFloatValue(name: string, value: number): void` | Set float value for an entity attribute. |
| `Attribute_SetIntValue(name: string, value: number): void` | Set int value for an entity attribute. |
| `DeleteAttribute(name: string): void` | Delete an entity attribute. |
| `EmitSound(soundname: string): void` | Plays a sound from this entity. |
| `EmitSoundParams(soundName: string, pitch: number, volume: number, delay: number): void` | Plays/modifies a sound from this entity. changes sound if nPitch and/or flVol<br>or flSoundTime is > 0. |
| `EyeAngles(): QAngle` | Get the qangles that this entity is looking at. |
| `EyePosition(): Vector` | Get vector to eye position - absolute coords. |
| `FirstMoveChild(): CBaseEntity` |  |
| `FollowEntity(entity: CBaseEntity, boneMerge: boolean): void` |  |
| `FollowEntityMerge(ent: object, boneOrAttachName: string): void` | HEntity to follow, string BoneOrAttachName. |
| `GatherCriteria(result: object): void` | Returns a table containing the criteria that would be used for response queries<br>on this entity. This is the same as the table that is passed to response rule<br>script function callbacks. |
| `GetAbsOrigin(): Vector` | **Availability:** `both` |
| `GetAbsScale(): number` |  |
| `GetAngles(): QAngle` |  |
| `GetAnglesAsVector(): Vector` | Get entity pitch, yaw, roll as a vector. |
| `GetAngularVelocity(): Vector` | Get the local angular velocity - returns a vector of pitch,yaw,roll. |
| `GetBaseVelocity(): Vector` | Get Base? velocity. |
| `GetBoundingMaxs(): Vector` | Get a vector containing max bounds, centered on object. |
| `GetBoundingMins(): Vector` | Get a vector containing min bounds, centered on object. |
| `GetBounds(): EntityBounds` | Get a table containing the 'Mins' & 'Maxs' vector bounds, centered on object. |
| `GetCenter(): Vector` | Get vector to center of object - absolute coords. |
| `GetChildren(): CBaseEntity[]` | Get the entities parented to this entity. |
| `GetContext(name: string): string \| number \| undefined` | Looks up a context and returns it if available. May return string, float, or<br>null (if the context isn't found). |
| `GetForwardVector(): Vector` | Get the forward vector of the entity. |
| `GetHealth(): number` | Get the health of this entity.<br><br>**Availability:** `both` |
| `GetLeftVector(): Vector` | Get the left vector of the entity. |
| `GetLocalAngles(): QAngle` | Get entity local pitch, yaw, roll as a QAngle. |
| `GetLocalAngularVelocity(): QAngle` | Maybe local angvel. |
| `GetLocalOrigin(): Vector` | Get entity local origin as a Vector. |
| `GetLocalScale(): number` |  |
| `GetLocalVelocity(): Vector` | Get Entity relative velocity. |
| `GetMass(): number` | Get the mass of an entity. (returns 0 if it doesn't have a physics object). |
| `GetMaxHealth(): number` | Get the maximum health of this entity.<br><br>**Availability:** `both` |
| `GetModelName(): string` | Returns the name of the model. |
| `GetMoveParent(): CBaseEntity` | If in hierarchy, retrieves the entity's parent. |
| `GetOrigin(): Vector` |  |
| `GetOwner(): CBaseEntity` | Gets this entity's owner. |
| `GetOwnerEntity(): CBaseEntity` | Get the owner entity, if there is one. |
| `GetRightVector(): Vector` | Get the right vector of the entity. WARNING: This produces a left-handed<br>coordinate system. Use GetLeftVector instead (which is aligned with the y axis<br>of the entity). |
| `GetRootMoveParent(): CBaseEntity` | If in hierarchy, walks up the hierarchy to find the root parent. |
| `GetSoundDuration(soundname: string, actormodel: string): number` | Returns float duration of the sound. Takes soundname and optional<br>actormodelname. |
| `GetSpawnGroupHandle(): SpawnGroupHandle` | Returns the spawn group handle of this entity. |
| `GetTeam(): DOTATeam_t` | Get the team number of this entity. |
| `GetTeamNumber(): DOTATeam_t` | Get the team number of this entity.<br><br>**Availability:** `both` |
| `GetUpVector(): Vector` | Get the up vector of the entity. |
| `GetVelocity(): Vector` |  |
| `HasAttribute(name: string): boolean` | See if an entity has a particular attribute. |
| `IsAlive(): boolean` | Is this entity alive? |
| `IsBaseNPC(): this is CDOTA_BaseNPC` | Is this entity an CDOTA_BaseNPC?<br><br>**Availability:** `both` |
| `IsDOTANPC(): boolean` | Is this entity a Dota NPC? |
| `IsInstance<T extends CBaseEntity>(classOrClassName: DotaConstructor<T>): this is T` | **Availability:** `both` |
| `IsNPC(): boolean` | Is this entity an CAI_BaseNPC? |
| `IsPlayer(): this is CDOTAPlayerController` | Back compat: Is this entity a player pawn *or* controller? |
| `IsPlayerController(): this is CDOTAPlayerController` | Is this entity a player controller? |
| `IsPlayerPawn(): this is CBasePlayerPawn` | Is this entity a player pawn? |
| `Kill(): void` |  |
| `NextMovePeer(): CBaseEntity` |  |
| `PrecacheScriptSound(soundname: string): void` | Precache a sound for later playing. |
| `RemoveEffects(flags: EntityEffects): void` | Removes the render effect flag. |
| `SetAbsAngles(pitch: number, yaw: number, roll: number): void` | Set entity pitch, yaw, roll by component. |
| `SetAbsOrigin(origin: Vector): void` |  |
| `SetAbsScale(scale: number): void` |  |
| `SetAngles(pitch: number, yaw: number, roll: number): void` | Set entity pitch, yaw, roll by component. |
| `SetAngularVelocity(pitchVel: number, yawVel: number, rollVel: number): void` | Set the local angular velocity. |
| `SetConstraint(pos: Vector): void` | Set the position of the constraint. |
| `SetContext(name: string, value: string, duration: number): void` | Store any key/value pair in this entity's dialog contexts. Value must be a<br>string. Will last for duration (set 0 to mean 'forever'). |
| `SetContextNum(name: string, value: number, duration: number): void` | Store any key/value pair in this entity's dialog contexts. Value must be a<br>number (int or float). Will last for duration (set 0 to mean 'forever'). |
| `SetContextThink( contextName: string, thinkFunc: ((this: this) => number \| undefined) \| undefined, interval: number, ): void` | Set a think function on this entity.<br><br>**Availability:** `both` |
| `SetEntityName(name: string): void` | Set the name of an entity. |
| `SetForwardVector(v: Vector): void` | Set the orientation of the entity to have this forward vector. |
| `SetFriction(friction: number): void` | Set PLAYER friction, ignored for objects. |
| `SetGravity(gravity: number): void` | Set PLAYER gravity, ignored for objects. |
| `SetHealth(health: number): void` | Set the health of this entity. |
| `SetLocalAngles(pitch: number, yaw: number, roll: number): void` | Set entity local pitch, yaw, roll by component. |
| `SetLocalOrigin(origin: Vector): void` | Set entity local origin from a Vector. |
| `SetLocalScale(scale: number): void` |  |
| `SetMass(mass: number): void` | Set the mass of an entity. (does nothing if it doesn't have a physics object). |
| `SetMaxHealth(amt: number): void` | Set the maximum health of this entity. |
| `SetOrigin(v: Vector): void` |  |
| `SetOwner(owner: CBaseEntity): void` | Sets this entity's owner. This entity will be returned by GetOwner() and<br>GetOwnerEntity(). GetPlayerOwner() and GetPlayerOwnerID() will be automatically<br>inferred from this entity. |
| `SetParent(parent: CBaseEntity, attachmentname: string): void` | Set the parent for this entity. |
| `SetTeam(teamNum: DOTATeam_t): void` |  |
| `SetThink( functionName: ((entity: CBaseEntity) => number \| undefined) \| string, context: object \| undefined, contextName: string \| undefined, initialDelay: number \| undefined, ): void` | Set a think function on this entity. Uses `CBaseEntity:SetContextThink`<br>internally.<br><br>Note: optional parameters can be given in any order.<br><br>**Availability:** `both`<br><br>**Parameters:**<br><br>- functionName If `context` is provided, think function would perform a<br>                    dynamic lookup on `context` table. Otherwise searches for<br>                    that function name in caller scope.<br><br>- contextName Defaults to `functionName` if it's a string.<br><br>- initialDelay Defaults to 0 (next game frame). |
| `SetVelocity(vecVelocity: Vector): void` |  |
| `StopSound(soundname: string): void` | Stops a named sound playing from this entity. |
| `StopThink(contextName: string): void` | Stops thinker created with `CBaseEntity.SetThink`.<br><br>Alias for `CBaseEntity:SetContextThink(contextName, nil, 0)`.<br><br>**Availability:** `both` |
| `TakeDamage(damageInfo: CTakeDamageInfo): number` | Apply damage to this entity. Use CreateDamageInfo() to create a damageinfo<br>object. |
| `TransformPointEntityToWorld(point: Vector): Vector` | Returns the input Vector transformed from entity to world space. |
| `TransformPointWorldToEntity(point: Vector): Vector` | Returns the input Vector transformed from world to entity space. |
| `Trigger(): void` | Fires off this entity's OnTrigger responses. |
| `ValidatePrivateScriptScope(): void` | Validates the private script scope and creates it if one doesn't exist. |

### CBaseModelEntity

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `GetAttachmentAngles(attachment: number): Vector` | Get the attachment id's angles as a p,y,r vector. |
| `GetAttachmentForward(attachment: number): Vector` | Get the attachment id's forward vector. |
| `GetAttachmentOrigin(attachment: number): Vector` | Get the attachment id's origin vector. |
| `GetMaterialGroupHash(): number` | Get the material group hash of this entity. |
| `GetMaterialGroupMask(): Uint64` | Get the mesh group mask of this entity. |
| `GetModelScale(): number` | Get scale of entity's model. |
| `GetRenderAlpha(): number` | Get the alpha modulation of this entity.<br><br>**Availability:** `both` |
| `GetRenderColor(): Vector` | Get the render color of the entity. |
| `ScriptLookupAttachment(attachmentName: string): number` | Get the named attachment id. |
| `SetBodygroup(bodyGroup: number, choice: number): void` | Sets a bodygroup. |
| `SetBodygroupByName(name: string, value: number): void` | Sets a bodygroup by name. |
| `SetMaterialGroup(materialGroup: string): void` | Set the material group of this entity. |
| `SetMaterialGroupHash(hash: number): void` | Set the material group hash of this entity. |
| `SetMaterialGroupMask(meshGroupMask: Uint64): void` | Set the mesh group mask of this entity. |
| `SetModel(modelName: string): void` |  |
| `SetModelScale(scale: number): void` | Set scale of entity's model. |
| `SetRenderAlpha(alpha: number): void` | Set the alpha modulation of this entity. |
| `SetRenderColor(r: number, g: number, b: number): void` | Sets the render color of the entity. |
| `SetRenderMode(mode: number): void` | Sets the render mode of the entity. |
| `SetSingleMeshGroup(meshGroupName: string): void` | Set a single mesh group for this entity. |
| `SetSize(mins: Vector, maxs: Vector): void` |  |
| `SetSkin(skin: number): void` |  |

### CBasePlayerController

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `GetPawn(): object` | Returns the pawn for this controller. |

### CBasePlayerPawn

Extends `CBaseCombatCharacter`

**Methods**

| Method | Description |
| --- | --- |
| `GetController(): object` | Returns the controller for this pawn. |
| `GetEquippedWeapons(): object` | Returns an array of all the equipped weapons. |
| `GetWeaponCount(): number` | Gets the number of weapons currently equipped. |
| `IsNoclipping(): boolean` | Returns true if the player is in noclip mode. |

### CBaseTrigger

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `Disable(): void` | Disable's the trigger. |
| `Enable(): void` | Enable the trigger. |
| `IsTouching(ent: CBaseEntity): boolean` | Checks whether the passed entity is touching the trigger. |

### CBodyComponent

**Methods**

| Method | Description |
| --- | --- |
| `AddImpulseAtPosition(arg1: Vector, arg2: Vector): void` | Apply an impulse at a worldspace position to the physics.<br><br>**Availability:** `both` |
| `AddVelocity(arg1: Vector, arg2: Vector): void` | Add linear and angular velocity to the physics object.<br><br>**Availability:** `both` |
| `DetachFromParent(): void` | Detach from its parent.<br><br>**Availability:** `both` |
| `IsAttachedToParent(): boolean` | Is attached to parent.<br><br>**Availability:** `both` |
| `SetAngularVelocity(arg1: Vector): void` | **Availability:** `both` |
| `SetMaterialGroup(arg1: string): void` | **Availability:** `both` |
| `SetVelocity(arg1: Vector): void` | **Availability:** `both` |

### CCustomGameEventManager

**Methods**

| Method | Description |
| --- | --- |
| `RegisterListener<T extends string \| object>( eventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, listener: ( userId: EntityIndex, event: NetworkedData<CCustomGameEventManager.InferEventType<T, object> & { PlayerID: PlayerID }>, ) => void, ): CustomGameEventListenerID` | Register a callback to be called when a particular custom event arrives.<br>Returns a listener ID that can be used to unregister later. |
| `Send_ServerToAllClients<T extends string \| object>( eventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, eventData: CCustomGameEventManager.InferEventType<T, never>, ): void` |  |
| `Send_ServerToPlayer<T extends string \| object>( player: CDOTAPlayerController, eventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, eventData: CCustomGameEventManager.InferEventType<T, never>, ): void` |  |
| `Send_ServerToTeam<T extends string \| object>( team: DOTATeam_t, eventName: (T extends string ? T : string) \| keyof CustomGameEventDeclarations, eventData: CCustomGameEventManager.InferEventType<T, never>, ): void` |  |
| `UnregisterListener(listenerId: CustomGameEventListenerID): void` | Unregister a specific listener. |

### CCustomNetTableManager

**Methods**

| Method | Description |
| --- | --- |
| `GetTableValue< TName extends keyof CustomNetTableDeclarations, T extends CustomNetTableDeclarations[TName], K extends keyof T, >( tableName: TName, keyName: K, ): NetworkedData<T[K]>` | **Availability:** `both` |
| `SetTableValue< TName extends keyof CustomNetTableDeclarations, T extends CustomNetTableDeclarations[TName], K extends keyof T, >( tableName: TName, keyName: K, value: T[K], ): boolean` |  |

### CDebugOverlayScriptHelper

**Methods**

| Method | Description |
| --- | --- |
| `Axis(arg1: Vector, arg2: Vector, arg3: number, arg4: boolean, arg5: number): void` | Draws an axis. Specify origin + orientation in world space.<br><br>**Availability:** `both` |
| `Box( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a world-space axis-aligned box. Specify bounds in world space.<br><br>**Availability:** `both` |
| `BoxAngles( arg1: Vector, arg2: Vector, arg3: Vector, arg4: Vector, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws an oriented box at the origin. Specify bounds in local space.<br><br>**Availability:** `both` |
| `Capsule( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws a capsule. Specify base in world space.<br><br>**Availability:** `both` |
| `Circle( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws a circle. Specify center in world space.<br><br>**Availability:** `both` |
| `CircleScreenOriented( arg1: Vector, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a circle oriented to the screen. Specify center in world space.<br><br>**Availability:** `both` |
| `Cone( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws a wireframe cone. Specify endpoint and direction in world space.<br><br>**Availability:** `both` |
| `Cross( arg1: Vector, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a screen-aligned cross. Specify origin in world space.<br><br>**Availability:** `both` |
| `Cross3D( arg1: Vector, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a world-aligned cross. Specify origin in world space.<br><br>**Availability:** `both` |
| `Cross3DOriented( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws an oriented cross. Specify origin in world space.<br><br>**Availability:** `both` |
| `DrawTickMarkedLine( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws a dashed line. Specify endpoints in world space.<br><br>**Availability:** `both` |
| `EntityAttachments(arg1: number, arg2: number, arg3: number): void` | Draws the attachments of the entity.<br><br>**Availability:** `both` |
| `EntityAxis(arg1: number, arg2: number, arg3: boolean, arg4: number): void` | Draws the axis of the entity origin.<br><br>**Availability:** `both` |
| `EntityBounds( arg1: number, arg2: number, arg3: number, arg4: number, arg5: number, arg6: boolean, arg7: number, ): void` | Draws bounds of an entity.<br><br>**Availability:** `both` |
| `EntitySkeleton(arg1: number, arg2: number): void` | Draws the skeleton of the entity.<br><br>**Availability:** `both` |
| `EntityText( arg1: number, arg2: number, arg3: string, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, ): void` | Draws text on an entity.<br><br>**Availability:** `both` |
| `FilledRect2D(arg1: never, arg2: never, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number): void` | Draws a screen-space filled 2D rectangle. Coordinates are in pixels.<br><br>**Availability:** `both` |
| `HorzArrow( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws a horizontal arrow. Specify endpoints in world space.<br><br>**Availability:** `both` |
| `Line( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a line between two points.<br><br>**Availability:** `both` |
| `Line2D(arg1: never, arg2: never, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number): void` | Draws a line between two points in screenspace.<br><br>**Availability:** `both` |
| `PopDebugOverlayScope(): void` | Pops the identifier used to group overlays. Overlays marked with this<br>identifier can be deleted in a big batch.<br><br>**Availability:** `both` |
| `PushAndClearDebugOverlayScope(arg1: string): void` | Pushes an identifier used to group overlays. Deletes all existing overlays<br>using this overlay id.<br><br>**Availability:** `both` |
| `PushDebugOverlayScope(arg1: string): void` | Pushes an identifier used to group overlays. Overlays marked with this<br>identifier can be deleted in a big batch.<br><br>**Availability:** `both` |
| `RemoveAllInScope(arg1: string): void` | Removes all overlays marked with a specific identifier, regardless of their<br>lifetime.<br><br>**Availability:** `both` |
| `SolidCone( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws a solid cone. Specify endpoint and direction in world space.<br><br>**Availability:** `both` |
| `Sphere( arg1: Vector, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number, arg7: boolean, arg8: number, ): void` | Draws a wireframe sphere. Specify center in world space.<br><br>**Availability:** `both` |
| `SweptBox( arg1: Vector, arg2: Vector, arg3: Vector, arg4: Vector, arg5: Vector, arg6: number, arg7: number, arg8: number, arg9: number, arg10: number, ): void` | Draws a swept box. Specify endpoints in world space and the bounds in local<br>space.<br><br>**Availability:** `both` |
| `Text( arg1: Vector, arg2: number, arg3: string, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: number, ): void` | Draws 2D text. Specify origin in world space.<br><br>**Availability:** `both` |
| `Texture( arg1: string, arg2: never, arg3: never, arg4: number, arg5: number, arg6: number, arg7: number, arg8: never, arg9: never, arg10: number, ): void` | Draws a screen-space texture. Coordinates are in pixels.<br><br>**Availability:** `both` |
| `Triangle( arg1: Vector, arg2: Vector, arg3: Vector, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws a filled triangle. Specify vertices in world space.<br><br>**Availability:** `both` |
| `VectorText3D( arg1: Vector, arg2: Vector, arg3: string, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws 3D text. Specify origin + orientation in world space.<br><br>**Availability:** `both` |
| `VertArrow( arg1: Vector, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: boolean, arg9: number, ): void` | Draws a vertical arrow. Specify endpoints in world space.<br><br>**Availability:** `both` |
| `YawArrow( arg1: Vector, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, arg9: boolean, arg10: number, ): void` | Draws a arrow associated with a specific yaw. Specify endpoints in world space.<br><br>**Availability:** `both` |

### CDOTA_Ability_Aghanim_Spear

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `LaunchSpear(target: Vector, start: Vector): void` | Launch Spear to a target position from a source position. |

### CDOTA_Ability_Animation_Attack

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `SetPlaybackRate(rate: number): void` | Override playbackrate. |

### CDOTA_Ability_Animation_TailSpin

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `SetPlaybackRate(rate: number): void` | Override playbackrate. |

### CDOTA_Ability_DataDriven

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `ApplyDataDrivenModifier( caster: CDOTA_BaseNPC, target: CDOTA_BaseNPC, modifierName: string, modifierTable: object \| undefined, ): CDOTA_Buff` | Applies a data driven modifier to the target. |
| `ApplyDataDrivenThinker( caster: CDOTA_BaseNPC, location: Vector, modifierName: string, modifierTable: object \| undefined, ): CDOTA_Buff` | Applies a data driven thinker at the location. |

### CDOTA_Ability_Lua

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `CastFilterResult(): UnitFilterResult` | Determine whether an issued command with no target is valid.<br><br>**Availability:** `both` |
| `CastFilterResultLocation(location: Vector): UnitFilterResult` | Determine whether an issued command on a location is valid.<br><br>**Availability:** `both` |
| `CastFilterResultTarget(target: CDOTA_BaseNPC): UnitFilterResult` | Determine whether an issued command on a target is valid.<br><br>**Availability:** `both` |
| `GetAbilityChargeRestoreTime(level: number): number` | **Availability:** `both` |
| `GetAbilityTextureName(): string` | Allows code overriding of the ability texture shown in the HUD.<br><br>**Availability:** `client` |
| `GetAOERadius(): number` | Controls the size of the AOE casting cursor.<br><br>**Availability:** `both` |
| `GetAssociatedPrimaryAbilities(): string` | Returns abilities that are stolen simultaneously, or otherwise related in<br>functionality. |
| `GetAssociatedSecondaryAbilities(): string` | Returns other abilities that are stolen simultaneously, or otherwise related in<br>functionality.  Generally hidden abilities. |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR \| Uint64` | Return cast behavior type of this ability.<br><br>**Availability:** `both` |
| `GetCastAnimation(): GameActivity_t` | Return casting animation of this ability. |
| `GetCastPoint(): number` | Return cast point of this ability.<br><br>**Availability:** `both` |
| `GetCastRange(location: Vector, target: CDOTA_BaseNPC \| undefined): number` | Return cast range of this ability.<br><br>**Availability:** `both` |
| `GetCastRangeBonus(target: object, pseudoCastRange: number): number` | **Availability:** `both` |
| `GetChannelAnimation(): GameActivity_t` | Return channel animation of this ability. |
| `GetChannelledHealthCostPerSecond(level: number): number` | Return health cost per second of channeling at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetChannelledManaCostPerSecond(level: number): number` | Return mana cost at the given level per second while channeling (-1 is current).<br><br>**Availability:** `both` |
| `GetChannelStartTime(): number` | Return the channel start time of this ability.<br><br>**Availability:** `both` |
| `GetChannelTime(): number` | Return the channel time of this ability.<br><br>**Availability:** `both` |
| `GetConceptRecipientType(): number` | Return who hears speech when this spell is cast. |
| `GetCooldown(level: number): number` | Return cooldown of this ability.<br><br>**Availability:** `both` |
| `GetCustomCastError(): string` | Return the error string of a failed command with no target.<br><br>**Availability:** `both` |
| `GetCustomCastErrorLocation(location: Vector): string` | Return the error string of a failed command on a location.<br><br>**Availability:** `both` |
| `GetCustomCastErrorTarget(target: CDOTA_BaseNPC): string` | Return the error string of a failed command on a target.<br><br>**Availability:** `both` |
| `GetCustomHudErrorMessage(reason: number): string` | (DOTA_INVALID_ORDERS nReason) Return the error string of a failed order.<br><br>**Availability:** `both` |
| `GetEffectiveCastRange(location: Vector, target: object): number` | Return cast range of this ability, accounting for modifiers.<br><br>**Availability:** `both` |
| `GetGoldCost(level: number): number` | Return gold cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetHealthCost(level: number): number` | Return health cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetIntrinsicModifierName(): string` | Returns the name of the modifier applied passively by this ability. |
| `GetManaCost(level: number): number` | Return mana cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetPlaybackRateOverride(): number` | Return the animation rate of the cast animation. |
| `IsAttributeBonus(): boolean` | Is this ability an Attribute Bonus.<br><br>**Availability:** `both` |
| `IsCosmetic(entity: object): boolean` | Is this a cosmetic only ability? |
| `IsHiddenAbilityCastable(): boolean` | Returns true if this ability can be used when not on the action panel.<br><br>**Availability:** `both` |
| `IsHiddenWhenStolen(): boolean` | Returns true if this ability is hidden when stolen by Spell Steal. |
| `IsRefreshable(): boolean` | Returns true if this ability is refreshed by Refresher Orb. |
| `IsStealable(): boolean` | Returns true if this ability can be stolen by Spell Steal. |
| `OnAbilityPhaseInterrupted(): void` | Cast time did not complete successfully. |
| `OnAbilityPhaseStart(): boolean` | Cast time begins (return true for successful cast). |
| `OnAbilityPinged(playerId: PlayerID, ctrlHeld: boolean): void` | The ability was pinged. |
| `OnAbilityUpgrade(upgradeAbility: object): void` |  |
| `OnChannelFinish(interrupted: boolean): void` | Channel finished. |
| `OnChannelThink(interval: number): void` | Channeling is taking place. |
| `OnHeroCalculateStatBonus(): void` | Caster (hero only) gained a level, skilled an ability, or received a new stat<br>bonus. |
| `OnHeroDiedNearby(unit: CDOTA_BaseNPC, attacker: CDOTA_BaseNPC, event: object): void` | A hero has died in the vicinity (ie Urn), takes table of params. |
| `OnHeroLevelUp(): void` | Caster gained a level. |
| `OnInventoryContentsChanged(): void` | Caster inventory changed. |
| `OnItemEquipped(item: CDOTA_Item): void` | Caster equipped item. |
| `OnOwnerDied(): void` | Caster died. |
| `OnOwnerSpawned(): void` | Caster respawned or spawned for the first time. |
| `OnProjectileHit(target: CDOTA_BaseNPC \| undefined, location: Vector): boolean \| void` | Projectile has collided with a given target or reached its destination. If<br>'true` is returned, projectile would be destroyed. |
| `OnProjectileHit_ExtraData(target: CDOTA_BaseNPC \| undefined, location: Vector, extraData: object): boolean \| void` | Projectile has collided with a given target or reached its destination. If<br>'true` is returned, projectile would be destroyed. |
| `OnProjectileHitHandle( target: CDOTA_BaseNPC \| undefined, location: Vector, projectileHandle: ProjectileID, ): boolean \| void` | Projectile has collided with a given target or reached its destination. If<br>'true` is returned, projectile would be destroyed. |
| `OnProjectileThink(location: Vector): void` | Projectile is actively moving. |
| `OnProjectileThink_ExtraData(location: Vector, extraData: object): void` | Projectile is actively moving. |
| `OnProjectileThinkHandle(projectileHandle: ProjectileID): void` | Projectile is actively moving. |
| `OnSpellStart(): void` | Cast time finished, spell effects begin. |
| `OnStolen(sourceAbility: CDOTABaseAbility): void` | Special behavior when stolen by Spell Steal. |
| `OnToggle(): void` | Ability is toggled on/off. |
| `OnUnStolen(): void` | Special behavior when lost by Spell Steal. |
| `OnUpgrade(): void` | Ability gained a level. |
| `OtherAbilitiesAlwaysInterruptChanneling(): boolean` |  |
| `PiercesDebuffImmunity(): boolean` | Return if an ability and its modifiers should pierce debuff immunity.<br><br>**Availability:** `both` |
| `ProcsMagicStick(): boolean` | Returns true if this ability will generate magic stick charges for nearby<br>enemies. |
| `RequiresFacing(): boolean` | Does this ability need the caster to face the target before executing? |
| `ResetToggleOnRespawn(): boolean` | Returns true if this ability should return to the default toggle state when its<br>parent respawns. |
| `SpeakTrigger(): number` | Return the type of speech used. |

**Other members**

| Member | Description |
| --- | --- |
| `Init?(): void` | Called first when ability entity is created.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `Precache?(context: CScriptPrecacheContext): void` | **Abstract** |
| `Spawn?(): void` | Called when ability entity is created, after Init.<br><br>**Availability:** `both`<br><br>**Abstract** |

### CDOTA_Ability_Nian_Dive

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `SetPlaybackRate(rate: number): void` | Override playbackrate. |

### CDOTA_Ability_Nian_Leap

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `SetPlaybackRate(rate: number): void` | Override playbackrate. |

### CDOTA_Ability_Nian_Roar

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `GetCastCount(): number` | Number of times Nian has used the roar. |

### CDOTA_BaseNPC

Extends `CBaseAnimatingOverlay`

**Methods**

| Method | Description |
| --- | --- |
| `AddAbility(abilityName: string): CDOTABaseAbility` | Add an ability to this unit by name. |
| `AddActivityModifier(name: string): void` | Add an activity modifier that affects future StartGesture calls.<br><br>**Parameters:**<br><br>- name The name of the activity modifier to add, e.g. 'haste'.<br> |
| `AddItem(item: CDOTA_Item): CDOTA_Item` | Add an item to this unit's inventory. |
| `AddItemByName(itemName: string): CDOTA_Item` | Add an item to this unit's inventory. |
| `AddNewModifier( caster: CDOTA_BaseNPC \| undefined, ability: CDOTABaseAbility \| undefined, modifierName: string, modifierTable: object \| undefined, ): CDOTA_Buff` | Add a modifier to this unit. |
| `AddNoDraw(): void` | Adds the no draw flag. |
| `AddSpeechBubble(bubble: number, speech: string, duration: number, unOffsetX: number, unOffsetY: number): void` | Add a speech bubble(1-4 live at a time) to this NPC. |
| `AlertNearbyUnits(attacker: CDOTA_BaseNPC, ability: CDOTABaseAbility): void` |  |
| `AngerNearbyUnits(): void` |  |
| `AttackNoEarlierThan(time: number, timeDisparityTolerance: number): void` |  |
| `AttackReady(): boolean` |  |
| `BoundingRadius2D(): number` |  |
| `CalculateGenericBonuses(): void` |  |
| `CanBeSeenByAnyOpposingTeam(): boolean` |  |
| `CanEntityBeSeenByMyTeam(entity: CDOTA_BaseNPC): boolean` | Check FoW to see if an entity is visible. |
| `CanSellItems(): boolean` | Query if this unit can sell items. |
| `CastAbilityImmediately(ability: CDOTABaseAbility, playerIndex: number): void` | Cast an ability immediately. |
| `CastAbilityNoTarget(ability: CDOTABaseAbility, playerIndex: number): void` | Cast an ability with no target. |
| `CastAbilityOnPosition(position: Vector, ability: CDOTABaseAbility, playerIndex: number): void` | Cast an ability on a position. |
| `CastAbilityOnTarget(target: CDOTA_BaseNPC, ability: CDOTABaseAbility, playerIndex: number): void` | Cast an ability on a target entity. |
| `CastAbilityToggle(ability: CDOTABaseAbility, playerIndex: number): void` | Toggle an ability. |
| `ChangeTeam(teamNum: number): void` |  |
| `ClearActivityModifiers(): void` | Clear Activity modifiers. |
| `ConsumeItem(item: object): void` | Consume the item, deleting it from the inventory and granting the hero the<br>specified bonuses. |
| `DestroyAllSpeechBubbles(): void` |  |
| `DisassembleItem(item: CDOTA_Item): void` | Disassemble the passed item in this unit's inventory. |
| `DropItemAtPosition(dest: Vector, item: CDOTA_Item): void` | Drop an item at a given point. |
| `DropItemAtPositionImmediate(item: CDOTA_Item, position: Vector): void` | Immediately drop a carried item at a given position. |
| `EjectItemFromStash(item: CDOTA_Item): void` | Drops the selected item out of this unit's stash. |
| `FaceTowards(target: Vector): void` | This unit will be set to face the target point. |
| `FadeGesture(activity: GameActivity_t): void` | Fade and remove the given gesture activity. |
| `FindAbilityByName(abilityName: string): CDOTABaseAbility \| undefined` | Retrieve an ability by name from the unit.<br><br>**Availability:** `both` |
| `FindAllModifiers(): CDOTA_Buff[]` | Returns a table of all of the modifiers on the NPC. |
| `FindAllModifiersByName(modifierName: string): CDOTA_Buff[]` | Returns a table of all of the modifiers on the NPC with the passed name<br>(modifierName). |
| `FindItemInInventory(itemName: string): CDOTA_Item \| undefined` | Get handle to first item in inventory, else nil. |
| `FindModifierByName(modifierName: string): CDOTA_Buff \| undefined` | Return a handle to the modifier of the given name if found, else nil (string<br>Name ). |
| `FindModifierByNameAndCaster(modifierName: string, caster: CDOTA_BaseNPC): CDOTA_Buff \| undefined` | Return a handle to the modifier of the given name from the passed caster if<br>found, else nil. |
| `ForceKill(reincarnate: boolean): void` | Kill this unit immediately. |
| `ForcePlayActivityOnce(activity: GameActivity_t): void` | Play an activity once, and then go back to idle. |
| `GetAbilityByIndex(index: number): CDOTABaseAbility \| undefined` | Retrieve an ability by index from the unit. |
| `GetAbilityCount(): number` | **Availability:** `both` |
| `GetAcquisitionRange(): number` | Gets the range at which this unit will auto-acquire. |
| `GetAdditionalBattleMusicWeight(): number` | Combat involving this creature will have this weight added to the music<br>calcuations. |
| `GetAggroTarget(): CDOTA_BaseNPC \| undefined` | Returns this unit's aggro target. |
| `GetAttackAnimationPoint(): number` |  |
| `GetAttackCapability(): DOTAUnitAttackCapability_t` |  |
| `GetAttackDamage(): number` | Returns a random integer between the minimum and maximum base damage of the<br>unit. |
| `GetAttackRangeBuffer(): number` | Gets the attack range buffer. |
| `GetAttackSpeed(ignoreTempAttackSpeed: boolean): number` | **Availability:** `both` |
| `GetAttacksPerSecond(ignoreTempAttackSpeed: boolean): number` | **Availability:** `both` |
| `GetAttackTarget(): CDOTA_BaseNPC \| undefined` |  |
| `GetAverageTrueAttackDamage(target: CDOTA_BaseNPC \| undefined): number` | Returns the average value of the minimum and maximum damage values. |
| `GetBaseAttackRange(): number` |  |
| `GetBaseAttackTime(): number` | **Availability:** `both` |
| `GetBaseDamageMax(): number` | Get the maximum attack damage of this unit. |
| `GetBaseDamageMin(): number` | Get the minimum attack damage of this unit. |
| `GetBaseDayTimeVisionRange(): number` | Returns the vision range before modifiers. |
| `GetBaseHealthBarOffset(): number` |  |
| `GetBaseHealthRegen(): number` |  |
| `GetBaseMagicalResistanceValue(): number` | Returns base magical armor value.<br><br>**Availability:** `both` |
| `GetBaseMaxHealth(): number` | Gets the base max health value. |
| `GetBaseMoveSpeed(): number` | **Availability:** `both` |
| `GetBaseNightTimeVisionRange(): number` | Returns the vision range after modifiers. |
| `GetBonusManaRegen(): number` | This Mana regen is derived from constant bonuses like Basilius. |
| `GetCastPoint(attack: boolean): number` |  |
| `GetCastRangeBonus(): number` | **Availability:** `both` |
| `GetCloneSource(): CDOTA_BaseNPC \| undefined` | Get clone source (Meepo Prime, if this is a Meepo). |
| `GetCollisionPadding(): number` | Returns the size of the collision padding around the hull.<br><br>**Availability:** `both` |
| `GetCooldownReduction(): number` | **Availability:** `both` |
| `GetCreationTime(): number` |  |
| `GetCurrentActiveAbility(): CDOTABaseAbility \| undefined` | Get the ability this unit is currently casting. |
| `GetCurrentVisionRange(): number` | Gets the current vision range.<br><br>**Availability:** `both` |
| `GetCursorCastTarget(): CDOTA_BaseNPC \| undefined` |  |
| `GetCursorPosition(): Vector` |  |
| `GetCursorTargetingNothing(): boolean` |  |
| `GetDamageMax(): number` | Get the maximum attack damage of this unit.<br><br>**Availability:** `both` |
| `GetDamageMin(): number` | Get the minimum attack damage of this unit.<br><br>**Availability:** `both` |
| `GetDayTimeVisionRange(): number` | Returns the vision range after modifiers.<br><br>**Availability:** `both` |
| `GetDeathXP(): number` | Get the XP bounty on this unit. |
| `GetDisplayAttackSpeed(): number` | Attack speed expressed as constant value. |
| `GetEvasion(): number` |  |
| `GetForceAttackTarget(): CDOTA_BaseNPC \| undefined` |  |
| `GetGoldBounty(): number` | Get the gold bounty on this unit. |
| `GetHasteFactor(): number` | **Availability:** `both` |
| `GetHealthDeficit(): number` | Returns integer amount of health missing from max. |
| `GetHealthPercent(): number` | Get the current health percent of the unit.<br><br>**Availability:** `both` |
| `GetHealthRegen(): number` |  |
| `GetHullRadius(): number` | Get the collision hull radius of this NPC.<br><br>**Availability:** `both` |
| `GetIdealSpeed(): number` | Returns speed after all modifiers.<br><br>**Availability:** `both` |
| `GetIdealSpeedNoSlows(): number` | Returns speed after all modifiers, but excluding those that reduce speed.<br><br>**Availability:** `both` |
| `GetIncreasedAttackSpeed(ignoreTempAttackSpeed: boolean): number` | **Availability:** `both` |
| `GetInitialGoalEntity(): CBaseEntity \| undefined` | Returns the initial waypoint goal for this NPC. |
| `GetInitialGoalPosition(): Vector` | Get waypoint position for this NPC. |
| `GetItemInSlot(slot: number): CDOTA_Item \| undefined` | Returns nth item in inventory slot (index is zero based). |
| `GetLastAttackTime(): number` |  |
| `GetLastDamageTime(): number` | Get the last time this NPC took damage. |
| `GetLastIdleChangeTime(): number` | Get the last game time that this unit switched to/from idle state. |
| `GetLevel(): number` | Returns the level of this unit.<br><br>**Availability:** `both` |
| `GetMainControllingPlayer(): number` | Returns the player ID of the controlling player. |
| `GetMana(): number` | Get the mana on this unit.<br><br>**Availability:** `both` |
| `GetManaPercent(): number` | Get the percent of mana remaining. |
| `GetManaRegen(): number` | **Availability:** `both` |
| `GetMaximumGoldBounty(): number` | Get the maximum gold bounty for this unit. |
| `GetMaxMana(): number` | Get the maximum mana of this unit.<br><br>**Availability:** `both` |
| `GetMinimumGoldBounty(): number` | Get the minimum gold bounty for this unit. |
| `GetModelRadius(): number` | **Availability:** `both` |
| `GetModifierCount(): number` | How many modifiers does this unit have? |
| `GetModifierNameByIndex(index: number): string` | Get a modifier name by index. |
| `GetModifierStackCount(modifierName: string, caster: CDOTA_BaseNPC): number` | Gets the stack count of a given modifier.<br><br>**Availability:** `both` |
| `GetMoveSpeedModifier(baseSpeed: number, returnUnslowed: boolean): number` | **Availability:** `both` |
| `GetMustReachEachGoalEntity(): boolean` | Set whether this NPC is required to reach each goal entity, rather than being<br>allowed to unkink their path. |
| `GetNeutralSpawnerName(): string` | Get the name of this camp's neutral spawner. |
| `GetNeverMoveToClearSpace(): boolean` | If set to true, we will never attempt to move this unit to clear space, even<br>when it unphases. |
| `GetNightTimeVisionRange(): number` | Returns the vision range after modifiers.<br><br>**Availability:** `both` |
| `GetOpposingTeamNumber(): DOTATeam_t` | **Availability:** `both` |
| `GetPaddedCollisionRadius(): number` | Get the collision hull radius (including padding) of this NPC.<br><br>**Availability:** `both` |
| `GetPhysicalArmorBaseValue(): number` | Returns base physical armor value.<br><br>**Availability:** `both` |
| `GetPhysicalArmorValue(ignoreBase: boolean): number` | Returns current physical armor value.<br><br>**Availability:** `both` |
| `GetPlayerOwner(): CDOTAPlayerController` | Returns the player that owns this unit. |
| `GetPlayerOwnerID(): PlayerID` | Get the owner player ID for this unit.<br><br>**Availability:** `both` |
| `GetProjectileSpeed(): number` |  |
| `GetRangedProjectileName(): string` |  |
| `GetRangeToUnit(npc: CDOTA_BaseNPC): number` |  |
| `GetRemainingPathLength(): number` |  |
| `GetSecondsPerAttack(ignoreTempAttackSpeed: boolean): number` | **Availability:** `both` |
| `GetSpellAmplification(baseOnly: boolean): number` |  |
| `GetStatusResistance(): number` |  |
| `GetTotalPurchasedUpgradeGoldCost(): number` | Get how much gold has been spent on ability upgrades.<br><br>**Availability:** `both` |
| `GetUnitLabel(): string` | **Availability:** `both` |
| `GetUnitLocToken(): string` | Get the localization token for this unit's name.<br><br>**Availability:** `client` |
| `GetUnitName(): string` | Get the name of this unit.<br><br>**Availability:** `both` |
| `GiveMana(mana: number): void` | Give mana to this unit, this can be used for mana gained by abilities or item<br>usage. |
| `HasAbility(abilityName: string): boolean` | See whether this unit has an ability by name. |
| `HasAnyActiveAbilities(): boolean` |  |
| `HasAttackCapability(): boolean` | **Availability:** `both` |
| `HasFlyingVision(): boolean` | **Availability:** `both` |
| `HasFlyMovementCapability(): boolean` | **Availability:** `both` |
| `HasGroundMovementCapability(): boolean` | **Availability:** `both` |
| `HasInventory(): boolean` | Does this unit have an inventory. |
| `HasItemInInventory(itemName: string): boolean` | See whether this unit has an item by name.<br><br>**Availability:** `both` |
| `HasModifier(scriptName: string): boolean` | Sees if this unit has a given modifier.<br><br>**Availability:** `both` |
| `HasMovementCapability(): boolean` | **Availability:** `both` |
| `HasScepter(): boolean` | **Availability:** `both` |
| `Heal(amount: number, inflictor: CDOTABaseAbility \| undefined): void` | Heal this unit. |
| `HealWithParams( amount: number, inflictor: object, lifesteal: boolean, amplify: boolean, source: object, spellLifesteal: boolean, ): void` | Heal this unit (with more parameters). |
| `Hold(): void` | Hold position. |
| `Interrupt(): void` |  |
| `InterruptChannel(): void` |  |
| `InterruptMotionControllers(findClearSpace: boolean): void` |  |
| `IsAlive(): boolean` | Is this unit alive? |
| `IsAncient(): boolean` | Is this unit an Ancient?<br><br>**Availability:** `both` |
| `IsAttackImmune(): boolean` | **Availability:** `both` |
| `IsAttacking(): boolean` |  |
| `IsAttackingEntity(entity: CDOTA_BaseNPC): boolean` |  |
| `IsBarracks(): this is CDOTA_BaseNPC_Building` | Is this unit a Barracks?<br><br>**Availability:** `both` |
| `IsBlind(): boolean` | **Availability:** `both` |
| `IsBlockDisabled(): boolean` |  |
| `IsBoss(): boolean` | Is this unit a boss?<br><br>**Availability:** `both` |
| `IsBossCreature(): boolean` | Is this unit a Boss Creature? (used by custom games). |
| `IsBuilding(): this is CDOTA_BaseNPC_Building` | Is this unit a building?<br><br>**Availability:** `both` |
| `IsChanneling(): boolean` | Is this unit currently channeling a spell? |
| `IsClone(): this is CDOTA_BaseNPC_Hero` | Is this unit a clone? (Meepo). |
| `IsCommandRestricted(): boolean` | **Availability:** `both` |
| `IsConsideredHero(): boolean` | Is this unit a considered a hero for targeting purposes?<br><br>**Availability:** `both` |
| `IsControllableByAnyPlayer(): boolean` | Is this unit controlled by any non-bot player?<br><br>**Availability:** `both` |
| `IsCourier(): this is CDOTA_Unit_Courier` | Is this unit a courier?<br><br>**Availability:** `both` |
| `IsCreature(): this is CDOTA_BaseNPC_Creature` | Is this a Creature type NPC?<br><br>**Availability:** `both` |
| `IsCreep(): boolean` | Is this unit a creep?<br><br>**Availability:** `both` |
| `IsCreepHero(): boolean` | Is this unit a creep hero?<br><br>**Availability:** `both` |
| `IsCurrentlyHorizontalMotionControlled(): boolean` |  |
| `IsCurrentlyVerticalMotionControlled(): boolean` |  |
| `IsDebuffImmune(): boolean` | **Availability:** `both` |
| `IsDisarmed(): boolean` | **Availability:** `both` |
| `IsDominated(): boolean` | **Availability:** `both` |
| `IsEvadeDisabled(): boolean` | **Availability:** `both` |
| `IsFeared(): boolean` | **Availability:** `both` |
| `IsFort(): this is CDOTA_BaseNPC_Building` | Is this unit an Ancient?<br><br>**Availability:** `both` |
| `IsFrozen(): boolean` | **Availability:** `both` |
| `IsHero(): this is CDOTA_BaseNPC_Hero` | Is this a hero or hero illusion?<br><br>**Availability:** `both` |
| `IsHeroWard(): boolean` | Is this a Hero Ward? |
| `IsHexed(): boolean` | **Availability:** `both` |
| `IsIdle(): boolean` | Is this creature currently idle? |
| `IsIllusion(): boolean` | **Availability:** `both` |
| `IsInRangeOfShop(shopType: DOTA_SHOP_TYPE, physical: boolean): boolean` | Ask whether this unit is in range of the specified shop. |
| `IsInventoryEnabled(): boolean` | Does this unit have an inventory.<br><br>**Availability:** `client` |
| `IsInvisible(): boolean` | **Availability:** `both` |
| `IsInvulnerable(): boolean` | **Availability:** `both` |
| `IsLowAttackPriority(): boolean` | **Availability:** `both` |
| `IsMagicImmune(): boolean` | **Availability:** `both` |
| `IsMovementImpaired(): boolean` |  |
| `IsMoving(): boolean` | Is this unit moving?<br><br>**Availability:** `both` |
| `IsMuted(): boolean` | **Availability:** `both` |
| `IsNeutralUnitType(): boolean` | Is this a neutral?<br><br>**Availability:** `both` |
| `IsNightmared(): boolean` | **Availability:** `both` |
| `IsOpposingTeam(team: DOTATeam_t): boolean` |  |
| `IsOther(): boolean` | Is this unit a ward-type unit?<br><br>**Availability:** `both` |
| `IsOutOfGame(): boolean` | **Availability:** `both` |
| `IsOwnedByAnyPlayer(): boolean` | Is this unit owned by any non-bot player?<br><br>**Availability:** `both` |
| `IsPhantom(): boolean` | Is this a phantom unit?<br><br>**Availability:** `both` |
| `IsPhantomBlocker(): boolean` |  |
| `IsPhased(): boolean` |  |
| `IsPositionInRange(position: Vector, range: number): boolean` |  |
| `IsRangedAttacker(): boolean` | Is this unit a ranged attacker?<br><br>**Availability:** `both` |
| `IsRealHero(): this is CDOTA_BaseNPC_Hero` | Is this a real hero?<br><br>**Availability:** `both` |
| `IsReincarnating(): boolean` |  |
| `IsRooted(): boolean` | **Availability:** `both` |
| `IsShrine(): this is CDOTA_BaseNPC_Building` | Is this a shrine? |
| `IsSilenced(): boolean` | **Availability:** `both` |
| `IsSpeciallyDeniable(): boolean` | **Availability:** `both` |
| `IsSpeciallyUndeniable(): boolean` | **Availability:** `both` |
| `IsStrongIllusion(): boolean` | **Availability:** `both` |
| `IsStunned(): boolean` | **Availability:** `both` |
| `IsSummoned(): boolean` | Is this unit summoned?<br><br>**Availability:** `both` |
| `IsTaunted(): boolean` | **Availability:** `both` |
| `IsTempestDouble(): this is CDOTA_BaseNPC_Hero` |  |
| `IsTower(): this is CDOTA_BaseNPC_Building` | Is this a tower?<br><br>**Availability:** `both` |
| `IsUnableToMiss(): boolean` |  |
| `IsUnselectable(): boolean` | **Availability:** `both` |
| `IsUntargetable(): boolean` | **Availability:** `client` |
| `IsUntargetableFrom(targettingSource: object): boolean` | **Availability:** `both` |
| `IsWard(): boolean` | Is this a Ward? |
| `IsZombie(): boolean` | Is this entity an Undying Zombie? |
| `Kill(ability: CDOTABaseAbility \| undefined, attacker: CDOTA_BaseNPC \| undefined): void` | Kills this NPC, with the params Ability and Attacker. |
| `Kill(): never` | **Deprecated:** Added for compatibility with CBaseEntity. Invalid at the runtime.<br> |
| `MakeIllusion(): void` |  |
| `MakePhantomBlocker(): void` |  |
| `MakeVisibleDueToAttack(team: DOTATeam_t, radius: number): void` |  |
| `MakeVisibleToTeam(team: DOTATeam_t, duration: number): void` |  |
| `ManageModelChanges(): void` |  |
| `ModifyHealth( desiredHealthValue: number, ability: CDOTABaseAbility \| undefined, lethal: boolean, additionalFlags: number, ): void` | Sets the health to a specific value, with optional flags or inflictors. |
| `MoveToNPC(npc: CDOTA_BaseNPC): void` | Move to follow a unit. |
| `MoveToNPCToGiveItem(npc: CDOTA_BaseNPC, item: CDOTA_Item): void` | Give an item to another unit. |
| `MoveToPosition(dest: Vector): void` | Issue a Move-To command. |
| `MoveToPositionAggressive(dest: Vector): void` | Issue an Attack-Move-To command. |
| `MoveToTargetToAttack(target: CDOTA_BaseNPC): void` | Move to a target to attack. |
| `NoHealthBar(): boolean` | **Availability:** `both` |
| `NoTeamMoveTo(): boolean` | **Availability:** `both` |
| `NoTeamSelect(): boolean` | **Availability:** `both` |
| `NotifyWearablesOfModelChange(originalModel: boolean): void` |  |
| `NotOnMinimap(): boolean` | **Availability:** `both` |
| `NotOnMinimapForEnemies(): boolean` | **Availability:** `both` |
| `NoUnitCollision(): boolean` | **Availability:** `both` |
| `OnCommandMoveToDirection(pos: Vector): void` | Tells the underlying AI to move in the given direction, skipping Dota orders. |
| `PassivesDisabled(): boolean` | **Availability:** `both` |
| `PatrolToPosition(dest: Vector): void` | Issue a Patrol-To command. |
| `PerformAttack( target: CDOTA_BaseNPC, useCastAttackOrb: boolean, processProcs: boolean, skipCooldown: boolean, ignoreInvis: boolean, useProjectile: boolean, fakeAttack: boolean, neverMiss: boolean, ): void` | Performs an attack on a target. |
| `PickupDroppedItem(item: CDOTA_Item): void` | Pick up a dropped item. |
| `PickupRune(item: CDOTA_Item): void` | Pick up a rune. |
| `PlayVCD(vcd: string): void` | Play a VCD on the NPC. |
| `ProvidesVision(): boolean` | **Availability:** `both` |
| `Purge( removePositiveBuffs: boolean, removeDebuffs: boolean, frameOnly: boolean, removeStuns: boolean, removeExceptions: boolean, ): void` |  |
| `QueueConcept<TCallbackInfo>( delay: number, criteriaTable: object, completionCallbackFn: (didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: undefined, callbackInfo: TCallbackInfo, ): void` | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a delay. |
| `QueueConcept<TCallbackInfo, TContext extends {}>( delay: number, criteriaTable: object, completionCallbackFn: (this: TContext, didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: TContext, callbackInfo: TCallbackInfo, ): void` |  |
| `QueueTeamConcept<TCallbackInfo>( delay: number, criteriaTable: object, completionCallbackFn: (didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: undefined, callbackInfo: TCallbackInfo, ): void` | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a<br>delay, for the same team this speaker is on. |
| `QueueTeamConcept<TCallbackInfo, TContext extends {}>( delay: number, criteriaTable: object, completionCallbackFn: (this: TContext, didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: TContext, callbackInfo: TCallbackInfo, ): void` |  |
| `QueueTeamConceptNoSpectators<TCallbackInfo>( delay: number, criteriaTable: object, completionCallbackFn: (didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: undefined, callbackInfo: TCallbackInfo, ): void` | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a<br>delay, for the same team this speaker is on. Is not played for spectators. |
| `QueueTeamConceptNoSpectators<TCallbackInfo, TContext extends {}>( delay: number, criteriaTable: object, completionCallbackFn: (this: TContext, didActuallySpeak: boolean, callbackInfo: TCallbackInfo) => void, context: TContext, callbackInfo: TCallbackInfo, ): void` |  |
| `RemoveAbility(abilityName: string): void` | Remove an ability from this unit by name. |
| `RemoveAbilityByHandle(ability: CDOTABaseAbility): void` | Remove the passed ability from this unit. |
| `RemoveAbilityFromIndexByName(abilityName: string): void` |  |
| `RemoveAllModifiers(targets: 0 \| 1 \| 2, now: boolean, permanent: boolean, death: boolean): void` | **Parameters:**<br><br>- targets 0=all, 1=enemy, 2=ally<br> |
| `RemoveAllModifiersOfName(scriptName: string): void` | Removes all copies of a modifier. |
| `RemoveGesture(activity: GameActivity_t): void` | Remove the given gesture activity. |
| `RemoveHorizontalMotionController(buff: CDOTA_Buff): void` |  |
| `RemoveItem(item: CDOTA_Item): void` | Removes the passed item from this unit's inventory and deletes it. |
| `RemoveModifierByName(scriptName: string): void` | Removes a modifier. |
| `RemoveModifierByNameAndCaster(scriptName: string, caster: CDOTA_BaseNPC): void` | Removes a modifier that was cast by the given caster. |
| `RemoveNoDraw(): void` | Remove the no draw flag. |
| `RemoveVerticalMotionController(buff: CDOTA_Buff): void` |  |
| `RespawnUnit(): void` | Respawns the target unit if it can be respawned. |
| `Script_GetAttackRange(): number` | Gets this unit's attack range after all modifiers.<br><br>**Availability:** `both` |
| `Script_GetMagicalArmorValue(inflictor: object): number` | Returns current magical armor value.<br><br>**Availability:** `both` |
| `Script_IsDeniable(): boolean` | **Availability:** `both` |
| `Script_ReduceMana(mana: number, ability: object): number` | Remove mana from this unit, this can be used for involuntary mana loss, not for<br>mana that is spent. |
| `SellItem(item: CDOTA_Item): void` | Sells the passed item in this unit's inventory. |
| `SetAbilityByIndex(ability: CDOTABaseAbility, index: number): void` | Set the ability by index. |
| `SetAcquisitionRange(range: number): void` |  |
| `SetAdditionalBattleMusicWeight(weight: number): void` | Combat involving this creature will have this weight added to the music<br>calcuations. |
| `SetAggroTarget(aggroTarget: CDOTA_BaseNPC): void` | Set this unit's aggro target to a specified unit. |
| `SetAttackCapability(attackCapabilities: DOTAUnitAttackCapability_t): void` |  |
| `SetAttacking(attackTarget: CDOTA_BaseNPC \| undefined): void` |  |
| `SetBaseAttackTime(baseAttackTime: number): void` |  |
| `SetBaseDamageMax(max: number): void` | Sets the maximum base damage. |
| `SetBaseDamageMin(min: number): void` | Sets the minimum base damage. |
| `SetBaseHealthRegen(healthRegen: number): void` |  |
| `SetBaseMagicalResistanceValue(magicalResistanceValue: number): void` | Sets base magical armor value. |
| `SetBaseManaRegen(manaRegen: number): void` |  |
| `SetBaseMaxHealth(baseMaxHealth: number): void` | Set a new base max health value. |
| `SetBaseMoveSpeed(moveSpeed: number): void` |  |
| `SetCanSellItems(canSell: boolean): void` | Set whether or not this unit is allowed to sell items (bCanSellItems). |
| `SetControllableByAllPlayers(controllableByAllPlayers: boolean): void` | Set this unit controllable by all players. |
| `SetControllableByPlayer(playerId: PlayerID, skipAdjustingPosition: boolean): void` | Set this unit controllable by the player with the passed ID. |
| `SetCursorCastTarget(entity: CDOTA_BaseNPC \| undefined): void` |  |
| `SetCursorPosition(location: Vector): void` |  |
| `SetCursorTargetingNothing(targetingNothing: boolean): void` |  |
| `SetCustomHealthLabel(label: string, r: number, g: number, b: number): void` |  |
| `SetDayTimeVisionRange(range: number): void` | Set the base vision range. |
| `SetDeathXP(xpBounty: number): void` | Set the XP bounty on this unit. |
| `SetFollowRange(followRange: number): void` |  |
| `SetForceAttackTarget(npc: CDOTA_BaseNPC \| undefined): void` |  |
| `SetForceAttackTargetAlly(npc: CDOTA_BaseNPC \| undefined): void` |  |
| `SetHasInventory(hasInventory: boolean): void` | Set if this unit has an inventory. |
| `SetHealthBarOffsetOverride(offset: number): void` |  |
| `SetHullRadius(hullRadius: number): void` | Set the collision hull radius of this NPC. |
| `SetIdleAcquire(idleAcquire: boolean): void` |  |
| `SetInitialGoalEntity(goal: CBaseEntity \| undefined): void` | Sets the initial waypoint goal for this NPC. |
| `SetInitialGoalPosition(position: Vector): void` | Set waypoint position for this NPC. |
| `SetMana(mana: number): void` | Set the mana on this unit. |
| `SetMaximumGoldBounty(goldBountyMax: number): void` | Set the maximum gold bounty for this unit. |
| `SetMaxMana(maxMana: number): void` | Set the maximum mana of this unit. |
| `SetMinimumGoldBounty(goldBountyMin: number): void` | Set the minimum gold bounty for this unit. |
| `SetModifierStackCount(scriptName: string, caster: CDOTA_BaseNPC, stackCount: number): void` | Sets the stack count of a given modifier. |
| `SetMoveCapability(moveCapabilities: DOTAUnitMoveCapability_t): void` |  |
| `SetMustReachEachGoalEntity(must: boolean): void` | Set whether this NPC is required to reach each goal entity, rather than being<br>allowed to unkink their path. |
| `SetNeverMoveToClearSpace(neverMoveToClearSpace: boolean): void` | If set to true, we will never attempt to move this unit to clear space, even<br>when it unphases. |
| `SetNightTimeVisionRange(range: number): void` | Returns the vision range after modifiers. |
| `SetOrigin(location: Vector): void` | Set the unit's origin. |
| `SetOriginalModel(modelName: string): void` | Sets the original model of this entity, which it will tend to fall back to<br>anytime its state changes. |
| `SetPhysicalArmorBaseValue(physicalArmorValue: number): void` | Sets base physical armor value. |
| `SetRangedProjectileName(projectileName: string): void` |  |
| `SetRevealRadius(revealRadius: number): void` | Sets the client side map reveal radius for this unit. |
| `SetShouldComputeRemainingPathLength(compute: boolean): void` |  |
| `SetShouldDoFlyHeightVisual(shouldVisuallyFly: boolean): void` |  |
| `SetStolenScepter(stolenScepter: boolean): void` |  |
| `SetUnitCanRespawn(canRespawn: boolean): void` |  |
| `SetUnitName(name: string): void` |  |
| `ShouldIdleAcquire(): boolean` |  |
| `SpeakConcept(criteriaTable: object): void` | Speak a response system concept with the TLK_DOTA_CUSTOM concept. |
| `SpendMana(manaSpent: number, ability: CDOTABaseAbility): void` | Spend mana from this unit, this can be used for spending mana from abilities or<br>item usage. |
| `StartGesture(activity: GameActivity_t): void` | Add the given gesture activity. |
| `StartGestureFadeWithSequenceSettings(activity: GameActivity_t): void` | Add the given gesture activity faded according to its sequence settings. |
| `StartGestureWithFade(activity: GameActivity_t, fadeIn: number, fadeOut: number): void` | Add the given gesture activity faded according to to the parameters. |
| `StartGestureWithFadeAndPlaybackRate(activity: number, fadeIn: number, fadeOut: number, rate: number): void` | Add the given gesture activity faded according to to the parameters and with a<br>playback rate override. |
| `StartGestureWithPlaybackRate(activity: GameActivity_t, rate: number): void` | Add the given gesture activity with a playback rate override. |
| `Stop(): void` | Stop the current order. |
| `StopFacing(): void` |  |
| `SwapAbilities(abilityName1: string, abilityName2: string, enable1: boolean, enable2: boolean): void` | Swaps the slots of the two passed abilities and sets them enabled/disabled. |
| `SwapItems(slot1: number, slot2: number): void` | Swap the contents of two item slots (slot1, slot2). |
| `TakeItem(item: CDOTA_Item): CDOTA_Item` | Removed the passed item from this unit's inventory. Returns the passed item. |
| `TimeUntilNextAttack(): number` |  |
| `TriggerModifierDodge(ability: object, buff: object): boolean` |  |
| `TriggerSpellAbsorb(ability: CDOTABaseAbility): boolean` |  |
| `TriggerSpellReflect(ability: CDOTABaseAbility): void` | Trigger the Lotus Orb-like effect.(hAbility). |
| `UnHideAbilityToSlot(abilityName: string, replacedAbilityName: string): void` | Makes the first ability unhidden, and puts it where second ability currently<br>is. Will do nothing if the first ability is already unhidden and in a valid<br>slot. |
| `UnitCanRespawn(): boolean` | Can the unit respawn?<br><br>**Availability:** `both` |
| `WasKilledPassively(): boolean` |  |

### CDOTA_BaseNPC_Building

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `GetInvulnCount(): number` | Get the invulnerability count for a building. |
| `SetInvulnCount(invulnCount: number): void` | Set the invulnerability counter of this building. |

### CDOTA_BaseNPC_Creature

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `AddItemDrop(dropData: object): void` | Add the specified item drop to this creature. |
| `CreatureLevelUp(levels: number): void` | Level the creature up by the specified number of levels. |
| `GetDisableResistance(): number` | Set creature's current disable resistance. |
| `GetUltimateDisableResistance(): number` | Set creature's current disable resistance from ultimates. |
| `IsChampion(): boolean` | Is this unit a champion? |
| `IsReincarnating(): boolean` | Is this creature respawning? |
| `RemoveAllItemDrops(): void` | Remove all item drops from this creature. |
| `SetAggroOnOwnerOnDamage(aggro: boolean): void` | Does this creature aggro on the owner of the attacking unit when taking damage? |
| `SetArmorGain(armorGain: number): void` | Set the armor gained per level on this creature. |
| `SetAttackTimeGain(attackTimeGain: number): void` | Set the attack time gained per level on this creature. |
| `SetBountyGain(bountyGain: number): void` | Set the bounty gold gained per level on this creature. |
| `SetChampion(isChampion: boolean): void` | Flag this unit as a champion creature. |
| `SetDamageGain(damageGain: number): void` | Set the damage gained per level on this creature. |
| `SetDisableResistance(disableResistance: number): void` | Set creature's current disable resistance. |
| `SetDisableResistanceGain(disableResistanceGain: number): void` | Set the disable resistance gained per level on this creature. |
| `SetEconItemGroup(group: number): void` | Switches visible econ item group. |
| `SetHPGain(hpGain: number): void` | Set the hit points gained per level on this creature. |
| `SetHPRegenGain(hpRegenGain: number): void` | Set the hit points regen gained per level on this creature. |
| `SetMagicResistanceGain(magicResistanceGain: number): void` | Set the magic resistance gained per level on this creature. |
| `SetManaGain(manaGain: number): void` | Set the mana points gained per level on this creature. |
| `SetManaRegenGain(manaRegenGain: number): void` | Set the mana points regen gained per level on this creature. |
| `SetMoveSpeedGain(moveSpeedGain: number): void` | Set the move speed gained per level on this creature. |
| `SetRequiresReachingEndPath(requiresReachingEndPath: boolean): void` | Set whether creatures require reaching their end path before becoming idle. |
| `SetUltimateDisableResistance(ultDisableResistance: number): void` | Set creature's current disable resistance from ultimates. |
| `SetXPGain(xpGain: number): void` | Set the XP gained per level on this creature. |

### CDOTA_BaseNPC_Hero

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `AddExperience( xp: number, reason: EDOTA_ModifyXP_Reason, applyBotDifficultyScaling: boolean, incrementTotal: boolean, cloneCount: number, ): boolean` |  |
| `Buyback(): void` | Spend the gold and buyback with this hero. |
| `CalculateStatBonus(force: boolean): void` | Recalculate all stats after the hero gains stats. |
| `CanEarnGold(): boolean` | Returns boolean value result of buyback gold limit time less than game time. |
| `ClearLastHitMultikill(): void` | Value is stored in PlayerResource. |
| `ClearLastHitStreak(): void` | Value is stored in PlayerResource. |
| `ClearStreak(): void` | Value is stored in PlayerResource. |
| `GetAbilityPoints(): number` | Gets the current unspent ability points. |
| `GetAdditionalOwnedUnits(): CDOTA_BaseNPC[]` |  |
| `GetAgility(): number` | **Availability:** `both` |
| `GetAgilityGain(): number` |  |
| `GetAssists(): number` | Value is stored in PlayerResource. |
| `GetAttacker(index: number): number` |  |
| `GetBaseAgility(): number` |  |
| `GetBaseDamageMax(): number` | Hero damage is also affected by attributes. |
| `GetBaseDamageMin(): number` | Hero damage is also affected by attributes. |
| `GetBaseIntellect(): number` |  |
| `GetBaseManaRegen(): number` | Returns the base mana regen. |
| `GetBaseStrength(): number` |  |
| `GetBonusDamageFromPrimaryStat(): number` |  |
| `GetBuybackCooldownTime(): number` | Return float value for the amount of time left on cooldown for this hero's<br>buyback. |
| `GetBuybackCost(): number` | Return integer value for the gold cost of a buyback. |
| `GetBuybackGoldLimitTime(): number` | Returns the amount of time gold gain is limited after buying back. |
| `GetCurrentXP(): number` | Returns the amount of XP. |
| `GetDeathGoldCost(): number` |  |
| `GetDeaths(): number` | Value is stored in PlayerResource. |
| `GetDenies(): number` | Value is stored in PlayerResource. |
| `GetGold(): number` | Returns gold amount for the player owning this hero. |
| `GetGoldBounty(): number` |  |
| `GetHeroFacetID(): number` | **Availability:** `both` |
| `GetHeroID(): number` |  |
| `GetIncreasedAttackSpeed(ignoreTempAttackSpeed: boolean): number` | Hero attack speed is also affected by agility. |
| `GetIntellect(skipNoConsume: boolean): number` | **Availability:** `both` |
| `GetIntellectGain(): number` |  |
| `GetKills(): number` | Value is stored in PlayerResource. |
| `GetLastHits(): number` | Value is stored in PlayerResource. |
| `GetMostRecentDamageTime(): number` |  |
| `GetMultipleKillCount(): number` |  |
| `GetNumAttackers(): number` |  |
| `GetNumItemsInInventory(): number` |  |
| `GetNumItemsInStash(): number` |  |
| `GetPhysicalArmorBaseValue(): number` | Hero armor is affected by attributes. |
| `GetPlayerID(): PlayerID` | Returns player ID of the player owning this hero. |
| `GetPrimaryAttribute(): Attributes` |  |
| `GetPrimaryStatValue(): number` |  |
| `GetReplicatingOtherHero(): CDOTA_BaseNPC_Hero \| undefined` | If hero is under Replicate effect, returns original hero entity. |
| `GetRespawnsDisabled(): boolean` | Is this hero prevented from respawning? |
| `GetRespawnTime(): number` |  |
| `GetStreak(): number` | Value is stored in PlayerResource. |
| `GetStrength(): number` | **Availability:** `both` |
| `GetStrengthGain(): number` |  |
| `GetTimeUntilRespawn(): number` |  |
| `GetTogglableWearable(slotType: DOTASlotType_t): CBaseAnimatingActivity \| undefined` | Get wearable entity in slot (slot). |
| `HasAnyAvailableInventorySpace(): boolean` |  |
| `HasFlyingVision(): boolean` |  |
| `HasOwnerAbandoned(): boolean` |  |
| `HasRoomForItem(itemName: string, includeStashCombines: boolean, allowSelling: boolean): number` |  |
| `HeroLevelUp(playEffects: boolean): void` | Levels up the hero, true or false to play effects. |
| `IncrementAssists(killerId: PlayerID): void` | Value is stored in PlayerResource. |
| `IncrementDeaths(killerId: PlayerID): void` | Value is stored in PlayerResource. |
| `IncrementDenies(): void` | Value is stored in PlayerResource. |
| `IncrementKills(victimId: PlayerID): void` | Passed ID is for the victim, killer ID is ID of the current hero.  Value is<br>stored in PlayerResource. |
| `IncrementLastHitMultikill(): void` | Value is stored in PlayerResource. |
| `IncrementLastHits(): void` | Value is stored in PlayerResource. |
| `IncrementLastHitStreak(): void` | Value is stored in PlayerResource. |
| `IncrementNearbyCreepDeaths(): void` | Value is stored in PlayerResource. |
| `IncrementStreak(): void` | Value is stored in PlayerResource. |
| `IsBuybackDisabledByDevilsBargain(): boolean` |  |
| `IsReincarnating(): boolean` |  |
| `IsStashEnabled(): boolean` |  |
| `KilledHero(hero: CDOTA_BaseNPC_Hero, inflictor: CDOTABaseAbility \| undefined): void` |  |
| `ModifyAgility(newAgility: number): void` | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `ModifyGold(goldChange: number, reliable: boolean, reason: EDOTA_ModifyGold_Reason): number` | Gives this hero some gold. |
| `ModifyGoldFiltered(goldChange: number, reliable: boolean, reason: EDOTA_ModifyGold_Reason): number` | Gives this hero some gold, using the gold filter if extra filtering is on. |
| `ModifyIntellect(newIntellect: number): void` | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `ModifyStrength(newStrength: number): void` | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `PerformTaunt(): void` |  |
| `RecordLastHit(): void` |  |
| `RespawnHero(buyBack: boolean, respawnPenalty: boolean): void` | Respawn this hero. |
| `SetAbilityPoints(points: number): void` | Sets the current unspent ability points. |
| `SetBaseAgility(agility: number): void` |  |
| `SetBaseIntellect(intellect: number): void` |  |
| `SetBaseStrength(strength: number): void` |  |
| `SetBotDifficulty(difficulty: number): void` |  |
| `SetBuybackCooldownTime(time: number): void` | Sets the buyback cooldown time. |
| `SetBuyBackDisabledByDevilsBargain(buybackDisabled: boolean): void` |  |
| `SetBuybackGoldLimitTime(time: number): void` | Set the amount of time gold gain is limited after buying back. |
| `SetCustomDeathXP(value: number): void` | Sets a custom experience value for this hero.  Note, GameRules boolean must be<br>set for this to work! |
| `SetGold(gold: number, reliable: boolean): void` | Sets the gold amount for the player owning this hero. |
| `SetPlayerID(playerId: PlayerID): void` |  |
| `SetPrimaryAttribute(primaryAttribute: Attributes): void` | Set this hero's primary attribute value. |
| `SetRespawnPosition(origin: Vector): void` |  |
| `SetRespawnsDisabled(disableRespawns: boolean): void` | Prevent this hero from respawning. |
| `SetStashEnabled(enabled: boolean): void` |  |
| `SetTimeUntilRespawn(time: number): void` |  |
| `ShouldDoFlyHeightVisual(): boolean` |  |
| `SpendGold(cost: number, reason: EDOTA_ModifyGold_Reason): void` |  |
| `UpgradeAbility(ability: CDOTABaseAbility): void` | This upgrades the passed ability if it exists and the hero has enough ability<br>points. |
| `WillReincarnate(): boolean` |  |

### CDOTA_BaseNPC_LotusPool

Extends `CDOTA_BaseNPC_Building`

_No members._

### CDOTA_BaseNPC_NeutralItemStash

Extends `CDOTA_BaseNPC_Building`

_No members._

### CDOTA_BaseNPC_Shop

Extends `CDOTA_BaseNPC_Building`

**Methods**

| Method | Description |
| --- | --- |
| `GetShopType(): DOTA_SHOP_TYPE` | Get the DOTA_SHOP_TYPE. |
| `SetShopType(shopType: DOTA_SHOP_TYPE): void` | Set the DOTA_SHOP_TYPE. |

### CDOTA_BaseNPC_Trap_Ward

Extends `CDOTA_BaseNPC_Creature`

**Methods**

| Method | Description |
| --- | --- |
| `GetTrapTarget(): Vector` | Get the trap target for this entity. |
| `SetAnimation(animation: string): void` | Set the animation sequence for this entity. |

### CDOTA_BaseNPC_Watch_Tower

Extends `CDOTA_BaseNPC_Building`

**Methods**

| Method | Description |
| --- | --- |
| `GetInteractAbilityName(): string` | The name of the ability used when triggering interaction on the outpost. |
| `SetInteractAbilityName(interactAbilityName: string): void` | The name of the ability used when triggering interaction on the outpost. |

### CDOTA_Buff

**Methods**

| Method | Description |
| --- | --- |
| `AddParticle( index: number, destroyImmediately: boolean, statusEffect: boolean, priority: number, heroEffect: boolean, overheadEffect: boolean, ): void` | **Availability:** `both` |
| `CheckStateToTable(table: object): void` | **Availability:** `both` |
| `DecrementStackCount(): void` | Decrease this modifier's stack count by 1.<br><br>**Availability:** `both` |
| `Destroy(): void` | Run all associated destroy functions, then remove the modifier.<br><br>**Availability:** `both` |
| `DestroyOnExpire(): boolean` | **Availability:** `both` |
| `ForceRefresh(): void` | Run all associated refresh functions on this modifier as if it was re-applied.<br><br>**Availability:** `both` |
| `GetAbility(): CDOTABaseAbility \| undefined` | Get the ability that generated the modifier.<br><br>**Availability:** `both` |
| `GetAuraDuration(): number` | Returns aura stickiness (default 0.5).<br><br>**Availability:** `both` |
| `GetAuraOwner(): CDOTA_BaseNPC \| undefined` | Returns the owner of the aura modifier, that applied this modifier. Always<br>`nil` on the client.<br><br>**Availability:** `both` |
| `GetCaster(): CDOTA_BaseNPC \| undefined` | Get the owner of the ability responsible for the modifier.<br><br>**Availability:** `both` |
| `GetClass(): string` | **Availability:** `both` |
| `GetCreationTime(): number` | **Availability:** `both` |
| `GetDieTime(): number` | **Availability:** `both` |
| `GetDuration(): number` | **Availability:** `both` |
| `GetElapsedTime(): number` | **Availability:** `both` |
| `GetLastAppliedTime(): number` | **Availability:** `both` |
| `GetName(): string` | **Availability:** `both` |
| `GetParent(): CDOTA_BaseNPC` | Get the unit the modifier is parented to.<br><br>**Availability:** `both` |
| `GetRemainingTime(): number` | **Availability:** `both` |
| `GetSerialNumber(): number` | **Availability:** `both` |
| `GetStackCount(): number` | **Availability:** `both` |
| `HasFunction(func: modifierfunction): boolean` | **Availability:** `both` |
| `IncrementStackCount(): void` | Increase this modifier's stack count by 1.<br><br>**Availability:** `both` |
| `IsDebuff(): boolean` | **Availability:** `both` |
| `IsHexDebuff(): boolean` | **Availability:** `both` |
| `IsNull(): boolean` | Has underlying C++ entity object been deleted?<br><br>**Availability:** `both` |
| `IsStunDebuff(): boolean` | **Availability:** `both` |
| `SendBuffRefreshToClients(): void` |  |
| `SetDuration(duration: number, informClient: boolean): void` | **Availability:** `both` |
| `SetOverheadEffectOffset(offset: number): boolean` | **Availability:** `both` |
| `SetStackCount(count: number): void` | **Availability:** `both` |
| `StartIntervalThink(interval: number): void` | Start this modifier's think function (OnIntervalThink) with the given interval<br>(float).  To stop, call with -1.<br><br>**Availability:** `both` |

### CDOTA_CustomUIManager

**Methods**

| Method | Description |
| --- | --- |
| `DynamicHud_Create(playerId: PlayerID, elementId: string, layoutFileName: string, dialogVariables: object): void` | Create a new custom UI HUD element for the specified player(s). |
| `DynamicHud_Destroy(playerId: PlayerID, elementId: string): void` | Destroy a custom hud element. |
| `DynamicHud_SetDialogVariables(playerId: PlayerID, elementId: string, dialogVariables: object): void` | Add or modify dialog variables for an existing custom hud element. |
| `DynamicHud_SetVisible(playerId: PlayerID, elementId: string, visible: boolean): void` | Toggle the visibility of an existing custom hud element. |

### CDOTA_Item

Extends `CDOTABaseAbility`

**Methods**

| Method | Description |
| --- | --- |
| `CanBeUsedOutOfInventory(): boolean` |  |
| `CanOnlyPlayerHeroPickup(): boolean` | **Availability:** `client` |
| `GetContainer(): CDOTA_Item_Physical \| undefined` | Get the container for this item. |
| `GetCost(): number` |  |
| `GetCurrentCharges(): number` | Get the number of charges this item currently has.<br><br>**Availability:** `both` |
| `GetInitialCharges(): number` | Get the initial number of charges this item has.<br><br>**Availability:** `both` |
| `GetItemSlot(): -1 \| DOTAScriptInventorySlot_t` | **Availability:** `both` |
| `GetItemState(): number` | Gets whether item is unequipped or ready. |
| `GetParent(): object` | Get the parent for this item. |
| `GetPurchaser(): CDOTA_BaseNPC \| undefined` | Get the purchaser for this item. |
| `GetPurchaseTime(): number` | Get the purchase time of this item. |
| `GetSecondaryCharges(): number` | Get the number of secondary charges this item currently has.<br><br>**Availability:** `both` |
| `GetShareability(): EShareAbility` | **Availability:** `both` |
| `GetValuelessCharges(): number` | Get the number of valueless charges this item currently has. |
| `IsActiveNeutral(): boolean` |  |
| `IsAlertableItem(): boolean` | **Availability:** `both` |
| `IsCastOnPickup(): boolean` | **Availability:** `both` |
| `IsCombinable(): boolean` |  |
| `IsCombineLocked(): boolean` |  |
| `IsDisassemblable(): boolean` | **Availability:** `both` |
| `IsDroppable(): boolean` | **Availability:** `both` |
| `IsInBackpack(): boolean` | **Availability:** `both` |
| `IsItem(): this is CDOTA_Item` | **Availability:** `both` |
| `IsKillable(): boolean` | **Availability:** `both` |
| `IsMuted(): boolean` | **Availability:** `both` |
| `IsPermanent(): boolean` | Is this a permanent item?<br><br>**Availability:** `both` |
| `IsPurchasable(): boolean` | **Availability:** `both` |
| `IsRecipe(): boolean` | **Availability:** `both` |
| `IsRecipeGenerated(): boolean` | **Availability:** `both` |
| `IsSellable(): boolean` | **Availability:** `both` |
| `IsStackable(): boolean` | **Availability:** `both` |
| `LaunchLoot( autoUse: boolean, height: number, duration: number, endPoint: Vector, teleportOwner: CDOTA_BaseNPC_Hero \| undefined, ): void` |  |
| `LaunchLootInitialHeight( autoUse: boolean, initialHeight: number, launchHeight: number, duration: number, endPoint: Vector, ): void` |  |
| `LaunchLootRequiredHeight( autoUse: boolean, requiredHeight: number, height: number, duration: number, endPoint: Vector, ): void` |  |
| `ModifyNumValuelessCharges(charges: number): void` | Modifies the number of valueless charges on this item. |
| `OnEquip(): void` |  |
| `OnUnequip(): void` |  |
| `RequiresCharges(): boolean` | **Availability:** `both` |
| `SetCanBeUsedOutOfInventory(value: boolean): void` |  |
| `SetCastOnPickup(castOnPickUp: boolean): void` |  |
| `SetCombineLocked(combineLocked: boolean): void` |  |
| `SetCurrentCharges(charges: number): void` | Set the number of charges on this item. |
| `SetDroppable(droppable: boolean): void` |  |
| `SetItemState(state: number): void` | Sets whether item is unequipped or ready. |
| `SetOnlyPlayerHeroPickup(onlyPlayerHero: boolean): void` |  |
| `SetPurchaser(purchaser: CDOTA_BaseNPC \| undefined): void` | Set the purchaser of record for this item. |
| `SetPurchaseTime(time: number): void` | Set the purchase time of this item. |
| `SetSecondaryCharges(charges: number): void` | Set the number of secondary charges on this item. |
| `SetSellable(sellable: boolean): void` |  |
| `SetShareability(shareability: EShareAbility): void` |  |
| `SetStacksWithOtherOwners(stacksWithOtherOwners: boolean): void` |  |
| `SpendCharge(delayRemove: number): void` |  |
| `StacksWithOtherOwners(): boolean` |  |
| `Think(): void` | Think this item. |

### CDOTA_Item_BagOfGold

Extends `CDOTA_Item`

**Methods**

| Method | Description |
| --- | --- |
| `SetLifeTime(time: number): void` | Set the life time of this item. |

### CDOTA_Item_DataDriven

Extends `CDOTA_Item`

**Methods**

| Method | Description |
| --- | --- |
| `ApplyDataDrivenModifier( caster: CDOTA_BaseNPC, target: CDOTA_BaseNPC, modifierName: string, modifierTable: object \| undefined, ): void` | Applies a data driven modifier to the target. |
| `ApplyDataDrivenThinker( caster: CDOTA_BaseNPC, location: Vector, modifierName: string, modifierTable: object \| undefined, ): CDOTA_Buff` | Applies a data driven thinker at the location. |

### CDOTA_Item_EmptyBottle

Extends `CDOTA_Item`

**Methods**

| Method | Description |
| --- | --- |
| `ClearStoredRune(): void` | Clear the stored rune. |
| `OnRune(runeType: number): boolean` | Place a rune in the bottle. |
| `SetStoredRune(runeType: number): void` | Set the stored rune. |

### CDOTA_Item_Lua

Extends `CDOTA_Item`

**Methods**

| Method | Description |
| --- | --- |
| `CanUnitPickUp(unit: CDOTA_BaseNPC): boolean` | Returns true if this item can be picked up by the target unit.<br><br>**Parameters:**<br><br>- unit Unit trying to pick up the item.<br> |
| `CastFilterResult(): UnitFilterResult` | Determine whether an issued command with no target is valid.<br><br>**Availability:** `both` |
| `CastFilterResultLocation(location: Vector): UnitFilterResult` | Determine whether an issued command on a location is valid.<br><br>**Availability:** `both` |
| `CastFilterResultTarget(target: CDOTA_BaseNPC): UnitFilterResult` | Determine whether an issued command on a target is valid.<br><br>**Availability:** `both` |
| `GetAbilityTextureName(): string` | Allows code overriding of the item texture shown in the HUD.<br><br>**Availability:** `client` |
| `GetAOERadius(): number` | Controls the size of the AOE casting cursor.<br><br>**Availability:** `client` |
| `GetAssociatedPrimaryAbilities(): string` | Returns abilities that are stolen simultaneously, or otherwise related in<br>functionality. |
| `GetAssociatedSecondaryAbilities(): string` | Returns other abilities that are stolen simultaneously, or otherwise related in<br>functionality.  Generally hidden abilities. |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR \| Uint64` | Return cast behavior type of this ability.<br><br>**Availability:** `both` |
| `GetCastRange(location: Vector, target: CDOTA_BaseNPC \| undefined): number` | Return cast range of this ability.<br><br>**Availability:** `both` |
| `GetChannelledHealthCostPerSecond(level: number): number` | Return health cost per second of channeling at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetChannelledManaCostPerSecond(level: number): number` | Return mana cost at the given level per second while channeling (-1 is current).<br><br>**Availability:** `both` |
| `GetChannelStartTime(): number` | Return the channel start time of this ability.<br><br>**Availability:** `both` |
| `GetChannelTime(): number` | Return the channel time of this ability.<br><br>**Availability:** `both` |
| `GetConceptRecipientType(): number` | Return who hears speech when this spell is cast. |
| `GetCooldown(level: number): number` | Return cooldown of this ability.<br><br>**Availability:** `both` |
| `GetCustomCastError(): string` | Return the error string of a failed command with no target.<br><br>**Availability:** `both` |
| `GetCustomCastErrorLocation(location: Vector): string` | Return the error string of a failed command on a location.<br><br>**Availability:** `both` |
| `GetCustomCastErrorTarget(target: CDOTA_BaseNPC): string` | Return the error string of a failed command on a target.<br><br>**Availability:** `both` |
| `GetCustomHudErrorMessage(reason: number): string` | (DOTA_INVALID_ORDERS nReason) Return the error string of a failed order.<br><br>**Availability:** `both` |
| `GetEffectiveCastRange(location: Vector, target: object): number` | Return cast range of this ability, taking modifiers into account.<br><br>**Availability:** `both` |
| `GetGoldCost(level: number): number` | Return gold cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetHealthCost(level: number): number` | Return health cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetIntrinsicModifierName(): string` | Returns the name of the modifier applied passively by this ability. |
| `GetManaCost(level: number): number` | Return mana cost at the given level (-1 is current).<br><br>**Availability:** `both` |
| `GetPlaybackRateOverride(): number` | Return the animation rate of the cast animation. |
| `IsHiddenAbilityCastable(): boolean` | Returns true if this ability can be used when not on the action panel. |
| `IsHiddenWhenStolen(): boolean` | Returns true if this ability is hidden when stolen by Spell Steal. |
| `IsMuted(): boolean` | Returns whether this item is muted or not.<br><br>**Availability:** `both` |
| `IsRefreshable(): boolean` | Returns true if this ability is refreshed by Refresher Orb. |
| `IsStealable(): boolean` | Returns true if this ability can be stolen by Spell Steal. |
| `OnAbilityPhaseInterrupted(): void` | Cast time did not complete successfully. |
| `OnAbilityPhaseStart(): boolean` | Cast time begins (return true for successful cast). |
| `OnChannelFinish(interrupted: boolean): void` | Channel finished. |
| `OnChannelThink(interval: number): void` | Channeling is taking place. |
| `OnChargeCountChanged(spent: boolean): void` | Runs when item's charge count changes. bSpent is true when the charge count<br>change is coming from SpendCharge. |
| `OnHeroCalculateStatBonus(): void` | Caster (hero only) gained a level, skilled an ability, or received a new stat<br>bonus. |
| `OnHeroDiedNearby(unit: CDOTA_BaseNPC, attacker: CDOTA_BaseNPC, event: object): void` | A hero has died in the vicinity (ie Urn), takes table of params. |
| `OnHeroLevelUp(): void` | Caster gained a level. |
| `OnInventoryContentsChanged(): void` | Caster inventory changed. |
| `OnItemEquipped(item: CDOTA_Item): void` | Caster equipped item. |
| `OnOwnerDied(): void` | Caster died. |
| `OnOwnerSpawned(): void` | Caster respawned or spawned for the first time. |
| `OnProjectileHit(target: CDOTA_BaseNPC \| undefined, location: Vector): boolean \| void` | Projectile has collided with a given target or reached its destination. If<br>'true` is returned, projectile would be destroyed. |
| `OnProjectileThink(location: Vector): void` | Projectile is actively moving. |
| `OnSpellStart(): void` | Cast time finished, spell effects begin. |
| `OnStolen(sourceAbility: CDOTABaseAbility): void` | Special behavior when stolen by Spell Steal. |
| `OnToggle(): void` | Ability is toggled on/off. |
| `OnUnStolen(): void` | Special behavior when lost by Spell Steal. |
| `OnUpgrade(): void` | Ability gained a level. |
| `ProcsMagicStick(): boolean` | Returns true if this ability will generate magic stick charges for nearby<br>enemies. |
| `SpeakTrigger(): number` | Return the type of speech used. |

**Other members**

| Member | Description |
| --- | --- |
| `Precache?(context: CScriptPrecacheContext): void` | **Abstract** |
| `Spawn?(): void` | Called when ability entity is created, after Init.<br><br>**Availability:** `both`<br><br>**Abstract** |

### CDOTA_Item_Physical

Extends `CBaseAnimatingActivity`

**Methods**

| Method | Description |
| --- | --- |
| `GetContainedItem(): CDOTA_Item` | Returned the contained item. |
| `GetCreationTime(): number` | Returns the game time when this item was created in the world. |
| `IsLoot(): boolean` | Is this drop flagged as a loot drop? |
| `SetContainedItem(item: CDOTA_Item): void` | Set the contained item. |
| `SetIsLoot(isLoot: boolean): void` | Set if this drop is flagged as a loot drop. |

### CDOTA_ItemSpawner

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `GetItemName(): string` | Returns the item name. |

### CDOTA_MapTree

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `CutDown(teamNumberKnownTo: number): void` | Cuts down this tree. |
| `CutDownRegrowAfter(regrowAfter: number, teamNumberKnownTo: number): void` | Cuts down this tree. |
| `GrowBack(): void` | Grows back the tree if it was cut down. |
| `IsStanding(): boolean` | Returns true if the tree is standing, false if it has been cut down. |

### CDOTA_Modifier_Lua

Extends `CDOTA_Buff`

**Methods**

| Method | Description |
| --- | --- |
| `AllowIllusionDuplicate(): boolean` | True/false if this modifier is active on illusions.<br><br>**Availability:** `both` |
| `CanParentBeAutoAttacked(): boolean` | **Availability:** `both` |
| `DestroyOnExpire(): boolean` | True/false if this buff is removed when the duration expires.<br><br>**Availability:** `both` |
| `GetAttributes(): DOTAModifierAttribute_t` | Return the types of attributes applied to this modifier.<br><br>**Availability:** `both` |
| `GetAuraDuration(): number` | Returns aura stickiness.<br><br>**Availability:** `both` |
| `GetAuraEntityReject(entity: CDOTA_BaseNPC): boolean` | Return true/false if this entity should receive the aura under specific<br>conditions.<br><br>**Availability:** `both` |
| `GetAuraRadius(): number` | Return the range around the parent this aura tries to apply its buff.<br><br>**Availability:** `both` |
| `GetAuraSearchFlags(): DOTA_UNIT_TARGET_FLAGS` | Return the unit flags this aura respects when placing buffs.<br><br>**Availability:** `both` |
| `GetAuraSearchTeam(): DOTA_UNIT_TARGET_TEAM` | Return the teams this aura applies its buff to.<br><br>**Availability:** `both` |
| `GetAuraSearchType(): DOTA_UNIT_TARGET_TYPE` | Return the unit classifications this aura applies its buff to.<br><br>**Availability:** `both` |
| `GetCritDamage(): number` | A Modifier that listens to MODIFIER_PROPERTY_PREATTACK_CRITICALSTRIKE has to<br>have a GetCritDamage implementation so we can know when to evaluate it. Value<br>should be in 'times the original value format' e.g: 1.5 not 150.<br><br>**Availability:** `both` |
| `GetEffectAttachType(): ParticleAttachment_t` | Return the attach type of the particle system from GetEffectName.<br><br>**Availability:** `both` |
| `GetEffectName(): string` | Return the name of the particle system that is created while this modifier is<br>active.<br><br>**Availability:** `both` |
| `GetHeroEffectName(): string` | Return the name of the hero effect particle system that is created while this<br>modifier is active.<br><br>**Availability:** `both` |
| `GetModifierAura(): string` | The name of the secondary modifier that will be applied by this modifier (if it<br>is an aura).<br><br>**Availability:** `both` |
| `GetPriority(): modifierpriority` | Return the priority order this modifier will be applied over others.<br><br>**Availability:** `both` |
| `GetStatusEffectName(): string` | Return the name of the status effect particle system that is created while this<br>modifier is active.<br><br>**Availability:** `both` |
| `GetTexture(): string` | Return the name of the buff icon to be shown for this modifier.<br><br>**Availability:** `both` |
| `HeroEffectPriority(): modifierpriority` | Relationship of this hero effect with those from other buffs (higher is more<br>likely to be shown).<br><br>**Availability:** `both` |
| `IsAura(): boolean` | True/false if this modifier is an aura.<br><br>**Availability:** `both` |
| `IsAuraActiveOnDeath(): boolean` | True/false if this aura provides buffs when the parent is dead.<br><br>**Availability:** `both` |
| `IsDebuff(): boolean` | True/false if this modifier should be displayed as a debuff.<br><br>**Availability:** `both` |
| `IsHidden(): boolean` | True/false if this modifier should be displayed on the buff bar.<br><br>**Availability:** `both` |
| `IsPermanent(): boolean` | **Availability:** `both` |
| `IsPurgable(): boolean` | True/false if this modifier can be purged.<br><br>**Availability:** `both` |
| `IsPurgeException(): boolean` | True/false if this modifier can be purged by strong dispels.<br><br>**Availability:** `both` |
| `IsStunDebuff(): boolean` | True/false if this modifier is considered a stun for purge reasons.<br><br>**Availability:** `both` |
| `OnCreated(params: object): void` | Runs when the modifier is created.<br><br>**Availability:** `both` |
| `OnDestroy(): void` | Runs when the modifier is destroyed (after unit loses modifier).<br><br>**Availability:** `both` |
| `OnIntervalThink(): void` | Runs when the think interval occurs.<br><br>**Availability:** `both` |
| `OnRefresh(params: object): void` | Runs when the modifier is refreshed.<br><br>**Availability:** `both` |
| `OnRemoved(death: boolean): void` | Runs when the modifier is destroyed (before unit loses modifier).<br><br>**Availability:** `both` |
| `OnStackCountChanged(stackCount: number): void` | Runs when stack count changes (param is old count).<br><br>**Availability:** `both` |
| `PiercesDebuffImmunity(): boolean` | Returns true or false on if the effects of this modifier should pierce debuff<br>immunity. By default uses the setting from the ability.<br><br>**Availability:** `both` |
| `RemoveOnDeath(): boolean` | True/false if this modifier is removed when the parent dies.<br><br>**Availability:** `both` |
| `SetHasCustomTransmitterData(hasCustomData: boolean): void` | **Availability:** `both` |
| `ShouldUseOverheadOffset(): boolean` | Apply the overhead offset to the attached effect.<br><br>**Availability:** `both` |
| `StatusEffectPriority(): modifierpriority` | Relationship of this status effect with those from other buffs (higher is more<br>likely to be shown).<br><br>**Availability:** `both` |

**Other members**

| Member | Description |
| --- | --- |
| `BotAttackScoreBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `CheckState?(): Partial<Record<modifierstate, boolean>>` | Return a map of enabled/disabled states.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `DeclareFunctions?(): modifierfunction[]` | Return a list of modifier functions this modifier implements.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetAbsoluteNoDamageMagical?(event: ModifierAttackEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetAbsoluteNoDamagePhysical?(event: ModifierAttackEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetAbsoluteNoDamagePure?(event: ModifierAttackEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetAbsorbSpell?(event: ModifierAbilityEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetActivityTranslationModifiers?(): string` | **Availability:** `both`<br><br>**Abstract** |
| `GetAllowEtherealAttack?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetAlwaysAllowAttack?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetAlwaysAutoAttackWhileHoldPosition?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetAttackSound?(): string` | **Availability:** `both`<br><br>**Abstract** |
| `GetBaseAttackPostBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetBonusDayVision?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetBonusDayVisionPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetBonusNightVision?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetBonusNightVisionUnique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetBonusVisionPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetBuffAmplification?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetConvertAttackPhysicalToPure?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetCriticalStrikeBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetDisableAutoAttack?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetDisableHealing?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetDisableManaGain?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetFixedDayVision?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetFixedNightVision?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetForceDrawOnMinimap?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetIsIllusion?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetMagicalArmorPiercingPercentageTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetMinHealth?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetMinMana?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAbilityLayout?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAbilityPoints?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAdditionalNutralItemDrops?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAoEBonusConstant?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAoEBonusConstantStacking?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAoEBonusPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackHeightBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackPointConstant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackRangeBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackRangeBonusPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackRangeBonusUnique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackRangeOverride?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeed_Limit?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeedAbsoluteMax?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeedBaseOverride?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeedBonus_Constant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeedPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAttackSpeedReductionPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAvoidAttackProcs?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAvoidDamage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAvoidDamageAfterReductions?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierAvoidSpell?(event: ModifierAttackEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseArmorPerAgiBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseAttack_BonusDamage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseAttackSpeedPerAgiBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseAttackTimeConstant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseAttackTimeConstant_Adjust?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseAttackTimePercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseDamageOutgoing_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseDamageOutgoing_PercentageUnique?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseHpRegenPerStrBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseMagicResistPerIntBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseManaRegenPerIntBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBaseRegen?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBecomeAgility?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBecomeIntelligence?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBecomeStrength?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBecomeUniversal?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusDamageOutgoing_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusLotusHeal?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Agility?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Agility_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Intellect?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Intellect_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Strength?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusStats_Strength_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBonusUphillMissChance?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierBuybackPenaltyPercent?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCanAttackTrees?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCastRangeBonus?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCastRangeBonusPercentage?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCastRangeBonusStacking?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCastRangeBonusTarget?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierChangeAbilityValue?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConstantDeathGoldCost?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConstantHealthRegen?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConstantManaRegen?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConstantManaRegenUnique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConstantRespawnTime?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierConvertManaCostToHealthCost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCooldownReduction_Constant?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCreateBonusIllusionChance?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCreateBonusIllusionCount?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierCreepDenyPercent?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDamageOutgoing_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDamageOutgoing_Percentage_Illusion?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDamageOutgoing_Percentage_Illusion_Amplify?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDamageOutgoing_PercentageMultiplicative?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDisableTurning?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDisassembleAnything?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierDodgeProjectile?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierEvasion_Constant?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraHealthBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraHealthPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraManaBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraManaBonusPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraManaPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierExtraStrengthBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierFixedAttackRate?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierFixedManaRegen?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierForceMaxHealth?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierForceMaxMana?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierFoWTeam?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHasBonusNeutralItemChoice?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealAmplify_PercentageSource?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealAmplify_PercentageTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealthBarPips?(event: ModifierAttackEvent): number` | Return value is a count of pips.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealthBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealthcostReduction_Constant?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealthRegenPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHealthRegenPercentageUnique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHeroFacetOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHeroLevelScale?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHPRegenAmplify_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierHPRegenMultiplierPreAmplification?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIgnoreCastAngle?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIgnoreCooldown?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIgnoreMovespeedLimit?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIgnorePhysicalArmor?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIllusionLabel?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIncomingDamage_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIncomingDamageConstant?(event: ModifierAttackEvent): number` | This property controls 'universal' shield, if defined both on client and<br>server. Return value on client should be current shield health, as a positive<br>integer, on server - amount of damage blocked.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierIncomingPhysicalDamage_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIncomingPhysicalDamageConstant?(event: ModifierAttackEvent): number` | This property controls 'physical' shield, if defined both on client and server.<br>Return value on client should be current shield health, as a positive integer,<br>on server - amount of damage blocked.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierIncomingSpellDamageConstant?(event: ModifierAttackEvent): number` | This property controls 'spell' shield, if defined both on client and server.<br>Return value on client should be current shield health, as a positive integer,<br>on server - amount of damage blocked.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierInnateDamageBlockPctOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIntellectNone?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierInventorySlotRestricted?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierInvisibilityAttackBehaviorException?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierInvisibilityLevel?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierIsPackRat?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierItemSellbackCost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierKillStreakBonusGoldPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierKnockbackAmplification_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierLifestealRegenAmplify_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagical_ConstantBlock?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceBaseReduction?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceBonus?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceBonusIllusions?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceBonusUnique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceDecrepifyUnique?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMagicalResistanceDirectModification?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierManaBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierManacostReduction_Constant?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierManaDrainAmplify_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMaxAttackRange?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMinPhysicalArmor?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMiss_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMiss_Percentage_Target?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierModelChange?(): string` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierModelScale?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierModelScaleAnimateTime?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierModelScaleConstant?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierModelScaleUseInOutEase?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_Absolute?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_AbsoluteMax?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_AbsoluteMin?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_Limit?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_MaxOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeed_MinOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Constant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Constant_Unique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Constant_Unique_2?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Percentage_Unique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Special_Boots?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedBonus_Special_Boots_2?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedMax_BonusConstant?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedOverride?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedPostMultiplierBonus_Constant?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMoveSpeedReductionPercentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMPRegenAmplify_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMPRegenAmplify_Percentage_Unique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierMPRestoreAmplify_Percentage?(): number` | Total amplify value is clamped to 0.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierNegativeEvasion_Constant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierNeutralEnhancementOptions?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierNeutralTrinketOptions?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierNoFreeTPScrollOnDeath?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierNoVisionOfAttacker?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideAbilitySpecial?(event: ModifierOverrideAbilitySpecialEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideAbilitySpecialValue?(event: ModifierOverrideAbilitySpecialEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideAttackDamage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideBaseDamage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideCreepBounty?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideUntargetableFrom?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierOverrideUntargetableTo?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageAttackAnimTime?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageCasttime?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageConvertExpToGold?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageCooldown?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageCooldownOngoing?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageCooldownStacking?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageDeathGoldCost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageExpRateBoost?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageGoldRateBoost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageHealthcost?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageHealthcostStacking?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageKillAssistGoldBoost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageManacost?(event: ModifierAbilityEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageManacostStacking?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPercentageRespawnTime?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPersistentInvisibility?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysical_ConstantBlock?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysical_ConstantBlockBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysical_ConstantBlockSpecial?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysical_ConstantBlockUnavoidablePreArmor?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorBase_Percentage?(): number` | Values above 100% are ignored.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorBonus?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorBonusPost?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorBonusUnique?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorBonusUniqueActive?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalArmorTotal_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPhysicalDamageOutgoing_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_BonusDamage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_BonusDamage_Proc?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_BonusDamage_Target?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_BonusDamagePostCrit?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_CriticalStrike?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_DeadlyBlow?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreAttack_Target_CriticalStrike?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPrereduceIncomingDamage_Mult?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPreserveNeutralItemPassives?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_BonusDamage_Magical?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_BonusDamage_Magical_Target?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_BonusDamage_Physical?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_BonusDamage_Pure?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_ConvertPhysicalToMagical?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProcAttack_Feedback?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProjectileName?(): string` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProjectileSpeed?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProjectileSpeedBonus?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProjectileSpeedBonusPercentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProjectileSpeedTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProperty_MagicalLifesteal?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProperty_PhysicalLifesteal?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyConsumableUseSpeed?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyForbidIllusions?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyHealingAmplificationUnique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyManacostOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyRedirectHealthGain?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyRestorationAmplification?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyRestorationAmplificationUnique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertySuppressInvalidMoveAttackOrders?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropertyUpgradeNeutralArtifacts?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierPropetyFailAttack?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierProvidesFOWVision?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierRadarCooldownReduction?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierScepter?(): 0 \| 1` | Applies scepter when this property is active<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierShard?(): 0 \| 1` | Applies shard when this property is active<br><br>**Availability:** `both`<br><br>**Abstract** |
| `GetModifierShareXPRune?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSlowResistance_Stacking?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GEtModifierSlowResistance_Unique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSlowResistanceAppliesToAttacks?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellAmplify_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellAmplify_PercentageTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellAmplify_PercentageUnique?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellLifestealRegenAmplify_Percentage?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellLifestealRegenAmplify_Percentage_Unique?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellRedirectTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSpellsRequireHP?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierStackingRespawnTime?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierStatusResistance?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierStatusResistanceCaster?(event: ModifierUnitEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierStatusResistanceStacking?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierStrongIllusion?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSuperIllusion?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSuperIllusionWithItems?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSuperIllusionWithUltimate?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierSuppressFullscreenDeathFX?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTempestDouble?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTickGold_Multiplier?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTotal_ConstantBlock?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTotal_ConstantBlockStacking?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTotalDamageOutgoing_Percentage?(event: ModifierAttackEvent): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTotalPercentageManaRegen?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTurnRate_Override?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTurnRate_Percentage?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierTurnRateConstant?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierUnitDisllowUpgrading?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierUnitStatsNeedsRefresh?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierXPDuringDeath?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModifierXPFountainCountdownTimeOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetModofierPropertyPseudoRandomBonus?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetOverrideAnimation?(): GameActivity_t` | **Availability:** `both`<br><br>**Abstract** |
| `GetOverrideAnimationRate?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetOverrideAttackMagical?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetPhysicalArmorPiercingPercentageTarget?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetPrimaryStatDamageMultiplier?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetRedirectSpell?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetReflectSpell?(event: ModifierAbilityEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetRequiredLevel?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetSkipAttackRegulator?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetSuppressAttackProcs?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetSuppressCleave?(event: ModifierAttackEvent): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetSuppressCrit?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetSuppressIncomingCrit?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetSuppressTeleport?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `GetTierTokenReroll?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetTriggerCosmeticAndEndAttack?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetUnitLifetimeFraction?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetVisionDegreeRestriction?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `GetVisualZDelta?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `GetVisualZSpeedBaseOverride?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `HasBonusNeutralItemPassive?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `MinAttributeLevel?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT_POST?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilityEndChannel?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilityExecuted?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilityFullyCast?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilityStart?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilitySwapped?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAbilityToggled?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAssist?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttack?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackAllied?(event: ModifierAttackEvent): void` | Happens even if attack can't be issued.<br><br>**Availability:** `both`<br><br>**Abstract** |
| `OnAttackCancelled?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttacked?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackFail?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackFinished?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackLanded?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackRecord?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackRecordDestroy?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttackStart?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnAttemptProjectileDodge?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnBreakInvisibility?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnBuildingKilled?(event: ModifierInstanceEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnCleaveAttackLanded?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDamageCalculated?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDamageHPLoss?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDamagePrevented?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDayStarted?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDeath?(event: ModifierInstanceEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDeathCompleted?(event: ModifierInstanceEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnDominated?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnForceProcMagicStick?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnFoWTeamChanged?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnHealReceived?(event: ModifierHealEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnHealthGained?(event: ModifierHealEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnHeroBeginDying?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnHeroKilled?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnIllusionCreated?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnKill?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnMagicDamageCalculated?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnManaGained?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnModelChanged?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnModifierAdded?(event: ModifierAddedEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnModifierRefreshed?(event: ModifierAddedEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnModifierRemoved?(event: ModifierAddedEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnMuteDamageAbilities?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnNightStarted?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnOrder?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnOrderReceived?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnProcessCleave?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnProjectileDodge?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnProjectileObstructionHit?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnPureDamageCalculated?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnPurged?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnRedirectHealthGain?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnRespawn?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnRuneSpawn?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnScepterUpgradeSelected?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSetLocation?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnShardUpgradeSelected?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSpellAppliedSuccessfully?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSpellTargetReady?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSpentHealth?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSpentItemCharge?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnSpentMana?(event: ModifierAbilityEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnStateChanged?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTakeDamage?(event: ModifierInstanceEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTakeDamageKillCredit?(event: ModifierAttackEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTakeDamagePostUnavoidableBlock?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTeleported?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTeleporting?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTierTokenRerolled?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnTooltip?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `OnTooltip2?(): number` | **Availability:** `both`<br><br>**Abstract** |
| `OnTreeCutDown?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `OnUnitMoved?(event: ModifierUnitEvent): void` | **Availability:** `both`<br><br>**Abstract** |
| `PreserveParticlesOnModelChanged?(): 0 \| 1` | **Availability:** `both`<br><br>**Abstract** |
| `ReincarnateSuppressFX?(): void` | **Availability:** `both`<br><br>**Abstract** |
| `ReincarnateTime?(): number` | **Availability:** `both`<br><br>**Abstract** |

### CDOTA_Modifier_Lua_Horizontal_Motion

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Description |
| --- | --- |
| `ApplyHorizontalMotionController(): boolean` | Starts the horizontal motion controller effects for this buff.  Returns true if<br>successful. |
| `GetPriority(): modifierpriority` | Get the priority. |
| `OnHorizontalMotionInterrupted(): void` | Called when the motion gets interrupted. |
| `SetPriority(motionPriority: modifierpriority): void` | Set the priority. |
| `UpdateHorizontalMotion(me: CDOTA_BaseNPC, dt: number): void` | Perform any motion from the given interval on the NPC. |

### CDOTA_Modifier_Lua_Motion_Both

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Description |
| --- | --- |
| `ApplyHorizontalMotionController(): boolean` | Starts the horizontal motion controller effects for this buff.  Returns true if<br>successful. |
| `ApplyVerticalMotionController(): boolean` | Starts the vertical motion controller effects for this buff.  Returns true if<br>successful. |
| `GetPriority(): modifierpriority` | Get the priority. |
| `OnHorizontalMotionInterrupted(): void` | Called when the motion gets interrupted. |
| `OnVerticalMotionInterrupted(): void` | Called when the motion gets interrupted. |
| `SetPriority(motionPriority: modifierpriority): void` | Set the priority. |
| `UpdateHorizontalMotion(me: CDOTA_BaseNPC, dt: number): void` | Perform any motion from the given interval on the NPC. |
| `UpdateVerticalMotion(me: CDOTA_BaseNPC, dt: number): void` | Perform any motion from the given interval on the NPC. |

### CDOTA_Modifier_Lua_Vertical_Motion

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Description |
| --- | --- |
| `ApplyVerticalMotionController(): boolean` | Starts the vertical motion controller effects for this buff.  Returns true if<br>successful. |
| `GetMotionPriority(): modifierpriority` | Get the priority. |
| `OnVerticalMotionInterrupted(): void` | Called when the motion gets interrupted. |
| `SetMotionPriority(motionPriority: modifierpriority): void` | Set the priority. |
| `UpdateVerticalMotion(me: CDOTA_BaseNPC, dt: number): void` | Perform any motion from the given interval on the NPC. |

### CDOTA_NeutralSpawner

Extends `CPointEntity`

**Methods**

| Method | Description |
| --- | --- |
| `CreatePendingUnits(): void` |  |
| `SelectSpawnType(): void` |  |
| `SpawnNextBatch(ignoreBlockers: boolean): void` |  |

### CDOTA_PlayerResource

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AddAegisPickup(playerId: PlayerID): void` |  |
| `AddCandyEvent(playerId: PlayerID, reason: number): void` |  |
| `AddClaimedFarm(playerId: PlayerID, farmValue: number, earnedValue: boolean): void` |  |
| `AddGoldSpentOnSupport(playerId: PlayerID, cost: number): void` |  |
| `AddNeutralItemToStash(playerId: PlayerID, teamNumber: DOTATeam_t, item: CDOTA_Item): void` |  |
| `AddRunePickup(playerId: PlayerID, runes: number): void` |  |
| `AreUnitsSharedWithPlayerID(unitOwnerPlayerId: PlayerID, otherPlayerId: PlayerID): boolean` |  |
| `CanRepick(playerId: PlayerID): boolean` |  |
| `ClearKillsMatrix(playerId: PlayerID): void` |  |
| `ClearLastHitMultikill(playerId: PlayerID): void` |  |
| `ClearLastHitStreak(playerId: PlayerID): void` |  |
| `ClearPlayer(playerId: PlayerID): void` |  |
| `ClearRawPlayerDamageMatrix(playerId: PlayerID): void` |  |
| `ClearStreak(playerId: PlayerID): void` |  |
| `GetAegisPickups(playerId: PlayerID): number` |  |
| `GetAssists(playerId: PlayerID): number` |  |
| `GetBroadcasterChannel(playerId: PlayerID): number` |  |
| `GetBroadcasterChannelSlot(playerId: PlayerID): number` |  |
| `GetClaimedDenies(playerId: PlayerID): number` |  |
| `GetClaimedFarm(playerId: PlayerID, onlyEarned: boolean): number` |  |
| `GetClaimedMisses(playerId: PlayerID): number` |  |
| `GetConnectionState(playerId: PlayerID): DOTAConnectionState_t` |  |
| `GetCreepDamageTaken(playerId: PlayerID, total: boolean): number` |  |
| `GetCustomBuybackCooldown(playerId: PlayerID): number` |  |
| `GetCustomBuybackCost(playerId: PlayerID): number` |  |
| `GetCustomTeamAssignment(playerId: PlayerID): number` | Get the current custom team assignment for this player. |
| `GetDamageDoneToHero(playerId: PlayerID, victimId: PlayerID): number` |  |
| `GetDeaths(playerId: PlayerID): number` |  |
| `GetDenies(playerId: PlayerID): number` |  |
| `GetEventGameUpgrades(playerId: PlayerID): object` | (nPlayerID). |
| `GetEventPointsForPlayerID(playerId: PlayerID): number` |  |
| `GetEventPremiumPoints(playerId: PlayerID): number` |  |
| `GetEventRanks(playerId: PlayerID): unknown` |  |
| `GetGold(playerId: PlayerID): number` |  |
| `GetGoldLostToDeath(playerId: PlayerID): number` |  |
| `GetGoldPerMin(playerId: PlayerID): number` |  |
| `GetGoldSpentOnBuybacks(playerId: PlayerID): number` |  |
| `GetGoldSpentOnConsumables(playerId: PlayerID): number` |  |
| `GetGoldSpentOnItems(playerId: PlayerID): number` |  |
| `GetGoldSpentOnSupport(playerId: PlayerID): number` |  |
| `GetHealing(playerId: PlayerID): number` |  |
| `GetHeroDamageTaken(playerId: PlayerID, total: boolean): number` |  |
| `GetKills(playerId: PlayerID): number` |  |
| `GetKillsDoneToHero(playerId: PlayerID, victimId: PlayerID): number` |  |
| `GetLabyrinthEventGameHeroUnlocks(playerId: PlayerID): object` | (nPlayerID). |
| `GetLastHitMultikill(playerId: PlayerID): number` |  |
| `GetLastHits(playerId: PlayerID): number` |  |
| `GetLastHitStreak(playerId: PlayerID): number` |  |
| `GetLevel(playerId: PlayerID): number` |  |
| `GetLiveSpectatorTeam(playerId: PlayerID): DOTATeam_t \| -1` |  |
| `GetMisses(playerId: PlayerID): number` |  |
| `GetNearbyCreepDeaths(playerId: PlayerID): number` |  |
| `GetNetworkedEventActionClaimCount(playerId: PlayerID, eventId: number, unActionId: number): number` |  |
| `GetNetworkedEventActionClaimCountByName(playerId: PlayerID, eventId: number, actionName: string): number` |  |
| `GetNetWorth(playerId: PlayerID): number` |  |
| `GetNthCourierForTeam(courierIndex: number, teamNumber: DOTATeam_t): CDOTA_Unit_Courier \| undefined` |  |
| `GetNthPlayerIDOnTeam(teamNumber: DOTATeam_t, nthPlayer: number): PlayerID` |  |
| `GetNumConnectedHumanPlayers(): number` | Players on a valid team (radiant, dire, or custom*) who haven't abandoned the<br>game. |
| `GetNumConsumablesPurchased(playerId: PlayerID): number` |  |
| `GetNumCouriersForTeam(teamNumber: DOTATeam_t): number` |  |
| `GetNumItemsPurchased(playerId: PlayerID): number` |  |
| `GetPartyID(playerId: PlayerID): Uint64` |  |
| `GetPlayer(playerId: PlayerID): CDOTAPlayerController \| undefined` | Returns player entity for a player with specified id. Player entity represents<br>a single connection, so a different entity might be returned. When player is<br>disconnected nil would be returned. |
| `GetPlayerCount(): number` | Includes spectators and players not assigned to a team. |
| `GetPlayerCountForTeam(team: DOTATeam_t): number` |  |
| `GetPlayerLoadedCompletely(playerId: PlayerID): boolean` |  |
| `GetPlayerName(playerId: PlayerID): string` |  |
| `GetPreferredCourierForPlayer(playerId: PlayerID): object` |  |
| `GetRawPlayerDamage(playerId: PlayerID): number` |  |
| `GetReliableGold(playerId: PlayerID): number` |  |
| `GetRespawnSeconds(playerId: PlayerID): number` |  |
| `GetRoshanKills(playerId: PlayerID): number` |  |
| `GetRunePickups(playerId: PlayerID): number` |  |
| `GetSelectedHeroEntity(playerId: PlayerID): CDOTA_BaseNPC_Hero \| undefined` |  |
| `GetSelectedHeroID(playerId: PlayerID): number` |  |
| `GetSelectedHeroName(playerId: PlayerID): string` |  |
| `GetSteamAccountID(playerId: PlayerID): number` |  |
| `GetSteamID(playerId: PlayerID): Uint64` | Get the 64 bit steam ID for a given player. |
| `GetStreak(playerId: PlayerID): number` |  |
| `GetStuns(playerId: PlayerID): number` |  |
| `GetTeam(playerId: PlayerID): DOTATeam_t` |  |
| `GetTeam(): never` | **Deprecated:** Added for compatibility with CBaseEntity. Invalid at the runtime.<br> |
| `GetTeamKills(team: DOTATeam_t): number` |  |
| `GetTeamPlayerCount(): number` | (Deprecated: use GetNumConnectedHumanPlayers) Players on a valid team (radiant,<br>dire, or custom*) who haven't abandoned the game. |
| `GetTimeOfLastConsumablePurchase(playerId: PlayerID): number` |  |
| `GetTimeOfLastDeath(playerId: PlayerID): number` |  |
| `GetTimeOfLastItemPurchase(playerId: PlayerID): number` |  |
| `GetTotalEarnedGold(playerId: PlayerID): number` |  |
| `GetTotalEarnedXP(playerId: PlayerID): number` |  |
| `GetTotalGoldSpent(playerId: PlayerID): number` |  |
| `GetTowerDamageTaken(playerId: PlayerID, total: boolean): number` |  |
| `GetTowerKills(playerId: PlayerID): number` |  |
| `GetUnitShareMaskForPlayer(playerId: PlayerID, otherPlayerId: PlayerID): number` |  |
| `GetUnreliableGold(playerId: PlayerID): number` |  |
| `GetXPPerMin(playerId: PlayerID): number` |  |
| `HasCustomGameTicketForPlayerID(playerId: PlayerID): boolean` | Does this player have a custom game ticket for this game? |
| `HasRandomed(playerId: PlayerID): boolean` |  |
| `HasSelectedHero(playerId: PlayerID): boolean` |  |
| `HasSetNetworkedEventActionClaimCount(): boolean` |  |
| `HaveAllPlayersJoined(): boolean` |  |
| `IncrementAssists(playerId: PlayerID, victimId: PlayerID): void` |  |
| `IncrementClaimedDenies(playerId: PlayerID, value: number): void` |  |
| `IncrementClaimedMisses(playerId: PlayerID, value: number): void` |  |
| `IncrementDeaths(playerId: PlayerID, killerId: PlayerID): void` |  |
| `IncrementDenies(playerId: PlayerID, value: number): void` |  |
| `IncrementKills(playerId: PlayerID, victimId: PlayerID): void` |  |
| `IncrementLastHitMultikill(playerId: PlayerID, count: number): void` |  |
| `IncrementLastHits(playerId: PlayerID, count: number): void` |  |
| `IncrementLastHitStreak(playerId: PlayerID, count: number): void` |  |
| `IncrementMisses(playerId: PlayerID, value: number): void` |  |
| `IncrementNearbyCreepDeaths(playerId: PlayerID, creeps: number): void` |  |
| `IncrementStreak(playerId: PlayerID, count: number): void` |  |
| `IncrementTotalEarnedXP(playerId: PlayerID, xp: number, reason: EDOTA_ModifyXP_Reason): void` |  |
| `IsBroadcaster(playerId: PlayerID): boolean` |  |
| `IsDisableHelpSetForPlayerID(playerId: PlayerID, otherPlayerId: PlayerID): boolean` |  |
| `IsFakeClient(playerId: PlayerID): boolean` |  |
| `IsHeroSelected(heroname: string, ignoreUnrevealedPick: boolean): boolean` |  |
| `IsHeroSharedWithPlayerID(unitOwnerPlayerId: PlayerID, otherPlayerId: PlayerID): boolean` |  |
| `IsValidPlayer(playerId: number): playerId is PlayerID` |  |
| `IsValidPlayerID(playerId: number): playerId is PlayerID` |  |
| `IsValidTeamPlayer(playerId: number): playerId is PlayerID` |  |
| `IsValidTeamPlayerID(playerId: number): playerId is PlayerID` |  |
| `ModifyGold(playerId: PlayerID, goldChange: number, reliable: boolean, reason: EDOTA_ModifyGold_Reason): number` |  |
| `NumPlayers(): number` |  |
| `NumTeamPlayers(): number` |  |
| `RecordConsumableAbilityChargeChange( playerId: PlayerID, itemDefinitionIndex: number, chargeIncrementOrDecrement: number, ): void` | Increment or decrement consumable charges (nPlayerID, item_definition_index,<br>nChargeIncrementOrDecrement). |
| `RecordEventActionGrant( playerId: PlayerID, event: number, unActionId: number, unAudit: number, unQuantity: number, unAuditData: number, ): void` |  |
| `RecordEventActionGrantForPrimaryEvent( playerId: PlayerID, actionName: string, unAudit: number, unQuantity: number, unAuditData: number, ): void` |  |
| `ReplaceHeroWith(playerId: PlayerID, heroClass: string, gold: number, xp: number): CDOTA_BaseNPC_Hero` | Replaces the player's hero with a new one of the specified class, gold and XP. |
| `ReplaceHeroWithNoTransfer(playerId: PlayerID, heroClass: string, gold: number, xp: number): object` | Replaces the player's hero with a new one of the specified class, gold and XP,<br>without transferring items/abilities if same hero. |
| `ResetBuybackCostTime(playerId: PlayerID): void` |  |
| `ResetTotalEarnedGold(playerId: PlayerID): void` |  |
| `SetBuybackCooldownTime(playerId: PlayerID, buybackCooldown: number): void` |  |
| `SetBuybackGoldLimitTime(playerId: PlayerID, buybackCooldown: number): void` |  |
| `SetCameraTarget(playerId: PlayerID, target: CBaseEntity \| undefined): void` | Force the given player's camera to follow the given entity. |
| `SetCanRepick(playerId: PlayerID, canRepick: boolean): void` |  |
| `SetCustomBuybackCooldown(playerId: PlayerID, cooldownTime: number): void` | Set the buyback cooldown for this player. |
| `SetCustomBuybackCost(playerId: PlayerID, goldCost: number): void` | Set the buyback cost for this player. |
| `SetCustomIntParam(playerId: PlayerID, param: number): void` |  |
| `SetCustomPlayerColor(playerId: PlayerID, r: number, g: number, b: number): void` | Set custom color for player. |
| `SetCustomTeamAssignment(playerId: PlayerID, teamAssignment: DOTATeam_t): void` | Set custom team assignment for this player. |
| `SetGold(playerId: PlayerID, gold: number, reliable: boolean): void` |  |
| `SetHasRandomed(playerId: PlayerID): void` |  |
| `SetLastBuybackTime(playerId: PlayerID, lastBuybackTime: number): void` |  |
| `SetOverrideSelectionEntity(playerId: PlayerID, entity: CDOTA_BaseNPC): void` | Set the forced selection entity for a player. |
| `SetUnitShareMaskForPlayer(playerId: PlayerID, otherPlayerId: PlayerID, flag: number, state: boolean): void` |  |
| `SpendGold(playerId: PlayerID, cost: number, reason: EDOTA_ModifyGold_Reason): void` |  |
| `UpdateTeamSlot(playerId: PlayerID, teamNumber: DOTATeam_t, desiredSlot: number): void` |  |
| `WhoSelectedHero(heroFilename: string, ignoreUnrevealedPick: boolean): PlayerID` |  |

### CDOTA_ShopTrigger

Extends `CBaseTrigger`

**Methods**

| Method | Description |
| --- | --- |
| `GetShopType(): DOTA_SHOP_TYPE` | Get the DOTA_SHOP_TYPE. |
| `SetShopType(shopType: DOTA_SHOP_TYPE): void` | Set the DOTA_SHOP_TYPE. |

### CDOTA_SimpleObstruction

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `IsEnabled(): boolean` | Returns whether the obstruction is currently active. |
| `SetEnabled(enabled: boolean, force: boolean): void` | Enable or disable the obstruction. |

### CDOTA_Unit_Courier

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `RespawnCourier(): void` | Respawn the courier. |
| `UpgradeCourier(level: number): void` | Upgrade the courier ( int param ) times. |

### CDOTA_Unit_CustomGameAnnouncer

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `SetServerAuthoritative(isServerAuthoritative: boolean): void` | Determines whether response criteria is matched on server or client. |

### CDOTA_Unit_CustomGameAnnouncerAghanim

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Description |
| --- | --- |
| `SetAnimation(animation: string): void` | Set the animation sequence for this entity. |
| `SetServerAuthoritative(isServerAuthoritative: boolean): void` | Determines whether response criteria is matched on server or client. |

### CDOTA_Unit_Nian

Extends `CDOTA_BaseNPC_Creature`

**Methods**

| Method | Description |
| --- | --- |
| `GetHorn(): object` | Is the Nian horn? |
| `GetTail(): object` | Is the Nian's tail broken? |
| `IsHornAlive(): boolean` | Is the Nian's horn broken? |
| `IsTailAlive(): boolean` | Is the Nian's tail broken? |

### CDOTA_Unit_Scout

Extends `CDOTA_BaseNPC`

_No members._

### CDOTABaseAbility

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `CanAbilityBeUpgraded(): boolean` |  |
| `CastAbility(): boolean` |  |
| `ContinueCasting(): boolean` |  |
| `CreateVisibilityNode(location: Vector, radius: number, duration: number): void` |  |
| `DecrementModifierRefCount(): void` |  |
| `EnableAbilityChargesOnTalentUpgrade(ability: object, talentName: string): void` |  |
| `EndChannel(interrupted: boolean): void` |  |
| `EndCooldown(): void` | Clear the cooldown remaining on this ability. |
| `ForceSetFrozenCooldown(value: number): void` |  |
| `GetAbilityChargeRestoreTime(level: number): number` |  |
| `GetAbilityDamage(): number` |  |
| `GetAbilityDamageType(): DAMAGE_TYPES` |  |
| `GetAbilityIndex(): number` |  |
| `GetAbilityKeyValues(): object` | Gets the key values definition for this ability. |
| `GetAbilityName(): string` | Returns the name of this ability.<br><br>**Availability:** `both` |
| `GetAbilityTargetFlags(): DOTA_UNIT_TARGET_FLAGS` |  |
| `GetAbilityTargetTeam(): DOTA_UNIT_TARGET_TEAM` |  |
| `GetAbilityTargetType(): DOTA_UNIT_TARGET_TYPE` |  |
| `GetAbilityType(): number` |  |
| `GetAltCastState(): boolean` | Gets the current Alt Cast State. |
| `GetAnimationIgnoresModelScale(): boolean` |  |
| `GetAOERadius(): number` |  |
| `GetAssociatedPrimaryAbilities(): string` |  |
| `GetAssociatedSecondaryAbilities(): string` |  |
| `GetAutoCastState(): boolean` |  |
| `GetBackswingTime(): number` |  |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR \| Uint64` | Always returns Uint64 at runtime, DOTA_ABILITY_BEHAVIOR is referenced only for<br>compatibility. |
| `GetBehaviorInt(): DOTA_ABILITY_BEHAVIOR` | Get ability behavior flags as an int for compatability.<br><br>**Availability:** `both` |
| `GetCaster(): CDOTA_BaseNPC` | Get the owner of this ability.<br><br>**Availability:** `both` |
| `GetCastPoint(): number` |  |
| `GetCastPointModifier(): number` | **Availability:** `both` |
| `GetCastRange(location: Vector \| undefined, target: CDOTA_BaseNPC \| undefined): number` | Gets the cast range of the ability. |
| `GetChannelledHealthCostPerSecond(level: number): number` |  |
| `GetChannelledManaCostPerSecond(level: number): number` |  |
| `GetChannelStartTime(): number` |  |
| `GetChannelTime(): number` |  |
| `GetCloneSource(): CDOTA_BaseNPC \| undefined` |  |
| `GetConceptRecipientType(): number` |  |
| `GetCooldown(level: number): number` | Get the cooldown duration for this ability at a given level, not the amount of<br>cooldown actually left. |
| `GetCooldownTime(): number` |  |
| `GetCooldownTimeRemaining(): number` |  |
| `GetCurrentAbilityCharges(): number` | The number of charges remaining on this ability.<br><br>**Availability:** `both` |
| `GetCursorPosition(): Vector` |  |
| `GetCursorTarget(): CDOTA_BaseNPC \| undefined` |  |
| `GetCursorTargetingNothing(): boolean` |  |
| `GetDuration(): number` |  |
| `GetEffectiveCastRange(location: Vector, target: object): number` | Gets the cast range of the ability, taking modifiers into account. |
| `GetEffectiveCooldown(level: number): number` |  |
| `GetEffectiveHealthCost(level: number): number` |  |
| `GetEffectiveManaCost(level: number): number` |  |
| `GetGoldCost(level: number): number` |  |
| `GetGoldCostForUpgrade(level: number): number` |  |
| `GetHealthCost(level: number): number` |  |
| `GetHeroLevelRequiredToUpgrade(): number` |  |
| `GetInitialAbilityCharges(level: number): number` |  |
| `GetIntrinsicModifierName(): string` |  |
| `GetLevel(): number` | Get the current level of the ability.<br><br>**Availability:** `both` |
| `GetLevelSpecialValueFor(name: string, level: number): number` | Gets a value from this ability's special value block for passed level.<br><br>**Availability:** `both` |
| `GetLevelSpecialValueNoOverride(name: string, level: number): number` | Gets a value from this ability's special value block for passed level, ignoring<br>MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL.<br><br>**Availability:** `both` |
| `GetManaCost(level: number): number` |  |
| `GetMaxAbilityCharges(level: number): number` |  |
| `GetMaxLevel(): number` |  |
| `GetModifierValue(): number` |  |
| `GetModifierValueBonus(): number` |  |
| `GetPlaybackRateOverride(): number` |  |
| `GetSharedCooldownName(): string` |  |
| `GetSpecialValueFor(name: string): number` | Gets a value from this ability's special value block for its current level.<br><br>**Availability:** `both` |
| `GetStolenActivityModifier(): string` |  |
| `GetToggleState(): boolean` | Whether or not this ability is toggled.<br><br>**Availability:** `both` |
| `GetUpgradeRecommended(): boolean` |  |
| `HeroXPChange(xp: number): boolean` |  |
| `IncrementModifierRefCount(): void` |  |
| `IsActivated(): boolean` |  |
| `IsAttributeBonus(): boolean` |  |
| `IsChanneling(): boolean` | Returns whether the ability is currently channeling. |
| `IsCooldownReady(): boolean` |  |
| `IsCosmetic(entity: CBaseEntity): boolean` |  |
| `IsFullyCastable(): boolean` | Returns whether the ability can be cast. |
| `IsHidden(): boolean` |  |
| `IsHiddenAsSecondaryAbility(): boolean` |  |
| `IsHiddenWhenStolen(): boolean` |  |
| `IsInAbilityPhase(): boolean` | Returns whether the ability is currently casting. |
| `IsItem(): this is CDOTA_Item` | Whether or not this ability is an item.<br><br>**Availability:** `both` |
| `IsOwnersGoldEnough(issuerPlayerId: PlayerID): boolean` |  |
| `IsOwnersGoldEnoughForUpgrade(): boolean` |  |
| `IsOwnersManaEnough(): boolean` |  |
| `IsPassive(): boolean` |  |
| `IsRefreshable(): boolean` |  |
| `IsSharedWithTeammates(): boolean` |  |
| `IsStealable(): boolean` |  |
| `IsStolen(): boolean` |  |
| `IsToggle(): boolean` |  |
| `IsTrained(): boolean` |  |
| `MarkAbilityButtonDirty(): void` | Mark the ability button for this ability as needing a refresh. |
| `NumModifiersUsingAbility(): number` |  |
| `OnAbilityPhaseInterrupted(): void` |  |
| `OnAbilityPhaseStart(): boolean` |  |
| `OnAbilityPinged(playerId: PlayerID, ctrlHeld: boolean): void` |  |
| `OnChannelFinish(interrupted: boolean): void` |  |
| `OnChannelThink(interval: number): void` |  |
| `OnHeroCalculateStatBonus(): void` |  |
| `OnHeroLevelUp(): void` |  |
| `OnOwnerDied(): void` |  |
| `OnOwnerSpawned(): void` |  |
| `OnSpellStart(): void` |  |
| `OnToggle(): void` |  |
| `OnUpgrade(): void` |  |
| `PayGoldCost(): void` |  |
| `PayGoldCostForUpgrade(): void` |  |
| `PayHealthCost(): void` |  |
| `PayManaCost(): void` |  |
| `PlaysDefaultAnimWhenStolen(): boolean` |  |
| `ProcsMagicStick(): boolean` |  |
| `RefCountsModifiers(): boolean` |  |
| `RefreshCharges(): void` |  |
| `RefreshIntrinsicModifier(): void` |  |
| `RefundHealthCost(): void` |  |
| `RefundManaCost(): void` |  |
| `RequiresFacing(): boolean` |  |
| `ResetToggleOnRespawn(): boolean` |  |
| `SetAbilityIndex(index: number): void` |  |
| `SetActivated(activated: boolean): void` |  |
| `SetAltCastState(altCastEnabled: boolean): void` | Set Alt Cast State to a specific value (true for on, false for off). |
| `SetChanneling(channeling: boolean): void` |  |
| `SetCurrentAbilityCharges(charges: number): void` |  |
| `SetFrozenCooldown(frozenCooldown: boolean): void` |  |
| `SetHidden(hidden: boolean): void` |  |
| `SetInAbilityPhase(inAbilityPhase: boolean): void` |  |
| `SetLevel(level: number): void` | Sets the level of this ability. |
| `SetOverrideCastPoint(castPoint: number): void` |  |
| `SetRefCountsModifiers(refCounts: boolean): void` |  |
| `SetStealable(stealable: boolean): void` |  |
| `SetStolen(stolen: boolean): void` |  |
| `SetUpgradeRecommended(upgradeRecommended: boolean): void` |  |
| `ShouldAltCast(): boolean` | This is what the Alt Cast State of the ability was when it was initially cast.<br>Updated during Execute Orders. |
| `ShouldUseResources(): boolean` |  |
| `SpeakAbilityConcept(concept: number): void` |  |
| `SpeakTrigger(): unknown` |  |
| `StartCooldown(cooldown: number): void` |  |
| `ToggleAbility(): void` |  |
| `ToggleAltCast(): void` | Toggle the Alt Cast State of an Ability. |
| `ToggleAutoCast(): void` |  |
| `UpgradeAbility(supressSpeech: boolean): void` |  |
| `UseResources(mana: boolean, useHealth: boolean, gold: boolean, cooldown: boolean): void` |  |

### CDOTABaseGameMode

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AddAbilityUpgradeToWhitelist(abilityName: string): void` | Const char* pszAbilityName. |
| `AddItemToCustomShop(itemName: string, shopName: string, category: string): void` | Add an item to purchase at a custom shop. |
| `AddRealTimeCombatAnalyzerQuery( queryTable: object, player: CDOTAPlayerController, queryName: string, ): CombatAnalyzerQueryID` | Begin tracking a sequence of events using the real time combat analyzer. |
| `AllocateFowBlockerRegion( minX: number, minY: number, maxX: number, maxY: number, gridSize: number, ): CFoWBlockerRegion` | Allocates an entity which can be used by custom games to control FoW occlusion<br>volumes. |
| `AreWeatherEffectsDisabled(): boolean` | Get if weather effects are disabled on the client. |
| `ClearBountyRunePickupFilter(): void` | Clear the script filter that controls bounty rune pickup behavior. |
| `ClearDamageFilter(): void` | Clear the script filter that controls how a unit takes damage. |
| `ClearExecuteOrderFilter(): void` | Clear the script filter that controls when a unit picks up an item. |
| `ClearHealingFilter(): void` | Clear the script filter that controls how a unit heals. |
| `ClearItemAddedToInventoryFilter(): void` | Clear the script filter that controls the item added to inventory filter. |
| `ClearModifierGainedFilter(): void` | Clear the script filter that controls the modifier filter. |
| `ClearModifyExperienceFilter(): void` | Clear the script filter that controls how hero experience is modified. |
| `ClearModifyGoldFilter(): void` | Clear the script filter that controls how hero gold is modified. |
| `ClearRuneSpawnFilter(): void` | Clear the script filter that controls what rune spawns. |
| `ClearTrackingProjectileFilter(): void` | Clear the script filter that controls when tracking projectiles are launched. |
| `DisableClumpingBehaviorByDefault(disabled: boolean): void` | Disable npc_dota_creature clumping behavior by default. |
| `DisableHudFlip(disable: boolean): void` | Use to disable hud flip for this mod. |
| `EnableAbilityUpgradeWhitelist(enabled: boolean): void` | Bool bEnabled. |
| `GetAlwaysShowPlayerInventory(): boolean` | Show the player hero's inventory in the HUD, regardless of what unit is<br>selected. |
| `GetAlwaysShowPlayerNames(): boolean` | Get whether player names are always shown, regardless of client setting. |
| `GetAnnouncerDisabled(): boolean` | Are in-game announcers disabled? |
| `GetAnnouncerGameModeAnnounceDisabled(): boolean` | Is the announcer announcing the mode / saying Choose Your Hero on start of<br>custom games disabled? |
| `GetCameraDistanceOverride(): number` | Set a different camera distance; dota default is 1134. |
| `GetCustomAttributeDerivedStatValue(derivedStatType: AttributeDerivedStats): number` | Get current derived stat value constant. |
| `GetCustomBackpackCooldownPercent(): number` | Get the current rate cooldown ticks down for items in the backpack. |
| `GetCustomBackpackSwapCooldown(): number` | Get the current custom backpack swap cooldown. |
| `GetCustomBuybackCooldownEnabled(): boolean` | Turns on capability to define custom buyback cooldowns. |
| `GetCustomBuybackCostEnabled(): boolean` | Turns on capability to define custom buyback costs. |
| `GetCustomDireScore(): number` | Get the topbar score display value for dire. |
| `GetCustomGlyphCooldown(): number` | Get the current custom glyph cooldown. |
| `GetCustomHeroMaxLevel(): number` | Allows definition of the max level heroes can achieve (default is 25). |
| `GetCustomRadiantScore(): number` | Get the topbar score display value for radiant. |
| `GetCustomScanCooldown(): number` | Get the current custom scan cooldown. |
| `GetDaynightCycleAdvanceRate(): number` | Get the rate at which the day/night cycle advances (1.0 = default). |
| `GetEventGameSeed(): number` | Get the Game Seed passed from the GC. |
| `GetEventWindowStartTime(): number` | Get the Event Window Start Time passed from the GC. |
| `GetFixedRespawnTime(): number` | Gets the fixed respawn time. |
| `GetFogOfWarDisabled(): boolean` | Turn the fog of war on or off. |
| `GetGoldSoundDisabled(): boolean` | Turn the sound when gold is acquired off/on. |
| `GetHUDVisible(element: number): boolean` | Returns the HUD element visibility. |
| `GetMaximumAttackSpeed(): number` | Get the maximum attack speed for units. |
| `GetMinimumAttackSpeed(): number` | Get the minimum attack speed for units. |
| `GetRecommendedItemsDisabled(): boolean` | Turn the panel for showing recommended items at the shop off/on. |
| `GetRespawnTimeScale(): number` | Returns the scale applied to non-fixed respawn times. |
| `GetStashPurchasingDisabled(): boolean` | Turn purchasing items to the stash off/on. If purchasing to the stash is off<br>the player must be at a shop to purchase items. |
| `GetStickyItemDisabled(): boolean` | Hide the sticky item in the quickbuy. |
| `GetTopBarTeamValuesOverride(): boolean` | Override the values of the team values on the top game bar. |
| `GetTopBarTeamValuesVisible(): boolean` | Turning on/off the team values on the top game bar. |
| `GetTowerBackdoorProtectionEnabled(): boolean` | Gets whether tower backdoor protection is enabled or not. |
| `GetUseCustomHeroLevels(): boolean` | Are custom-defined XP values for hero level ups in use? |
| `GetWaterRuneLastSpawnTime(): number` | Gets the time from game start during which water runes spawn. |
| `IsAbilityUpgradeWhitelisted(abilityName: string): boolean` | Const char* pszAbilityName. |
| `IsBuybackEnabled(): boolean` | Enables or disables buyback completely. |
| `IsDaynightCycleDisabled(): boolean` | Is the day/night cycle disabled? |
| `ListenForQueryFailed<TContext extends {}>( func: (this: TContext, result: CombatAnalyzerQueryResult) => void, context: TContext, ): void` | Set function and context for real time combat analyzer query failed. |
| `ListenForQueryProgressChanged<TContext extends {}>( func: (this: TContext, result: CombatAnalyzerQueryResult) => void, context: TContext, ): void` | Set function and context for real time combat analyzer query progress changed. |
| `ListenForQuerySucceeded<TContext extends {}>( func: (this: TContext, result: CombatAnalyzerQueryResult) => void, context: TContext, ): void` | Set function and context for real time combat analyzer query succeeded. |
| `RemoveAbilityUpgradeFromWhitelist(abilityName: string): void` | Const char* pszAbilityName. |
| `RemoveItemFromCustomShop(itemName: string, shopName: string): void` | Remove an item to purchase at a custom shop. |
| `RemoveRealTimeCombatAnalyzerQuery(queryId: CombatAnalyzerQueryID): void` | Stop tracking a combat analyzer query. |
| `SetAbilityTuningValueFilter<TContext extends {}>( filterFunc: (this: TContext, event: AbilityTuningValueFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the tuning values that abilities use. (Modify<br>the table and Return true to use new values, return false to use the old<br>values). |
| `SetAllowNeutralItemDrops(enabled: boolean): void` | If set to true, neutral items will be dropped on killing neutral monsters.<br>Otherwise nothing will be dropped. |
| `SetAlwaysShowPlayerInventory(alwaysShow: boolean): void` | Show the player hero's inventory in the HUD, regardless of what unit is<br>selected. |
| `SetAlwaysShowPlayerNames(enabled: boolean): void` | Set whether player names are always shown, regardless of client setting. |
| `SetAnnouncerDisabled(disabled: boolean): void` | Mutes the in-game announcer. |
| `SetAnnouncerGameModeAnnounceDisabled(disabled: boolean): void` | Disables the announcer announcing the mode / saying Choose Your Hero on start<br>of custom games. |
| `SetBotsAlwaysPushWithHuman(alwaysPush: boolean): void` | Set if the bots should try their best to push with a human player. |
| `SetBotsInLateGame(lateGame: boolean): void` | Set if bots should enable their late game behavior. |
| `SetBotsMaxPushTier(maxTier: number): void` | Set the max tier of tower that bots want to push. (-1 to disable). |
| `SetBotThinkingEnabled(enabled: boolean): void` | Enables/Disables bots in custom games. Note: this will only work with default<br>heroes in the dota map. |
| `SetBountyRunePickupFilter<TContext extends {}>( filterFunc: (this: TContext, event: BountyRunePickupFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a bounty rune is picked up.<br>(Modify the table and Return true to use new values, return false to cancel the<br>event). |
| `SetBountyRuneSpawnInterval(interval: number): void` | Set bounty rune spawn rate. |
| `SetBuybackEnabled(enabled: boolean): void` | Enables or disables buyback completely. |
| `SetCameraDistanceOverride(cameraDistanceOverride: number): void` | Set a different camera distance; dota default is 1134. |
| `SetCameraSmoothCountOverride(smoothCount: number): void` | Set a different camera smooth count; dota default is 8. |
| `SetCameraZRange(minZ: number, maxZ: number): void` | Sets the camera Z range. |
| `SetCanSellAnywhere(allow: boolean): void` | Bool bAllow. |
| `SetCustomAttributeDerivedStatValue(statType: AttributeDerivedStats, newValue: number): void` | Modify derived stat value constants. |
| `SetCustomBackpackCooldownPercent(percent: number): void` | Set the rate cooldown ticks down for items in the backpack. |
| `SetCustomBackpackSwapCooldown(cooldown: number): void` | Set a custom cooldown for swapping items into the backpack. |
| `SetCustomBuybackCooldownEnabled(enabled: boolean): void` | Turns on capability to define custom buyback cooldowns. |
| `SetCustomBuybackCostEnabled(enabled: boolean): void` | Turns on capability to define custom buyback costs. |
| `SetCustomDireScore(score: number): void` | Sets the topbar score display value for dire. |
| `SetCustomGameForceHero(heroName: string): void` | Force all players to use the specified hero and disable the normal hero<br>selection process. Must be used before hero selection. |
| `SetCustomGlyphCooldown(cooldown: number): void` | Set a custom cooldown for team Glyph ability. |
| `SetCustomHeroMaxLevel(maxLevel: number): void` | Allows definition of the max level heroes can achieve (default is 25). |
| `SetCustomRadiantScore(score: number): void` | Sets the topbar score display value for radiant. |
| `SetCustomScanCooldown(cooldown: number): void` | Set a custom cooldown for team Scan ability. |
| `SetCustomScanMaxCharges(maxCharges: number): void` | Set a custom max charges for team Scan ability. |
| `SetCustomTerrainWeatherEffect(effectName: string): void` | Set the effect used as a custom weather effect, when units are on non-default<br>terrain, in this mode. |
| `SetCustomXPRequiredToReachNextLevel(table: Record<number, number>): void` | Allows definition of a table of hero XP values.<br><br>Requires `SetUseCustomHeroLevels` to be enabled. |
| `SetDamageFilter<TContext extends {}>( filterFunc: (this: TContext, event: DamageFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a unit takes damage. (Modify<br>the table and Return true to use new values, return false to cancel the event). |
| `SetDaynightCycleAdvanceRate(rate: number): void` | Sets the rate at which the day/night cycle advances (1.0 = default). |
| `SetDaynightCycleDisabled(disable: boolean): void` | Enable or disable the day/night cycle. |
| `SetDeathOverlayDisabled(disabled: boolean): void` | Specify whether the full screen death overlay effect plays when the selected<br>hero dies. |
| `SetDeathTipsDisabled(disabled: boolean): void` | Disables chat tips on death. |
| `SetDefaultStickyItem(item: string): void` | Sets the default sticky item in the quickbuy. |
| `SetDraftingBanningTimeOverride(value: number): void` | Set drafting hero banning time. |
| `SetDraftingHeroPickSelectTimeOverride(value: number): void` | Set drafting hero pick time. |
| `SetExecuteOrderFilter<TContext extends {}>( filterFunc: (this: TContext, event: ExecuteOrderFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a unit picks up an item.<br>(Modify the table and Return true to use new values, return false to cancel the<br>event). |
| `SetFixedRespawnTime(fixedRespawnTime: number): void` | Set a fixed delay for all players to respawn after. |
| `SetFogOfWarDisabled(disabled: boolean): void` | Turn the fog of war on or off. |
| `SetForcedHeroCapOnReset(cap: number): void` | Caps the number of players spawned when the game is reset. Used in tutorials<br>where players are spawned in the script. |
| `SetForcedHUDSkin(value: string): void` | Specify a HUD skin that is forced on for this game mode. |
| `SetForceRightClickAttackDisabled(disabled: boolean): void` | Prevent users from using the right click deny setting. |
| `SetFountainConstantManaRegen(constantManaRegen: number): void` | Set the constant rate that the fountain will regen mana. (-1 for default). |
| `SetFountainPercentageHealthRegen(percentageHealthRegen: number): void` | Set the percentage rate that the fountain will regen health. (-1 for default). |
| `SetFountainPercentageManaRegen(percentageManaRegen: number): void` | Set the percentage rate that the fountain will regen mana. (-1 for default). |
| `SetFreeCourierModeEnabled(enabled: boolean): void` | If set to true, enable 7.23 free courier mode. |
| `SetFriendlyBuildingMoveToEnabled(enabled: boolean): void` | Allows clicks on friendly buildings to be handled normally. |
| `SetGiveFreeTPOnDeath(give: boolean): void` | Bool bGive. |
| `SetGoldSoundDisabled(disabled: boolean): void` | Turn the sound when gold is acquired off/on. |
| `SetHealingFilter<TContext extends {}>( filterFunc: (this: TContext, event: HealingFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a unit heals. (Modify the<br>table and Return true to use new values, return false to cancel the event). |
| `SetHudCombatEventsDisabled(disabled: boolean): void` | Specify whether the default combat events will show in the HUD. |
| `SetHUDVisible(hudElement: DOTAHUDVisibility_t, visible: boolean): void` | Set the HUD element visibility. |
| `SetInnateMeleeDamageBlockAmount(amount: number): void` | Set the amount blocked innately by melee heroes. |
| `SetInnateMeleeDamageBlockPercent(percent: number): void` | Set the percent chance a melee hero will innately block damage. |
| `SetInnateMeleeDamageBlockPerLevelAmount(perLevelAmount: number): void` | Set the amount innately blocked by melee heroes gained per level. |
| `SetItemAddedToInventoryFilter<TContext extends {}>( filterFunc: (this: TContext, event: ItemAddedToInventoryFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control what happens to items that are added to an<br>inventory, return false to cancel the event. |
| `SetKillableTombstones(enabled: boolean): void` | Set whether tombstones can be channeled to be removed by enemy heroes. |
| `SetKillingSpreeAnnouncerDisabled(disabled: boolean): void` | Mutes the in-game killing spree announcer. |
| `SetLoseGoldOnDeath(enabled: boolean): void` | Use to disable gold loss on death. |
| `SetLuaGameMode(script: object): void` |  |
| `SetMaximumAttackSpeed(maxSpeed: number): void` | Set the maximum attack speed for units. |
| `SetMinimumAttackSpeed(minSpeed: number): void` | Set the minimum attack speed for units. |
| `SetModifierGainedFilter<TContext extends {}>( filterFunc: (this: TContext, event: ModifierGainedFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control modifiers that are gained, return false to<br>destroy modifier. |
| `SetModifyExperienceFilter<TContext extends {}>( filterFunc: (this: TContext, event: ModifyExperienceFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a hero's experience is<br>modified. (Modify the table and Return true to use new values, return false to<br>cancel the event). |
| `SetModifyGoldFilter<TContext extends {}>( filterFunc: (this: TContext, event: ModifyGoldFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control the behavior when a hero's gold is modified.<br>(Modify the table and Return true to use new values, return false to cancel the<br>event). |
| `SetNeutralItemHideUndiscoveredEnabled(enable: boolean): void` | When enabled, undiscovered items in the neutral item stash are hidden. |
| `SetNeutralStashEnabled(enable: boolean): void` | Allow items to be sent to the neutral stash. |
| `SetNeutralStashTeamViewOnlyEnabled(enable: boolean): void` | When enabled, the all neutral items tab cannot be viewed. |
| `SetOverrideSelectionEntity(overrideEntity: CDOTA_BaseNPC \| undefined): void` | Set an override for the default selection entity, instead of each player's hero. |
| `SetPauseEnabled(enabled: boolean): void` | Set pausing enabled/disabled. |
| `SetPlayerHeroAvailabilityFiltered(filter: boolean): void` | Bool bFilter. |
| `SetPowerRuneSpawnInterval(interval: number): void` | Set power rune spawn rate. |
| `SetRandomHeroBonusItemGrantDisabled(disabled: boolean): void` | Disables bonus items for randoming a hero. |
| `SetRecommendedItemsDisabled(disabled: boolean): void` | Turn the panel for showing recommended items at the shop off/on. |
| `SetRemoveIllusionsOnDeath(remove: boolean): void` | Make it so illusions are immediately removed upon death, rather than sticking<br>around for a few seconds. |
| `SetRespawnTimeScale(value: number): void` | Sets the scale applied to non-fixed respawn times. 1 = default DOTA respawn<br>calculations. |
| `SetRuneEnabled(rune: DOTA_RUNES, enabled: boolean): void` | Set if a given type of rune is enabled. |
| `SetRuneSpawnFilter<TContext extends {}>( filterFunc: (this: TContext, event: RuneSpawnFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control what rune spawns. (Modify the table and Return<br>true to use new values, return false to cancel the event). |
| `SetSelectionGoldPenaltyEnabled(enabled: boolean): void` | Enable/disable gold penalty for late picking. |
| `SetSendToStashEnabled(enable: boolean): void` | Allow items to be sent to the stash. |
| `SetStashPurchasingDisabled(disabled: boolean): void` | Turn purchasing items to the stash off/on. If purchasing to the stash is off<br>the player must be at a shop to purchase items. |
| `SetStickyItemDisabled(disabled: boolean): void` | Hide the sticky item in the quickbuy. |
| `SetTopBarTeamValue(team: DOTATeam_t, value: number): void` | Set the team values on the top game bar. |
| `SetTopBarTeamValuesOverride(override: boolean): void` | Override the values of the team values on the top game bar. |
| `SetTopBarTeamValuesVisible(visible: boolean): void` | Turning on/off the team values on the top game bar. |
| `SetTowerBackdoorProtectionEnabled(enabled: boolean): void` | Enables/Disables tower backdoor protection. |
| `SetTPScrollSlotItemOverride(itemName: string): void` | Sets the item which goes in the TP scroll slot. |
| `SetTrackingProjectileFilter<TContext extends {}>( filterFunc: (this: TContext, event: TrackingProjectileFilterEvent) => boolean, context: TContext, ): void` | Set a filter function to control when tracking projectiles are launched.<br>(Modify the table and Return true to use new values, return false to cancel the<br>event). |
| `SetUnseenFogOfWarEnabled(enabled: boolean): void` | Enable or disable unseen fog of war. When enabled parts of the map the player<br>has never seen will be completely hidden by fog of war. |
| `SetUseCustomHeroLevels(enabled: boolean): void` | Turn on custom-defined XP values for hero level ups.  The table should be<br>defined before switching this on. |
| `SetUseDefaultDOTARuneSpawnLogic(enabled: boolean): void` | If set to true, use current rune spawn rules.  Either setting respects custom<br>spawn intervals. |
| `SetUseTurboCouriers(enabled: boolean): void` | Enables or disables turbo couriers. |
| `SetWaterRuneLastSpawnTime(value: number): void` | Sets the time from game start during which water runes spawn. |
| `SetWeatherEffectsDisabled(disable: boolean): void` | Set if weather effects are disabled. |
| `SetXPRuneSpawnInterval(interval: number): void` | Set xp rune spawn rate. |
| `ShouldGiveFreeTPOnDeath(): boolean` |  |

### CDOTAGameManager

**Methods**

| Method | Description |
| --- | --- |
| `GetHeroDataByName_Script(heroName: string): object` | Get the hero unit.<br><br>**Availability:** `both` |
| `GetHeroIDByName(heroName: string): number` | Get the hero ID given the hero name.<br><br>**Availability:** `both` |
| `GetHeroLocTokenByID(arg1: number): string` | Get the localization token for the given hero ID.<br><br>**Availability:** `both` |
| `GetHeroNameByID(heroId: number): string` | Get the hero name given a hero ID.<br><br>**Availability:** `both` |
| `GetHeroNameForUnitName(unitName: string): string` | Get the hero name given a unit name.<br><br>**Availability:** `both` |
| `GetHeroUnitNameByID(heroId: number): string` | Get the hero unit name given the hero ID.<br><br>**Availability:** `both` |

### CDOTAGameRules

**Methods**

| Method | Description |
| --- | --- |
| `AddBotPlayerWithEntityScript( heroName: string, playerName: string, team: DOTATeam_t, entityScript: string, arg5: boolean, ): CDOTA_BaseNPC_Hero \| undefined` | Spawn a bot player of the passed hero name, player name, and team.<br><br>**Parameters:**<br><br>- entityScript Path to a script file executed in the context of spawned<br>                    hero entity.<br> |
| `AddEventMetadataLeaderboardEntry( nameSuffix: string, stars: number, maxStars: number, extraData1: number, extraData2: number, extraData3: number, extraData4: number, extraData5: number, extraData6: number, ): boolean` | Event-only. |
| `AddEventMetadataLeaderboardEntryRawScore( nameSuffix: string, score: number, extraData1: number, extraData2: number, extraData3: number, extraData4: number, extraData5: number, extraData6: number, ): boolean` | Event-only. |
| `AddHeroIDToBlacklist(arg1: number): void` | Add the hero ID to the hero blacklist if it is not already present. |
| `AddHeroIDToWhitelist(arg1: number): void` | Add the hero ID to the hero whitelist if it is not already present. |
| `AddHeroToBlacklist(arg1: string): void` | Add the hero to the hero blacklist if it is not already present. |
| `AddHeroToPlayerAvailability(arg1: number, arg2: number): void` | Adds hero of given ID to available heroes of player of given ID. |
| `AddHeroToWhitelist(arg1: string): void` | Add the hero to the hero whitelist if it is not already present. |
| `AddItemToWhiteList(itemName: string): void` | Add an item to the whitelist. |
| `AddMinimapDebugPoint( arg1: number, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, ): void` | Add a point on the minimap. |
| `AddMinimapDebugPointForTeam( arg1: number, arg2: Vector, arg3: number, arg4: number, arg5: number, arg6: number, arg7: number, arg8: number, ): void` | Add a point on the minimap for a specific team. |
| `BeginNightstalkerNight(duration: number): void` | Begin night stalker night. |
| `BeginTemporaryNight(duration: number, arg2: number): void` | Begin temporary night. |
| `BotPopulate(): void` | Fills all the teams with bots if cheat mode is enabled. |
| `ClearHeroBlacklist(): void` | Clears the hero blacklist. |
| `ClearHeroWhitelist(): void` | Clears the hero whitelist. |
| `ClearPlayerHeroAvailability(arg1: number): void` | Clears available heroes of player of given ID. |
| `ClearRiverPaint(): void` | Clears the current river paint. |
| `Defeated(): void` | Kills the ancient, etc. |
| `DidMatchSignoutTimeOut(): boolean` | True when we have waited some time after end of the game and not received<br>signout. |
| `EnableCustomGameSetupAutoLaunch(enabled: boolean): void` | Enabled (true) or disable (false) auto launch for custom game setup. |
| `ExecuteTeamPing( team: DOTATeam_t, xCoord: number, yCoord: number, entity: CBaseEntity \| undefined, type: 0 \| 1 \| 2 \| 3 \| 4 \| 5 \| 6, ): void` | Sends a minimap ping to all players on the team. |
| `FinishCustomGameSetup(): void` | Indicate that the custom game setup phase is complete, and advance to the game. |
| `ForceCreepSpawn(): void` | Spawn the next wave of creeps. |
| `ForceGameStart(): void` | Transition game state to DOTA_GAMERULES_STATE_GAME_IN_PROGRESS. |
| `GetAnnouncer(team: DOTATeam_t): CDOTA_BaseNPC \| undefined` | Get the announcer for a team. |
| `GetBannedHeroes(): string[]` | Returns the hero unit names banned in this game, if any.<br><br>**Availability:** `both` |
| `GetBannedHeroIDs(): object` | Returns the hero unit IDs banned in this game, if any.<br><br>**Availability:** `both` |
| `GetCustomGameDifficulty(): number` | Returns the difficulty level of the custom game mode.<br><br>**Availability:** `both` |
| `GetCustomGameTeamMaxPlayers(team: DOTATeam_t): number` | Get whether a team is selectable during game setup. |
| `GetDifficulty(): number` | Returns difficulty level of the custom game mode.<br><br>**Availability:** `both` |
| `GetDOTATime(includePreGame: boolean, includeNegativeTime: boolean): number` | Returns the actual DOTA in-game clock time.<br><br>**Availability:** `both` |
| `GetDroppedItem(index: number): CDOTA_Item_Physical \| undefined` | Gets the Xth dropped item. |
| `GetGameFrameTime(): number` | Returns the number of seconds elapsed since the last frame was renderered. This<br>time doesn't count up when the game is paused.<br><br>**Availability:** `both` |
| `GetGameModeEntity(): CDOTABaseGameMode` | Get the game mode entity. |
| `GetGameSessionConfigValue(arg1: string, arg2: string): string` | Get a string value from the game session config (map options). |
| `GetGameTime(): number` | Returns the number of seconds elapsed since map start. This time doesn't count<br>up when the game is paused.<br><br>**Availability:** `both` |
| `GetIetmStockDuration(arg1: number, arg2: string, arg3: number): number` | Get the time it takes to add a new item to stock.<br><br>**Availability:** `both` |
| `GetItemStockCount(team: DOTATeam_t, itemName: string, playerId: PlayerID): number` | Get the stock count of the item.<br><br>**Availability:** `both`<br><br>**Parameters:**<br><br>- playerId Used only for items with "PlayerSpecificCooldown" |
| `GetItemStockTime(team: DOTATeam_t, itemName: string, playerId: PlayerID): number` | Get the time an item will be added to stock.<br><br>**Availability:** `both`<br><br>**Parameters:**<br><br>- playerId Used only for items with "PlayerSpecificCooldown" |
| `GetMatchSignoutComplete(): boolean` | Have we received the post match signout message that includes reward<br>information. |
| `GetNeutralInitialSpawnOffset(): number` | Gets the extra offset to initial neutral creep spawn delay.<br><br>**Availability:** `both` |
| `GetNextBountyRuneSpawnTime(): number` | Gets next bounty rune spawn time. |
| `GetNextRuneSpawnTime(): number` | Gets next rune spawn time. |
| `GetNianTotalDamageTaken(): number` | For New Bloom, get total damage taken by the Nian / Year Beast. |
| `GetPlayerCustomGameAccountRecord(playerId: PlayerID): object` | Gets the player's custom game account record, as it looked at the start of this<br>session.<br><br>**Deprecated:** Unreleased.<br> |
| `GetStateTransitionTime(): number` | Get time remaining between state changes. |
| `GetTimeOfDay(): number` | Get the time of day. |
| `GetWeatherWindDirection(): Vector` | Get Weather Wind Direction Vector.<br><br>**Availability:** `both` |
| `IncreaseItemStock(team: DOTATeam_t, itemName: string, count: number, playerId: PlayerID): void` | Increase an item's stock count, clamped to item max.<br><br>**Parameters:**<br><br>- count Negative values decrease stock count.<br><br>- playerId Values other than -1 work only for items with<br>                "PlayerSpecificCooldown" property.<br> |
| `IsCheatMode(): boolean` | Are cheats enabled on the server.<br><br>**Availability:** `both` |
| `IsDaytime(): boolean` | Is it day time? |
| `IsDev(): boolean` | **Availability:** `both` |
| `IsGamePaused(): boolean` | Returns whether the game is paused. |
| `IsHeroEnabledViaLists(arg1: string): boolean` | Is the hero not blacklisted, and is it either whitelisted or the whitelist is<br>empty?<br><br>**Availability:** `both` |
| `IsHeroRespawnEnabled(): boolean` | Returns whether hero respawn is enabled. |
| `IsInBanPhase(): boolean` | Are we in the ban phase of hero pick? |
| `IsItemInWhiteList(itemName: string): boolean` | Query an item in the whitelist. |
| `IsNightstalkerNight(): boolean` | Is it night stalker night-time? |
| `IsSuggestAbilitiesEnabled(): boolean` | Returns whether Dota Plus ability suggestions are enabled or disabled. |
| `IsSuggestItemsEnabled(): boolean` | Returns whether Dota Plus item suggestions are enabled or disabled. |
| `IsTemporaryNight(): boolean` | Is it temporarily night-time? |
| `LockCustomGameSetupTeamAssignment(locked: boolean): void` | Lock (true) or unlock (false) team assignemnt. If team assignment is locked<br>players cannot change teams. |
| `MakeTeamLose(team: DOTATeam_t): void` | Makes the specified team lose. |
| `ModifyGoldFiltered( playerId: PlayerID, goldChange: number, reliable: boolean, reason: EDOTA_ModifyGold_Reason, ): number` | Like ModifyGold, but will use the gold filter if SetFilterMoreGold has been set<br>true. |
| `NumDroppedItems(): number` | Returns the number of items currently dropped on the ground. |
| `PlayerHasCustomGameHostPrivileges(player: CDOTAPlayerController): boolean` | Whether a player has custom game host privileges (shuffle teams, etc.). |
| `Playtesting_UpdateAddOnKeyValues(): void` | Updates custom hero, unit and ability KeyValues in memory with the latest<br>values from disk. |
| `PrepareSpawners(arg1: number): void` | Prepare Dota lane style spawners with a given interval. |
| `RemoveFakeClient(playerId: PlayerID): void` | Removes a fake client. |
| `RemoveHeroFromBlacklist(arg1: string): void` | Remove the hero from the hero blacklist if present. |
| `RemoveHeroFromWhitelist(arg1: string): void` | Remove the hero from the hero whitelist if present. |
| `RemoveHeroIDFromBlacklist(arg1: number): void` | Remove the hero ID from the hero blacklist if present. |
| `RemoveHeroIDFromWhitelist(arg1: number): void` | Remove the hero ID from the hero whitelist if present. |
| `RemoveItemFromWhiteList(itemName: string): void` | Remove an item from the whitelist. |
| `ResetDefeated(): void` | Restart after killing the ancient, etc. |
| `ResetGameTime(): void` | Restart gametime from 0. |
| `ResetPlayer(arg1: number): void` | Resets the player of a given ID. |
| `ResetToCustomGameSetup(): void` | Restart at custom game setup. |
| `ResetToHeroSelection(): void` | Restart the game at hero selection. |
| `Script_GetMatchID(): Uint64` | Get the MatchID for this game. |
| `SendCustomMessage(arg1: string, arg2: number, arg3: number): void` | Sends a message on behalf of a player. |
| `SendCustomMessageToTeam(arg1: string, arg2: number, arg3: number, arg4: number): void` | Sends a message on behalf of a player to the specified team. |
| `SetAllowOutpostBonuses(arg1: boolean): void` | Allow Outposts granting XP. |
| `SetCreepMinimapIconScale(scale: number): void` | Scale the creep icons on the minimap. |
| `SetCreepSpawningEnabled(arg1: boolean): void` | Sets whether the regular Dota creeps spawn. |
| `SetCustomGameAccountRecordSaveFunction(arg1: object, arg2: object): void` | Sets a callback to handle saving custom game account records (callback is<br>passed a Player ID and should return a flat simple table).<br><br>**Deprecated:** Unreleased.<br> |
| `SetCustomGameAllowBattleMusic(allow: boolean): void` | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowHeroPickMusic(allow: boolean): void` | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowMusicAtGameStart(allow: boolean): void` | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowSecondaryAbilitiesOnOtherUnits(arg1: boolean): void` | Sets a flag to enable/disable the casting secondary abilities from units other<br>than the player's own hero. |
| `SetCustomGameBansPerTeam(arg1: number): void` | Set number of hero bans each team gets. |
| `SetCustomGameDifficulty(difficulty: number): void` | Set the difficulty level of the custom game mode. |
| `SetCustomGameEndDelay(delay: number): void` | Sets the game end delay. |
| `SetCustomGameSetupAutoLaunchDelay(delay: number): void` | Set the amount of time to wait for auto launch. |
| `SetCustomGameSetupRemainingTime(remainingTime: number): void` | Set the amount of remaining time, in seconds, for custom game setup. 0 = finish<br>immediately, -1 = wait forever. |
| `SetCustomGameSetupTimeout(timeout: number): void` | Setup (pre-gameplay) phase timeout. 0 = instant, -1 = forever (until<br>FinishCustomGameSetup is called). |
| `SetCustomGameTeamMaxPlayers(team: DOTATeam_t, maxPlayers: number): void` | Set whether a team is selectable during game setup. |
| `SetCustomVictoryMessage(message: string): void` | Sets the victory message. |
| `SetCustomVictoryMessageDuration(duration: number): void` | Sets the victory message duration. |
| `SetEnableAlternateHeroGrids(arg1: boolean): void` | Allow alternate hero grids to be used (DOTA+, etc).  True by default. |
| `SetEventMetadataCustomTable(metadataTable: object): boolean` | Event-only. |
| `SetEventSignoutCustomTable(metadataTable: object): boolean` | Event-only. |
| `SetFilterMoreGold(arg1: boolean): void` | Sets whether to filter more gold events than normal. |
| `SetFirstBloodActive(active: boolean): void` | Sets whether First Blood has been triggered. |
| `SetGameWinner(team: DOTATeam_t): void` | Makes the specified team win. |
| `SetGlyphCooldown(team: DOTATeam_t, cooldown: number): void` | Set Glyph cooldown for team. |
| `SetGoldPerTick(amount: number): void` | Set the auto gold increase per timed interval. |
| `SetGoldTickTime(time: number): void` | Set the time interval between auto gold increases. |
| `SetHeroMinimapIconScale(scale: number): void` | Scale the hero minimap icons on the minimap. |
| `SetHeroRespawnEnabled(enabled: boolean): void` | Control if the normal DOTA hero respawn rules apply. |
| `SetHeroSelectionTime(selectionTime: number): void` | Sets the amount of time players have to pick their hero. |
| `SetHeroSelectPenaltyTime(arg1: number): void` | Sets amount of penalty time before randoming a hero. |
| `SetHideBlacklistedHeroes(arg1: boolean): void` | Should blacklisted heroes be hidden, or just dimmed, in hero picking? |
| `SetHideKillMessageHeaders(hideHeaders: boolean): void` | Sets whether the multikill, streak, and first-blood banners appear at the top<br>of the screen. |
| `SetIgnoreLobbyTeamsInCustomGame(arg1: boolean): void` | Set whether custom and event games should ignore Lobby teams when assigning<br>players to teams. Defaults to true. |
| `SetItemStockCount(count: number, team: DOTATeam_t, itemName: string, playerId: PlayerID): void` | Set the stock count of the item.<br><br>**Parameters:**<br><br>- playerId Used only for items with "PlayerSpecificCooldown"<br> |
| `SetNeutralInitialSpawnOffset(arg1: number): void` | Sets the extra offset to initial neutral creep spawn delay. |
| `SetNextBountyRuneSpawnTime(arg1: number): void` | Sets next bounty rune spawn time. |
| `SetNextRuneSpawnTime(arg1: number): void` | Sets next rune spawn time. |
| `SetOverlayHealthBarUnit(unit: CDOTA_BaseNPC, style: number): void` | Show this unit's health on the overlay health bar. |
| `SetPostGameColumns(arg1: object): boolean` | Set columns to show in post game. |
| `SetPostGameLayout(arg1: number): void` | Configure post game to be single or double column layout. |
| `SetPostGameTeamScores(arg1: object): boolean` | Set score value for each team. First element is for DOTA_TEAM_GOODGUYS. |
| `SetPostGameTime(time: number): void` | Sets the amount of time players have between the game ending and the server<br>disconnecting them. |
| `SetPreGameTime(time: number): void` | Sets the amount of time players have between picking their hero and game start. |
| `SetRiverPaint(arg1: number, arg2: number): void` | Paints the river for a duration. |
| `SetRuneMinimapIconScale(minimapRuneIconScale: number): void` | Scale the rune icons on the minimap. |
| `SetRuneSpawnTime(time: number): void` | Sets the amount of time between rune spawns. |
| `SetSafeToLeave(safeToLeave: boolean): void` | Mark this game as safe to leave. |
| `SetSameHeroSelectionEnabled(enabled: boolean): void` | When true, players can repeatedly pick the same hero. |
| `SetShowcaseTime(time: number): void` | Sets the amount of time players have between the strategy phase and entering<br>the pre-game phase. |
| `SetSpeechUseSpawnInsteadOfRespawnConcept(arg1: boolean): void` | Set whether to speak a Spawn concept instead of a Respawn concept on respawn. |
| `SetStartingGold(amount: number): void` | Set the starting gold amount. |
| `SetStrategyTime(time: number): void` | Sets the amount of time players have between the hero selection and entering<br>the showcase phase. |
| `SetSuggestAbilitiesEnabled(arg1: boolean): void` | Sets Dota Plus ability suggestions enabled or disabled. |
| `SetSuggestItemsEnabled(arg1: boolean): void` | Sets Dota Plus ability item enabled or disabled. |
| `SetTimeOfDay(time: number): void` | Set the time of day. |
| `SetTreeRegrowTime(time: number): void` | Sets the tree regrow time in seconds. |
| `SetUseBaseGoldBountyOnHeroes(useBaseGoldBounties: boolean): void` | Heroes will use the basic NPC functionality for determining their bounty,<br>rather than DOTA specific formulas. |
| `SetUseCustomHeroXPValues(useCustomXPValues: boolean): void` | Allows heroes in the map to give a specific amount of XP (this value must be<br>set). |
| `SetUseUniversalShopMode(useUniversalShopMode: boolean): void` | When true, all items are available at as long as any shop is in range. |
| `SetWeatherWindDirection(arg1: Vector): void` | Set Weather Wind Direction Vector. |
| `SetWhiteListEnabled(whiteListEnabled: boolean): void` | Item whitelist functionality enable/disable. |
| `ShouldHideBlacklistedHeroes(): boolean` | Are blacklisted heroes hidden, or just dimmed, in hero picking?<br><br>**Availability:** `both` |
| `SpawnAndReleaseCreeps(): void` | Spawn and release the next creep wave from Dota lane style spawners. |
| `SpawnNeutralCreeps(): void` | Spawn and release the next set of neutral camps. |
| `State_Get(): DOTA_GameState` | Get the current Gamerules state.<br><br>**Availability:** `both` |

### CDOTAPlayerController

Extends `CBaseAnimatingActivity`

**Methods**

| Method | Description |
| --- | --- |
| `CheckForCourierSpawning(hero: CDOTA_BaseNPC_Hero): object` | Attempt to spawn the appropriate couriers for this mode. |
| `GetActiveAbility(): object` | **Availability:** `client` |
| `GetAssignedHero(): CDOTA_BaseNPC_Hero` | Get the player's hero. |
| `GetClickBehaviors(): unknown` | **Availability:** `client` |
| `GetPlayerID(): PlayerID` | Get the player's official PlayerID; notably is -1 when the player isn't yet on<br>a team. |
| `GetQueryUnit(): object` | **Availability:** `client` |
| `MakeRandomHeroSelection(): void` | Randoms this player's hero. |
| `SetAssignedHeroEntity(hero: object): void` | Sets this player's hero . |
| `SetKillCamUnit(entity: CDOTA_BaseNPC): void` | Set the kill cam unit for this hero. |
| `SetMusicStatus(musicStatus: number, intensity: number): void` | Set the music status for this player, note this will only really apply if<br>dota_music_battle_enable is off. |
| `SetSelectedHero(heroName: string): void` | Sets this player's hero selection. |
| `ShouldDisplayInWorldUIElements(): boolean` | **Availability:** `client` |
| `SpawnCourierAtPosition(location: Vector): CDOTA_Unit_Courier` | Spawn a courier for this player at the given position. |

### CDotaQuest

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AddSubquest(subquest: object): void` | Add a subquest to this quest. |
| `CompleteQuest(): void` | Mark this quest complete. |
| `GetSubquest(index: number): object` | Finds a subquest from this quest by index. |
| `GetSubquestByName(name: string): object` | Finds a subquest from this quest by name. |
| `RemoveSubquest(subquest: object): void` | Remove a subquest from this quest. |
| `SetTextReplaceString(string: string): void` | Set the text replace string for this quest. |
| `SetTextReplaceValue(valueSlot: number, value: number): void` | Set a quest value. |

### CDotaSubquestBase

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `CompleteSubquest(): void` | Mark this subquest complete. |
| `SetTextReplaceString(string: string): void` | Set the text replace string for this subquest. |
| `SetTextReplaceValue(valueSlot: number, value: number): void` | Set a subquest value. |

### CDOTATutorial

**Methods**

| Method | Description |
| --- | --- |
| `AddBot(heroName: string, arg2: string, arg3: string, arg4: boolean): boolean` | Add a computer controlled bot. |
| `AddQuest(arg1: string, arg2: number, arg3: string, arg4: string): void` | Add a quest to the quest log. |
| `AddShopWhitelistItem(itemName: string): void` | Add an item to the shop whitelist. |
| `CompleteQuest(arg1: string): void` | Complete a quest,. |
| `CreateLocationTask(arg1: Vector): void` | Add a task to move to a specific location. |
| `EnableCreepAggroViz(arg1: boolean): void` | Alert the player when a creep becomes agro to their hero. |
| `EnablePlayerOffscreenTip(arg1: boolean): void` | Enable the tip to alert players how to find their hero. |
| `EnableTowerAggroViz(arg1: boolean): void` | Alert the player when a tower becomes agro to their hero. |
| `FinishTutorial(): void` | End the tutorial. |
| `ForceGameStart(): void` | Force the start of the game. |
| `IsItemInWhiteList(itemName: string): boolean` | Is this item currently in the white list. |
| `MoveCameraToLocation(arg1: Vector): void` | Moves the camera to a position. |
| `RemoveShopWhitelistItem(itemName: string): void` | Remove an item from the shop whitelist. |
| `SelectHero(heroName: string): void` | Select a hero for the local player. |
| `SelectPlayerTeam(arg1: string): void` | Select the team for the local player. |
| `SetItemGuide(arg1: string): void` | Set the current item guide. |
| `SetOrModifyPlayerGold(goldAmount: number, setNotModify: boolean): void` | Set gold amount for the tutorial player.<br><br>**Parameters:**<br><br>- setNotModify When true sets gold amount, otherwise modifies it<br> |
| `SetQuickBuy(itemName: string): void` | Set players quick buy item. |
| `SetShopOpen(open: boolean): void` | Set the shop open or closed. |
| `SetTutorialConvar(arg1: string, arg2: string): void` | Set a tutorial convar. |
| `SetTutorialUI(arg1: number): void` | Set the UI to use a reduced version to focus attention to specific elements. |
| `SetWhiteListEnabled(whiteListEnabled: boolean): void` | Set if we should whitelist shop items. |
| `StartTutorialMode(): void` | Initialize Tutorial Mode. |
| `UpgradePlayerAbility(abilityName: string): void` | Upgrade a specific ability for the local hero. |

### CDotaTutorialNPCBlocker

Extends `CBaseAnimatingOverlay`

**Methods**

| Method | Description |
| --- | --- |
| `SetEnabled(enabled: boolean): void` |  |
| `SetOtherBlocker(blocker: object): void` |  |

### CDOTAVoteSystem

**Methods**

| Method | Description |
| --- | --- |
| `StartVote(arg1: object): void` | Starts a vote, based upon a table of parameters. |

### CEntities

**Methods**

| Method | Description |
| --- | --- |
| `CreateByClassname(className: string): CBaseEntity` | Creates an entity by classname. |
| `FindAllByClassname(className: string): CBaseEntity[]` | Finds all entities by class name. Returns an array containing all the found<br>entities. |
| `FindAllByClassnameWithin(arg1: string, location: Vector, arg3: number): object` | Find entities by class name within a radius. |
| `FindAllByModel(modelName: string): CBaseEntity[]` | Find entities by model name. |
| `FindAllByName(name: string): CBaseEntity[]` | Find all entities by name. Returns an array containing all the found entities<br>in it. |
| `FindAllByNameWithin(arg1: string, location: Vector, arg3: number): object` | Find entities by name within a radius. |
| `FindAllByTarget(target: string): CBaseEntity[]` | Find entities by targetname. |
| `FindAllInSphere(location: Vector, arg2: number): object` | Find entities within a radius. |
| `FindByClassname(previous: CBaseEntity \| undefined, className: string): CBaseEntity \| undefined` | Find entities by class name. Pass 'null' to start an iteration, or reference to<br>a previously found entity to continue a search. |
| `FindByClassnameNearest(arg1: string, location: Vector, arg3: number): object` | Find entities by class name nearest to a point. |
| `FindByClassnameWithin(arg1: object, arg2: string, location: Vector, arg4: number): object` | Find entities by class name within a radius. Pass 'null' to start an iteration,<br>or reference to a previously found entity to continue a search. |
| `FindByModel(previous: CBaseEntity \| undefined, modelName: string): CBaseEntity \| undefined` | Find entities by model name. Pass 'null' to start an iteration, or reference to<br>a previously found entity to continue a search. |
| `FindByModelWithin(arg1: object, arg2: string, location: Vector, arg4: number): object` | Find entities by model name within a radius. Pass 'null' to start an iteration,<br>or reference to a previously found entity to continue a search. |
| `FindByName(previous: CBaseEntity \| undefined, name: string): CBaseEntity \| undefined` | Find entities by name. Pass 'null' to start an iteration, or reference to a<br>previously found entity to continue a search. |
| `FindByNameNearest(arg1: string, location: Vector, arg3: number): object` | Find entities by name nearest to a point. |
| `FindByNameWithin(arg1: object, arg2: string, location: Vector, arg4: number): object` | Find entities by name within a radius. Pass 'null' to start an iteration, or<br>reference to a previously found entity to continue a search. |
| `FindByTarget(previous: CBaseEntity \| undefined, target: string): CBaseEntity \| undefined` | Find entities by targetname. Pass 'null' to start an iteration, or reference to<br>a previously found entity to continue a search. |
| `FindInSphere(arg1: object, location: Vector, arg3: number): object` | Find entities within a radius. Pass 'null' to start an iteration, or reference<br>to a previously found entity to continue a search. |
| `First(): CBaseEntity` | Begin an iteration over the list of entities.<br><br>**Availability:** `both` |
| `GetLocalPlayer(): CDOTAPlayerController` | Get the local player controller (backcompat).<br><br>**Availability:** `both` |
| `GetLocalPlayerController(): object` | Get the local player controller.<br><br>**Availability:** `both` |
| `GetLocalPlayerPawn(): object` | Get the local player pawn.<br><br>**Availability:** `both` |
| `Next(previous: CBaseEntity \| undefined): CBaseEntity \| undefined` | Continue an iteration over the list of entities, providing reference to a<br>previously found entity.<br><br>**Availability:** `both` |

### CEntityInstance

**Methods**

| Method | Description |
| --- | --- |
| `ConnectOutput(arg1: string, arg2: string): void` | Adds an I/O connection that will call the named function on this entity when<br>the specified output fires.<br><br>**Availability:** `both` |
| `Destroy(): void` | **Availability:** `both` |
| `DisconnectOutput(arg1: string, arg2: string): void` | Removes a connected script function from an I/O event on this entity.<br><br>**Availability:** `both` |
| `DisconnectRedirectedOutput(arg1: string, arg2: string, arg3: object): void` | Removes a connected script function from an I/O event on the passed entity.<br><br>**Availability:** `both` |
| `entindex(): EntityIndex` | **Availability:** `both` |
| `FireOutput(arg1: string, arg2: object, arg3: object, arg4: object, arg5: number): void` | Fire an entity output.<br><br>**Availability:** `both` |
| `GetClassname(): string` | **Availability:** `both` |
| `GetDebugName(): string` | Get the entity name w/help if not defined (i.e. classname/etc).<br><br>**Availability:** `both` |
| `GetEntityHandle(): number` | Get the entity as an EHANDLE.<br><br>**Availability:** `both` |
| `GetEntityIndex(): EntityIndex` | **Availability:** `both` |
| `GetIntAttr(arg1: string): number` | Get Integer Attribute.<br><br>**Availability:** `both` |
| `GetName(): string` | Get the entity name.<br><br>**Availability:** `both` |
| `GetOrCreatePrivateScriptScope(): object` | Retrieve, creating if necessary, the private per-instance script-side data<br>associated with an entity.<br><br>**Availability:** `both` |
| `GetOrCreatePublicScriptScope(): object` | Retrieve, creating if necessary, the public script-side data associated with an<br>entity.<br><br>**Availability:** `both` |
| `GetPrivateScriptScope(): object` | Retrieve the private per-instance script-side data associated with an entity.<br><br>**Availability:** `both` |
| `GetPublicScriptScope(): object` | Retrieve the public script-side data associated with an entity.<br><br>**Availability:** `both` |
| `IsNull(): boolean` | Has underlying C++ entity object been deleted?<br><br>**Availability:** `both` |
| `RedirectOutput(arg1: string, arg2: string, arg3: object): void` | Adds an I/O connection that will call the named function on the passed entity<br>when the specified output fires.<br><br>**Availability:** `both` |
| `RemoveSelf(): void` | Delete this entity.<br><br>**Availability:** `both` |
| `SetIntAttr(arg1: string, arg2: number): void` | Set Integer Attribute.<br><br>**Availability:** `both` |

### CEntityScriptFramework

_No members._

### CEnvEntityMaker

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `SpawnEntity(): void` | Create an entity at the location of the maker. |
| `SpawnEntityAtEntityOrigin(entity: object): void` | Create an entity at the location of a specified entity instance. |
| `SpawnEntityAtLocation(vecAlternateOrigin: Vector, vecAlternateAngles: Vector): void` | Create an entity at a specified location and orientaton, orientation is Euler<br>angle in degrees. |
| `SpawnEntityAtNamedEntityOrigin(name: string): void` | Create an entity at the location of a named entity. |

### CFoWBlockerRegion

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AddRectangularBlocker(mins: Vector, maxs: Vector, clearRegion: boolean): void` | Sets or clears a blocker rectangle. |
| `AddRectangularOutlineBlocker(mins: Vector, maxs: Vector, clearRegion: boolean): void` | Sets or clears a blocker rectangle outline. |

### CInfoData

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `QueryColor(tok: string, defaultValue: Vector): Vector` | Query color data for this key. |
| `QueryFloat(tok: string, defaultValue: number): number` | Query float data for this key. |
| `QueryInt(tok: string, defaultValue: number): number` | Query int data for this key. |
| `QueryNumber(tok: string, defaultValue: number): number` | Query number data for this key. |
| `QueryString(tok: string, defaultValue: string): string` | Query string data for this key. |
| `QueryVector(tok: string, defaultValue: Vector): Vector` | Query vector data for this key. |

### CInfoPlayerStartDota

Extends `CPointEntity`

**Methods**

| Method | Description |
| --- | --- |
| `IsEnabled(): boolean` | Returns whether the object is currently active. |
| `SetEnabled(enabled: boolean): void` | Enable or disable the obstruction. |

### CInfoWorldLayer

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `HideWorldLayer(): void` | Hides this layer.<br><br>**Availability:** `both` |
| `ShowWorldLayer(): void` | Shows this layer.<br><br>**Availability:** `both` |

### CLogicRelay

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `Trigger(activator: CBaseEntity \| undefined, caller: CBaseEntity \| undefined): void` | Triggers the logic_relay.<br><br>**Availability:** `both` |
| `Trigger(): never` | **Deprecated:** Added for compatibility with CBaseEntity. Invalid at the runtime.<br> |

### CLogicScript

Extends `CBaseEntity`

_No members._

### CMarkupVolumeTagged

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `HasTag(tagName: unknown): boolean` | Does this volume have the given tag. |

### CNativeOutputs

**Methods**

| Method | Description |
| --- | --- |
| `AddOutput(arg1: string, arg2: string): void` | Add an output.<br><br>**Availability:** `both` |
| `Init(arg1: number): void` | Initialize with number of outputs.<br><br>**Availability:** `both` |

### Convars

**Methods**

| Method | Description |
| --- | --- |
| `GetBool(name: string): boolean \| undefined` | Returns the convar as a boolean flag.<br><br>**Availability:** `both` |
| `GetCommandClient(): CDOTAPlayerController` | Returns the player who issued this console command.<br><br>**Availability:** `both` |
| `GetDOTACommandClient(): CDOTAPlayerController` | Returns the DOTA player who issued this console command.<br><br>**Availability:** `both` |
| `GetFloat(name: string): number \| undefined` | Returns the convar as a float. May return null if no such convar.<br><br>**Availability:** `both` |
| `GetInt(name: string): number \| undefined` | Returns the convar as an int. May return null if no such convar.<br><br>**Availability:** `both` |
| `GetStr(name: string): string \| undefined` | Returns the convar as a string. May return null if no such convar.<br><br>**Availability:** `both` |
| `RegisterCommand( name: string, callback: (name: string, ...args: string[]) => void, helpString: string, flags: ConVarFlags, ): void` | Register a console command.<br><br>**Availability:** `both` |
| `RegisterConvar(name: string, defaultValue: string, helpString: string, flags: ConVarFlags): void` | Register a new console variable.<br><br>**Availability:** `both` |
| `SetBool(name: string, value: boolean): void` | Sets the value of the convar to the bool.<br><br>**Availability:** `both` |
| `SetFloat(name: string, value: number): void` | Sets the value of the convar to the float.<br><br>**Availability:** `both` |
| `SetInt(name: string, value: number): void` | Sets the value of the convar to the int.<br><br>**Availability:** `both` |
| `SetStr(name: string, value: string): void` | Sets the value of the convar to the string.<br><br>**Availability:** `both` |

### CParticleSystem

Extends `CBaseModelEntity`

_No members._

### CPhysicsProp

Extends `CBaseAnimatingActivity`

**Methods**

| Method | Description |
| --- | --- |
| `DisableMotion(): void` | Disable motion for the prop. |
| `EnableMotion(): void` | Enable motion for the prop. |

### CPointClientUIWorldPanel

Extends `CBaseModelEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AcceptUserInput(): void` | Tells the panel to accept user input. |
| `AddCSSClasses(classes: string): void` | Adds CSS class(es) to the panel. |
| `IgnoreUserInput(): void` | Tells the panel to ignore user input. |
| `IsGrabbable(): boolean` | Returns whether this entity is grabbable. |
| `RemoveCSSClasses(classes: string): void` | Remove CSS class(es) from the panel. |

### CPointEntity

Extends `CBaseEntity`

_No members._

### CPointTemplate

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `DeleteCreatedSpawnGroups(): void` | Deletes any spawn groups that this point_template has spawned. Note: The<br>point_template will not be deleted by this.<br><br>**Availability:** `both` |
| `ForceSpawn(): void` | Spawns all of the entities the point_template is pointing at.<br><br>**Availability:** `both` |
| `GetSpawnedEntities(): object` | Get the list of the most recent spawned entities.<br><br>**Availability:** `both` |
| `SetSpawnCallback(callbackFunc: object, callbackScope: object): void` | Set a callback for when the template spawns entities. The spawned entities will<br>be passed in as an array.<br><br>**Availability:** `both` |

### CPointWorldText

Extends `CBaseModelEntity`

**Methods**

| Method | Description |
| --- | --- |
| `SetMessage(message: string): void` | Set the message on this entity.<br><br>**Availability:** `both` |

### CSceneEntity

Extends `CBaseEntity`

**Methods**

| Method | Description |
| --- | --- |
| `AddBroadcastTeamTarget(arg1: number): void` | Adds a team (by index) to the broadcast list. |
| `Cancel(): void` | Cancel scene playback. |
| `EstimateLength(): number` | Returns length of this scene in seconds. |
| `FindNamedEntity(arg1: string): object` | Given an entity reference, such as !target, get actual entity from scene object. |
| `IsPaused(): boolean` | If this scene is currently paused. |
| `IsPlayingBack(): boolean` | If this scene is currently playing. |
| `RemoveBroadcastTeamTarget(arg1: number): void` | Removes a team (by index) from the broadcast list. |
| `Start(arg1: object): void` | Start scene playback, takes activatorEntity as param. |

### CScriptHeroList

**Methods**

| Method | Description |
| --- | --- |
| `GetAllHeroes(): CDOTA_BaseNPC_Hero[]` | Returns all the heroes in the world. |
| `GetHero(nth: number): CDOTA_BaseNPC_Hero \| undefined` | Get the Nth hero in the Hero List. |
| `GetHeroCount(): number` | Returns the number of heroes in the world. |

### CScriptHTTPRequest

Note: Actual `CScriptHTTPRequest` global exists only after CreateHTTPRequest is
called.

**Methods**

| Method | Description |
| --- | --- |
| `Send(callback: (response: CScriptHTTPResponse) => void): boolean` | Send a HTTP request.<br><br>**Availability:** `both` |
| `SetHTTPRequestAbsoluteTimeoutMS(milliseconds: number): boolean` | Set the total timeout on the request.<br><br>**Availability:** `both` |
| `SetHTTPRequestGetOrPostParameter(name: string, value: string): boolean` | Set a POST or GET parameter on the request.<br><br>**Availability:** `both` |
| `SetHTTPRequestHeaderValue(name: string, value: string): boolean` | Set a header value on the request.<br><br>**Availability:** `both` |
| `SetHTTPRequestNetworkActivityTimeout(seconds: number): boolean` | Set the network timeout on the request - this timer is reset when any data is<br>received.<br><br>**Availability:** `both` |
| `SetHTTPRequestRawPostBody(contentType: string, body: string): boolean` | Set the literal body of a post - invalid after setting a post parameter.<br><br>**Availability:** `both` |

### CScriptKeyValues

**Methods**

| Method | Description |
| --- | --- |
| `GetValue(arg1: string): object` | Reads a spawn key.<br><br>**Availability:** `both` |

### CScriptParticleManager

**Methods**

| Method | Description |
| --- | --- |
| `CreateParticle( particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| undefined, ): ParticleID` | Creates a new particle effect.<br><br>**Availability:** `both` |
| `CreateParticleForPlayer( particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| undefined, player: CDOTAPlayerController, ): ParticleID` | Creates a new particle effect that only plays for the specified player.<br><br>**Availability:** `both` |
| `CreateParticleForTeam( particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| undefined, team: DOTATeam_t, ): ParticleID` | Creates a new particle effect that only plays for the specified team.<br><br>**Availability:** `both` |
| `DestroyParticle(particle: ParticleID, immediate: boolean): void` | Destroy a particle, if bDestroyImmediately destroy it without playing end caps.<br><br>**Availability:** `both` |
| `GetParticleReplacement(particleName: string, hero: CDOTA_BaseNPC_Hero \| undefined): string` | **Availability:** `both` |
| `ReleaseParticleIndex(particle: ParticleID): void` | Frees the specified particle index.<br><br>**Availability:** `both` |
| `SetParticleAlwaysSimulate(particle: ParticleID): void` | **Availability:** `both` |
| `SetParticleControl(particle: ParticleID, controlPoint: number, value: Vector): void` | Set the control point data for a control on a particle effect.<br><br>**Availability:** `both` |
| `SetParticleControlEnt( particle: ParticleID, controlPoint: number, unit: CBaseEntity, particleAttach: ParticleAttachment_t, attachment: string, offset: Vector, lockOrientation: boolean, ): void` | **Availability:** `both` |
| `SetParticleControlFallback(particle: ParticleID, controlPoint: number, vecPosition: Vector): void` | **Availability:** `both` |
| `SetParticleControlForward(particle: ParticleID, controlPoint: number, arg3: Vector): void` | [OBSOLETE - Use SetParticleControlTransformForward] (int nFXIndex, int nPoint,<br>vForward).<br><br>**Availability:** `both` |
| `SetParticleControlOrientation( particle: ParticleID, controlPoint: number, arg3: Vector, arg4: Vector, arg5: Vector, ): void` | [OBSOLETE - Use SetParticleControlTransform] (int nFXIndex, int nPoint,<br>vForward, vRight, vUp) - Set the orientation for a control on a particle effect<br>(NOTE: This is left handed -- bad!!).<br><br>**Availability:** `both` |
| `SetParticleControlOrientationFLU( particle: ParticleID, controlPoint: number, arg3: Vector, arg4: Vector, arg5: Vector, ): void` | [OBSOLETE - Use SetParticleControlTransform] (int nFXIndex, int nPoint, Vector<br>vecForward, Vector vecLeft, Vector vecUp) - Set the orientation for a control<br>on a particle effect.<br><br>**Availability:** `both` |
| `SetParticleControlTransform(fxIndex: number, point: number, origin: Vector, qAngles: QAngle): void` | **Availability:** `both` |
| `SetParticleControlTransformForward(fxIndex: number, point: number, origin: Vector, forward: Vector): void` | **Availability:** `both` |
| `SetParticleFoWProperties(particle: ParticleID, controlPoint: number, controlPoint2: number, radius: number): void` | **Availability:** `both` |
| `SetParticleShouldCheckFoW(particle: ParticleID, checkFoW: boolean): boolean` | **Availability:** `both` |

### CScriptPrecacheContext

**Methods**

| Method | Description |
| --- | --- |
| `AddResource(resource: string): void` | Precaches a specific resource.<br><br>**Availability:** `both` |
| `GetValue(key: string): object` | Reads a spawn key.<br><br>**Availability:** `both` |

### CScriptUniformRandomStream

**Methods**

| Method | Description |
| --- | --- |
| `RandomFloat(minVal: number, maxVal: number): number` | **Availability:** `both` |
| `RandomFloatExp(minVal: number, maxVal: number, exponent: number): number` | **Availability:** `both` |
| `RandomInt(minVal: number, maxVal: number): number` | **Availability:** `both` |
| `RollPercentage(percentage: number): boolean` | **Availability:** `both` |

### CTakeDamageInfo

**Methods**

| Method | Description |
| --- | --- |
| `AddDamage(addAmount: number): void` |  |
| `AddDamageType(damageType: number): void` |  |
| `GetAmmoType(): number` |  |
| `GetAttacker(): object` |  |
| `GetDamage(): number` |  |
| `GetDamageCustom(): number` |  |
| `GetDamageForce(): Vector` |  |
| `GetDamagePosition(): Vector` |  |
| `GetDamageType(): DAMAGE_TYPES` |  |
| `GetInflictor(): object` |  |
| `GetOriginalDamage(): number` |  |
| `GetReportedPosition(): Vector` |  |
| `GetTotalledDamage(): number` |  |
| `HasDamageType(damageType: number): boolean` |  |
| `ScaleDamage(scaleAmount: number): void` |  |
| `SetAmmoType(ammoType: number): void` |  |
| `SetAttacker(attacker: object): void` |  |
| `SetDamage(damage: number): void` |  |
| `SetDamageCustom(damageCustom: number): void` |  |
| `SetDamageForce(damageForce: Vector): void` |  |
| `SetDamagePosition(damagePosition: Vector): void` |  |
| `SetDamageType(damageType: number): void` |  |
| `SetOriginalDamage(originalDamage: number): void` |  |
| `SetReportedPosition(reportedPosition: Vector): void` |  |

### GlobalSys

**Methods**

| Method | Description |
| --- | --- |
| `CommandLineCheck(name: string): object` | Returns true if the command line param was used, otherwise false.<br><br>**Availability:** `both` |
| `CommandLineFloat(arg1: string, arg2: number): object` | Returns the command line param as a float.<br><br>**Availability:** `both` |
| `CommandLineInt(arg1: string, arg2: number): object` | Returns the command line param as an int.<br><br>**Availability:** `both` |
| `CommandLineStr(arg1: string, arg2: string): object` | Returns the command line param as a string.<br><br>**Availability:** `both` |

### GridNav

**Methods**

| Method | Description |
| --- | --- |
| `CanFindPath(start: Vector, end: Vector): boolean` | Determine if it is possible to reach the specified end point from the specified<br>start point. bool. |
| `DestroyTreesAroundPoint(arg1: Vector, arg2: number, arg3: boolean): void` | Destroy all trees in the area(vPosition, flRadius, bFullCollision. |
| `FindPathLength(start: Vector, end: Vector): number` | Find a path between the two points an return the length of the path. If there<br>is not a path between the points the returned value will be -1. |
| `GetAllTreesAroundPoint(position: Vector, radius: number, fullCollision: boolean): CDOTA_MapTree[]` | Returns a table full of tree HSCRIPTS. |
| `GridPosToWorldCenterX(arg1: number): number` | Get the X position of the center of a given X index. |
| `GridPosToWorldCenterY(arg1: number): number` | Get the Y position of the center of a given Y index. |
| `IsBlocked(arg1: Vector): boolean` | Checks whether the given position is blocked. |
| `IsNearbyTree(position: Vector, radius: number, checkFullTreeRadius: boolean): boolean` | Checks whether there are any trees overlapping the given point. |
| `IsTraversable(arg1: Vector): boolean` | Checks whether the given position is traversable. |
| `RegrowAllTrees(): void` | Causes all trees in the map to regrow. |
| `WorldToGridPosX(arg1: number): number` | Get the X index of a given world X position. |
| `WorldToGridPosY(arg1: number): number` | Get the Y index of a given world Y position. |

### ProjectileManager

**Methods**

| Method | Description |
| --- | --- |
| `ChangeTrackingProjectileSpeed(ability: CDOTABaseAbility, speed: number): void` | Update speed. |
| `CreateLinearProjectile(options: CreateLinearProjectileOptions): ProjectileID` | Creates a linear projectile and returns the projectile ID. |
| `CreateTrackingProjectile(options: CreateTrackingProjectileOptions): ProjectileID` | Creates a tracking projectile. |
| `DestroyLinearProjectile(projectile: ProjectileID): void` | Destroys the linear projectile matching the argument ID. |
| `DestroyTrackingProjectile(projectile: ProjectileID): void` | Destroy a tracking projectile early. |
| `GetLinearProjectileLocation(projectile: ProjectileID): Vector` | Returns current location of projectile. |
| `GetLinearProjectileRadius(projectile: ProjectileID): number` | Returns current radius of projectile. |
| `GetLinearProjectileVelocity(projectile: ProjectileID): Vector` | Returns a vector representing the current velocity of the projectile. |
| `GetTrackingProjectileLocation(projectile: ProjectileID): Vector` | Returns current location of projectile. |
| `IsValidProjectile(value: number): value is ProjectileID` | Is this a valid projectile? |
| `ProjectileDodge(unit: CDOTA_BaseNPC): void` | Makes the specified unit dodge projectiles. |
| `UpdateLinearProjectileDirection(projectile: ProjectileID, direction: Vector, speed: number): void` | Update velocity. |

### SteamInfo

**Methods**

| Method | Description |
| --- | --- |
| `IsPublicUniverse(): boolean` | Is the script connected to the public Steam universe. |

### Uint64

Integer with binary operations.

**Methods**

| Method | Description |
| --- | --- |
| `__eq(b: Uint64): boolean` |  |
| `__tostring(): string` | Overloaded .. Converts Uint64s to strings. |
| `BitwiseAnd(operand: Uint64): Uint64` | Performs bitwise AND between two integers. |
| `BitwiseOr(operand: Uint64): Uint64` | Performs bitwise OR between two integers. |
| `BitwiseXor(operand: Uint64): Uint64` | Performs bitwise XOR between two integers. |
| `BitwiseNot(): Uint64` | Performs bitwise NOT. |
| `SetBit(bitvalue: number): void` | Sets the specified bit. |
| `ClearBit(bitvalue: number): number` | Clears the specified bit. |
| `IsBitSet(bitvalue: number): number \| undefined` | Checks if bit is set. |
| `ToggleBit(bitvalue: number): number` | Toggles the specified bit. |
| `ToHexString(): string` | Returns a hexadecimal string representation of the integer. |

## Additional interfaces

### CustomGameEventDeclarations

The type used for validation of custom events.

This type may be augmented via interface merging.

_No members._

### CustomNetTableDeclarations

The type used for validation of custom net tables.

This type may be augmented via interface merging.

_No members._

### GameEventProvidedProperties

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `game_event_listener` | `EventListenerID` |  |
| `game_event_name` | `string` |  |
| `splitscreenplayer` | `number` |  |

## Type aliases

### QAngle

```ts
declare type QAngle = __NumberLike & {
    /**
     * Pitch angle
     */
    x: number;
    /**
     * Yaw angle
     */
    y: number;
    /**
     * Roll angle
     */
    z: number;
    /**
     * Overloaded +. Adds angles together.
     *
     * @both
     */
    __add(b: QAngle): QAngle;
    /**
     * Overloaded ==. Tests for Equality.
     *
     * @both
     */
    __eq(b: QAngle): boolean;
    /**
     * Overloaded .. Converts the QAngles to strings.
     *
     * @both
     */
    __tostring(): string;
    /**
     * Returns the forward vector.
     *
     * @both
     */
    Forward(): Vector;
    /**
     * Returns the left vector.
     *
     * @both
     */
    Left(): Vector;
    /**
     * Returns the up vector.
     *
     * @both
     */
    Up(): Vector;
    __kind__: 'instance';
};
```

QAngle class.

### Vector

```ts
declare type Vector = __NumberLike & {
    /**
     * X-axis
     */
    x: number;
    /**
     * Y-axis
     */
    y: number;
    /**
     * Z-axis
     */
    z: number;
    /**
     * Overloaded +. Adds vectors together.
     *
     * @both
     */
    __add(b: Vector): Vector;
    /**
     * Overloaded /. Divides vectors.
     *
     * @both
     */
    __div(b: Vector): Vector;
    /**
     * Overloaded ==. Tests for Equality.
     *
     * @both
     */
    __eq(b: Vector): boolean;
    /**
     * Overloaded # returns the length of the vector.
     *
     * @both
     */
    __len(): number;
    /**
     * Overloaded * returns the vectors multiplied together. Can also be used to
     * multiply with scalars.
     *
     * @both
     */
    __mul(b: Vector | number): Vector;
    /**
     * Overloaded -. Subtracts vectors.
     *
     * @both
     */
    __sub(b: Vector): Vector;
    /**
     * Overloaded .. Converts vectors to strings.
     *
     * @both
     */
    __tostring(): string;
    /**
     * Overloaded - operator. Reverses the vector.
     *
     * @both
     */
    __unm(): Vector;
    /**
     * Cross product of two vectors.
     *
     * @both
     */
    Cross(b: Vector): Vector;
    /**
     * Dot product of two vectors.
     *
     * @both
     */
    Dot(b: Vector): number;
    /**
     * Length of the Vector.
     *
     * @both
     */
    Length(): number;
    /**
     * Length of the Vector in the XY plane.
     *
     * @both
     */
    Length2D(): number;
    /**
     * Returns the vector normalized.
     *
     * @both
     */
    Normalized(): Vector;
    /**
     * Linearly interpolates between two vectors.
     *
     * This is most commonly used to find a point some fraction of the way along a
     * line between two endpoints.
     *
     * Same as `this + (b - this) * t`.
     *
     * @param t Interpolant
     * @both
     */
    Lerp(b: Vector, t: number): Vector;
    __kind__: 'instance';
};
```

3D Vector class.

## Namespaces

### CCustomGameEventManager

```ts
declare namespace CCustomGameEventManager {
    type InferEventType<T extends string | object, TUntyped> = T extends string
        ? T extends keyof CustomGameEventDeclarations
            ? CustomGameEventDeclarations[T]
            : TUntyped
        : T;
}
```

## Global constants

These include generated constructor globals for classes.

| Name | Type / value | Description |
| --- | --- | --- |
| `C_BaseAnimatingOverlay` | `typeof CBaseAnimatingOverlay` | **Availability:** `client` |
| `C_BaseCombatCharacter` | `typeof CBaseCombatCharacter` | **Availability:** `client` |
| `C_BaseEntity` | `typeof CBaseEntity` | **Availability:** `client` |
| `C_BaseModelEntity` | `typeof CBaseModelEntity` | **Availability:** `client` |
| `C_DOTA_Ability_Lua` | `typeof CDOTA_Ability_Lua` | **Availability:** `client` |
| `C_DOTA_BaseNPC` | `typeof CDOTA_BaseNPC` | **Availability:** `client` |
| `C_DOTA_BaseNPC_Hero` | `typeof CDOTA_BaseNPC_Hero` | **Availability:** `client` |
| `C_DOTA_Item` | `typeof CDOTA_Item` | **Availability:** `client` |
| `C_DOTA_Item_EmptyBottle` | `typeof CDOTA_Item_EmptyBottle` | **Availability:** `client` |
| `C_DOTA_Item_Lua` | `typeof CDOTA_Item_Lua` | **Availability:** `client` |
| `C_DOTABaseAbility` | `typeof CDOTABaseAbility` | **Availability:** `client` |
| `C_DOTAPlayerController` | `typeof CDOTAPlayerController` | **Availability:** `client` |
| `C_PointEntity` | `typeof CPointEntity` | **Availability:** `client` |
| `C_PointWorldText` | `typeof CPointWorldText` | **Availability:** `client` |
| `CBaseAnimatingActivity` | `DotaConstructor<CBaseAnimatingActivity>` | **Availability:** `both` |
| `CBaseAnimatingOverlay` | `DotaConstructor<CBaseAnimatingOverlay>` |  |
| `CBaseAnimGraph` | `DotaConstructor<CBaseAnimGraph>` | **Availability:** `both` |
| `CBaseCombatCharacter` | `DotaConstructor<CBaseCombatCharacter>` |  |
| `CBaseEntity` | `DotaConstructor<CBaseEntity>` |  |
| `CBaseModelEntity` | `DotaConstructor<CBaseModelEntity>` |  |
| `CBasePlayerController` | `DotaConstructor<CBasePlayerController>` |  |
| `CBasePlayerPawn` | `DotaConstructor<CBasePlayerPawn>` |  |
| `CBaseTrigger` | `DotaConstructor<CBaseTrigger>` |  |
| `CBodyComponent` | `DotaConstructor<CBodyComponent>` | **Availability:** `both` |
| `CCustomGameEventManager` | `DotaConstructor<CCustomGameEventManager>` |  |
| `CCustomNetTableManager` | `DotaConstructor<CCustomNetTableManager>` | **Availability:** `both` |
| `CDebugOverlayScriptHelper` | `DotaConstructor<CDebugOverlayScriptHelper>` | **Availability:** `both` |
| `CDOTA_Ability_Aghanim_Spear` | `DotaConstructor<CDOTA_Ability_Aghanim_Spear>` |  |
| `CDOTA_Ability_Animation_Attack` | `DotaConstructor<CDOTA_Ability_Animation_Attack>` |  |
| `CDOTA_Ability_Animation_TailSpin` | `DotaConstructor<CDOTA_Ability_Animation_TailSpin>` |  |
| `CDOTA_Ability_DataDriven` | `DotaConstructor<CDOTA_Ability_DataDriven>` |  |
| `CDOTA_Ability_Lua` | `DotaConstructor<CDOTA_Ability_Lua>` |  |
| `CDOTA_Ability_Nian_Dive` | `DotaConstructor<CDOTA_Ability_Nian_Dive>` |  |
| `CDOTA_Ability_Nian_Leap` | `DotaConstructor<CDOTA_Ability_Nian_Leap>` |  |
| `CDOTA_Ability_Nian_Roar` | `DotaConstructor<CDOTA_Ability_Nian_Roar>` |  |
| `CDOTA_BaseNPC` | `DotaConstructor<CDOTA_BaseNPC>` |  |
| `CDOTA_BaseNPC_Building` | `DotaConstructor<CDOTA_BaseNPC_Building>` |  |
| `CDOTA_BaseNPC_Creature` | `DotaConstructor<CDOTA_BaseNPC_Creature>` |  |
| `CDOTA_BaseNPC_Hero` | `DotaConstructor<CDOTA_BaseNPC_Hero>` |  |
| `CDOTA_BaseNPC_LotusPool` | `DotaConstructor<CDOTA_BaseNPC_LotusPool>` |  |
| `CDOTA_BaseNPC_NeutralItemStash` | `DotaConstructor<CDOTA_BaseNPC_NeutralItemStash>` |  |
| `CDOTA_BaseNPC_Shop` | `DotaConstructor<CDOTA_BaseNPC_Shop>` |  |
| `CDOTA_BaseNPC_Trap_Ward` | `DotaConstructor<CDOTA_BaseNPC_Trap_Ward>` |  |
| `CDOTA_BaseNPC_Watch_Tower` | `DotaConstructor<CDOTA_BaseNPC_Watch_Tower>` |  |
| `CDOTA_Buff` | `DotaConstructor<CDOTA_Buff>` | **Availability:** `both` |
| `CDOTA_CustomUIManager` | `DotaConstructor<CDOTA_CustomUIManager>` |  |
| `CDOTA_Item` | `DotaConstructor<CDOTA_Item>` |  |
| `CDOTA_Item_BagOfGold` | `DotaConstructor<CDOTA_Item_BagOfGold>` |  |
| `CDOTA_Item_DataDriven` | `DotaConstructor<CDOTA_Item_DataDriven>` |  |
| `CDOTA_Item_EmptyBottle` | `DotaConstructor<CDOTA_Item_EmptyBottle>` |  |
| `CDOTA_Item_Lua` | `DotaConstructor<CDOTA_Item_Lua>` |  |
| `CDOTA_Item_Physical` | `DotaConstructor<CDOTA_Item_Physical>` |  |
| `CDOTA_ItemSpawner` | `DotaConstructor<CDOTA_ItemSpawner>` |  |
| `CDOTA_MapTree` | `DotaConstructor<CDOTA_MapTree>` |  |
| `CDOTA_Modifier_Lua` | `DotaConstructor<CDOTA_Modifier_Lua>` | **Availability:** `both` |
| `CDOTA_Modifier_Lua_Horizontal_Motion` | `DotaConstructor<CDOTA_Modifier_Lua_Horizontal_Motion>` | **Availability:** `both` |
| `CDOTA_Modifier_Lua_Motion_Both` | `DotaConstructor<CDOTA_Modifier_Lua_Motion_Both>` | **Availability:** `both` |
| `CDOTA_Modifier_Lua_Vertical_Motion` | `DotaConstructor<CDOTA_Modifier_Lua_Vertical_Motion>` | **Availability:** `both` |
| `CDOTA_NeutralSpawner` | `DotaConstructor<CDOTA_NeutralSpawner>` |  |
| `CDOTA_PlayerResource` | `DotaConstructor<CDOTA_PlayerResource>` |  |
| `CDOTA_ShopTrigger` | `DotaConstructor<CDOTA_ShopTrigger>` |  |
| `CDOTA_SimpleObstruction` | `DotaConstructor<CDOTA_SimpleObstruction>` |  |
| `CDOTA_Unit_Courier` | `DotaConstructor<CDOTA_Unit_Courier>` |  |
| `CDOTA_Unit_CustomGameAnnouncer` | `DotaConstructor<CDOTA_Unit_CustomGameAnnouncer>` |  |
| `CDOTA_Unit_CustomGameAnnouncerAghanim` | `DotaConstructor<CDOTA_Unit_CustomGameAnnouncerAghanim>` |  |
| `CDOTA_Unit_Nian` | `DotaConstructor<CDOTA_Unit_Nian>` |  |
| `CDOTA_Unit_Scout` | `DotaConstructor<CDOTA_Unit_Scout>` |  |
| `CDOTABaseAbility` | `DotaConstructor<CDOTABaseAbility>` |  |
| `CDOTABaseGameMode` | `DotaConstructor<CDOTABaseGameMode>` |  |
| `CDOTAGameManager` | `DotaConstructor<CDOTAGameManager>` | **Availability:** `both` |
| `CDOTAGameRules` | `DotaConstructor<CDOTAGameRules>` | **Availability:** `both` |
| `CDOTAPlayerController` | `DotaConstructor<CDOTAPlayerController>` |  |
| `CDotaQuest` | `DotaConstructor<CDotaQuest>` |  |
| `CDotaSubquestBase` | `DotaConstructor<CDotaSubquestBase>` |  |
| `CDOTATutorial` | `DotaConstructor<CDOTATutorial>` |  |
| `CDotaTutorialNPCBlocker` | `DotaConstructor<CDotaTutorialNPCBlocker>` |  |
| `CDOTAVoteSystem` | `DotaConstructor<CDOTAVoteSystem>` |  |
| `CEntities` | `DotaConstructor<CEntities>` | **Availability:** `both` |
| `CEntityInstance` | `DotaConstructor<CEntityInstance>` | **Availability:** `both` |
| `CEntityScriptFramework` | `DotaConstructor<CEntityScriptFramework>` | **Availability:** `both` |
| `CEnvEntityMaker` | `DotaConstructor<CEnvEntityMaker>` |  |
| `CFoWBlockerRegion` | `DotaConstructor<CFoWBlockerRegion>` |  |
| `CInfoData` | `DotaConstructor<CInfoData>` |  |
| `CInfoPlayerStartDota` | `DotaConstructor<CInfoPlayerStartDota>` |  |
| `CInfoWorldLayer` | `DotaConstructor<CInfoWorldLayer>` | **Availability:** `both` |
| `CLogicRelay` | `DotaConstructor<CLogicRelay>` | **Availability:** `both` |
| `CLogicScript` | `DotaConstructor<CLogicScript>` |  |
| `CMarkupVolumeTagged` | `DotaConstructor<CMarkupVolumeTagged>` |  |
| `CNativeOutputs` | `DotaConstructor<CNativeOutputs>` | **Availability:** `both` |
| `Convars` | `Convars` | **Availability:** `both` |
| `CParticleSystem` | `DotaConstructor<CParticleSystem>` |  |
| `CPhysicsProp` | `DotaConstructor<CPhysicsProp>` |  |
| `CPointClientUIWorldPanel` | `DotaConstructor<CPointClientUIWorldPanel>` |  |
| `CPointEntity` | `DotaConstructor<CPointEntity>` |  |
| `CPointTemplate` | `DotaConstructor<CPointTemplate>` | **Availability:** `both` |
| `CPointWorldText` | `DotaConstructor<CPointWorldText>` |  |
| `CSceneEntity` | `DotaConstructor<CSceneEntity>` |  |
| `CScriptHeroList` | `DotaConstructor<CScriptHeroList>` |  |
| `CScriptHTTPRequest` | `DotaConstructor<CScriptHTTPRequest>` | **Availability:** `both` |
| `CScriptKeyValues` | `DotaConstructor<CScriptKeyValues>` | **Availability:** `both` |
| `CScriptParticleManager` | `DotaConstructor<CScriptParticleManager>` | **Availability:** `both` |
| `CScriptPrecacheContext` | `DotaConstructor<CScriptPrecacheContext>` | **Availability:** `both` |
| `CScriptUniformRandomStream` | `DotaConstructor<CScriptUniformRandomStream>` | **Availability:** `both` |
| `CTakeDamageInfo` | `DotaConstructor<CTakeDamageInfo>` |  |
| `CustomGameEventManager` | `CCustomGameEventManager` |  |
| `CustomNetTables` | `CCustomNetTableManager` |  |
| `CustomUI` | `CDOTA_CustomUIManager` |  |
| `debugoverlay` | `CDebugOverlayScriptHelper` |  |
| `DOTAGameManager` | `CDOTAGameManager` |  |
| `Entities` | `CEntities` |  |
| `GameRules` | `CDOTAGameRules` |  |
| `GlobalSys` | `GlobalSys` | **Availability:** `both` |
| `GridNav` | `GridNav` |  |
| `HeroList` | `CScriptHeroList` |  |
| `NativeFunctions` | `CEntityScriptFramework` |  |
| `ParticleManager` | `CScriptParticleManager` |  |
| `PlayerResource` | `CDOTA_PlayerResource` |  |
| `ProjectileManager` | `ProjectileManager` |  |
| `QAngle` | `DotaConstructor<QAngle> & ((x: number \| undefined, y: number \| undefined, z: number \| undefined) => QAngle)` | **Availability:** `both` |
| `SteamInfo` | `SteamInfo` |  |
| `Tutorial` | `CDOTATutorial` |  |
| `Uint64` | `DotaConstructor<Uint64>` |  |
| `Vector` | `DotaConstructor<Vector> & ((x?: number, y?: number, z?: number) => Vector)` | **Availability:** `both` |
| `VoteSystem` | `CDOTAVoteSystem` |  |
