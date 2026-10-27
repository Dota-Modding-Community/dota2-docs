# VScripts API



Server and client Lua API. 97 classes and 242 global functions.

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
- [QAngle](#qangle)
- [SteamInfo](#steaminfo)
- [Uint64](#uint64)
- [Vector](#vector)

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

`AddFOWViewer(teamId: DOTATeam_t, location: Vector, radius: float, duration: float, obstructedVision: bool): ViewerID`

Availability: `server`

Add temporary vision for a given team.

### AngleDiff

`AngleDiff(arg1: float, arg2: float): float`

Availability: `both`

Returns the number of degrees difference between two yaw angles.

### AnglesToVector

`AnglesToVector(arg1: QAngle): Vector`

Availability: `both`

Generate a vector given a QAngles.

### AppendToLogFile

`AppendToLogFile(arg1: string, arg2: string): nil`

Availability: `both` · **Deprecated:** AppendToLogFile is deprecated. Print to the console for logging instead.

### ApplyDamage

`ApplyDamage(options: ApplyDamageOptions): float`

Availability: `server`

Damage an npc.

### AxisAngleToQuaternion

`AxisAngleToQuaternion(arg1: Vector, arg2: float): Quaternion`

Availability: `both`

Constructs a quaternion representing a rotation by angle around the specified vector axis.

### CalcClosestPointOnEntityOBB

`CalcClosestPointOnEntityOBB(arg1: handle, arg2: Vector): Vector`

Availability: `both`

Compute the closest point on the OBB of an entity.

### CalcDistanceBetweenEntityOBB

`CalcDistanceBetweenEntityOBB(arg1: handle, arg2: handle): float`

Availability: `both`

Compute the distance between two entity OBB. A negative return value indicates an input error. A return value of zero indicates that the OBBs are overlapping.

### CalcDistanceToLineSegment2D

`CalcDistanceToLineSegment2D(arg1: Vector, arg2: Vector, arg3: Vector): float`

Availability: `both`

### CancelEntityIOEvents

`CancelEntityIOEvents(arg1: ehandle): nil`

Availability: `both`

Create all I/O events for a particular entity.

### CenterCameraOnUnit

`CenterCameraOnUnit(playerId: PlayerID, unit: CBaseEntity | nil): nil`

Availability: `server`

Centers each players' camera on a unit.

### ClearTeamCustomHealthbarColor

`ClearTeamCustomHealthbarColor(team: DOTATeam_t): nil`

Availability: `server`

### CreateDamageInfo

`CreateDamageInfo(arg1: handle, arg2: handle, arg3: Vector, arg4: Vector, arg5: float, arg6: int): CTakeDamageInfo`

Availability: `server`

Allocate a damageinfo object, used as an argument to TakeDamage(). Call DestroyDamageInfo( hInfo ) to free the object.

### CreateEffect

`CreateEffect(arg1: handle): bool`

Availability: `both`

Pass table - Inputs: entity, effect.

### CreateHeroForPlayer

`CreateHeroForPlayer(heroName: string, player: CDOTAPlayerController): CDOTA_BaseNPC_Hero`

Availability: `server`

Creates a DOTA hero by its dota_npc_units.txt name and sets it as the given player's controlled hero.

### CreateHTTPRequest

`CreateHTTPRequest(method: string, url: string): CScriptHTTPRequest`

Availability: `both`

Create an HTTP request.

### CreateHTTPRequestScriptVM

`CreateHTTPRequestScriptVM(method: string, url: string): CScriptHTTPRequest`

Availability: `both`

Create an HTTP request.

### CreateIllusions

`CreateIllusions(owner: CBaseEntity, heroToCopy: CDOTA_BaseNPC_Hero, modifierKeys: CreateIllusionsModifierKeys, numIllusions: int, padding: int, scramblePosition: bool, findClearSpace: bool): {'kind': 'array', 'types': ['CDOTA_BaseNPC_Hero']}`

Availability: `server`

Create illusions of the passed hero that belong to passed unit using passed modifier data.

### CreateItem

`CreateItem(itemName: string, owner: CDOTAPlayerController | nil, purchaser: CDOTA_BaseNPC_Hero | nil): CDOTA_Item, nil`

Availability: `server`

Create a DOTA item.

### CreateItemOnPositionForLaunch

`CreateItemOnPositionForLaunch(location: Vector, item: CDOTA_Item | nil): CDOTA_Item_Physical`

Availability: `server`

Create a physical item at a given location, can start in air (but doesn't clear a space).

### CreateItemOnPositionSync

`CreateItemOnPositionSync(location: Vector, item: CDOTA_Item | nil): CDOTA_Item_Physical`

Availability: `server`

Create a physical item at a given location.

### CreateModifierThinker

`CreateModifierThinker(caster: CDOTA_BaseNPC | nil, ability: CDOTABaseAbility | nil, modifierName: string, paramTable: table | nil, origin: Vector, teamNumber: DOTATeam_t, phantomBlocker: bool): CDOTA_BaseNPC`

Availability: `server`

Create a modifier not associated with an NPC.

### CreateRune

`CreateRune(location: Vector, runeType: DOTA_RUNES): CBaseAnimatingActivity`

Availability: `server`

Create a rune of the specified type.

### CreateSceneEntity

`CreateSceneEntity(arg1: string): CBaseAnimatingActivity`

Availability: `server`

Create a scene entity to play the specified scene.

### CreateTempTree

`CreateTempTree(location: Vector, duration: float): CBaseAnimatingActivity`

Availability: `server`

Create a temporary tree, uses a default tree model.

### CreateTempTreeWithModel

`CreateTempTreeWithModel(location: Vector, duration: float, modelName: string): CBaseAnimatingActivity`

Availability: `server`

Create a temporary tree, specifying the tree model name.

### CreateTrigger

`CreateTrigger(arg1: Vector, arg2: Vector, arg3: Vector): CBaseTrigger`

Availability: `server`

Creates and returns an AABB trigger.

### CreateTriggerRadiusApproximate

`CreateTriggerRadiusApproximate(vecOrigin: Vector, radius: float): CBaseTrigger`

Availability: `server`

Creates and returns an AABB trigger thats bigger than the radius provided.

### CreateUniformRandomStream

`CreateUniformRandomStream(seed: int): CScriptUniformRandomStream`

Availability: `both`

Creates a separate random number stream.

### CreateUnitByName

`CreateUnitByName(unitName: string, location: Vector, findClearSpace: bool, npcOwner: CBaseEntity | nil, entityOwner: CBaseEntity | nil, team: DOTATeam_t): CDOTA_BaseNPC`

Availability: `server`

Creates a unit by its dota_npc_units.txt name.
The spawned unit will not be controllable by default. You can use unit.SetControllableByPlayer() to change this.
Warning: mass synchronous unit spawning may be slow. Prefer CreateUnitByNameAsync unless synchronous access is required.

### CreateUnitByNameAsync

`CreateUnitByNameAsync(unitName: string, location: Vector, findClearSpace: bool, npcOwner: CBaseEntity | nil, entityOwner: CBaseEntity | nil, team: DOTATeam_t, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'unit', 'types': ['CDOTA_BaseNPC']}]}): SpawnGroupHandle`

Availability: `server`

Creates a unit by its dota_npc_units.txt name.
The spawned unit will not be controllable by default. You can use unit.SetControllableByPlayer() to change this.

### CreateUnitFromTable

`CreateUnitFromTable(options: CreateUnitFromTableOptions, location: Vector): CDOTA_BaseNPC`

Availability: `server`

Creates a DOTA unit by its dota_npc_units.txt name from a table of entity key values and a position to spawn at.

### CrossVectors

`CrossVectors(arg1: Vector, arg2: Vector): Vector`

Availability: `both`

Cross product between two vectors.

### cvar_getf

`cvar_getf(arg1: string): float`

Availability: `both`

Gets the value of the given cvar, as a float.

### cvar_setf

`cvar_setf(arg1: string, arg2: float): bool`

Availability: `both`

Sets the value of the given cvar, as a float.

### DebugBreak

`DebugBreak(): nil`

Availability: `both`

Breaks in the debugger.

### DebugChangeTeam

`DebugChangeTeam(arg1: handle): nil`

Availability: `server`

Changes the team of the hero.

### DebugCreateHeroWithVariant

`DebugCreateHeroWithVariant(arg1: handle, arg2: string, arg3: int, arg4: int, arg5: bool, arg6: handle): int`

Availability: `server`

Creates a unit with a specified hero variant, controllable by the specified player.

### DebugCreateUnit

`DebugCreateUnit(playerOwner: CDOTAPlayerController, unitName: string, team: DOTATeam_t, arg4: bool, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'unit', 'types': ['CDOTA_BaseNPC']}]}): int`

Availability: `server`

Creates a test unit controllable by the specified player.

### DebugDrawBox

`DebugDrawBox(arg1: Vector, arg2: Vector, arg3: Vector, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float): nil`

Availability: `both`

Draw a debug overlay box.

### DebugDrawBoxDirection

`DebugDrawBoxDirection(cent: Vector, min: Vector, max: Vector, forward: Vector, rgb: Vector, a: float, duration: float): nil`

Availability: `both`

Draw a debug forward box.

### DebugDrawCircle

`DebugDrawCircle(center: Vector, rgb: Vector, a: float, rad: float, ztest: bool, duration: float): nil`

Availability: `both`

Draw a debug circle.

### DebugDrawClear

`DebugDrawClear(): nil`

Availability: `both`

Try to clear all the debug overlay info.

### DebugDrawLine

`DebugDrawLine(origin: Vector, target: Vector, r: int, g: int, b: int, ztest: bool, duration: float): nil`

Availability: `both`

Draw a debug overlay line.

### DebugDrawLine_vCol

`DebugDrawLine_vCol(arg1: Vector, arg2: Vector, arg3: Vector, arg4: bool, arg5: float): nil`

Availability: `both`

Draw a debug line using color vec.

### DebugDrawScreenTextLine

`DebugDrawScreenTextLine(x: float, y: float, lineOffset: int, text: string, r: int, g: int, b: int, a: int, duration: float): nil`

Availability: `both`

Draw text with a line offset.

### DebugDrawSphere

`DebugDrawSphere(center: Vector, rgb: Vector, a: float, rad: float, ztest: bool, duration: float): nil`

Availability: `both`

Draw a debug sphere.

### DebugDrawText

`DebugDrawText(origin: Vector, text: string, viewCheck: bool, duration: float): nil`

Availability: `both`

Draw text in 3d.

### DebugScreenTextPretty

`DebugScreenTextPretty(x: float, y: float, lineOffset: int, text: string, r: int, g: int, b: int, a: int, duration: float, font: string, size: int, bold: bool): nil`

Availability: `both`

Draw pretty debug text.

### DeepPrintTable

`DeepPrintTable(table: table | nil): nil`

Availability: `both`

Print out a table (and subtables) to the console.

### DestroyDamageInfo

`DestroyDamageInfo(damageInfo: CTakeDamageInfo): nil`

Availability: `server`

Free a damageinfo object that was created with CreateDamageInfo().

### DisconnectClient

`DisconnectClient(arg1: int, arg2: bool): nil`

Availability: `server`

Kick a specific player from the game.

### DoCleaveAttack

`DoCleaveAttack(attacker: CDOTA_BaseNPC, target: CDOTA_BaseNPC, ability: CDOTABaseAbility | nil, damage: float, startRadius: float, endRadius: float, distance: float, effectName: string): int`

Availability: `server`

### DoEntFire

`DoEntFire(arg1: string, arg2: string, arg3: string, arg4: float, arg5: handle, arg6: handle): nil`

Availability: `server`

Generate and entity i/o event.

### DoEntFireByInstanceHandle

`DoEntFireByInstanceHandle(arg1: handle, arg2: string, arg3: string, arg4: float, arg5: handle, arg6: handle): nil`

Availability: `server`

Generate and entity i/o event.

### DoIncludeScript

`DoIncludeScript(arg1: string, arg2: handle): bool`

Availability: `both`

Execute a script (internal).

### DoScriptAssert

`DoScriptAssert(arg1: bool, arg2: string): nil`

Availability: `both`

Asserts the passed in value. Prints out a message and brings up the assert dialog.

### DOTA_SpawnMapAtPosition

`DOTA_SpawnMapAtPosition(mapName: string, location: Vector, deferCompletion: bool, onReadyToSpawn: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'spawnGroupHandle', 'types': ['SpawnGroupHandle']}]}, onSpawnComplete: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'spawnGroupHandle', 'types': ['SpawnGroupHandle']}]}, context: table | nil): SpawnGroupHandle`

Availability: `server`

Spawn a .vmap at the target location.

### DotProduct

`DotProduct(arg1: Vector, arg2: Vector): float`

Availability: `server`

### DoUniqueString

`DoUniqueString(seed: string): string`

Availability: `both`

Generate a string guaranteed to be unique across the life of the script VM, with an optional root string. Useful for adding data to tables when not sure what keys are already in use in that table.

### DropNeutralItemAtPositionForHero

`DropNeutralItemAtPositionForHero(itemName: string, location: Vector, unit: CDOTA_BaseNPC, tier: int, arg5: bool): CDOTA_Item_Physical`

Availability: `server`

Drop a neutral item for the team of the hero at the given tier.

### DropNeutralItemAtPositionForHeroWithOffset

`DropNeutralItemAtPositionForHeroWithOffset(arg1: string, arg2: Vector, arg3: handle, arg4: int, arg5: bool, arg6: Vector): handle`

Availability: `server`

Drop a neutral item for the team of the hero at the given tier.

### Dynamic_Wrap

`Dynamic_Wrap(context: table, name: string): unknown`

Availability: `both`

A function to re-lookup a function by name every time.

### EmitAnnouncerSound

`EmitAnnouncerSound(soundName: string): nil`

Availability: `server`

Emit an announcer sound for all players.

### EmitAnnouncerSoundForPlayer

`EmitAnnouncerSoundForPlayer(soundName: string, playerId: PlayerID): nil`

Availability: `server`

Emit an announcer sound for a player.

### EmitAnnouncerSoundForTeam

`EmitAnnouncerSoundForTeam(soundName: string, team: DOTATeam_t): nil`

Availability: `server`

Emit an announcer sound for a team.

### EmitAnnouncerSoundForTeamOnLocation

`EmitAnnouncerSoundForTeamOnLocation(soundName: string, team: DOTATeam_t, location: Vector): nil`

Availability: `server`

Emit an announcer sound for a team at a specific location.

### EmitGlobalSound

`EmitGlobalSound(soundName: string): nil`

Availability: `server`

Play named sound for all players.

### EmitSoundOn

`EmitSoundOn(soundName: string, entity: CBaseEntity): nil`

Availability: `both`

Play named sound on Entity.

### EmitSoundOnClient

`EmitSoundOnClient(soundName: string, arg2: handle): nil`

Availability: `both`

Play named sound only on the client for the passed in player.

### EmitSoundOnEntityForPlayer

`EmitSoundOnEntityForPlayer(arg1: string, arg2: handle, arg3: int): nil`

Availability: `server`

Emit a sound on an entity for only a specific player.

### EmitSoundOnLocationForAllies

`EmitSoundOnLocationForAllies(location: Vector, soundName: string, caster: CBaseEntity): nil`

Availability: `server`

Emit a sound on a location from a unit, only for players allied with that unit.

### EmitSoundOnLocationForPlayer

`EmitSoundOnLocationForPlayer(arg1: string, arg2: Vector, arg3: int): nil`

Availability: `server`

Emit a sound on a location for only a specific player.

### EmitSoundOnLocationWithCaster

`EmitSoundOnLocationWithCaster(location: Vector, soundName: string, caster: CDOTA_BaseNPC): nil`

Availability: `server`

Emit a sound on a location from a unit.

### EntIndexToHScript

`EntIndexToHScript(entityIndex: EntityIndex): CBaseEntity, nil`

Availability: `both`

Turn an entity index integer to an HScript representing that entity's script instance.

### ExecuteOrderFromTable

`ExecuteOrderFromTable(order: ExecuteOrderOptions): nil`

Availability: `server`

Issue an order from a script table.

### ExponentialDecay

`ExponentialDecay(arg1: float, arg2: float, arg3: float): float`

Availability: `both`

Smooth curve decreasing slower as it approaches zero.

### FindClearRandomPositionAroundUnit

`FindClearRandomPositionAroundUnit(arg1: handle, arg2: handle, arg3: int): bool`

Availability: `server`

Finds a clear random position around a given target unit, using the target unit's padded collision radius.

### FindClearSpaceForUnit

`FindClearSpaceForUnit(unit: CDOTA_BaseNPC, location: Vector, arg3: bool): bool`

Availability: `server`

Place a unit somewhere not already occupied.

### FindSpawnEntityForTeam

`FindSpawnEntityForTeam(team: DOTATeam_t): CBaseEntity, nil`

Availability: `server`

Find a spawn point for the given team.

### FindUnitsInLine

`FindUnitsInLine(team: DOTATeam_t, startPos: Vector, endPos: Vector, cacheUnit: CBaseEntity | nil, width: float, teamFilter: DOTA_UNIT_TARGET_TEAM, typeFilter: DOTA_UNIT_TARGET_TYPE, flagFilter: DOTA_UNIT_TARGET_FLAGS): {'kind': 'array', 'types': ['CDOTA_BaseNPC']}`

Availability: `server`

Find units that intersect the given line with the given flags.

### FindUnitsInRadius

`FindUnitsInRadius(team: DOTATeam_t, location: Vector, cacheUnit: CBaseEntity | nil, radius: float, teamFilter: DOTA_UNIT_TARGET_TEAM, typeFilter: DOTA_UNIT_TARGET_TYPE, flagFilter: DOTA_UNIT_TARGET_FLAGS, order: FindOrder, canGrowCache: bool): {'kind': 'array', 'types': ['CDOTA_BaseNPC']}`

Availability: `server`

Finds the units in a given radius with the given flags.

### FireEntityIOInputNameOnly

`FireEntityIOInputNameOnly(arg1: ehandle, arg2: string): nil`

Availability: `both`

Fire Entity's Action Input w/no data.

### FireEntityIOInputString

`FireEntityIOInputString(arg1: ehandle, arg2: string, arg3: string): nil`

Availability: `both`

Fire Entity's Action Input with passed String - you own the memory.

### FireEntityIOInputVec

`FireEntityIOInputVec(arg1: ehandle, arg2: string, arg3: Vector): nil`

Availability: `both`

Fire Entity's Action Input with passed Vector - you own the memory.

### FireGameEvent

`FireGameEvent(eventName: string, eventData: table): nil`

Availability: `both`

Fire a game event.

### FireGameEventLocal

`FireGameEventLocal(eventName: string, eventData: table): nil`

Availability: `both`

Fire a game event without broadcasting to the client.

### FrameTime

`FrameTime(): float`

Availability: `both`

Get the time spent on the server in the last frame.

### GetAbilityKeyValuesByName

`GetAbilityKeyValuesByName(arg1: string): table`

Availability: `both`

Get ability data by ability name.

### GetAbilityTextureNameForAbility

`GetAbilityTextureNameForAbility(abilityName: string): string`

Availability: `both`

Gets the ability texture name for an ability.

### GetActiveSpawnGroupHandle

`GetActiveSpawnGroupHandle(): SpawnGroupHandle`

Availability: `both`

Returns the currently active spawn group handle.

### GetClearSpaceForUnit

`GetClearSpaceForUnit(arg1: handle, arg2: Vector): Vector`

Availability: `server`

Returns a location for the unit that is not already occupied.

### GetDedicatedServerKey

`GetDedicatedServerKey(version: string): string`

Availability: `server` · **Deprecated:** This function is unsafe. Prefer using `GetDedicatedServerKeyV2` instead.

### GetDedicatedServerKeyV2

`GetDedicatedServerKeyV2(version: string): string`

Availability: `server`

### GetDedicatedServerKeyV3

`GetDedicatedServerKeyV3(version: string): string`

Availability: `server`

### GetEntityIndexForTreeId

`GetEntityIndexForTreeId(treeId: uint): EntityIndex`

Availability: `server`

Get the enity index for a tree id specified as the entindex_target of a DOTA_UNIT_ORDER_CAST_TARGET_TREE.

### GetFrameCount

`GetFrameCount(): int`

Availability: `both`

Returns the engines current frame count.

### GetGroundHeight

`GetGroundHeight(location: Vector, unitHull: CDOTA_BaseNPC | nil): float`

Availability: `server`

### GetGroundPosition

`GetGroundPosition(location: Vector, unitHull: CDOTA_BaseNPC | nil): Vector`

Availability: `server`

Returns the supplied position moved to the ground. Second parameter is an NPC for measuring movement collision hull offset.

### GetItemCost

`GetItemCost(arg1: string): int`

Availability: `server`

Get the cost of an item by name.

### GetItemDefOwnedCount

`GetItemDefOwnedCount(arg1: int, arg2: int): int`

Availability: `server`

### GetItemDefQuantity

`GetItemDefQuantity(arg1: int, arg2: int): int`

Availability: `server`

### GetListenServerHost

`GetListenServerHost(): CDOTAPlayerController`

Availability: `both`

Get the local player on a listen server.

### GetLobbyEventGameDetails

`GetLobbyEventGameDetails(): table`

Availability: `server`

### GetLocalPlayerID

`GetLocalPlayerID(): PlayerID`

Availability: `client`

Get the local player ID.

### GetLocalPlayerTeam

`GetLocalPlayerTeam(arg1: int): DOTATeam_t`

Availability: `client`

Get the local player team.

### GetMapName

`GetMapName(): string`

Availability: `both`

Get the name of the map.

### GetMaxOutputDelay

`GetMaxOutputDelay(arg1: ehandle, arg2: string): float`

Availability: `both`

Get the longest delay for all events attached to an output.

### GetPhysAngularVelocity

`GetPhysAngularVelocity(arg1: handle): Vector`

Availability: `both`

Get Angular Velocity for VPHYS or normal object. Returns a vector of the axis of rotation, multiplied by the degrees of rotation per second.

### GetPhysVelocity

`GetPhysVelocity(arg1: handle): Vector`

Availability: `both`

Get Velocity for VPHYS or normal object.

### GetPotentialNeutralItemDrop

`GetPotentialNeutralItemDrop(tier: int, team: DOTATeam_t): string`

Availability: `server`

Given the item tier and the team, roll for the name of a valid neutral item drop, considering previous drops and consumables.

### GetSystemDate

`GetSystemDate(): string`

Availability: `server`

Get the current real world date.

### GetSystemTime

`GetSystemTime(): string`

Availability: `server`

Get the current real world time.

### GetSystemTimeMS

`GetSystemTimeMS(): double`

Availability: `server`

Get system time in milliseconds.

### GetTargetAOELocation

`GetTargetAOELocation(arg1: int, arg2: int, arg3: int, arg4: Vector, arg5: int, arg6: int, arg7: int): Vector`

Availability: `server`

### GetTargetLinearLocation

`GetTargetLinearLocation(arg1: int, arg2: int, arg3: int, arg4: Vector, arg5: int, arg6: int, arg7: int): Vector`

Availability: `server`

### GetTeamHeroKills

`GetTeamHeroKills(team: DOTATeam_t): int`

Availability: `server`

### GetTeamName

`GetTeamName(team: DOTATeam_t): string`

Availability: `server`

### GetTreeIdForEntityIndex

`GetTreeIdForEntityIndex(entityIndex: EntityIndex): int`

Availability: `server`

Given and entity index of a tree, get the tree id for use for use with with unit orders.

### GetUnitKeyValuesByName

`GetUnitKeyValuesByName(arg1: string): table`

Availability: `both`

Get unit data by ability name.

### GetWorldMaxX

`GetWorldMaxX(): float`

Availability: `server`

Gets the world's maximum X position.

### GetWorldMaxY

`GetWorldMaxY(): float`

Availability: `server`

Gets the world's maximum Y position.

### GetWorldMinX

`GetWorldMinX(): float`

Availability: `server`

Gets the world's minimum X position.

### GetWorldMinY

`GetWorldMinY(): float`

Availability: `server`

Gets the world's minimum Y position.

### GetXPNeededToReachNextLevel

`GetXPNeededToReachNextLevel(level: int): int`

Availability: `server`

Get amount of XP required to reach the next level.

### HeroMaxLevel

`HeroMaxLevel(arg1: handle): nil`

Availability: `server`

Max out a hero's level and give them all appropriate abilities and talents.

### InitLogFile

`InitLogFile(arg1: string, arg2: string): nil`

Availability: `both` · **Deprecated:** InitLogFile is deprecated. Print to the console for logging instead.

### IsClient

`IsClient(): bool`

Availability: `both`

Returns true if this is lua running from the client.dll.

### IsDedicatedServer

`IsDedicatedServer(): bool`

Availability: `both`

Returns true if this server is a dedicated server.

### IsDotaAltPressed

`IsDotaAltPressed(): bool`

Availability: `client`

Returns true if whatever alt is remapped to is pressed.

### IsDotaCtrlPressed

`IsDotaCtrlPressed(): bool`

Availability: `client`

Returns true if whatever ctrl is remapped to is pressed.

### IsInToolsMode

`IsInToolsMode(): bool`

Availability: `both`

Returns true if this is lua running within tools mode.

### IsLocationVisible

`IsLocationVisible(team: DOTATeam_t, location: Vector): bool`

Availability: `server`

Ask fog of war if a location is visible to a certain team.

### IsMangoTree

`IsMangoTree(entity: CBaseEntity): bool`

Availability: `server`

Is this entity a mango tree? (hEntity).

### IsMarkedForDeletion

`IsMarkedForDeletion(entity: CBaseEntity): bool`

Availability: `both`

Returns true if the entity is valid and marked for deletion.

### IsServer

`IsServer(): bool`

Availability: `both`

Returns true if this is lua running from the server.dll.

### IsUnitInValidPosition

`IsUnitInValidPosition(unit: CBaseEntity): bool`

Availability: `server`

Returns true if the unit is in a valid position in the gridnav.

### IsValidEntity

`IsValidEntity(entity: table | nil): bool`

Availability: `both`

Checks to see if the given hScript is a valid entity.

### LerpVectors

`LerpVectors(arg1: Vector, arg2: Vector, arg3: float): Vector`

Availability: `both`

Lerp between two vectors by a float factor returning new vector.

### LimitPathingSearchDepth

`LimitPathingSearchDepth(arg1: float): nil`

Availability: `server`

Set the limit on the pathfinding search space.

### LinkLuaModifier

`LinkLuaModifier(className: string, filePath: string, luaModifierType: LuaModifierType): nil`

Availability: `both`

Link a lua-defined modifier with the associated class.

### ListenToGameEvent

`ListenToGameEvent(eventName: string, listener: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'event', 'types': ['table']}]}, context: table | nil): EventListenerID`

Availability: `both`

Register as a listener for a game event from script.

### LoadKeyValues

`LoadKeyValues(filePath: string): table`

Availability: `both`

Creates a table from the specified keyvalues text file.

### LoadKeyValuesFromString

`LoadKeyValuesFromString(kvString: string): table`

Availability: `both`

Creates a table from the specified keyvalues string.

### LocalTime

`LocalTime(): LocalTime`

Availability: `both`

Get the current local time.

### MakeStringToken

`MakeStringToken(arg1: string): int`

Availability: `both`

Checks to see if the given hScript is a valid entity.

### ManuallyTriggerSpawnGroupCompletion

`ManuallyTriggerSpawnGroupCompletion(handle: SpawnGroupHandle): nil`

Availability: `both`

Triggers the creation of entities in a manually-completed spawn group.

### MinimapEvent

`MinimapEvent(team: DOTATeam_t, entity: CBaseEntity, xCoord: int, yCoord: int, eventType: DOTAMinimapEvent_t, eventDuration: int): nil`

Availability: `server`

Start a minimap event.

### Msg

`Msg(message: string): nil`

Availability: `both`

Print a message.

### PauseGame

`PauseGame(paused: bool): nil`

Availability: `server`

Pause or unpause the game.

### Plat_FloatTime

`Plat_FloatTime(): float`

Availability: `both`

Get the current float time from the engine.

### PlayerInstanceFromIndex

`PlayerInstanceFromIndex(entityIndex: EntityIndex): CDOTAPlayerController, nil`

Availability: `both`

Get a script instance of a player by index.

### PrecacheEntityFromTable

`PrecacheEntityFromTable(arg1: string, arg2: handle, context: CScriptPrecacheContext): nil`

Availability: `both`

Precache an entity from KeyValues in table.

### PrecacheEntityListFromTable

`PrecacheEntityListFromTable(arg1: handle, context: CScriptPrecacheContext): nil`

Availability: `both`

Precache a list of entity KeyValues tables.

### PrecacheItemByNameAsync

`PrecacheItemByNameAsync(itemName: string, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'precacheId', 'types': ['int']}]}): nil`

Availability: `server`

Asynchronously precaches a DOTA item by its dota_npc_items.txt name, provides a callback when it's finished.

### PrecacheItemByNameSync

`PrecacheItemByNameSync(itemName: string, context: CScriptPrecacheContext): nil`

Availability: `server`

Precaches a DOTA item by its dota_npc_items.txt name.

### PrecacheModel

`PrecacheModel(modelName: string, context: CScriptPrecacheContext): nil`

Availability: `server`

Manually precache a single model.

### PrecacheResource

`PrecacheResource(arg1: string, arg2: string, context: CScriptPrecacheContext): nil`

Availability: `server`

Manually precache a single resource.

### PrecacheUnitByNameAsync

`PrecacheUnitByNameAsync(unitName: string, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'precacheId', 'types': ['int']}]}, playerId: PlayerID | nil): nil`

Availability: `server`

Asynchronously precaches a DOTA unit by its dota_npc_units.txt name, provides a callback when it's finished.

### PrecacheUnitByNameSync

`PrecacheUnitByNameSync(unitName: string, context: CScriptPrecacheContext, playerId: PlayerID | nil): nil`

Availability: `server`

Precaches a DOTA unit by its dota_npc_units.txt name.

### PrecacheUnitFromTableAsync

`PrecacheUnitFromTableAsync(arg1: handle, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'precacheId', 'types': ['int']}]}): nil`

Availability: `server`

Precaches a DOTA unit from a table of entity key values.

### PrecacheUnitFromTableSync

`PrecacheUnitFromTableSync(arg1: handle, context: CScriptPrecacheContext): nil`

Availability: `server`

Precaches a DOTA unit from a table of entity key values.

### PrintLinkedConsoleMessage

`PrintLinkedConsoleMessage(message: string, tooltip: string): nil`

Availability: `both`

Print a console message with a linked console command.

### QSlerp

`QSlerp(from_angle: QAngle, to_angle: QAngle, time: float): QAngle`

Availability: `both`

Spherical lerp of angle from->to based on time.

### RandomFloat

`RandomFloat(min: float, max: float): float`

Availability: `server`

Get a random float within a range.

### RandomFloatWrapper

`RandomFloatWrapper(arg1: float, arg2: float): float`

Availability: `both`

Generate a random floating point number within a range, inclusive.

### RandomInt

`RandomInt(min: int, max: int): int`

Availability: `both`

Get a random int within a range.

### RandomVector

`RandomVector(length: float): Vector`

Availability: `server`

Get a random 2D vector of the given length.

### RecordNeutralItemEarned

`RecordNeutralItemEarned(arg1: handle, arg2: handle, arg3: int): nil`

Availability: `server`

Record in player resources that a new neutral item has been created, if it hasn't already been, and show a toast.

### RegisterCustomAnimationScriptForModel

`RegisterCustomAnimationScriptForModel(arg1: string, arg2: string): nil`

Availability: `server`

Register a custom animation script to run when a model loads.

### RegisterSpawnGroupFilterProxy

`RegisterSpawnGroupFilterProxy(arg1: string): nil`

Availability: `both`

Create a C proxy for a script-based spawn group filter.

### ReloadMOTD

`ReloadMOTD(): nil`

Availability: `both`

Reloads the MotD file.

### RemoveFOWViewer

`RemoveFOWViewer(teamId: DOTATeam_t, viewerId: ViewerID): nil`

Availability: `server`

Remove temporary vision for a given team.

### RemoveSpawnGroupFilterProxy

`RemoveSpawnGroupFilterProxy(arg1: string): nil`

Availability: `both`

Remove the C proxy for a script-based spawn group filter.

### ResolveNPCPositions

`ResolveNPCPositions(location: Vector, radius: float): nil`

Availability: `server`

Check and fix units that have been assigned a position inside collision radius of other NPCs.

### RollPercentage

`RollPercentage(successPercentage: int): bool`

Availability: `server`

Rolls a number from 1 to 100 and returns true if the roll is less than or equal to the number specified.

### RollPseudoRandomPercentage

`RollPseudoRandomPercentage(chance: uint, pseudoRandomId: PseudoRandom, unit: CDOTA_BaseNPC): bool`

Availability: `server`

### RotateOrientation

`RotateOrientation(arg1: QAngle, arg2: QAngle): QAngle`

Availability: `both`

Rotate a QAngle by another QAngle.

### RotatePosition

`RotatePosition(arg1: Vector, arg2: QAngle, arg3: Vector): Vector`

Availability: `both`

Rotate a Vector around a point.

### RotateQuaternionByAxisAngle

`RotateQuaternionByAxisAngle(arg1: Quaternion, arg2: Vector, arg3: float): Quaternion`

Availability: `both`

Rotates a quaternion by the specified angle around the specified vector axis.

### RotationDelta

`RotationDelta(arg1: QAngle, arg2: QAngle): QAngle`

Availability: `both`

Find the delta between two QAngles.

### RotationDeltaAsAngularVelocity

`RotationDeltaAsAngularVelocity(arg1: QAngle, arg2: QAngle): Vector`

Availability: `both`

Converts delta QAngle to an angular velocity Vector.

### Say

`Say(entity: CBaseEntity | nil, message: string, teamOnly: bool): nil`

Availability: `server`

Have Entity say string, and teamOnly or not.

### ScreenShake

`ScreenShake(center: Vector, amplitude: float, frequency: float, duration: float, radius: float, command: {'kind': 'literal', 'value': 0} | {'kind': 'literal', 'value': 1}, airShake: bool): nil`

Availability: `both`

Start a screenshake.

### Script_RandomFloat

`Script_RandomFloat(arg1: float, arg2: float): float`

Availability: `both`

Get a random float within a range.

### Script_RemapValClamped

`Script_RemapValClamped(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float): float`

Availability: `server`

RemapValClamped.

### SendOverheadEventMessage

`SendOverheadEventMessage(sendToPlayer: CDOTAPlayerController | nil, messageType: DOTA_OVERHEAD_ALERT, targetEntity: CDOTA_BaseNPC, value: int, sourcePlayer: CDOTAPlayerController | nil): nil`

Availability: `server`

### SendToConsole

`SendToConsole(arg1: string): nil`

Availability: `both`

Send a string to the console as a client command.

### SendToServerConsole

`SendToServerConsole(arg1: string): nil`

Availability: `server`

Send a string to the console as a server command.

### SetOpvarFloatAll

`SetOpvarFloatAll(arg1: string, arg2: string, arg3: string, arg4: float): nil`

Availability: `both`

Sets an opvar value for all players.

### SetOpvarFloatPlayer

`SetOpvarFloatPlayer(arg1: string, arg2: string, arg3: string, arg4: float, arg5: handle): nil`

Availability: `both`

Sets an opvar value for a single player.

### SetPhysAngularVelocity

`SetPhysAngularVelocity(arg1: handle, arg2: Vector): nil`

Availability: `both`

Set Angular Velocity for VPHYS or normal object, from a vector of the axis of rotation, multiplied by the degrees of rotation per second.

### SetQuestName

`SetQuestName(arg1: string): nil`

Availability: `both`

Set the current quest name.

### SetQuestPhase

`SetQuestPhase(arg1: int): nil`

Availability: `both`

Set the current quest phase.

### SetRenderingEnabled

`SetRenderingEnabled(arg1: ehandle, arg2: bool): nil`

Availability: `both` · **Deprecated:** Instantly crashes the game.

Set rendering on/off for an ehandle.

### SetTeamCustomHealthbarColor

`SetTeamCustomHealthbarColor(team: DOTATeam_t, r: int, g: int, b: int): nil`

Availability: `server`

### ShowCustomHeaderMessage

`ShowCustomHeaderMessage(message: string, playerId: PlayerID, value: int, time: float): nil`

Availability: `server`

Supports localized strings - %s1 = PlayerName, %s2 = Value, %s3 = TeamName.

### ShowGenericPopup

`ShowGenericPopup(arg1: string, arg2: string, arg3: string, arg4: string, arg5: int): nil`

Availability: `server`

Show a generic popup dialog for all players.

### ShowGenericPopupToPlayer

`ShowGenericPopupToPlayer(arg1: handle, arg2: string, arg3: string, arg4: string, arg5: string, arg6: int): nil`

Availability: `server`

Show a generic popup dialog to a specific player.

### ShowMessage

`ShowMessage(arg1: string): nil`

Availability: `server`

Print a hud message on all clients.

### SpawnDOTAShopTriggerRadiusApproximate

`SpawnDOTAShopTriggerRadiusApproximate(origin: Vector, radius: float): CDOTA_ShopTrigger`

Availability: `server`

### SpawnEffigyOfUnitOrModel

`SpawnEffigyOfUnitOrModel(arg1: string, arg2: int, arg3: Vector, arg4: Vector, arg5: float, arg6: float, arg7: int): handle`

Availability: `server`

Spawn an effigy of the target unit.

### SpawnEntityFromTableAsynchronous

`SpawnEntityFromTableAsynchronous(arg1: string, arg2: handle, arg3: handle, arg4: handle): nil`

Availability: `both`

Asynchronously spawns a single entity from a table.

### SpawnEntityFromTableSynchronous

`SpawnEntityFromTableSynchronous(baseclass: string, data: table): CBaseEntity`

Availability: `both`

Synchronously spawns a single entity from a table.

### SpawnEntityGroupFromTable

`SpawnEntityGroupFromTable(arg1: handle, arg2: bool, arg3: handle): bool`

Availability: `both`

Hierarchically spawn an entity group from a set of spawn tables.

### SpawnEntityListFromTableAsynchronous

`SpawnEntityListFromTableAsynchronous(arg1: handle, arg2: handle): int`

Availability: `both`

Asynchronously spawn an entity group from a list of spawn tables. A callback will be triggered when the spawning is complete.

### SpawnEntityListFromTableSynchronous

`SpawnEntityListFromTableSynchronous(arg1: handle): handle`

Availability: `both`

Synchronously spawn an entity group from a list of spawn tables.

### SpawnMangoTree

`SpawnMangoTree(pos: Vector, team: int, duration: float, mangoInterval: float, initialMangoes: int): handle`

Availability: `server`

Spawn a mango tree.

### SplineQuaternions

`SplineQuaternions(arg1: Quaternion, arg2: Quaternion, arg3: float): Quaternion`

Availability: `both`

Very basic interpolation of v0 to v1 over t on [0,1].

### SplineVectors

`SplineVectors(arg1: Vector, arg2: Vector, arg3: float): Vector`

Availability: `both`

Very basic interpolation of v0 to v1 over t on [0,1].

### StartSoundEvent

`StartSoundEvent(arg1: string, arg2: handle): nil`

Availability: `both`

Start a sound event.

### StartSoundEventFromPosition

`StartSoundEventFromPosition(soundName: string, position: Vector): nil`

Availability: `both`

Start a sound event from position.

### StartSoundEventFromPositionReliable

`StartSoundEventFromPositionReliable(soundName: string, position: Vector): nil`

Availability: `both`

Start a sound event from position with reliable delivery.

### StartSoundEventFromPositionUnreliable

`StartSoundEventFromPositionUnreliable(soundName: string, position: Vector): nil`

Availability: `both`

Start a sound event from position with optional delivery.

### StartSoundEventReliable

`StartSoundEventReliable(arg1: string, arg2: handle): nil`

Availability: `both`

Start a sound event with reliable delivery.

### StartSoundEventUnreliable

`StartSoundEventUnreliable(arg1: string, arg2: handle): nil`

Availability: `both`

Start a sound event with optional delivery.

### StopEffect

`StopEffect(arg1: handle, arg2: string): nil`

Availability: `both`

Pass entity and effect name.

### StopGlobalSound

`StopGlobalSound(arg1: string): nil`

Availability: `server`

Stop named sound for all players.

### StopListeningToAllGameEvents

`StopListeningToAllGameEvents(arg1: handle): nil`

Availability: `both`

Stop listening to all game events within a specific context.

### StopListeningToGameEvent

`StopListeningToGameEvent(listenerId: EventListenerID): bool`

Availability: `both`

Stop listening to a particular game event.

### StopSoundEvent

`StopSoundEvent(arg1: string, arg2: handle): nil`

Availability: `both`

Stops a sound event with optional delivery.

### StopSoundOn

`StopSoundOn(arg1: string, arg2: handle): nil`

Availability: `both`

Stop named sound on Entity.

### Time

`Time(): float`

Availability: `both`

Get the current server time.

### TraceCollideable

`TraceCollideable(query: TraceCollideableInputs): bool`

Availability: `both`

### TraceHull

`TraceHull(query: TraceHullInputs): bool`

Availability: `both`

### TraceLine

`TraceLine(query: TraceLineInputs): bool`

Availability: `both`

### UnitFilter

`UnitFilter(npc: CDOTA_BaseNPC, teamFilter: DOTA_UNIT_TARGET_TEAM, typeFilter: DOTA_UNIT_TARGET_TYPE, flagFilter: DOTA_UNIT_TARGET_FLAGS, team: DOTATeam_t): UnitFilterResult`

Availability: `both`

Check if a unit passes a set of filters.

### UnloadSpawnGroup

`UnloadSpawnGroup(arg1: string): nil`

Availability: `both`

Unload a spawn group by name.

### UnloadSpawnGroupByHandle

`UnloadSpawnGroupByHandle(handle: SpawnGroupHandle): nil`

Availability: `both`

Unload a spawn group by handle.

### UpdateEventPoints

`UpdateEventPoints(eventPointData: handle): nil`

Availability: `server`

### UserIDToControllerHScript

`UserIDToControllerHScript(arg1: int): handle`

Availability: `both`

Turn a userid integer (typically, fields named 'userid' in game events) to an HScript representing the associated player controller's script instance.

### UTIL_MessageText

`UTIL_MessageText(arg1: int, arg2: string, arg3: int, arg4: int, arg5: int, arg6: int): nil`

Availability: `server`

Sends colored text to one client.

### UTIL_MessageText_WithContext

`UTIL_MessageText_WithContext(arg1: int, arg2: string, arg3: int, arg4: int, arg5: int, arg6: int, arg7: handle): nil`

Availability: `server`

Sends colored text to one client. (Valid context keys: player_id, value, team_id).

### UTIL_MessageTextAll

`UTIL_MessageTextAll(arg1: string, arg2: int, arg3: int, arg4: int, arg5: int): nil`

Availability: `server`

Sends colored text to all clients.

### UTIL_MessageTextAll_WithContext

`UTIL_MessageTextAll_WithContext(arg1: string, arg2: int, arg3: int, arg4: int, arg5: int, arg6: handle): nil`

Availability: `server`

Sends colored text to all clients. (Valid context keys: player_id, value, team_id).

### UTIL_Remove

`UTIL_Remove(entity: CBaseEntity | nil): nil`

Availability: `both`

Removes the specified entity.

### UTIL_RemoveImmediate

`UTIL_RemoveImmediate(entity: CBaseEntity | nil): nil`

Availability: `both`

Immediately removes the specified entity.

### UTIL_ResetMessageText

`UTIL_ResetMessageText(arg1: int): nil`

Availability: `server`

Clear all message text on one client.

### UTIL_ResetMessageTextAll

`UTIL_ResetMessageTextAll(): nil`

Availability: `server`

Clear all message text from all clients.

### VectorAngles

`VectorAngles(arg1: Vector): QAngle`

Availability: `server`

### VectorToAngles

`VectorToAngles(arg1: Vector): QAngle`

Availability: `both`

Get Qangles (with no roll) for a Vector.

### Warning

`Warning(message: string): nil`

Availability: `both`

Print a warning.

## Classes

### CBaseAnimatingActivity

Extends `CBaseModelEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ActiveSequenceDuration(): float` | server | Returns the duration in seconds of the active sequence. |
| `GetCycle(): float` | server | Get the cycle of the animation. |
| `GetSequence(): string` | server | Returns the name of the active sequence. |
| `IsSequenceFinished(): bool` | server | Ask whether the main sequence is done playing. |
| `ResetSequence(sequenceName: string): nil` | server | Sets the active sequence by name, resetting the current cycle. |
| `SequenceDuration(sequenceName: string): float` | server | Returns the duration in seconds of the given sequence name. |
| `SetCycle(cycle: float): nil` | server | Set the cycle of the animation. |
| `SetPoseParameter(name: string, value: float): float` | server | Set the specified pose parameter to the specified value. |
| `SetSequence(sequenceName: string): nil` | server | Sets the active sequence by name, keeping the current cycle. |
| `StopAnimation(): nil` | server | Stop the current animation by setting playback rate to 0.0. |

### CBaseAnimatingOverlay

Client name: `C_BaseAnimatingOverlay` · Extends `CBaseAnimatingActivity`

_No members._

### CBaseAnimGraph

Extends `CBaseModelEntity`

_No members._

### CBaseCombatCharacter

Client name: `C_BaseCombatCharacter` · Extends `CBaseAnimatingOverlay`

_No members._

### CBaseEntity

Client name: `C_BaseEntity` · Extends `CEntityInstance`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddEffects(flags: EntityEffects): nil` | server | Adds the render effect flag. |
| `ApplyAbsVelocityImpulse(vecImpulse: Vector): nil` | server | Apply a Velocity Impulse. |
| `ApplyLocalAngularVelocityImpulse(angImpulse: Vector): nil` | server | Apply an Ang Velocity Impulse. |
| `Attribute_GetFloatValue(name: string, default: float): float` | server | Get float value for an entity attribute. |
| `Attribute_GetIntValue(name: string, default: int): int` | server | Get int value for an entity attribute. |
| `Attribute_SetFloatValue(name: string, value: float): nil` | server | Set float value for an entity attribute. |
| `Attribute_SetIntValue(name: string, value: int): nil` | server | Set int value for an entity attribute. |
| `DeleteAttribute(name: string): nil` | server | Delete an entity attribute. |
| `EmitSound(soundname: string): nil` | server | Plays a sound from this entity. |
| `EmitSoundParams(soundName: string, pitch: int, volume: float, delay: float): nil` | server | Plays/modifies a sound from this entity. changes sound if nPitch and/or flVol or flSoundTime is > 0. |
| `EyeAngles(): QAngle` | server | Get the qangles that this entity is looking at. |
| `EyePosition(): Vector` | server | Get vector to eye position - absolute coords. |
| `FirstMoveChild(): CBaseEntity` | server |  |
| `FollowEntity(entity: CBaseEntity, boneMerge: bool): nil` | server |  |
| `FollowEntityMerge(ent: handle, boneOrAttachName: string): nil` | server | HEntity to follow, string BoneOrAttachName. |
| `GatherCriteria(result: handle): nil` | server | Returns a table containing the criteria that would be used for response queries on this entity. This is the same as the table that is passed to response rule script function callbacks. |
| `GetAbsOrigin(): Vector` | both |  |
| `GetAbsScale(): float` | server |  |
| `GetAngles(): QAngle` | server |  |
| `GetAnglesAsVector(): Vector` | server | Get entity pitch, yaw, roll as a vector. |
| `GetAngularVelocity(): Vector` | server | Get the local angular velocity - returns a vector of pitch,yaw,roll. |
| `GetBaseVelocity(): Vector` | server | Get Base? velocity. |
| `GetBoundingMaxs(): Vector` | server | Get a vector containing max bounds, centered on object. |
| `GetBoundingMins(): Vector` | server | Get a vector containing min bounds, centered on object. |
| `GetBounds(): EntityBounds` | server | Get a table containing the 'Mins' & 'Maxs' vector bounds, centered on object. |
| `GetCenter(): Vector` | server | Get vector to center of object - absolute coords. |
| `GetChildren(): {'kind': 'array', 'types': ['CBaseEntity']}` | server | Get the entities parented to this entity. |
| `GetContext(name: string): string, float, nil` | server | Looks up a context and returns it if available. May return string, float, or null (if the context isn't found). |
| `GetForwardVector(): Vector` | server | Get the forward vector of the entity. |
| `GetHealth(): int` | both | Get the health of this entity. |
| `GetLeftVector(): Vector` | server | Get the left vector of the entity. |
| `GetLocalAngles(): QAngle` | server | Get entity local pitch, yaw, roll as a QAngle. |
| `GetLocalAngularVelocity(): QAngle` | server | Maybe local angvel. |
| `GetLocalOrigin(): Vector` | server | Get entity local origin as a Vector. |
| `GetLocalScale(): float` | server |  |
| `GetLocalVelocity(): Vector` | server | Get Entity relative velocity. |
| `GetMass(): float` | server | Get the mass of an entity. (returns 0 if it doesn't have a physics object). |
| `GetMaxHealth(): int` | both | Get the maximum health of this entity. |
| `GetModelName(): string` | server | Returns the name of the model. |
| `GetMoveParent(): CBaseEntity` | server | If in hierarchy, retrieves the entity's parent. |
| `GetOrigin(): Vector` | server |  |
| `GetOwner(): CBaseEntity` | server | Gets this entity's owner. |
| `GetOwnerEntity(): CBaseEntity` | server | Get the owner entity, if there is one. |
| `GetRightVector(): Vector` | server | Get the right vector of the entity. WARNING: This produces a left-handed coordinate system. Use GetLeftVector instead (which is aligned with the y axis of the entity). |
| `GetRootMoveParent(): CBaseEntity` | server | If in hierarchy, walks up the hierarchy to find the root parent. |
| `GetSoundDuration(soundname: string, actormodel: string): float` | server | Returns float duration of the sound. Takes soundname and optional actormodelname. |
| `GetSpawnGroupHandle(): SpawnGroupHandle` | server | Returns the spawn group handle of this entity. |
| `GetTeam(): DOTATeam_t` | server | Get the team number of this entity. |
| `GetTeamNumber(): DOTATeam_t` | both | Get the team number of this entity. |
| `GetUpVector(): Vector` | server | Get the up vector of the entity. |
| `GetVelocity(): Vector` | server |  |
| `HasAttribute(name: string): bool` | server | See if an entity has a particular attribute. |
| `IsAlive(): bool` | server | Is this entity alive? |
| `IsBaseNPC(): bool` | both | Is this entity an CDOTA_BaseNPC? |
| `IsDOTANPC(): bool` | server | Is this entity a Dota NPC? |
| `IsInstance(classOrClassName: string \| table): bool` | both |  |
| `IsNPC(): bool` | server | Is this entity an CAI_BaseNPC? |
| `IsPlayer(): bool` | server | Back compat: Is this entity a player pawn *or* controller? |
| `IsPlayerController(): bool` | server | Is this entity a player controller? |
| `IsPlayerPawn(): bool` | server | Is this entity a player pawn? |
| `Kill(): nil` | server |  |
| `NextMovePeer(): CBaseEntity` | server |  |
| `PrecacheScriptSound(soundname: string): nil` | server | Precache a sound for later playing. |
| `RemoveEffects(flags: EntityEffects): nil` | server | Removes the render effect flag. |
| `SetAbsAngles(pitch: float, yaw: float, roll: float): nil` | server | Set entity pitch, yaw, roll by component. |
| `SetAbsOrigin(origin: Vector): nil` | server |  |
| `SetAbsScale(scale: float): nil` | server |  |
| `SetAngles(pitch: float, yaw: float, roll: float): nil` | server | Set entity pitch, yaw, roll by component. |
| `SetAngularVelocity(pitchVel: float, yawVel: float, rollVel: float): nil` | server | Set the local angular velocity. |
| `SetConstraint(pos: Vector): nil` | server | Set the position of the constraint. |
| `SetContext(name: string, value: string, duration: float): nil` | server | Store any key/value pair in this entity's dialog contexts. Value must be a string. Will last for duration (set 0 to mean 'forever'). |
| `SetContextNum(name: string, value: float, duration: float): nil` | server | Store any key/value pair in this entity's dialog contexts. Value must be a number (int or float). Will last for duration (set 0 to mean 'forever'). |
| `SetContextThink(contextName: string, thinkFunc: {'kind': 'function', 'returns': ['float', 'nil'], 'args': [{'name': 'entity', 'types': ['CBaseEntity']}]} \| nil, interval: float): nil` | both | Set a think function on this entity. |
| `SetEntityName(name: string): nil` | server | Set the name of an entity. |
| `SetForwardVector(v: Vector): nil` | server | Set the orientation of the entity to have this forward vector. |
| `SetFriction(friction: float): nil` | server | Set PLAYER friction, ignored for objects. |
| `SetGravity(gravity: float): nil` | server | Set PLAYER gravity, ignored for objects. |
| `SetHealth(health: int): nil` | server | Set the health of this entity. |
| `SetLocalAngles(pitch: float, yaw: float, roll: float): nil` | server | Set entity local pitch, yaw, roll by component. |
| `SetLocalOrigin(origin: Vector): nil` | server | Set entity local origin from a Vector. |
| `SetLocalScale(scale: float): nil` | server |  |
| `SetMass(mass: float): nil` | server | Set the mass of an entity. (does nothing if it doesn't have a physics object). |
| `SetMaxHealth(amt: int): nil` | server | Set the maximum health of this entity. |
| `SetOrigin(v: Vector): nil` | server |  |
| `SetOwner(owner: CBaseEntity): nil` | server | Sets this entity's owner. This entity will be returned by GetOwner() and GetOwnerEntity(). GetPlayerOwner() and GetPlayerOwnerID() will be automatically inferred from this entity. |
| `SetParent(parent: CBaseEntity, attachmentname: string): nil` | server | Set the parent for this entity. |
| `SetTeam(teamNum: DOTATeam_t): nil` | server |  |
| `SetThink(functionName: {'kind': 'function', 'returns': ['float', 'nil'], 'args': [{'name': 'entity', 'types': ['CBaseEntity']}]} \| string, context: table \| nil, contextName: string \| nil, initialDelay: float \| nil): nil` | both | Set a think function on this entity. Uses `CBaseEntity:SetContextThink` internally.<br>Note: optional parameters can be given in any order. |
| `SetVelocity(vecVelocity: Vector): nil` | server |  |
| `StopSound(soundname: string): nil` | server | Stops a named sound playing from this entity. |
| `StopThink(contextName: string): nil` | both | Stops thinker created with `CBaseEntity.SetThink`.<br>Alias for `CBaseEntity:SetContextThink(contextName, nil, 0)`. |
| `TakeDamage(damageInfo: CTakeDamageInfo): int` | server | Apply damage to this entity. Use CreateDamageInfo() to create a damageinfo object. |
| `TransformPointEntityToWorld(point: Vector): Vector` | server | Returns the input Vector transformed from entity to world space. |
| `TransformPointWorldToEntity(point: Vector): Vector` | server | Returns the input Vector transformed from world to entity space. |
| `Trigger(): nil` | server | Fires off this entity's OnTrigger responses. |
| `ValidatePrivateScriptScope(): nil` | server | Validates the private script scope and creates it if one doesn't exist. |

### CBaseModelEntity

Client name: `C_BaseModelEntity` · Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetAttachmentAngles(attachment: int): Vector` | server | Get the attachment id's angles as a p,y,r vector. |
| `GetAttachmentForward(attachment: int): Vector` | server | Get the attachment id's forward vector. |
| `GetAttachmentOrigin(attachment: int): Vector` | server | Get the attachment id's origin vector. |
| `GetMaterialGroupHash(): uint` | server | Get the material group hash of this entity. |
| `GetMaterialGroupMask(): Uint64` | server | Get the mesh group mask of this entity. |
| `GetModelScale(): float` | server | Get scale of entity's model. |
| `GetRenderAlpha(): int` | both | Get the alpha modulation of this entity. |
| `GetRenderColor(): Vector` | server | Get the render color of the entity. |
| `ScriptLookupAttachment(attachmentName: string): int` | server | Get the named attachment id. |
| `SetBodygroup(bodyGroup: int, choice: int): nil` | server | Sets a bodygroup. |
| `SetBodygroupByName(name: string, value: int): nil` | server | Sets a bodygroup by name. |
| `SetMaterialGroup(materialGroup: string): nil` | server | Set the material group of this entity. |
| `SetMaterialGroupHash(hash: uint): nil` | server | Set the material group hash of this entity. |
| `SetMaterialGroupMask(meshGroupMask: Uint64): nil` | server | Set the mesh group mask of this entity. |
| `SetModel(modelName: string): nil` | server |  |
| `SetModelScale(scale: float): nil` | server | Set scale of entity's model. |
| `SetRenderAlpha(alpha: int): nil` | server | Set the alpha modulation of this entity. |
| `SetRenderColor(r: int, g: int, b: int): nil` | server | Sets the render color of the entity. |
| `SetRenderMode(mode: int): nil` | server | Sets the render mode of the entity. |
| `SetSingleMeshGroup(meshGroupName: string): nil` | server | Set a single mesh group for this entity. |
| `SetSize(mins: Vector, maxs: Vector): nil` | server |  |
| `SetSkin(skin: int): nil` | server |  |

### CBasePlayerController

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetPawn(): handle` | server | Returns the pawn for this controller. |

### CBasePlayerPawn

Extends `CBaseCombatCharacter`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetController(): handle` | server | Returns the controller for this pawn. |
| `GetEquippedWeapons(): table` | server | Returns an array of all the equipped weapons. |
| `GetWeaponCount(): int` | server | Gets the number of weapons currently equipped. |
| `IsNoclipping(): bool` | server | Returns true if the player is in noclip mode. |

### CBaseTrigger

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `Disable(): nil` | server | Disable's the trigger. |
| `Enable(): nil` | server | Enable the trigger. |
| `IsTouching(ent: CBaseEntity): bool` | server | Checks whether the passed entity is touching the trigger. |

### CBodyComponent

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddImpulseAtPosition(arg1: Vector, arg2: Vector): nil` | both | Apply an impulse at a worldspace position to the physics. |
| `AddVelocity(arg1: Vector, arg2: Vector): nil` | both | Add linear and angular velocity to the physics object. |
| `DetachFromParent(): nil` | both | Detach from its parent. |
| `IsAttachedToParent(): bool` | both | Is attached to parent. |
| `SetAngularVelocity(arg1: Vector): nil` | both |  |
| `SetMaterialGroup(arg1: string): nil` | both |  |
| `SetVelocity(arg1: Vector): nil` | both |  |

### CCustomGameEventManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `RegisterListener(eventName: string, listener: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'userId', 'types': ['EntityIndex']}, {'name': 'event', 'types': ['table']}]}): CustomGameEventListenerID` | server | Register a callback to be called when a particular custom event arrives. Returns a listener ID that can be used to unregister later. |
| `Send_ServerToAllClients(eventName: string, eventData: table): nil` | server |  |
| `Send_ServerToPlayer(player: CDOTAPlayerController, eventName: string, eventData: table): nil` | server |  |
| `Send_ServerToTeam(team: DOTATeam_t, eventName: string, eventData: table): nil` | server |  |
| `UnregisterListener(listenerId: CustomGameEventListenerID): nil` | server | Unregister a specific listener. |

### CCustomNetTableManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetTableValue(tableName: string, keyName: string): table` | both |  |
| `SetTableValue(tableName: string, keyName: string, value: handle): bool` | server |  |

### CDebugOverlayScriptHelper

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `Axis(arg1: Vector, arg2: Vector, arg3: float, arg4: bool, arg5: float): nil` | both | Draws an axis. Specify origin + orientation in world space. |
| `Box(arg1: Vector, arg2: Vector, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a world-space axis-aligned box. Specify bounds in world space. |
| `BoxAngles(arg1: Vector, arg2: Vector, arg3: Vector, arg4: Vector, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws an oriented box at the origin. Specify bounds in local space. |
| `Capsule(arg1: Vector, arg2: Vector, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws a capsule. Specify base in world space. |
| `Circle(arg1: Vector, arg2: Vector, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws a circle. Specify center in world space. |
| `CircleScreenOriented(arg1: Vector, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a circle oriented to the screen. Specify center in world space. |
| `Cone(arg1: Vector, arg2: Vector, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws a wireframe cone. Specify endpoint and direction in world space. |
| `Cross(arg1: Vector, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a screen-aligned cross. Specify origin in world space. |
| `Cross3D(arg1: Vector, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a world-aligned cross. Specify origin in world space. |
| `Cross3DOriented(arg1: Vector, arg2: Vector, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws an oriented cross. Specify origin in world space. |
| `DrawTickMarkedLine(arg1: Vector, arg2: Vector, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws a dashed line. Specify endpoints in world space. |
| `EntityAttachments(arg1: ehandle, arg2: float, arg3: float): nil` | both | Draws the attachments of the entity. |
| `EntityAxis(arg1: ehandle, arg2: float, arg3: bool, arg4: float): nil` | both | Draws the axis of the entity origin. |
| `EntityBounds(arg1: ehandle, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: float): nil` | both | Draws bounds of an entity. |
| `EntitySkeleton(arg1: ehandle, arg2: float): nil` | both | Draws the skeleton of the entity. |
| `EntityText(arg1: ehandle, arg2: int, arg3: string, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float): nil` | both | Draws text on an entity. |
| `FilledRect2D(arg1: Vector2D, arg2: Vector2D, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float): nil` | both | Draws a screen-space filled 2D rectangle. Coordinates are in pixels. |
| `HorzArrow(arg1: Vector, arg2: Vector, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws a horizontal arrow. Specify endpoints in world space. |
| `Line(arg1: Vector, arg2: Vector, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a line between two points. |
| `Line2D(arg1: Vector2D, arg2: Vector2D, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float): nil` | both | Draws a line between two points in screenspace. |
| `PopDebugOverlayScope(): nil` | both | Pops the identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch. |
| `PushAndClearDebugOverlayScope(arg1: string): nil` | both | Pushes an identifier used to group overlays. Deletes all existing overlays using this overlay id. |
| `PushDebugOverlayScope(arg1: string): nil` | both | Pushes an identifier used to group overlays. Overlays marked with this identifier can be deleted in a big batch. |
| `RemoveAllInScope(arg1: string): nil` | both | Removes all overlays marked with a specific identifier, regardless of their lifetime. |
| `SolidCone(arg1: Vector, arg2: Vector, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws a solid cone. Specify endpoint and direction in world space. |
| `Sphere(arg1: Vector, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: float): nil` | both | Draws a wireframe sphere. Specify center in world space. |
| `SweptBox(arg1: Vector, arg2: Vector, arg3: Vector, arg4: Vector, arg5: Vector, arg6: int, arg7: int, arg8: int, arg9: int, arg10: float): nil` | both | Draws a swept box. Specify endpoints in world space and the bounds in local space. |
| `Text(arg1: Vector, arg2: int, arg3: string, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: float): nil` | both | Draws 2D text. Specify origin in world space. |
| `Texture(arg1: string, arg2: Vector2D, arg3: Vector2D, arg4: int, arg5: int, arg6: int, arg7: int, arg8: Vector2D, arg9: Vector2D, arg10: float): nil` | both | Draws a screen-space texture. Coordinates are in pixels. |
| `Triangle(arg1: Vector, arg2: Vector, arg3: Vector, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws a filled triangle. Specify vertices in world space. |
| `VectorText3D(arg1: Vector, arg2: Vector, arg3: string, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws 3D text. Specify origin + orientation in world space. |
| `VertArrow(arg1: Vector, arg2: Vector, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: float): nil` | both | Draws a vertical arrow. Specify endpoints in world space. |
| `YawArrow(arg1: Vector, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: float): nil` | both | Draws a arrow associated with a specific yaw. Specify endpoints in world space. |

### CDOTA_Ability_Aghanim_Spear

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `LaunchSpear(target: Vector, start: Vector): nil` | server | Launch Spear to a target position from a source position. |

### CDOTA_Ability_Animation_Attack

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetPlaybackRate(rate: float): nil` | server | Override playbackrate. |

### CDOTA_Ability_Animation_TailSpin

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetPlaybackRate(rate: float): nil` | server | Override playbackrate. |

### CDOTA_Ability_DataDriven

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ApplyDataDrivenModifier(caster: CDOTA_BaseNPC, target: CDOTA_BaseNPC, modifierName: string, modifierTable: table \| nil): CDOTA_Buff` | server | Applies a data driven modifier to the target. |
| `ApplyDataDrivenThinker(caster: CDOTA_BaseNPC, location: Vector, modifierName: string, modifierTable: table \| nil): CDOTA_Buff` | server | Applies a data driven thinker at the location. |

### CDOTA_Ability_Lua

Client name: `C_DOTA_Ability_Lua` · Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CastFilterResult(): UnitFilterResult` | both | Determine whether an issued command with no target is valid. |
| `CastFilterResultLocation(location: Vector): UnitFilterResult` | both | Determine whether an issued command on a location is valid. |
| `CastFilterResultTarget(target: CDOTA_BaseNPC): UnitFilterResult` | both | Determine whether an issued command on a target is valid. |
| `GetAbilityChargeRestoreTime(level: int): float` | both |  |
| `GetAbilityTextureName(): string` | client | Allows code overriding of the ability texture shown in the HUD. |
| `GetAOERadius(): float` | both | Controls the size of the AOE casting cursor. |
| `GetAssociatedPrimaryAbilities(): string` | server | Returns abilities that are stolen simultaneously, or otherwise related in functionality. |
| `GetAssociatedSecondaryAbilities(): string` | server | Returns other abilities that are stolen simultaneously, or otherwise related in functionality.  Generally hidden abilities. |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR` | both | Return cast behavior type of this ability. |
| `GetCastAnimation(): GameActivity_t` | server | Return casting animation of this ability. |
| `GetCastPoint(): float` | both | Return cast point of this ability. |
| `GetCastRange(location: Vector, target: CDOTA_BaseNPC \| nil): int` | both | Return cast range of this ability. |
| `GetCastRangeBonus(target: handle, pseudoCastRange: int): int` | both |  |
| `GetChannelAnimation(): GameActivity_t` | server | Return channel animation of this ability. |
| `GetChannelledHealthCostPerSecond(level: int): int` | both | Return health cost per second of channeling at the given level (-1 is current). |
| `GetChannelledManaCostPerSecond(level: int): int` | both | Return mana cost at the given level per second while channeling (-1 is current). |
| `GetChannelStartTime(): float` | both | Return the channel start time of this ability. |
| `GetChannelTime(): float` | both | Return the channel time of this ability. |
| `GetConceptRecipientType(): int` | server | Return who hears speech when this spell is cast. |
| `GetCooldown(level: int): float` | both | Return cooldown of this ability. |
| `GetCustomCastError(): string` | both | Return the error string of a failed command with no target. |
| `GetCustomCastErrorLocation(location: Vector): string` | both | Return the error string of a failed command on a location. |
| `GetCustomCastErrorTarget(target: CDOTA_BaseNPC): string` | both | Return the error string of a failed command on a target. |
| `GetCustomHudErrorMessage(reason: int): string` | both | (DOTA_INVALID_ORDERS nReason) Return the error string of a failed order. |
| `GetEffectiveCastRange(location: Vector, target: handle): int` | both | Return cast range of this ability, accounting for modifiers. |
| `GetGoldCost(level: int): int` | both | Return gold cost at the given level (-1 is current). |
| `GetHealthCost(level: int): int` | both | Return health cost at the given level (-1 is current). |
| `GetIntrinsicModifierName(): string` | server | Returns the name of the modifier applied passively by this ability. |
| `GetManaCost(level: int): int` | both | Return mana cost at the given level (-1 is current). |
| `GetPlaybackRateOverride(): float` | server | Return the animation rate of the cast animation. |
| `IsAttributeBonus(): bool` | both | Is this ability an Attribute Bonus. |
| `IsCosmetic(entity: handle): bool` | server | Is this a cosmetic only ability? |
| `IsHiddenAbilityCastable(): bool` | both | Returns true if this ability can be used when not on the action panel. |
| `IsHiddenWhenStolen(): bool` | server | Returns true if this ability is hidden when stolen by Spell Steal. |
| `IsRefreshable(): bool` | server | Returns true if this ability is refreshed by Refresher Orb. |
| `IsStealable(): bool` | server | Returns true if this ability can be stolen by Spell Steal. |
| `OnAbilityPhaseInterrupted(): nil` | server | Cast time did not complete successfully. |
| `OnAbilityPhaseStart(): bool` | server | Cast time begins (return true for successful cast). |
| `OnAbilityPinged(playerId: PlayerID, ctrlHeld: bool): nil` | server | The ability was pinged. |
| `OnAbilityUpgrade(upgradeAbility: handle): nil` | server |  |
| `OnChannelFinish(interrupted: bool): nil` | server | Channel finished. |
| `OnChannelThink(interval: float): nil` | server | Channeling is taking place. |
| `OnHeroCalculateStatBonus(): nil` | server | Caster (hero only) gained a level, skilled an ability, or received a new stat bonus. |
| `OnHeroDiedNearby(unit: CDOTA_BaseNPC, attacker: CDOTA_BaseNPC, event: table): nil` | server | A hero has died in the vicinity (ie Urn), takes table of params. |
| `OnHeroLevelUp(): nil` | server | Caster gained a level. |
| `OnInventoryContentsChanged(): nil` | server | Caster inventory changed. |
| `OnItemEquipped(item: CDOTA_Item): nil` | server | Caster equipped item. |
| `OnOwnerDied(): nil` | server | Caster died. |
| `OnOwnerSpawned(): nil` | server | Caster respawned or spawned for the first time. |
| `OnProjectileHit(target: CDOTA_BaseNPC \| nil, location: Vector): bool, nil` | server | Projectile has collided with a given target or reached its destination. If 'true` is returned, projectile would be destroyed. |
| `OnProjectileHit_ExtraData(target: CDOTA_BaseNPC \| nil, location: Vector, extraData: table): bool, nil` | server | Projectile has collided with a given target or reached its destination. If 'true` is returned, projectile would be destroyed. |
| `OnProjectileHitHandle(target: CDOTA_BaseNPC \| nil, location: Vector, projectileHandle: ProjectileID): bool, nil` | server | Projectile has collided with a given target or reached its destination. If 'true` is returned, projectile would be destroyed. |
| `OnProjectileThink(location: Vector): nil` | server | Projectile is actively moving. |
| `OnProjectileThink_ExtraData(location: Vector, extraData: table): nil` | server | Projectile is actively moving. |
| `OnProjectileThinkHandle(projectileHandle: ProjectileID): nil` | server | Projectile is actively moving. |
| `OnSpellStart(): nil` | server | Cast time finished, spell effects begin. |
| `OnStolen(sourceAbility: CDOTABaseAbility): nil` | server | Special behavior when stolen by Spell Steal. |
| `OnToggle(): nil` | server | Ability is toggled on/off. |
| `OnUnStolen(): nil` | server | Special behavior when lost by Spell Steal. |
| `OnUpgrade(): nil` | server | Ability gained a level. |
| `OtherAbilitiesAlwaysInterruptChanneling(): bool` | server |  |
| `PiercesDebuffImmunity(): bool` | both | Return if an ability and its modifiers should pierce debuff immunity. |
| `ProcsMagicStick(): bool` | server | Returns true if this ability will generate magic stick charges for nearby enemies. |
| `RequiresFacing(): bool` | server | Does this ability need the caster to face the target before executing? |
| `ResetToggleOnRespawn(): bool` | server | Returns true if this ability should return to the default toggle state when its parent respawns. |
| `SpeakTrigger(): int` | server | Return the type of speech used. |
| `Init(): nil` | both | Called first when ability entity is created. |
| `Precache(context: CScriptPrecacheContext): nil` | server |  |
| `Spawn(): nil` | both | Called when ability entity is created, after Init. |

### CDOTA_Ability_Nian_Dive

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetPlaybackRate(rate: float): nil` | server | Override playbackrate. |

### CDOTA_Ability_Nian_Leap

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetPlaybackRate(rate: float): nil` | server | Override playbackrate. |

### CDOTA_Ability_Nian_Roar

Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetCastCount(): int` | server | Number of times Nian has used the roar. |

### CDOTA_BaseNPC

Client name: `C_DOTA_BaseNPC` · Extends `CBaseAnimatingOverlay`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddAbility(abilityName: string): CDOTABaseAbility` | server | Add an ability to this unit by name. |
| `AddActivityModifier(name: string): nil` | server | Add an activity modifier that affects future StartGesture calls. |
| `AddItem(item: CDOTA_Item): CDOTA_Item` | server | Add an item to this unit's inventory. |
| `AddItemByName(itemName: string): CDOTA_Item` | server | Add an item to this unit's inventory. |
| `AddNewModifier(caster: CDOTA_BaseNPC \| nil, ability: CDOTABaseAbility \| nil, modifierName: string, modifierTable: table \| nil): CDOTA_Buff` | server | Add a modifier to this unit. |
| `AddNoDraw(): nil` | server | Adds the no draw flag. |
| `AddSpeechBubble(bubble: int, speech: string, duration: float, unOffsetX: uint, unOffsetY: uint): nil` | server | Add a speech bubble(1-4 live at a time) to this NPC. |
| `AlertNearbyUnits(attacker: CDOTA_BaseNPC, ability: CDOTABaseAbility): nil` | server |  |
| `AngerNearbyUnits(): nil` | server |  |
| `AttackNoEarlierThan(time: float, timeDisparityTolerance: float): nil` | server |  |
| `AttackReady(): bool` | server |  |
| `BoundingRadius2D(): float` | server |  |
| `CalculateGenericBonuses(): nil` | server |  |
| `CanBeSeenByAnyOpposingTeam(): bool` | server |  |
| `CanEntityBeSeenByMyTeam(entity: CDOTA_BaseNPC): bool` | server | Check FoW to see if an entity is visible. |
| `CanSellItems(): bool` | server | Query if this unit can sell items. |
| `CastAbilityImmediately(ability: CDOTABaseAbility, playerIndex: int): nil` | server | Cast an ability immediately. |
| `CastAbilityNoTarget(ability: CDOTABaseAbility, playerIndex: int): nil` | server | Cast an ability with no target. |
| `CastAbilityOnPosition(position: Vector, ability: CDOTABaseAbility, playerIndex: int): nil` | server | Cast an ability on a position. |
| `CastAbilityOnTarget(target: CDOTA_BaseNPC, ability: CDOTABaseAbility, playerIndex: int): nil` | server | Cast an ability on a target entity. |
| `CastAbilityToggle(ability: CDOTABaseAbility, playerIndex: int): nil` | server | Toggle an ability. |
| `ChangeTeam(teamNum: int): nil` | server |  |
| `ClearActivityModifiers(): nil` | server | Clear Activity modifiers. |
| `ConsumeItem(item: handle): nil` | server | Consume the item, deleting it from the inventory and granting the hero the specified bonuses. |
| `DestroyAllSpeechBubbles(): nil` | server |  |
| `DisassembleItem(item: CDOTA_Item): nil` | server | Disassemble the passed item in this unit's inventory. |
| `DropItemAtPosition(dest: Vector, item: CDOTA_Item): nil` | server | Drop an item at a given point. |
| `DropItemAtPositionImmediate(item: CDOTA_Item, position: Vector): nil` | server | Immediately drop a carried item at a given position. |
| `EjectItemFromStash(item: CDOTA_Item): nil` | server | Drops the selected item out of this unit's stash. |
| `FaceTowards(target: Vector): nil` | server | This unit will be set to face the target point. |
| `FadeGesture(activity: GameActivity_t): nil` | server | Fade and remove the given gesture activity. |
| `FindAbilityByName(abilityName: string): CDOTABaseAbility, nil` | both | Retrieve an ability by name from the unit. |
| `FindAllModifiers(): {'kind': 'array', 'types': ['CDOTA_Buff']}` | server | Returns a table of all of the modifiers on the NPC. |
| `FindAllModifiersByName(modifierName: string): {'kind': 'array', 'types': ['CDOTA_Buff']}` | server | Returns a table of all of the modifiers on the NPC with the passed name (modifierName). |
| `FindItemInInventory(itemName: string): CDOTA_Item, nil` | server | Get handle to first item in inventory, else nil. |
| `FindModifierByName(modifierName: string): CDOTA_Buff, nil` | server | Return a handle to the modifier of the given name if found, else nil (string Name ). |
| `FindModifierByNameAndCaster(modifierName: string, caster: CDOTA_BaseNPC): CDOTA_Buff, nil` | server | Return a handle to the modifier of the given name from the passed caster if found, else nil. |
| `ForceKill(reincarnate: bool): nil` | server | Kill this unit immediately. |
| `ForcePlayActivityOnce(activity: GameActivity_t): nil` | server | Play an activity once, and then go back to idle. |
| `GetAbilityByIndex(index: int): CDOTABaseAbility, nil` | server | Retrieve an ability by index from the unit. |
| `GetAbilityCount(): int` | both |  |
| `GetAcquisitionRange(): float` | server | Gets the range at which this unit will auto-acquire. |
| `GetAdditionalBattleMusicWeight(): float` | server | Combat involving this creature will have this weight added to the music calcuations. |
| `GetAggroTarget(): CDOTA_BaseNPC, nil` | server | Returns this unit's aggro target. |
| `GetAttackAnimationPoint(): float` | server |  |
| `GetAttackCapability(): DOTAUnitAttackCapability_t` | server |  |
| `GetAttackDamage(): int` | server | Returns a random integer between the minimum and maximum base damage of the unit. |
| `GetAttackRangeBuffer(): float` | server | Gets the attack range buffer. |
| `GetAttackSpeed(ignoreTempAttackSpeed: bool): float` | both |  |
| `GetAttacksPerSecond(ignoreTempAttackSpeed: bool): float` | both |  |
| `GetAttackTarget(): CDOTA_BaseNPC, nil` | server |  |
| `GetAverageTrueAttackDamage(target: CDOTA_BaseNPC \| nil): int` | server | Returns the average value of the minimum and maximum damage values. |
| `GetBaseAttackRange(): int` | server |  |
| `GetBaseAttackTime(): float` | both |  |
| `GetBaseDamageMax(): int` | server | Get the maximum attack damage of this unit. |
| `GetBaseDamageMin(): int` | server | Get the minimum attack damage of this unit. |
| `GetBaseDayTimeVisionRange(): int` | server | Returns the vision range before modifiers. |
| `GetBaseHealthBarOffset(): int` | server |  |
| `GetBaseHealthRegen(): float` | server |  |
| `GetBaseMagicalResistanceValue(): float` | both | Returns base magical armor value. |
| `GetBaseMaxHealth(): float` | server | Gets the base max health value. |
| `GetBaseMoveSpeed(): float` | both |  |
| `GetBaseNightTimeVisionRange(): int` | server | Returns the vision range after modifiers. |
| `GetBonusManaRegen(): float` | server | This Mana regen is derived from constant bonuses like Basilius. |
| `GetCastPoint(attack: bool): float` | server |  |
| `GetCastRangeBonus(): float` | both |  |
| `GetCloneSource(): CDOTA_BaseNPC, nil` | server | Get clone source (Meepo Prime, if this is a Meepo). |
| `GetCollisionPadding(): float` | both | Returns the size of the collision padding around the hull. |
| `GetCooldownReduction(): float` | both |  |
| `GetCreationTime(): float` | server |  |
| `GetCurrentActiveAbility(): CDOTABaseAbility, nil` | server | Get the ability this unit is currently casting. |
| `GetCurrentVisionRange(): int` | both | Gets the current vision range. |
| `GetCursorCastTarget(): CDOTA_BaseNPC, nil` | server |  |
| `GetCursorPosition(): Vector` | server |  |
| `GetCursorTargetingNothing(): bool` | server |  |
| `GetDamageMax(): int` | both | Get the maximum attack damage of this unit. |
| `GetDamageMin(): int` | both | Get the minimum attack damage of this unit. |
| `GetDayTimeVisionRange(): int` | both | Returns the vision range after modifiers. |
| `GetDeathXP(): int` | server | Get the XP bounty on this unit. |
| `GetDisplayAttackSpeed(): float` | server | Attack speed expressed as constant value. |
| `GetEvasion(): float` | server |  |
| `GetForceAttackTarget(): CDOTA_BaseNPC, nil` | server |  |
| `GetGoldBounty(): int` | server | Get the gold bounty on this unit. |
| `GetHasteFactor(): float` | both |  |
| `GetHealthDeficit(): int` | server | Returns integer amount of health missing from max. |
| `GetHealthPercent(): int` | both | Get the current health percent of the unit. |
| `GetHealthRegen(): float` | server |  |
| `GetHullRadius(): float` | both | Get the collision hull radius of this NPC. |
| `GetIdealSpeed(): float` | both | Returns speed after all modifiers. |
| `GetIdealSpeedNoSlows(): float` | both | Returns speed after all modifiers, but excluding those that reduce speed. |
| `GetIncreasedAttackSpeed(ignoreTempAttackSpeed: bool): float` | both |  |
| `GetInitialGoalEntity(): CBaseEntity, nil` | server | Returns the initial waypoint goal for this NPC. |
| `GetInitialGoalPosition(): Vector` | server | Get waypoint position for this NPC. |
| `GetItemInSlot(slot: int): CDOTA_Item, nil` | server | Returns nth item in inventory slot (index is zero based). |
| `GetLastAttackTime(): float` | server |  |
| `GetLastDamageTime(): float` | server | Get the last time this NPC took damage. |
| `GetLastIdleChangeTime(): float` | server | Get the last game time that this unit switched to/from idle state. |
| `GetLevel(): int` | both | Returns the level of this unit. |
| `GetMainControllingPlayer(): int` | server | Returns the player ID of the controlling player. |
| `GetMana(): float` | both | Get the mana on this unit. |
| `GetManaPercent(): int` | server | Get the percent of mana remaining. |
| `GetManaRegen(): float` | both |  |
| `GetMaximumGoldBounty(): int` | server | Get the maximum gold bounty for this unit. |
| `GetMaxMana(): float` | both | Get the maximum mana of this unit. |
| `GetMinimumGoldBounty(): int` | server | Get the minimum gold bounty for this unit. |
| `GetModelRadius(): float` | both |  |
| `GetModifierCount(): int` | server | How many modifiers does this unit have? |
| `GetModifierNameByIndex(index: int): string` | server | Get a modifier name by index. |
| `GetModifierStackCount(modifierName: string, caster: CDOTA_BaseNPC): int` | both | Gets the stack count of a given modifier. |
| `GetMoveSpeedModifier(baseSpeed: float, returnUnslowed: bool): float` | both |  |
| `GetMustReachEachGoalEntity(): bool` | server | Set whether this NPC is required to reach each goal entity, rather than being allowed to unkink their path. |
| `GetNeutralSpawnerName(): string` | server | Get the name of this camp's neutral spawner. |
| `GetNeverMoveToClearSpace(): bool` | server | If set to true, we will never attempt to move this unit to clear space, even when it unphases. |
| `GetNightTimeVisionRange(): int` | both | Returns the vision range after modifiers. |
| `GetOpposingTeamNumber(): DOTATeam_t` | both |  |
| `GetPaddedCollisionRadius(): float` | both | Get the collision hull radius (including padding) of this NPC. |
| `GetPhysicalArmorBaseValue(): float` | both | Returns base physical armor value. |
| `GetPhysicalArmorValue(ignoreBase: bool): float` | both | Returns current physical armor value. |
| `GetPlayerOwner(): CDOTAPlayerController` | server | Returns the player that owns this unit. |
| `GetPlayerOwnerID(): PlayerID` | both | Get the owner player ID for this unit. |
| `GetProjectileSpeed(): int` | server |  |
| `GetRangedProjectileName(): string` | server |  |
| `GetRangeToUnit(npc: CDOTA_BaseNPC): float` | server |  |
| `GetRemainingPathLength(): float` | server |  |
| `GetSecondsPerAttack(ignoreTempAttackSpeed: bool): float` | both |  |
| `GetSpellAmplification(baseOnly: bool): float` | server |  |
| `GetStatusResistance(): float` | server |  |
| `GetTotalPurchasedUpgradeGoldCost(): int` | both | Get how much gold has been spent on ability upgrades. |
| `GetUnitLabel(): string` | both |  |
| `GetUnitLocToken(): string` | client | Get the localization token for this unit's name. |
| `GetUnitName(): string` | both | Get the name of this unit. |
| `GiveMana(mana: float): nil` | server | Give mana to this unit, this can be used for mana gained by abilities or item usage. |
| `HasAbility(abilityName: string): bool` | server | See whether this unit has an ability by name. |
| `HasAnyActiveAbilities(): bool` | server |  |
| `HasAttackCapability(): bool` | both |  |
| `HasFlyingVision(): bool` | both |  |
| `HasFlyMovementCapability(): bool` | both |  |
| `HasGroundMovementCapability(): bool` | both |  |
| `HasInventory(): bool` | server | Does this unit have an inventory. |
| `HasItemInInventory(itemName: string): bool` | both | See whether this unit has an item by name. |
| `HasModifier(scriptName: string): bool` | both | Sees if this unit has a given modifier. |
| `HasMovementCapability(): bool` | both |  |
| `HasScepter(): bool` | both |  |
| `Heal(amount: float, inflictor: CDOTABaseAbility \| nil): nil` | server | Heal this unit. |
| `HealWithParams(amount: float, inflictor: handle, lifesteal: bool, amplify: bool, source: handle, spellLifesteal: bool): nil` | server | Heal this unit (with more parameters). |
| `Hold(): nil` | server | Hold position. |
| `Interrupt(): nil` | server |  |
| `InterruptChannel(): nil` | server |  |
| `InterruptMotionControllers(findClearSpace: bool): nil` | server |  |
| `IsAlive(): bool` | server | Is this unit alive? |
| `IsAncient(): bool` | both | Is this unit an Ancient? |
| `IsAttackImmune(): bool` | both |  |
| `IsAttacking(): bool` | server |  |
| `IsAttackingEntity(entity: CDOTA_BaseNPC): bool` | server |  |
| `IsBarracks(): bool` | both | Is this unit a Barracks? |
| `IsBlind(): bool` | both |  |
| `IsBlockDisabled(): bool` | server |  |
| `IsBoss(): bool` | both | Is this unit a boss? |
| `IsBossCreature(): bool` | server | Is this unit a Boss Creature? (used by custom games). |
| `IsBuilding(): bool` | both | Is this unit a building? |
| `IsChanneling(): bool` | server | Is this unit currently channeling a spell? |
| `IsClone(): bool` | server | Is this unit a clone? (Meepo). |
| `IsCommandRestricted(): bool` | both |  |
| `IsConsideredHero(): bool` | both | Is this unit a considered a hero for targeting purposes? |
| `IsControllableByAnyPlayer(): bool` | both | Is this unit controlled by any non-bot player? |
| `IsCourier(): bool` | both | Is this unit a courier? |
| `IsCreature(): bool` | both | Is this a Creature type NPC? |
| `IsCreep(): bool` | both | Is this unit a creep? |
| `IsCreepHero(): bool` | both | Is this unit a creep hero? |
| `IsCurrentlyHorizontalMotionControlled(): bool` | server |  |
| `IsCurrentlyVerticalMotionControlled(): bool` | server |  |
| `IsDebuffImmune(): bool` | both |  |
| `IsDisarmed(): bool` | both |  |
| `IsDominated(): bool` | both |  |
| `IsEvadeDisabled(): bool` | both |  |
| `IsFeared(): bool` | both |  |
| `IsFort(): bool` | both | Is this unit an Ancient? |
| `IsFrozen(): bool` | both |  |
| `IsHero(): bool` | both | Is this a hero or hero illusion? |
| `IsHeroWard(): bool` | server | Is this a Hero Ward? |
| `IsHexed(): bool` | both |  |
| `IsIdle(): bool` | server | Is this creature currently idle? |
| `IsIllusion(): bool` | both |  |
| `IsInRangeOfShop(shopType: DOTA_SHOP_TYPE, physical: bool): bool` | server | Ask whether this unit is in range of the specified shop. |
| `IsInventoryEnabled(): bool` | client | Does this unit have an inventory. |
| `IsInvisible(): bool` | both |  |
| `IsInvulnerable(): bool` | both |  |
| `IsLowAttackPriority(): bool` | both |  |
| `IsMagicImmune(): bool` | both |  |
| `IsMovementImpaired(): bool` | server |  |
| `IsMoving(): bool` | both | Is this unit moving? |
| `IsMuted(): bool` | both |  |
| `IsNeutralUnitType(): bool` | both | Is this a neutral? |
| `IsNightmared(): bool` | both |  |
| `IsOpposingTeam(team: DOTATeam_t): bool` | server |  |
| `IsOther(): bool` | both | Is this unit a ward-type unit? |
| `IsOutOfGame(): bool` | both |  |
| `IsOwnedByAnyPlayer(): bool` | both | Is this unit owned by any non-bot player? |
| `IsPhantom(): bool` | both | Is this a phantom unit? |
| `IsPhantomBlocker(): bool` | server |  |
| `IsPhased(): bool` | server |  |
| `IsPositionInRange(position: Vector, range: float): bool` | server |  |
| `IsRangedAttacker(): bool` | both | Is this unit a ranged attacker? |
| `IsRealHero(): bool` | both | Is this a real hero? |
| `IsReincarnating(): bool` | server |  |
| `IsRooted(): bool` | both |  |
| `IsShrine(): bool` | server | Is this a shrine? |
| `IsSilenced(): bool` | both |  |
| `IsSpeciallyDeniable(): bool` | both |  |
| `IsSpeciallyUndeniable(): bool` | both |  |
| `IsStrongIllusion(): bool` | both |  |
| `IsStunned(): bool` | both |  |
| `IsSummoned(): bool` | both | Is this unit summoned? |
| `IsTaunted(): bool` | both |  |
| `IsTempestDouble(): bool` | server |  |
| `IsTower(): bool` | both | Is this a tower? |
| `IsUnableToMiss(): bool` | server |  |
| `IsUnselectable(): bool` | both |  |
| `IsUntargetable(): bool` | client |  |
| `IsUntargetableFrom(targettingSource: handle): bool` | both |  |
| `IsWard(): bool` | server | Is this a Ward? |
| `IsZombie(): bool` | server | Is this entity an Undying Zombie? |
| `Kill(ability: CDOTABaseAbility \| nil, attacker: CDOTA_BaseNPC \| nil): nil` | server | Kills this NPC, with the params Ability and Attacker. |
| `MakeIllusion(): nil` | server |  |
| `MakePhantomBlocker(): nil` | server |  |
| `MakeVisibleDueToAttack(team: DOTATeam_t, radius: float): nil` | server |  |
| `MakeVisibleToTeam(team: DOTATeam_t, duration: float): nil` | server |  |
| `ManageModelChanges(): nil` | server |  |
| `ModifyHealth(desiredHealthValue: int, ability: CDOTABaseAbility \| nil, lethal: bool, additionalFlags: int): nil` | server | Sets the health to a specific value, with optional flags or inflictors. |
| `MoveToNPC(npc: CDOTA_BaseNPC): nil` | server | Move to follow a unit. |
| `MoveToNPCToGiveItem(npc: CDOTA_BaseNPC, item: CDOTA_Item): nil` | server | Give an item to another unit. |
| `MoveToPosition(dest: Vector): nil` | server | Issue a Move-To command. |
| `MoveToPositionAggressive(dest: Vector): nil` | server | Issue an Attack-Move-To command. |
| `MoveToTargetToAttack(target: CDOTA_BaseNPC): nil` | server | Move to a target to attack. |
| `NoHealthBar(): bool` | both |  |
| `NoTeamMoveTo(): bool` | both |  |
| `NoTeamSelect(): bool` | both |  |
| `NotifyWearablesOfModelChange(originalModel: bool): nil` | server |  |
| `NotOnMinimap(): bool` | both |  |
| `NotOnMinimapForEnemies(): bool` | both |  |
| `NoUnitCollision(): bool` | both |  |
| `OnCommandMoveToDirection(pos: Vector): nil` | server | Tells the underlying AI to move in the given direction, skipping Dota orders. |
| `PassivesDisabled(): bool` | both |  |
| `PatrolToPosition(dest: Vector): nil` | server | Issue a Patrol-To command. |
| `PerformAttack(target: CDOTA_BaseNPC, useCastAttackOrb: bool, processProcs: bool, skipCooldown: bool, ignoreInvis: bool, useProjectile: bool, fakeAttack: bool, neverMiss: bool): nil` | server | Performs an attack on a target. |
| `PickupDroppedItem(item: CDOTA_Item): nil` | server | Pick up a dropped item. |
| `PickupRune(item: CDOTA_Item): nil` | server | Pick up a rune. |
| `PlayVCD(vcd: string): nil` | server | Play a VCD on the NPC. |
| `ProvidesVision(): bool` | both |  |
| `Purge(removePositiveBuffs: bool, removeDebuffs: bool, frameOnly: bool, removeStuns: bool, removeExceptions: bool): nil` | server |  |
| `QueueConcept(delay: float, criteriaTable: handle, completionCallbackFn: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'didActuallySpeak', 'types': ['bool']}, {'name': 'callbackInfo', 'types': ['table']}]}, context: table, callbackInfo: table): nil` | server | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a delay. |
| `QueueTeamConcept(delay: float, criteriaTable: handle, completionCallbackFn: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'didActuallySpeak', 'types': ['bool']}, {'name': 'callbackInfo', 'types': ['table']}]}, context: table, callbackInfo: table): nil` | server | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a delay, for the same team this speaker is on. |
| `QueueTeamConceptNoSpectators(delay: float, criteriaTable: handle, completionCallbackFn: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'didActuallySpeak', 'types': ['bool']}, {'name': 'callbackInfo', 'types': ['table']}]}, context: table, callbackInfo: table): nil` | server | Queue a response system concept with the TLK_DOTA_CUSTOM concept, after a delay, for the same team this speaker is on. Is not played for spectators. |
| `RemoveAbility(abilityName: string): nil` | server | Remove an ability from this unit by name. |
| `RemoveAbilityByHandle(ability: CDOTABaseAbility): nil` | server | Remove the passed ability from this unit. |
| `RemoveAbilityFromIndexByName(abilityName: string): nil` | server |  |
| `RemoveAllModifiers(targets: {'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1} \| {'kind': 'literal', 'value': 2}, now: bool, permanent: bool, death: bool): nil` | server |  |
| `RemoveAllModifiersOfName(scriptName: string): nil` | server | Removes all copies of a modifier. |
| `RemoveGesture(activity: GameActivity_t): nil` | server | Remove the given gesture activity. |
| `RemoveHorizontalMotionController(buff: CDOTA_Buff): nil` | server |  |
| `RemoveItem(item: CDOTA_Item): nil` | server | Removes the passed item from this unit's inventory and deletes it. |
| `RemoveModifierByName(scriptName: string): nil` | server | Removes a modifier. |
| `RemoveModifierByNameAndCaster(scriptName: string, caster: CDOTA_BaseNPC): nil` | server | Removes a modifier that was cast by the given caster. |
| `RemoveNoDraw(): nil` | server | Remove the no draw flag. |
| `RemoveVerticalMotionController(buff: CDOTA_Buff): nil` | server |  |
| `RespawnUnit(): nil` | server | Respawns the target unit if it can be respawned. |
| `Script_GetAttackRange(): float` | both | Gets this unit's attack range after all modifiers. |
| `Script_GetMagicalArmorValue(inflictor: handle): float` | both | Returns current magical armor value. |
| `Script_IsDeniable(): bool` | both |  |
| `Script_ReduceMana(mana: float, ability: handle): float` | server | Remove mana from this unit, this can be used for involuntary mana loss, not for mana that is spent. |
| `SellItem(item: CDOTA_Item): nil` | server | Sells the passed item in this unit's inventory. |
| `SetAbilityByIndex(ability: CDOTABaseAbility, index: int): nil` | server | Set the ability by index. |
| `SetAcquisitionRange(range: int): nil` | server |  |
| `SetAdditionalBattleMusicWeight(weight: float): nil` | server | Combat involving this creature will have this weight added to the music calcuations. |
| `SetAggroTarget(aggroTarget: CDOTA_BaseNPC): nil` | server | Set this unit's aggro target to a specified unit. |
| `SetAttackCapability(attackCapabilities: DOTAUnitAttackCapability_t): nil` | server |  |
| `SetAttacking(attackTarget: CDOTA_BaseNPC \| nil): nil` | server |  |
| `SetBaseAttackTime(baseAttackTime: float): nil` | server |  |
| `SetBaseDamageMax(max: int): nil` | server | Sets the maximum base damage. |
| `SetBaseDamageMin(min: int): nil` | server | Sets the minimum base damage. |
| `SetBaseHealthRegen(healthRegen: float): nil` | server |  |
| `SetBaseMagicalResistanceValue(magicalResistanceValue: float): nil` | server | Sets base magical armor value. |
| `SetBaseManaRegen(manaRegen: float): nil` | server |  |
| `SetBaseMaxHealth(baseMaxHealth: float): nil` | server | Set a new base max health value. |
| `SetBaseMoveSpeed(moveSpeed: int): nil` | server |  |
| `SetCanSellItems(canSell: bool): nil` | server | Set whether or not this unit is allowed to sell items (bCanSellItems). |
| `SetControllableByAllPlayers(controllableByAllPlayers: bool): nil` | server | Set this unit controllable by all players. |
| `SetControllableByPlayer(playerId: PlayerID, skipAdjustingPosition: bool): nil` | server | Set this unit controllable by the player with the passed ID. |
| `SetCursorCastTarget(entity: CDOTA_BaseNPC \| nil): nil` | server |  |
| `SetCursorPosition(location: Vector): nil` | server |  |
| `SetCursorTargetingNothing(targetingNothing: bool): nil` | server |  |
| `SetCustomHealthLabel(label: string, r: int, g: int, b: int): nil` | server |  |
| `SetDayTimeVisionRange(range: int): nil` | server | Set the base vision range. |
| `SetDeathXP(xpBounty: int): nil` | server | Set the XP bounty on this unit. |
| `SetFollowRange(followRange: float): nil` | server |  |
| `SetForceAttackTarget(npc: CDOTA_BaseNPC \| nil): nil` | server |  |
| `SetForceAttackTargetAlly(npc: CDOTA_BaseNPC \| nil): nil` | server |  |
| `SetHasInventory(hasInventory: bool): nil` | server | Set if this unit has an inventory. |
| `SetHealthBarOffsetOverride(offset: int): nil` | server |  |
| `SetHullRadius(hullRadius: float): nil` | server | Set the collision hull radius of this NPC. |
| `SetIdleAcquire(idleAcquire: bool): nil` | server |  |
| `SetInitialGoalEntity(goal: CBaseEntity \| nil): nil` | server | Sets the initial waypoint goal for this NPC. |
| `SetInitialGoalPosition(position: Vector): nil` | server | Set waypoint position for this NPC. |
| `SetMana(mana: float): nil` | server | Set the mana on this unit. |
| `SetMaximumGoldBounty(goldBountyMax: int): nil` | server | Set the maximum gold bounty for this unit. |
| `SetMaxMana(maxMana: float): nil` | server | Set the maximum mana of this unit. |
| `SetMinimumGoldBounty(goldBountyMin: int): nil` | server | Set the minimum gold bounty for this unit. |
| `SetModifierStackCount(scriptName: string, caster: CDOTA_BaseNPC, stackCount: int): nil` | server | Sets the stack count of a given modifier. |
| `SetMoveCapability(moveCapabilities: DOTAUnitMoveCapability_t): nil` | server |  |
| `SetMustReachEachGoalEntity(must: bool): nil` | server | Set whether this NPC is required to reach each goal entity, rather than being allowed to unkink their path. |
| `SetNeverMoveToClearSpace(neverMoveToClearSpace: bool): nil` | server | If set to true, we will never attempt to move this unit to clear space, even when it unphases. |
| `SetNightTimeVisionRange(range: int): nil` | server | Returns the vision range after modifiers. |
| `SetOrigin(location: Vector): nil` | server | Set the unit's origin. |
| `SetOriginalModel(modelName: string): nil` | server | Sets the original model of this entity, which it will tend to fall back to anytime its state changes. |
| `SetPhysicalArmorBaseValue(physicalArmorValue: float): nil` | server | Sets base physical armor value. |
| `SetRangedProjectileName(projectileName: string): nil` | server |  |
| `SetRevealRadius(revealRadius: float): nil` | server | Sets the client side map reveal radius for this unit. |
| `SetShouldComputeRemainingPathLength(compute: bool): nil` | server |  |
| `SetShouldDoFlyHeightVisual(shouldVisuallyFly: bool): nil` | server |  |
| `SetStolenScepter(stolenScepter: bool): nil` | server |  |
| `SetUnitCanRespawn(canRespawn: bool): nil` | server |  |
| `SetUnitName(name: string): nil` | server |  |
| `ShouldIdleAcquire(): bool` | server |  |
| `SpeakConcept(criteriaTable: handle): nil` | server | Speak a response system concept with the TLK_DOTA_CUSTOM concept. |
| `SpendMana(manaSpent: float, ability: CDOTABaseAbility): nil` | server | Spend mana from this unit, this can be used for spending mana from abilities or item usage. |
| `StartGesture(activity: GameActivity_t): nil` | server | Add the given gesture activity. |
| `StartGestureFadeWithSequenceSettings(activity: GameActivity_t): nil` | server | Add the given gesture activity faded according to its sequence settings. |
| `StartGestureWithFade(activity: GameActivity_t, fadeIn: float, fadeOut: float): nil` | server | Add the given gesture activity faded according to to the parameters. |
| `StartGestureWithFadeAndPlaybackRate(activity: int, fadeIn: float, fadeOut: float, rate: float): nil` | server | Add the given gesture activity faded according to to the parameters and with a playback rate override. |
| `StartGestureWithPlaybackRate(activity: GameActivity_t, rate: float): nil` | server | Add the given gesture activity with a playback rate override. |
| `Stop(): nil` | server | Stop the current order. |
| `StopFacing(): nil` | server |  |
| `SwapAbilities(abilityName1: string, abilityName2: string, enable1: bool, enable2: bool): nil` | server | Swaps the slots of the two passed abilities and sets them enabled/disabled. |
| `SwapItems(slot1: int, slot2: int): nil` | server | Swap the contents of two item slots (slot1, slot2). |
| `TakeItem(item: CDOTA_Item): CDOTA_Item` | server | Removed the passed item from this unit's inventory. Returns the passed item. |
| `TimeUntilNextAttack(): float` | server |  |
| `TriggerModifierDodge(ability: handle, buff: handle): bool` | server |  |
| `TriggerSpellAbsorb(ability: CDOTABaseAbility): bool` | server |  |
| `TriggerSpellReflect(ability: CDOTABaseAbility): nil` | server | Trigger the Lotus Orb-like effect.(hAbility). |
| `UnHideAbilityToSlot(abilityName: string, replacedAbilityName: string): nil` | server | Makes the first ability unhidden, and puts it where second ability currently is. Will do nothing if the first ability is already unhidden and in a valid slot. |
| `UnitCanRespawn(): bool` | both | Can the unit respawn? |
| `WasKilledPassively(): bool` | server |  |

### CDOTA_BaseNPC_Building

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetInvulnCount(): int` | server | Get the invulnerability count for a building. |
| `SetInvulnCount(invulnCount: int): nil` | server | Set the invulnerability counter of this building. |

### CDOTA_BaseNPC_Creature

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddItemDrop(dropData: table): nil` | server | Add the specified item drop to this creature. |
| `CreatureLevelUp(levels: int): nil` | server | Level the creature up by the specified number of levels. |
| `GetDisableResistance(): float` | server | Set creature's current disable resistance. |
| `GetUltimateDisableResistance(): float` | server | Set creature's current disable resistance from ultimates. |
| `IsChampion(): bool` | server | Is this unit a champion? |
| `IsReincarnating(): bool` | server | Is this creature respawning? |
| `RemoveAllItemDrops(): nil` | server | Remove all item drops from this creature. |
| `SetAggroOnOwnerOnDamage(aggro: bool): nil` | server | Does this creature aggro on the owner of the attacking unit when taking damage? |
| `SetArmorGain(armorGain: float): nil` | server | Set the armor gained per level on this creature. |
| `SetAttackTimeGain(attackTimeGain: float): nil` | server | Set the attack time gained per level on this creature. |
| `SetBountyGain(bountyGain: int): nil` | server | Set the bounty gold gained per level on this creature. |
| `SetChampion(isChampion: bool): nil` | server | Flag this unit as a champion creature. |
| `SetDamageGain(damageGain: int): nil` | server | Set the damage gained per level on this creature. |
| `SetDisableResistance(disableResistance: float): nil` | server | Set creature's current disable resistance. |
| `SetDisableResistanceGain(disableResistanceGain: float): nil` | server | Set the disable resistance gained per level on this creature. |
| `SetEconItemGroup(group: int): nil` | server | Switches visible econ item group. |
| `SetHPGain(hpGain: int): nil` | server | Set the hit points gained per level on this creature. |
| `SetHPRegenGain(hpRegenGain: float): nil` | server | Set the hit points regen gained per level on this creature. |
| `SetMagicResistanceGain(magicResistanceGain: float): nil` | server | Set the magic resistance gained per level on this creature. |
| `SetManaGain(manaGain: int): nil` | server | Set the mana points gained per level on this creature. |
| `SetManaRegenGain(manaRegenGain: float): nil` | server | Set the mana points regen gained per level on this creature. |
| `SetMoveSpeedGain(moveSpeedGain: int): nil` | server | Set the move speed gained per level on this creature. |
| `SetRequiresReachingEndPath(requiresReachingEndPath: bool): nil` | server | Set whether creatures require reaching their end path before becoming idle. |
| `SetUltimateDisableResistance(ultDisableResistance: float): nil` | server | Set creature's current disable resistance from ultimates. |
| `SetXPGain(xpGain: int): nil` | server | Set the XP gained per level on this creature. |

### CDOTA_BaseNPC_Hero

Client name: `C_DOTA_BaseNPC_Hero` · Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddExperience(xp: float, reason: EDOTA_ModifyXP_Reason, applyBotDifficultyScaling: bool, incrementTotal: bool, cloneCount: int): bool` | server |  |
| `Buyback(): nil` | server | Spend the gold and buyback with this hero. |
| `CalculateStatBonus(force: bool): nil` | server | Recalculate all stats after the hero gains stats. |
| `CanEarnGold(): bool` | server | Returns boolean value result of buyback gold limit time less than game time. |
| `ClearLastHitMultikill(): nil` | server | Value is stored in PlayerResource. |
| `ClearLastHitStreak(): nil` | server | Value is stored in PlayerResource. |
| `ClearStreak(): nil` | server | Value is stored in PlayerResource. |
| `GetAbilityPoints(): int` | server | Gets the current unspent ability points. |
| `GetAdditionalOwnedUnits(): {'kind': 'array', 'types': ['CDOTA_BaseNPC']}` | server |  |
| `GetAgility(): float` | both |  |
| `GetAgilityGain(): float` | server |  |
| `GetAssists(): int` | server | Value is stored in PlayerResource. |
| `GetAttacker(index: int): int` | server |  |
| `GetBaseAgility(): float` | server |  |
| `GetBaseDamageMax(): int` | server | Hero damage is also affected by attributes. |
| `GetBaseDamageMin(): int` | server | Hero damage is also affected by attributes. |
| `GetBaseIntellect(): float` | server |  |
| `GetBaseManaRegen(): float` | server | Returns the base mana regen. |
| `GetBaseStrength(): float` | server |  |
| `GetBonusDamageFromPrimaryStat(): int` | server |  |
| `GetBuybackCooldownTime(): float` | server | Return float value for the amount of time left on cooldown for this hero's buyback. |
| `GetBuybackCost(): int` | server | Return integer value for the gold cost of a buyback. |
| `GetBuybackGoldLimitTime(): float` | server | Returns the amount of time gold gain is limited after buying back. |
| `GetCurrentXP(): int` | server | Returns the amount of XP. |
| `GetDeathGoldCost(): int` | server |  |
| `GetDeaths(): int` | server | Value is stored in PlayerResource. |
| `GetDenies(): int` | server | Value is stored in PlayerResource. |
| `GetGold(): int` | server | Returns gold amount for the player owning this hero. |
| `GetGoldBounty(): int` | server |  |
| `GetHeroFacetID(): uint` | both |  |
| `GetHeroID(): int` | server |  |
| `GetIncreasedAttackSpeed(ignoreTempAttackSpeed: bool): float` | server | Hero attack speed is also affected by agility. |
| `GetIntellect(skipNoConsume: bool): float` | both |  |
| `GetIntellectGain(): float` | server |  |
| `GetKills(): int` | server | Value is stored in PlayerResource. |
| `GetLastHits(): int` | server | Value is stored in PlayerResource. |
| `GetMostRecentDamageTime(): float` | server |  |
| `GetMultipleKillCount(): int` | server |  |
| `GetNumAttackers(): int` | server |  |
| `GetNumItemsInInventory(): int` | server |  |
| `GetNumItemsInStash(): int` | server |  |
| `GetPhysicalArmorBaseValue(): float` | server | Hero armor is affected by attributes. |
| `GetPlayerID(): PlayerID` | server | Returns player ID of the player owning this hero. |
| `GetPrimaryAttribute(): Attributes` | server |  |
| `GetPrimaryStatValue(): float` | server |  |
| `GetReplicatingOtherHero(): CDOTA_BaseNPC_Hero, nil` | server | If hero is under Replicate effect, returns original hero entity. |
| `GetRespawnsDisabled(): bool` | server | Is this hero prevented from respawning? |
| `GetRespawnTime(): float` | server |  |
| `GetStreak(): int` | server | Value is stored in PlayerResource. |
| `GetStrength(): float` | both |  |
| `GetStrengthGain(): float` | server |  |
| `GetTimeUntilRespawn(): float` | server |  |
| `GetTogglableWearable(slotType: DOTASlotType_t): CBaseAnimatingActivity, nil` | server | Get wearable entity in slot (slot). |
| `HasAnyAvailableInventorySpace(): bool` | server |  |
| `HasFlyingVision(): bool` | server |  |
| `HasOwnerAbandoned(): bool` | server |  |
| `HasRoomForItem(itemName: string, includeStashCombines: bool, allowSelling: bool): int` | server |  |
| `HeroLevelUp(playEffects: bool): nil` | server | Levels up the hero, true or false to play effects. |
| `IncrementAssists(killerId: PlayerID): nil` | server | Value is stored in PlayerResource. |
| `IncrementDeaths(killerId: PlayerID): nil` | server | Value is stored in PlayerResource. |
| `IncrementDenies(): nil` | server | Value is stored in PlayerResource. |
| `IncrementKills(victimId: PlayerID): nil` | server | Passed ID is for the victim, killer ID is ID of the current hero.  Value is stored in PlayerResource. |
| `IncrementLastHitMultikill(): nil` | server | Value is stored in PlayerResource. |
| `IncrementLastHits(): nil` | server | Value is stored in PlayerResource. |
| `IncrementLastHitStreak(): nil` | server | Value is stored in PlayerResource. |
| `IncrementNearbyCreepDeaths(): nil` | server | Value is stored in PlayerResource. |
| `IncrementStreak(): nil` | server | Value is stored in PlayerResource. |
| `IsBuybackDisabledByDevilsBargain(): bool` | server |  |
| `IsReincarnating(): bool` | server |  |
| `IsStashEnabled(): bool` | server |  |
| `KilledHero(hero: CDOTA_BaseNPC_Hero, inflictor: CDOTABaseAbility \| nil): nil` | server |  |
| `ModifyAgility(newAgility: float): nil` | server | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `ModifyGold(goldChange: int, reliable: bool, reason: EDOTA_ModifyGold_Reason): int` | server | Gives this hero some gold. |
| `ModifyGoldFiltered(goldChange: int, reliable: bool, reason: EDOTA_ModifyGold_Reason): int` | server | Gives this hero some gold, using the gold filter if extra filtering is on. |
| `ModifyIntellect(newIntellect: float): nil` | server | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `ModifyStrength(newStrength: float): nil` | server | Adds passed value to base attribute value, then calls CalculateStatBonus. |
| `PerformTaunt(): nil` | server |  |
| `RecordLastHit(): nil` | server |  |
| `RespawnHero(buyBack: bool, respawnPenalty: bool): nil` | server | Respawn this hero. |
| `SetAbilityPoints(points: int): nil` | server | Sets the current unspent ability points. |
| `SetBaseAgility(agility: float): nil` | server |  |
| `SetBaseIntellect(intellect: float): nil` | server |  |
| `SetBaseStrength(strength: float): nil` | server |  |
| `SetBotDifficulty(difficulty: int): nil` | server |  |
| `SetBuybackCooldownTime(time: float): nil` | server | Sets the buyback cooldown time. |
| `SetBuyBackDisabledByDevilsBargain(buybackDisabled: bool): nil` | server |  |
| `SetBuybackGoldLimitTime(time: float): nil` | server | Set the amount of time gold gain is limited after buying back. |
| `SetCustomDeathXP(value: int): nil` | server | Sets a custom experience value for this hero.  Note, GameRules boolean must be set for this to work! |
| `SetGold(gold: int, reliable: bool): nil` | server | Sets the gold amount for the player owning this hero. |
| `SetPlayerID(playerId: PlayerID): nil` | server |  |
| `SetPrimaryAttribute(primaryAttribute: Attributes): nil` | server | Set this hero's primary attribute value. |
| `SetRespawnPosition(origin: Vector): nil` | server |  |
| `SetRespawnsDisabled(disableRespawns: bool): nil` | server | Prevent this hero from respawning. |
| `SetStashEnabled(enabled: bool): nil` | server |  |
| `SetTimeUntilRespawn(time: float): nil` | server |  |
| `ShouldDoFlyHeightVisual(): bool` | server |  |
| `SpendGold(cost: int, reason: EDOTA_ModifyGold_Reason): nil` | server |  |
| `UpgradeAbility(ability: CDOTABaseAbility): nil` | server | This upgrades the passed ability if it exists and the hero has enough ability points. |
| `WillReincarnate(): bool` | server |  |

### CDOTA_BaseNPC_LotusPool

Extends `CDOTA_BaseNPC_Building`

_No members._

### CDOTA_BaseNPC_NeutralItemStash

Extends `CDOTA_BaseNPC_Building`

_No members._

### CDOTA_BaseNPC_Shop

Extends `CDOTA_BaseNPC_Building`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetShopType(): DOTA_SHOP_TYPE` | server | Get the DOTA_SHOP_TYPE. |
| `SetShopType(shopType: DOTA_SHOP_TYPE): nil` | server | Set the DOTA_SHOP_TYPE. |

### CDOTA_BaseNPC_Trap_Ward

Extends `CDOTA_BaseNPC_Creature`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetTrapTarget(): Vector` | server | Get the trap target for this entity. |
| `SetAnimation(animation: string): nil` | server | Set the animation sequence for this entity. |

### CDOTA_BaseNPC_Watch_Tower

Extends `CDOTA_BaseNPC_Building`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetInteractAbilityName(): string` | server | The name of the ability used when triggering interaction on the outpost. |
| `SetInteractAbilityName(interactAbilityName: string): nil` | server | The name of the ability used when triggering interaction on the outpost. |

### CDOTA_Buff

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddParticle(index: int, destroyImmediately: bool, statusEffect: bool, priority: int, heroEffect: bool, overheadEffect: bool): nil` | both |  |
| `CheckStateToTable(table: handle): nil` | both |  |
| `DecrementStackCount(): nil` | both | Decrease this modifier's stack count by 1. |
| `Destroy(): nil` | both | Run all associated destroy functions, then remove the modifier. |
| `DestroyOnExpire(): bool` | both |  |
| `ForceRefresh(): nil` | both | Run all associated refresh functions on this modifier as if it was re-applied. |
| `GetAbility(): CDOTABaseAbility, nil` | both | Get the ability that generated the modifier. |
| `GetAuraDuration(): float` | both | Returns aura stickiness (default 0.5). |
| `GetAuraOwner(): CDOTA_BaseNPC, nil` | both | Returns the owner of the aura modifier, that applied this modifier. Always `nil` on the client. |
| `GetCaster(): CDOTA_BaseNPC, nil` | both | Get the owner of the ability responsible for the modifier. |
| `GetClass(): string` | both |  |
| `GetCreationTime(): float` | both |  |
| `GetDieTime(): float` | both |  |
| `GetDuration(): float` | both |  |
| `GetElapsedTime(): float` | both |  |
| `GetLastAppliedTime(): float` | both |  |
| `GetName(): string` | both |  |
| `GetParent(): CDOTA_BaseNPC` | both | Get the unit the modifier is parented to. |
| `GetRemainingTime(): float` | both |  |
| `GetSerialNumber(): int` | both |  |
| `GetStackCount(): int` | both |  |
| `HasFunction(function: modifierfunction): bool` | both |  |
| `IncrementStackCount(): nil` | both | Increase this modifier's stack count by 1. |
| `IsDebuff(): bool` | both |  |
| `IsHexDebuff(): bool` | both |  |
| `IsNull(): bool` | both | Has underlying C++ entity object been deleted? |
| `IsStunDebuff(): bool` | both |  |
| `SendBuffRefreshToClients(): nil` | server |  |
| `SetDuration(duration: float, informClient: bool): nil` | both |  |
| `SetOverheadEffectOffset(offset: float): bool` | both |  |
| `SetStackCount(count: int): nil` | both |  |
| `StartIntervalThink(interval: float): nil` | both | Start this modifier's think function (OnIntervalThink) with the given interval (float).  To stop, call with -1. |

### CDOTA_CustomUIManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `DynamicHud_Create(playerId: PlayerID, elementId: string, layoutFileName: string, dialogVariables: handle): nil` | server | Create a new custom UI HUD element for the specified player(s). |
| `DynamicHud_Destroy(playerId: PlayerID, elementId: string): nil` | server | Destroy a custom hud element. |
| `DynamicHud_SetDialogVariables(playerId: PlayerID, elementId: string, dialogVariables: handle): nil` | server | Add or modify dialog variables for an existing custom hud element. |
| `DynamicHud_SetVisible(playerId: PlayerID, elementId: string, visible: bool): nil` | server | Toggle the visibility of an existing custom hud element. |

### CDOTA_Item

Client name: `C_DOTA_Item` · Extends `CDOTABaseAbility`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CanBeUsedOutOfInventory(): bool` | server |  |
| `CanOnlyPlayerHeroPickup(): bool` | client |  |
| `GetContainer(): CDOTA_Item_Physical, nil` | server | Get the container for this item. |
| `GetCost(): int` | server |  |
| `GetCurrentCharges(): int` | both | Get the number of charges this item currently has. |
| `GetInitialCharges(): int` | both | Get the initial number of charges this item has. |
| `GetItemSlot(): {'kind': 'literal', 'value': -1}, DOTAScriptInventorySlot_t` | both |  |
| `GetItemState(): int` | server | Gets whether item is unequipped or ready. |
| `GetParent(): handle` | server | Get the parent for this item. |
| `GetPurchaser(): CDOTA_BaseNPC, nil` | server | Get the purchaser for this item. |
| `GetPurchaseTime(): float` | server | Get the purchase time of this item. |
| `GetSecondaryCharges(): int` | both | Get the number of secondary charges this item currently has. |
| `GetShareability(): EShareAbility` | both |  |
| `GetValuelessCharges(): int` | server | Get the number of valueless charges this item currently has. |
| `IsActiveNeutral(): bool` | server |  |
| `IsAlertableItem(): bool` | both |  |
| `IsCastOnPickup(): bool` | both |  |
| `IsCombinable(): bool` | server |  |
| `IsCombineLocked(): bool` | server |  |
| `IsDisassemblable(): bool` | both |  |
| `IsDroppable(): bool` | both |  |
| `IsInBackpack(): bool` | both |  |
| `IsItem(): bool` | both |  |
| `IsKillable(): bool` | both |  |
| `IsMuted(): bool` | both |  |
| `IsPermanent(): bool` | both | Is this a permanent item? |
| `IsPurchasable(): bool` | both |  |
| `IsRecipe(): bool` | both |  |
| `IsRecipeGenerated(): bool` | both |  |
| `IsSellable(): bool` | both |  |
| `IsStackable(): bool` | both |  |
| `LaunchLoot(autoUse: bool, height: float, duration: float, endPoint: Vector, teleportOwner: CDOTA_BaseNPC_Hero \| nil): nil` | server |  |
| `LaunchLootInitialHeight(autoUse: bool, initialHeight: float, launchHeight: float, duration: float, endPoint: Vector): nil` | server |  |
| `LaunchLootRequiredHeight(autoUse: bool, requiredHeight: float, height: float, duration: float, endPoint: Vector): nil` | server |  |
| `ModifyNumValuelessCharges(charges: int): nil` | server | Modifies the number of valueless charges on this item. |
| `OnEquip(): nil` | server |  |
| `OnUnequip(): nil` | server |  |
| `RequiresCharges(): bool` | both |  |
| `SetCanBeUsedOutOfInventory(value: bool): nil` | server |  |
| `SetCastOnPickup(castOnPickUp: bool): nil` | server |  |
| `SetCombineLocked(combineLocked: bool): nil` | server |  |
| `SetCurrentCharges(charges: int): nil` | server | Set the number of charges on this item. |
| `SetDroppable(droppable: bool): nil` | server |  |
| `SetItemState(state: int): nil` | server | Sets whether item is unequipped or ready. |
| `SetOnlyPlayerHeroPickup(onlyPlayerHero: bool): nil` | server |  |
| `SetPurchaser(purchaser: CDOTA_BaseNPC \| nil): nil` | server | Set the purchaser of record for this item. |
| `SetPurchaseTime(time: float): nil` | server | Set the purchase time of this item. |
| `SetSecondaryCharges(charges: int): nil` | server | Set the number of secondary charges on this item. |
| `SetSellable(sellable: bool): nil` | server |  |
| `SetShareability(shareability: EShareAbility): nil` | server |  |
| `SetStacksWithOtherOwners(stacksWithOtherOwners: bool): nil` | server |  |
| `SpendCharge(delayRemove: float): nil` | server |  |
| `StacksWithOtherOwners(): bool` | server |  |
| `Think(): nil` | server | Think this item. |

### CDOTA_Item_BagOfGold

Extends `CDOTA_Item`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetLifeTime(time: float): nil` | server | Set the life time of this item. |

### CDOTA_Item_DataDriven

Extends `CDOTA_Item`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ApplyDataDrivenModifier(caster: CDOTA_BaseNPC, target: CDOTA_BaseNPC, modifierName: string, modifierTable: table \| nil): nil` | server | Applies a data driven modifier to the target. |
| `ApplyDataDrivenThinker(caster: CDOTA_BaseNPC, location: Vector, modifierName: string, modifierTable: table \| nil): CDOTA_Buff` | server | Applies a data driven thinker at the location. |

### CDOTA_Item_EmptyBottle

Client name: `C_DOTA_Item_EmptyBottle` · Extends `CDOTA_Item`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ClearStoredRune(): nil` | server | Clear the stored rune. |
| `OnRune(runeType: int): bool` | server | Place a rune in the bottle. |
| `SetStoredRune(runeType: int): nil` | server | Set the stored rune. |

### CDOTA_Item_Lua

Client name: `C_DOTA_Item_Lua` · Extends `CDOTA_Item`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CanUnitPickUp(unit: CDOTA_BaseNPC): bool` | server | Returns true if this item can be picked up by the target unit. |
| `CastFilterResult(): UnitFilterResult` | both | Determine whether an issued command with no target is valid. |
| `CastFilterResultLocation(location: Vector): UnitFilterResult` | both | Determine whether an issued command on a location is valid. |
| `CastFilterResultTarget(target: CDOTA_BaseNPC): UnitFilterResult` | both | Determine whether an issued command on a target is valid. |
| `GetAbilityTextureName(): string` | client | Allows code overriding of the item texture shown in the HUD. |
| `GetAOERadius(): float` | client | Controls the size of the AOE casting cursor. |
| `GetAssociatedPrimaryAbilities(): string` | server | Returns abilities that are stolen simultaneously, or otherwise related in functionality. |
| `GetAssociatedSecondaryAbilities(): string` | server | Returns other abilities that are stolen simultaneously, or otherwise related in functionality.  Generally hidden abilities. |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR` | both | Return cast behavior type of this ability. |
| `GetCastRange(location: Vector, target: CDOTA_BaseNPC \| nil): int` | both | Return cast range of this ability. |
| `GetChannelledHealthCostPerSecond(level: int): int` | both | Return health cost per second of channeling at the given level (-1 is current). |
| `GetChannelledManaCostPerSecond(level: int): int` | both | Return mana cost at the given level per second while channeling (-1 is current). |
| `GetChannelStartTime(): float` | both | Return the channel start time of this ability. |
| `GetChannelTime(): float` | both | Return the channel time of this ability. |
| `GetConceptRecipientType(): int` | server | Return who hears speech when this spell is cast. |
| `GetCooldown(level: int): float` | both | Return cooldown of this ability. |
| `GetCustomCastError(): string` | both | Return the error string of a failed command with no target. |
| `GetCustomCastErrorLocation(location: Vector): string` | both | Return the error string of a failed command on a location. |
| `GetCustomCastErrorTarget(target: CDOTA_BaseNPC): string` | both | Return the error string of a failed command on a target. |
| `GetCustomHudErrorMessage(reason: int): string` | both | (DOTA_INVALID_ORDERS nReason) Return the error string of a failed order. |
| `GetEffectiveCastRange(location: Vector, target: handle): int` | both | Return cast range of this ability, taking modifiers into account. |
| `GetGoldCost(level: int): int` | both | Return gold cost at the given level (-1 is current). |
| `GetHealthCost(level: int): int` | both | Return health cost at the given level (-1 is current). |
| `GetIntrinsicModifierName(): string` | server | Returns the name of the modifier applied passively by this ability. |
| `GetManaCost(level: int): int` | both | Return mana cost at the given level (-1 is current). |
| `GetPlaybackRateOverride(): float` | server | Return the animation rate of the cast animation. |
| `IsHiddenAbilityCastable(): bool` | server | Returns true if this ability can be used when not on the action panel. |
| `IsHiddenWhenStolen(): bool` | server | Returns true if this ability is hidden when stolen by Spell Steal. |
| `IsMuted(): bool` | both | Returns whether this item is muted or not. |
| `IsRefreshable(): bool` | server | Returns true if this ability is refreshed by Refresher Orb. |
| `IsStealable(): bool` | server | Returns true if this ability can be stolen by Spell Steal. |
| `OnAbilityPhaseInterrupted(): nil` | server | Cast time did not complete successfully. |
| `OnAbilityPhaseStart(): bool` | server | Cast time begins (return true for successful cast). |
| `OnChannelFinish(interrupted: bool): nil` | server | Channel finished. |
| `OnChannelThink(interval: float): nil` | server | Channeling is taking place. |
| `OnChargeCountChanged(spent: bool): nil` | server | Runs when item's charge count changes. bSpent is true when the charge count change is coming from SpendCharge. |
| `OnHeroCalculateStatBonus(): nil` | server | Caster (hero only) gained a level, skilled an ability, or received a new stat bonus. |
| `OnHeroDiedNearby(unit: CDOTA_BaseNPC, attacker: CDOTA_BaseNPC, event: table): nil` | server | A hero has died in the vicinity (ie Urn), takes table of params. |
| `OnHeroLevelUp(): nil` | server | Caster gained a level. |
| `OnInventoryContentsChanged(): nil` | server | Caster inventory changed. |
| `OnItemEquipped(item: CDOTA_Item): nil` | server | Caster equipped item. |
| `OnOwnerDied(): nil` | server | Caster died. |
| `OnOwnerSpawned(): nil` | server | Caster respawned or spawned for the first time. |
| `OnProjectileHit(target: CDOTA_BaseNPC \| nil, location: Vector): bool, nil` | server | Projectile has collided with a given target or reached its destination. If 'true` is returned, projectile would be destroyed. |
| `OnProjectileThink(location: Vector): nil` | server | Projectile is actively moving. |
| `OnSpellStart(): nil` | server | Cast time finished, spell effects begin. |
| `OnStolen(sourceAbility: CDOTABaseAbility): nil` | server | Special behavior when stolen by Spell Steal. |
| `OnToggle(): nil` | server | Ability is toggled on/off. |
| `OnUnStolen(): nil` | server | Special behavior when lost by Spell Steal. |
| `OnUpgrade(): nil` | server | Ability gained a level. |
| `ProcsMagicStick(): bool` | server | Returns true if this ability will generate magic stick charges for nearby enemies. |
| `SpeakTrigger(): int` | server | Return the type of speech used. |
| `Precache(context: CScriptPrecacheContext): nil` | server |  |
| `Spawn(): nil` | both | Called when ability entity is created, after Init. |

### CDOTA_Item_Physical

Extends `CBaseAnimatingActivity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetContainedItem(): CDOTA_Item` | server | Returned the contained item. |
| `GetCreationTime(): float` | server | Returns the game time when this item was created in the world. |
| `IsLoot(): bool` | server | Is this drop flagged as a loot drop? |
| `SetContainedItem(item: CDOTA_Item): nil` | server | Set the contained item. |
| `SetIsLoot(isLoot: bool): nil` | server | Set if this drop is flagged as a loot drop. |

### CDOTA_ItemSpawner

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetItemName(): string` | server | Returns the item name. |

### CDOTA_MapTree

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CutDown(teamNumberKnownTo: int): nil` | server | Cuts down this tree. |
| `CutDownRegrowAfter(regrowAfter: float, teamNumberKnownTo: int): nil` | server | Cuts down this tree. |
| `GrowBack(): nil` | server | Grows back the tree if it was cut down. |
| `IsStanding(): bool` | server | Returns true if the tree is standing, false if it has been cut down. |

### CDOTA_Modifier_Lua

Extends `CDOTA_Buff`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AllowIllusionDuplicate(): bool` | both | True/false if this modifier is active on illusions. |
| `CanParentBeAutoAttacked(): bool` | both |  |
| `DestroyOnExpire(): bool` | both | True/false if this buff is removed when the duration expires. |
| `GetAttributes(): DOTAModifierAttribute_t` | both | Return the types of attributes applied to this modifier. |
| `GetAuraDuration(): float` | both | Returns aura stickiness. |
| `GetAuraEntityReject(entity: CDOTA_BaseNPC): bool` | both | Return true/false if this entity should receive the aura under specific conditions. |
| `GetAuraRadius(): float` | both | Return the range around the parent this aura tries to apply its buff. |
| `GetAuraSearchFlags(): DOTA_UNIT_TARGET_FLAGS` | both | Return the unit flags this aura respects when placing buffs. |
| `GetAuraSearchTeam(): DOTA_UNIT_TARGET_TEAM` | both | Return the teams this aura applies its buff to. |
| `GetAuraSearchType(): DOTA_UNIT_TARGET_TYPE` | both | Return the unit classifications this aura applies its buff to. |
| `GetCritDamage(): float` | both | A Modifier that listens to MODIFIER_PROPERTY_PREATTACK_CRITICALSTRIKE has to have a GetCritDamage implementation so we can know when to evaluate it. Value should be in 'times the original value format' e.g: 1.5 not 150. |
| `GetEffectAttachType(): ParticleAttachment_t` | both | Return the attach type of the particle system from GetEffectName. |
| `GetEffectName(): string` | both | Return the name of the particle system that is created while this modifier is active. |
| `GetHeroEffectName(): string` | both | Return the name of the hero effect particle system that is created while this modifier is active. |
| `GetModifierAura(): string` | both | The name of the secondary modifier that will be applied by this modifier (if it is an aura). |
| `GetPriority(): modifierpriority` | both | Return the priority order this modifier will be applied over others. |
| `GetStatusEffectName(): string` | both | Return the name of the status effect particle system that is created while this modifier is active. |
| `GetTexture(): string` | both | Return the name of the buff icon to be shown for this modifier. |
| `HeroEffectPriority(): modifierpriority` | both | Relationship of this hero effect with those from other buffs (higher is more likely to be shown). |
| `IsAura(): bool` | both | True/false if this modifier is an aura. |
| `IsAuraActiveOnDeath(): bool` | both | True/false if this aura provides buffs when the parent is dead. |
| `IsDebuff(): bool` | both | True/false if this modifier should be displayed as a debuff. |
| `IsHidden(): bool` | both | True/false if this modifier should be displayed on the buff bar. |
| `IsPermanent(): bool` | both |  |
| `IsPurgable(): bool` | both | True/false if this modifier can be purged. |
| `IsPurgeException(): bool` | both | True/false if this modifier can be purged by strong dispels. |
| `IsStunDebuff(): bool` | both | True/false if this modifier is considered a stun for purge reasons. |
| `OnCreated(params: table): nil` | both | Runs when the modifier is created. |
| `OnDestroy(): nil` | both | Runs when the modifier is destroyed (after unit loses modifier). |
| `OnIntervalThink(): nil` | both | Runs when the think interval occurs. |
| `OnRefresh(params: table): nil` | both | Runs when the modifier is refreshed. |
| `OnRemoved(death: bool): nil` | both | Runs when the modifier is destroyed (before unit loses modifier). |
| `OnStackCountChanged(stackCount: int): nil` | both | Runs when stack count changes (param is old count). |
| `PiercesDebuffImmunity(): bool` | both | Returns true or false on if the effects of this modifier should pierce debuff immunity. By default uses the setting from the ability. |
| `RemoveOnDeath(): bool` | both | True/false if this modifier is removed when the parent dies. |
| `SetHasCustomTransmitterData(hasCustomData: bool): nil` | both |  |
| `ShouldUseOverheadOffset(): bool` | both | Apply the overhead offset to the attached effect. |
| `StatusEffectPriority(): modifierpriority` | both | Relationship of this status effect with those from other buffs (higher is more likely to be shown). |
| `BotAttackScoreBonus(): nil` | both |  |
| `CheckState(): {'kind': 'table', 'key': ['modifierstate'], 'value': ['bool']}` | both | Return a map of enabled/disabled states. |
| `DeclareFunctions(): {'kind': 'array', 'types': ['modifierfunction']}` | both | Return a list of modifier functions this modifier implements. |
| `GetAbsoluteNoDamageMagical(event: ModifierAttackEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetAbsoluteNoDamagePhysical(event: ModifierAttackEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetAbsoluteNoDamagePure(event: ModifierAttackEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetAbsorbSpell(event: ModifierAbilityEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetActivityTranslationModifiers(): string` | both |  |
| `GetAllowEtherealAttack(): nil` | both |  |
| `GetAlwaysAllowAttack(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetAlwaysAutoAttackWhileHoldPosition(): nil` | both |  |
| `GetAttackSound(): string` | both |  |
| `GetBaseAttackPostBonus(): nil` | both |  |
| `GetBonusDayVision(): float` | both |  |
| `GetBonusDayVisionPercentage(): nil` | both |  |
| `GetBonusNightVision(): float` | both |  |
| `GetBonusNightVisionUnique(): float` | both |  |
| `GetBonusVisionPercentage(): float` | both |  |
| `GetBuffAmplification(): nil` | both |  |
| `GetConvertAttackPhysicalToPure(): nil` | both |  |
| `GetCriticalStrikeBonus(): nil` | both |  |
| `GetDisableAutoAttack(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetDisableHealing(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetDisableManaGain(): nil` | both |  |
| `GetFixedDayVision(): float` | both |  |
| `GetFixedNightVision(): float` | both |  |
| `GetForceDrawOnMinimap(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetIsIllusion(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetMagicalArmorPiercingPercentageTarget(): nil` | both |  |
| `GetMinHealth(): float` | both |  |
| `GetMinMana(): nil` | both |  |
| `GetModifierAbilityLayout(): float` | both |  |
| `GetModifierAbilityPoints(): nil` | both |  |
| `GetModifierAdditionalNutralItemDrops(): nil` | both |  |
| `GetModifierAoEBonusConstant(): nil` | both |  |
| `GetModifierAoEBonusConstantStacking(): nil` | both |  |
| `GetModifierAoEBonusPercentage(): float` | both |  |
| `GetModifierAttackHeightBonus(): nil` | both |  |
| `GetModifierAttackPointConstant(): float` | both |  |
| `GetModifierAttackRangeBonus(): float` | both |  |
| `GetModifierAttackRangeBonusPercentage(): float` | both |  |
| `GetModifierAttackRangeBonusUnique(): float` | both |  |
| `GetModifierAttackRangeOverride(): float` | both |  |
| `GetModifierAttackSpeed_Limit(): nil` | both |  |
| `GetModifierAttackSpeedAbsoluteMax(): nil` | both |  |
| `GetModifierAttackSpeedBaseOverride(): float` | both |  |
| `GetModifierAttackSpeedBonus_Constant(): float` | both |  |
| `GetModifierAttackSpeedPercentage(): float` | both |  |
| `GetModifierAttackSpeedReductionPercentage(): float` | both |  |
| `GetModifierAvoidAttackProcs(): nil` | both |  |
| `GetModifierAvoidDamage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierAvoidDamageAfterReductions(event: ModifierAttackEvent): float` | both |  |
| `GetModifierAvoidSpell(event: ModifierAttackEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierBaseArmorPerAgiBonusPercentage(): nil` | both |  |
| `GetModifierBaseAttack_BonusDamage(): float` | both |  |
| `GetModifierBaseAttackSpeedPerAgiBonusPercentage(): nil` | both |  |
| `GetModifierBaseAttackTimeConstant(): float` | both |  |
| `GetModifierBaseAttackTimeConstant_Adjust(): float` | both |  |
| `GetModifierBaseAttackTimePercentage(): float` | both |  |
| `GetModifierBaseDamageOutgoing_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierBaseDamageOutgoing_PercentageUnique(event: ModifierAttackEvent): float` | both |  |
| `GetModifierBaseHpRegenPerStrBonusPercentage(): nil` | both |  |
| `GetModifierBaseMagicResistPerIntBonusPercentage(): nil` | both |  |
| `GetModifierBaseManaRegenPerIntBonusPercentage(): nil` | both |  |
| `GetModifierBaseRegen(): float` | both |  |
| `GetModifierBecomeAgility(): nil` | both |  |
| `GetModifierBecomeIntelligence(): nil` | both |  |
| `GetModifierBecomeStrength(): nil` | both |  |
| `GetModifierBecomeUniversal(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierBonusDamageOutgoing_Percentage(): nil` | both |  |
| `GetModifierBonusLotusHeal(): nil` | both |  |
| `GetModifierBonusStats_Agility(): float` | both |  |
| `GetModifierBonusStats_Agility_Percentage(): float` | both |  |
| `GetModifierBonusStats_Intellect(): float` | both |  |
| `GetModifierBonusStats_Intellect_Percentage(): float` | both |  |
| `GetModifierBonusStats_Strength(): float` | both |  |
| `GetModifierBonusStats_Strength_Percentage(): float` | both |  |
| `GetModifierBonusUphillMissChance(): nil` | both |  |
| `GetModifierBuybackPenaltyPercent(): nil` | both |  |
| `GetModifierCanAttackTrees(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierCastRangeBonus(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierCastRangeBonusPercentage(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierCastRangeBonusStacking(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierCastRangeBonusTarget(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierChangeAbilityValue(): nil` | both |  |
| `GetModifierConstantDeathGoldCost(): float` | both |  |
| `GetModifierConstantHealthRegen(): float` | both |  |
| `GetModifierConstantManaRegen(): float` | both |  |
| `GetModifierConstantManaRegenUnique(): float` | both |  |
| `GetModifierConstantRespawnTime(): float` | both |  |
| `GetModifierConvertManaCostToHealthCost(): nil` | both |  |
| `GetModifierCooldownReduction_Constant(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierCreateBonusIllusionChance(): nil` | both |  |
| `GetModifierCreateBonusIllusionCount(): nil` | both |  |
| `GetModifierCreepDenyPercent(): nil` | both |  |
| `GetModifierDamageOutgoing_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierDamageOutgoing_Percentage_Illusion(event: ModifierAttackEvent): float` | both |  |
| `GetModifierDamageOutgoing_Percentage_Illusion_Amplify(): nil` | both |  |
| `GetModifierDamageOutgoing_PercentageMultiplicative(): nil` | both |  |
| `GetModifierDisableTurning(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierDisassembleAnything(): nil` | both |  |
| `GetModifierDodgeProjectile(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierEvasion_Constant(event: ModifierAttackEvent): float` | both |  |
| `GetModifierExtraHealthBonus(): float` | both |  |
| `GetModifierExtraHealthPercentage(): float` | both |  |
| `GetModifierExtraManaBonus(): float` | both |  |
| `GetModifierExtraManaBonusPercentage(): nil` | both |  |
| `GetModifierExtraManaPercentage(): nil` | both |  |
| `GetModifierExtraStrengthBonus(): float` | both |  |
| `GetModifierFixedAttackRate(): float` | both |  |
| `GetModifierFixedManaRegen(): nil` | both |  |
| `GetModifierForceMaxHealth(): nil` | both |  |
| `GetModifierForceMaxMana(): nil` | both |  |
| `GetModifierFoWTeam(): nil` | both |  |
| `GetModifierHasBonusNeutralItemChoice(): nil` | both |  |
| `GetModifierHealAmplify_PercentageSource(): nil` | both |  |
| `GetModifierHealAmplify_PercentageTarget(): nil` | both |  |
| `GetModifierHealthBarPips(event: ModifierAttackEvent): float` | both | Return value is a count of pips. |
| `GetModifierHealthBonus(): float` | both |  |
| `GetModifierHealthcostReduction_Constant(): nil` | both |  |
| `GetModifierHealthRegenPercentage(): float` | both |  |
| `GetModifierHealthRegenPercentageUnique(): float` | both |  |
| `GetModifierHeroFacetOverride(): nil` | both |  |
| `GetModifierHeroLevelScale(): nil` | both |  |
| `GetModifierHPRegenAmplify_Percentage(): float` | both |  |
| `GetModifierHPRegenMultiplierPreAmplification(): nil` | both |  |
| `GetModifierIgnoreCastAngle(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierIgnoreCooldown(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierIgnoreMovespeedLimit(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierIgnorePhysicalArmor(event: ModifierAttackEvent): float` | both |  |
| `GetModifierIllusionLabel(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierIncomingDamage_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierIncomingDamageConstant(event: ModifierAttackEvent): float` | both | This property controls 'universal' shield, if defined both on client and server. Return value on client should be current shield health, as a positive integer, on server - amount of damage blocked. |
| `GetModifierIncomingPhysicalDamage_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierIncomingPhysicalDamageConstant(event: ModifierAttackEvent): float` | both | This property controls 'physical' shield, if defined both on client and server. Return value on client should be current shield health, as a positive integer, on server - amount of damage blocked. |
| `GetModifierIncomingSpellDamageConstant(event: ModifierAttackEvent): float` | both | This property controls 'spell' shield, if defined both on client and server. Return value on client should be current shield health, as a positive integer, on server - amount of damage blocked. |
| `GetModifierInnateDamageBlockPctOverride(): nil` | both |  |
| `GetModifierIntellectNone(): nil` | both |  |
| `GetModifierInventorySlotRestricted(): nil` | both |  |
| `GetModifierInvisibilityAttackBehaviorException(): nil` | both |  |
| `GetModifierInvisibilityLevel(): float` | both |  |
| `GetModifierIsPackRat(): nil` | both |  |
| `GetModifierItemSellbackCost(): nil` | both |  |
| `GetModifierKillStreakBonusGoldPercentage(): nil` | both |  |
| `GetModifierKnockbackAmplification_Percentage(): nil` | both |  |
| `GetModifierLifestealRegenAmplify_Percentage(): nil` | both |  |
| `GetModifierMagical_ConstantBlock(event: ModifierAttackEvent): float` | both |  |
| `GetModifierMagicalResistanceBaseReduction(): nil` | both |  |
| `GetModifierMagicalResistanceBonus(event: ModifierAttackEvent): float` | both |  |
| `GetModifierMagicalResistanceBonusIllusions(): nil` | both |  |
| `GetModifierMagicalResistanceBonusUnique(): nil` | both |  |
| `GetModifierMagicalResistanceDecrepifyUnique(event: ModifierAttackEvent): float` | both |  |
| `GetModifierMagicalResistanceDirectModification(event: ModifierAttackEvent): float` | both |  |
| `GetModifierManaBonus(): float` | both |  |
| `GetModifierManacostReduction_Constant(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierManaDrainAmplify_Percentage(): nil` | both |  |
| `GetModifierMaxAttackRange(): float` | both |  |
| `GetModifierMinPhysicalArmor(): nil` | both |  |
| `GetModifierMiss_Percentage(): float` | both |  |
| `GetModifierMiss_Percentage_Target(): nil` | both |  |
| `GetModifierModelChange(): string` | both |  |
| `GetModifierModelScale(): float` | both |  |
| `GetModifierModelScaleAnimateTime(): nil` | both |  |
| `GetModifierModelScaleConstant(): nil` | both |  |
| `GetModifierModelScaleUseInOutEase(): nil` | both |  |
| `GetModifierMoveSpeed_Absolute(): float` | both |  |
| `GetModifierMoveSpeed_AbsoluteMax(): nil` | both |  |
| `GetModifierMoveSpeed_AbsoluteMin(): float` | both |  |
| `GetModifierMoveSpeed_Limit(): float` | both |  |
| `GetModifierMoveSpeed_MaxOverride(): nil` | both |  |
| `GetModifierMoveSpeed_MinOverride(): nil` | both |  |
| `GetModifierMoveSpeedBonus_Constant(): float` | both |  |
| `GetModifierMoveSpeedBonus_Constant_Unique(): nil` | both |  |
| `GetModifierMoveSpeedBonus_Constant_Unique_2(): float` | both |  |
| `GetModifierMoveSpeedBonus_Percentage(): float` | both |  |
| `GetModifierMoveSpeedBonus_Percentage_Unique(): float` | both |  |
| `GetModifierMoveSpeedBonus_Special_Boots(): float` | both |  |
| `GetModifierMoveSpeedBonus_Special_Boots_2(): float` | both |  |
| `GetModifierMoveSpeedMax_BonusConstant(): nil` | both |  |
| `GetModifierMoveSpeedOverride(): float` | both |  |
| `GetModifierMoveSpeedPostMultiplierBonus_Constant(): nil` | both |  |
| `GetModifierMoveSpeedReductionPercentage(): nil` | both |  |
| `GetModifierMPRegenAmplify_Percentage(): float` | both |  |
| `GetModifierMPRegenAmplify_Percentage_Unique(): nil` | both |  |
| `GetModifierMPRestoreAmplify_Percentage(): float` | both | Total amplify value is clamped to 0. |
| `GetModifierNegativeEvasion_Constant(): float` | both |  |
| `GetModifierNeutralEnhancementOptions(): nil` | both |  |
| `GetModifierNeutralTrinketOptions(): nil` | both |  |
| `GetModifierNoFreeTPScrollOnDeath(): nil` | both |  |
| `GetModifierNoVisionOfAttacker(): nil` | both |  |
| `GetModifierOverrideAbilitySpecial(event: ModifierOverrideAbilitySpecialEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierOverrideAbilitySpecialValue(event: ModifierOverrideAbilitySpecialEvent): float` | both |  |
| `GetModifierOverrideAttackDamage(): float` | both |  |
| `GetModifierOverrideBaseDamage(): nil` | both |  |
| `GetModifierOverrideCreepBounty(): nil` | both |  |
| `GetModifierOverrideUntargetableFrom(): nil` | both |  |
| `GetModifierOverrideUntargetableTo(): nil` | both |  |
| `GetModifierPercentageAttackAnimTime(): float` | both |  |
| `GetModifierPercentageCasttime(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageConvertExpToGold(): nil` | both |  |
| `GetModifierPercentageCooldown(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageCooldownOngoing(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageCooldownStacking(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageDeathGoldCost(): nil` | both |  |
| `GetModifierPercentageExpRateBoost(): float` | both |  |
| `GetModifierPercentageGoldRateBoost(): nil` | both |  |
| `GetModifierPercentageHealthcost(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageHealthcostStacking(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageKillAssistGoldBoost(): nil` | both |  |
| `GetModifierPercentageManacost(event: ModifierAbilityEvent): float` | both |  |
| `GetModifierPercentageManacostStacking(): float` | both |  |
| `GetModifierPercentageRespawnTime(): float` | both |  |
| `GetModifierPersistentInvisibility(): float` | both |  |
| `GetModifierPhysical_ConstantBlock(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPhysical_ConstantBlockBonus(): nil` | both |  |
| `GetModifierPhysical_ConstantBlockSpecial(): float` | both |  |
| `GetModifierPhysical_ConstantBlockUnavoidablePreArmor(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPhysicalArmorBase_Percentage(): float` | both | Values above 100% are ignored. |
| `GetModifierPhysicalArmorBonus(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPhysicalArmorBonusPost(): nil` | both |  |
| `GetModifierPhysicalArmorBonusUnique(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPhysicalArmorBonusUniqueActive(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPhysicalArmorTotal_Percentage(): nil` | both |  |
| `GetModifierPhysicalDamageOutgoing_Percentage(): nil` | both |  |
| `GetModifierPreAttack(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPreAttack_BonusDamage(): float` | both |  |
| `GetModifierPreAttack_BonusDamage_Proc(): float` | both |  |
| `GetModifierPreAttack_BonusDamage_Target(): nil` | both |  |
| `GetModifierPreAttack_BonusDamagePostCrit(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPreAttack_CriticalStrike(event: ModifierAttackEvent): float` | both |  |
| `GetModifierPreAttack_DeadlyBlow(): nil` | both |  |
| `GetModifierPreAttack_Target_CriticalStrike(): float` | both |  |
| `GetModifierPrereduceIncomingDamage_Mult(): nil` | both |  |
| `GetModifierPreserveNeutralItemPassives(): nil` | both |  |
| `GetModifierProcAttack_BonusDamage_Magical(event: ModifierAttackEvent): float` | both |  |
| `GetModifierProcAttack_BonusDamage_Magical_Target(): nil` | both |  |
| `GetModifierProcAttack_BonusDamage_Physical(event: ModifierAttackEvent): float` | both |  |
| `GetModifierProcAttack_BonusDamage_Pure(event: ModifierAttackEvent): float` | both |  |
| `GetModifierProcAttack_ConvertPhysicalToMagical(): nil` | both |  |
| `GetModifierProcAttack_Feedback(event: ModifierAttackEvent): float` | both |  |
| `GetModifierProjectileName(): string` | both |  |
| `GetModifierProjectileSpeed(): float` | both |  |
| `GetModifierProjectileSpeedBonus(): float` | both |  |
| `GetModifierProjectileSpeedBonusPercentage(): float` | both |  |
| `GetModifierProjectileSpeedTarget(): nil` | both |  |
| `GetModifierProperty_MagicalLifesteal(): nil` | both |  |
| `GetModifierProperty_PhysicalLifesteal(): nil` | both |  |
| `GetModifierPropertyConsumableUseSpeed(): nil` | both |  |
| `GetModifierPropertyForbidIllusions(): nil` | both |  |
| `GetModifierPropertyHealingAmplificationUnique(): nil` | both |  |
| `GetModifierPropertyManacostOverride(): nil` | both |  |
| `GetModifierPropertyRedirectHealthGain(): nil` | both |  |
| `GetModifierPropertyRestorationAmplification(): nil` | both |  |
| `GetModifierPropertyRestorationAmplificationUnique(): nil` | both |  |
| `GetModifierPropertySuppressInvalidMoveAttackOrders(): nil` | both |  |
| `GetModifierPropertyUpgradeNeutralArtifacts(): nil` | both |  |
| `GetModifierPropetyFailAttack(): nil` | both |  |
| `GetModifierProvidesFOWVision(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierRadarCooldownReduction(): float` | both |  |
| `GetModifierScepter(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both | Applies scepter when this property is active |
| `GetModifierShard(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both | Applies shard when this property is active |
| `GetModifierShareXPRune(): nil` | both |  |
| `GetModifierSlowResistance_Stacking(): nil` | both |  |
| `GEtModifierSlowResistance_Unique(): nil` | both |  |
| `GetModifierSlowResistanceAppliesToAttacks(): nil` | both |  |
| `GetModifierSpellAmplify_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierSpellAmplify_PercentageTarget(): nil` | both |  |
| `GetModifierSpellAmplify_PercentageUnique(): float` | both |  |
| `GetModifierSpellLifestealRegenAmplify_Percentage(): nil` | both |  |
| `GetModifierSpellLifestealRegenAmplify_Percentage_Unique(): nil` | both |  |
| `GetModifierSpellRedirectTarget(): nil` | both |  |
| `GetModifierSpellsRequireHP(): float` | both |  |
| `GetModifierStackingRespawnTime(): float` | both |  |
| `GetModifierStatusResistance(): float` | both |  |
| `GetModifierStatusResistanceCaster(event: ModifierUnitEvent): float` | both |  |
| `GetModifierStatusResistanceStacking(): float` | both |  |
| `GetModifierStrongIllusion(): nil` | both |  |
| `GetModifierSuperIllusion(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierSuperIllusionWithItems(): nil` | both |  |
| `GetModifierSuperIllusionWithUltimate(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierSuppressFullscreenDeathFX(): nil` | both |  |
| `GetModifierTempestDouble(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierTickGold_Multiplier(): nil` | both |  |
| `GetModifierTotal_ConstantBlock(event: ModifierAttackEvent): float` | both |  |
| `GetModifierTotal_ConstantBlockStacking(): nil` | both |  |
| `GetModifierTotalDamageOutgoing_Percentage(event: ModifierAttackEvent): float` | both |  |
| `GetModifierTotalPercentageManaRegen(): float` | both |  |
| `GetModifierTurnRate_Override(): float` | both |  |
| `GetModifierTurnRate_Percentage(): float` | both |  |
| `GetModifierTurnRateConstant(): float` | both |  |
| `GetModifierUnitDisllowUpgrading(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierUnitStatsNeedsRefresh(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetModifierXPDuringDeath(): nil` | both |  |
| `GetModifierXPFountainCountdownTimeOverride(): nil` | both |  |
| `GetModofierPropertyPseudoRandomBonus(): nil` | both |  |
| `GetOverrideAnimation(): GameActivity_t` | both |  |
| `GetOverrideAnimationRate(): float` | both |  |
| `GetOverrideAttackMagical(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetPhysicalArmorPiercingPercentageTarget(): nil` | both |  |
| `GetPrimaryStatDamageMultiplier(): float` | both |  |
| `GetRedirectSpell(): nil` | both |  |
| `GetReflectSpell(event: ModifierAbilityEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetRequiredLevel(): nil` | both |  |
| `GetSkipAttackRegulator(): nil` | both |  |
| `GetSuppressAttackProcs(): nil` | both |  |
| `GetSuppressCleave(event: ModifierAttackEvent): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetSuppressCrit(): nil` | both |  |
| `GetSuppressIncomingCrit(): nil` | both |  |
| `GetSuppressTeleport(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `GetTierTokenReroll(): nil` | both |  |
| `GetTriggerCosmeticAndEndAttack(): nil` | both |  |
| `GetUnitLifetimeFraction(): float` | both |  |
| `GetVisionDegreeRestriction(): nil` | both |  |
| `GetVisualZDelta(): float` | both |  |
| `GetVisualZSpeedBaseOverride(): nil` | both |  |
| `HasBonusNeutralItemPassive(): nil` | both |  |
| `MinAttributeLevel(): nil` | both |  |
| `MODIFIER_PROPERTY_INCOMING_DAMAGE_CONSTANT_POST(): nil` | both |  |
| `OnAbilityEndChannel(event: ModifierAbilityEvent): nil` | both |  |
| `OnAbilityExecuted(event: ModifierAbilityEvent): nil` | both |  |
| `OnAbilityFullyCast(event: ModifierAbilityEvent): nil` | both |  |
| `OnAbilityStart(event: ModifierAbilityEvent): nil` | both |  |
| `OnAbilitySwapped(event: ModifierAbilityEvent): nil` | both |  |
| `OnAbilityToggled(event: ModifierAbilityEvent): nil` | both |  |
| `OnAssist(event: ModifierUnitEvent): nil` | both |  |
| `OnAttack(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackAllied(event: ModifierAttackEvent): nil` | both | Happens even if attack can't be issued. |
| `OnAttackCancelled(event: ModifierAttackEvent): nil` | both |  |
| `OnAttacked(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackFail(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackFinished(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackLanded(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackRecord(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackRecordDestroy(event: ModifierAttackEvent): nil` | both |  |
| `OnAttackStart(event: ModifierAttackEvent): nil` | both |  |
| `OnAttemptProjectileDodge(): nil` | both |  |
| `OnBreakInvisibility(): nil` | both |  |
| `OnBuildingKilled(event: ModifierInstanceEvent): nil` | both |  |
| `OnCleaveAttackLanded(): nil` | both |  |
| `OnDamageCalculated(event: ModifierAttackEvent): nil` | both |  |
| `OnDamageHPLoss(event: ModifierAttackEvent): nil` | both |  |
| `OnDamagePrevented(event: ModifierAttackEvent): nil` | both |  |
| `OnDayStarted(): nil` | both |  |
| `OnDeath(event: ModifierInstanceEvent): nil` | both |  |
| `OnDeathCompleted(event: ModifierInstanceEvent): nil` | both |  |
| `OnDominated(event: ModifierUnitEvent): nil` | both |  |
| `OnForceProcMagicStick(): nil` | both |  |
| `OnFoWTeamChanged(): nil` | both |  |
| `OnHealReceived(event: ModifierHealEvent): nil` | both |  |
| `OnHealthGained(event: ModifierHealEvent): nil` | both |  |
| `OnHeroBeginDying(event: ModifierAttackEvent): nil` | both |  |
| `OnHeroKilled(event: ModifierAttackEvent): nil` | both |  |
| `OnIllusionCreated(event: ModifierUnitEvent): nil` | both |  |
| `OnKill(event: ModifierUnitEvent): nil` | both |  |
| `OnMagicDamageCalculated(event: ModifierAttackEvent): nil` | both |  |
| `OnManaGained(event: ModifierUnitEvent): nil` | both |  |
| `OnModelChanged(event: ModifierUnitEvent): nil` | both |  |
| `OnModifierAdded(event: ModifierAddedEvent): nil` | both |  |
| `OnModifierRefreshed(event: ModifierAddedEvent): nil` | both |  |
| `OnModifierRemoved(event: ModifierAddedEvent): nil` | both |  |
| `OnMuteDamageAbilities(): nil` | both |  |
| `OnNightStarted(): nil` | both |  |
| `OnOrder(event: ModifierUnitEvent): nil` | both |  |
| `OnOrderReceived(): nil` | both |  |
| `OnProcessCleave(): nil` | both |  |
| `OnProjectileDodge(event: ModifierAttackEvent): nil` | both |  |
| `OnProjectileObstructionHit(): nil` | both |  |
| `OnPureDamageCalculated(): nil` | both |  |
| `OnPurged(event: ModifierUnitEvent): nil` | both |  |
| `OnRedirectHealthGain(): nil` | both |  |
| `OnRespawn(event: ModifierUnitEvent): nil` | both |  |
| `OnRuneSpawn(event: ModifierUnitEvent): nil` | both |  |
| `OnScepterUpgradeSelected(): nil` | both |  |
| `OnSetLocation(event: ModifierUnitEvent): nil` | both |  |
| `OnShardUpgradeSelected(): nil` | both |  |
| `OnSpellAppliedSuccessfully(event: ModifierAbilityEvent): nil` | both |  |
| `OnSpellTargetReady(): nil` | both |  |
| `OnSpentHealth(event: ModifierAbilityEvent): nil` | both |  |
| `OnSpentItemCharge(): nil` | both |  |
| `OnSpentMana(event: ModifierAbilityEvent): nil` | both |  |
| `OnStateChanged(event: ModifierUnitEvent): nil` | both |  |
| `OnTakeDamage(event: ModifierInstanceEvent): nil` | both |  |
| `OnTakeDamageKillCredit(event: ModifierAttackEvent): nil` | both |  |
| `OnTakeDamagePostUnavoidableBlock(): nil` | both |  |
| `OnTeleported(event: ModifierUnitEvent): nil` | both |  |
| `OnTeleporting(event: ModifierUnitEvent): nil` | both |  |
| `OnTierTokenRerolled(): nil` | both |  |
| `OnTooltip(): float` | both |  |
| `OnTooltip2(): float` | both |  |
| `OnTreeCutDown(event: ModifierUnitEvent): nil` | both |  |
| `OnUnitMoved(event: ModifierUnitEvent): nil` | both |  |
| `PreserveParticlesOnModelChanged(): {'kind': 'literal', 'value': 0}, {'kind': 'literal', 'value': 1}` | both |  |
| `ReincarnateSuppressFX(): nil` | both |  |
| `ReincarnateTime(): float` | both |  |

### CDOTA_Modifier_Lua_Horizontal_Motion

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ApplyHorizontalMotionController(): bool` | server | Starts the horizontal motion controller effects for this buff.  Returns true if successful. |
| `GetPriority(): modifierpriority` | server | Get the priority. |
| `OnHorizontalMotionInterrupted(): nil` | server | Called when the motion gets interrupted. |
| `SetPriority(motionPriority: modifierpriority): nil` | server | Set the priority. |
| `UpdateHorizontalMotion(me: CDOTA_BaseNPC, dt: float): nil` | server | Perform any motion from the given interval on the NPC. |

### CDOTA_Modifier_Lua_Motion_Both

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ApplyHorizontalMotionController(): bool` | server | Starts the horizontal motion controller effects for this buff.  Returns true if successful. |
| `ApplyVerticalMotionController(): bool` | server | Starts the vertical motion controller effects for this buff.  Returns true if successful. |
| `GetPriority(): modifierpriority` | server | Get the priority. |
| `OnHorizontalMotionInterrupted(): nil` | server | Called when the motion gets interrupted. |
| `OnVerticalMotionInterrupted(): nil` | server | Called when the motion gets interrupted. |
| `SetPriority(motionPriority: modifierpriority): nil` | server | Set the priority. |
| `UpdateHorizontalMotion(me: CDOTA_BaseNPC, dt: float): nil` | server | Perform any motion from the given interval on the NPC. |
| `UpdateVerticalMotion(me: CDOTA_BaseNPC, dt: float): nil` | server | Perform any motion from the given interval on the NPC. |

### CDOTA_Modifier_Lua_Vertical_Motion

Extends `CDOTA_Modifier_Lua`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ApplyVerticalMotionController(): bool` | server | Starts the vertical motion controller effects for this buff.  Returns true if successful. |
| `GetMotionPriority(): modifierpriority` | server | Get the priority. |
| `OnVerticalMotionInterrupted(): nil` | server | Called when the motion gets interrupted. |
| `SetMotionPriority(motionPriority: modifierpriority): nil` | server | Set the priority. |
| `UpdateVerticalMotion(me: CDOTA_BaseNPC, dt: float): nil` | server | Perform any motion from the given interval on the NPC. |

### CDOTA_NeutralSpawner

Extends `CPointEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CreatePendingUnits(): nil` | server |  |
| `SelectSpawnType(): nil` | server |  |
| `SpawnNextBatch(ignoreBlockers: bool): nil` | server |  |

### CDOTA_PlayerResource

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddAegisPickup(playerId: PlayerID): nil` | server |  |
| `AddCandyEvent(playerId: PlayerID, reason: int): nil` | server |  |
| `AddClaimedFarm(playerId: PlayerID, farmValue: float, earnedValue: bool): nil` | server |  |
| `AddGoldSpentOnSupport(playerId: PlayerID, cost: int): nil` | server |  |
| `AddNeutralItemToStash(playerId: PlayerID, teamNumber: DOTATeam_t, item: CDOTA_Item): nil` | server |  |
| `AddRunePickup(playerId: PlayerID, runes: int): nil` | server |  |
| `AreUnitsSharedWithPlayerID(unitOwnerPlayerId: PlayerID, otherPlayerId: PlayerID): bool` | server |  |
| `CanRepick(playerId: PlayerID): bool` | server |  |
| `ClearKillsMatrix(playerId: PlayerID): nil` | server |  |
| `ClearLastHitMultikill(playerId: PlayerID): nil` | server |  |
| `ClearLastHitStreak(playerId: PlayerID): nil` | server |  |
| `ClearPlayer(playerId: PlayerID): nil` | server |  |
| `ClearRawPlayerDamageMatrix(playerId: PlayerID): nil` | server |  |
| `ClearStreak(playerId: PlayerID): nil` | server |  |
| `GetAegisPickups(playerId: PlayerID): int` | server |  |
| `GetAssists(playerId: PlayerID): int` | server |  |
| `GetBroadcasterChannel(playerId: PlayerID): uint` | server |  |
| `GetBroadcasterChannelSlot(playerId: PlayerID): uint` | server |  |
| `GetClaimedDenies(playerId: PlayerID): int` | server |  |
| `GetClaimedFarm(playerId: PlayerID, onlyEarned: bool): float` | server |  |
| `GetClaimedMisses(playerId: PlayerID): int` | server |  |
| `GetConnectionState(playerId: PlayerID): DOTAConnectionState_t` | server |  |
| `GetCreepDamageTaken(playerId: PlayerID, total: bool): float` | server |  |
| `GetCustomBuybackCooldown(playerId: PlayerID): float` | server |  |
| `GetCustomBuybackCost(playerId: PlayerID): int` | server |  |
| `GetCustomTeamAssignment(playerId: PlayerID): int` | server | Get the current custom team assignment for this player. |
| `GetDamageDoneToHero(playerId: PlayerID, victimId: PlayerID): float` | server |  |
| `GetDeaths(playerId: PlayerID): int` | server |  |
| `GetDenies(playerId: PlayerID): int` | server |  |
| `GetEventGameUpgrades(playerId: PlayerID): handle` | server | (nPlayerID). |
| `GetEventPointsForPlayerID(playerId: PlayerID): uint` | server |  |
| `GetEventPremiumPoints(playerId: PlayerID): uint` | server |  |
| `GetEventRanks(playerId: PlayerID): unknown` | server |  |
| `GetGold(playerId: PlayerID): int` | server |  |
| `GetGoldLostToDeath(playerId: PlayerID): int` | server |  |
| `GetGoldPerMin(playerId: PlayerID): float` | server |  |
| `GetGoldSpentOnBuybacks(playerId: PlayerID): int` | server |  |
| `GetGoldSpentOnConsumables(playerId: PlayerID): int` | server |  |
| `GetGoldSpentOnItems(playerId: PlayerID): int` | server |  |
| `GetGoldSpentOnSupport(playerId: PlayerID): int` | server |  |
| `GetHealing(playerId: PlayerID): float` | server |  |
| `GetHeroDamageTaken(playerId: PlayerID, total: bool): float` | server |  |
| `GetKills(playerId: PlayerID): int` | server |  |
| `GetKillsDoneToHero(playerId: PlayerID, victimId: PlayerID): int` | server |  |
| `GetLabyrinthEventGameHeroUnlocks(playerId: PlayerID): handle` | server | (nPlayerID). |
| `GetLastHitMultikill(playerId: PlayerID): int` | server |  |
| `GetLastHits(playerId: PlayerID): int` | server |  |
| `GetLastHitStreak(playerId: PlayerID): int` | server |  |
| `GetLevel(playerId: PlayerID): int` | server |  |
| `GetLiveSpectatorTeam(playerId: PlayerID): DOTATeam_t, {'kind': 'literal', 'value': -1}` | server |  |
| `GetMisses(playerId: PlayerID): int` | server |  |
| `GetNearbyCreepDeaths(playerId: PlayerID): int` | server |  |
| `GetNetworkedEventActionClaimCount(playerId: PlayerID, eventId: int, unActionId: uint): int` | server |  |
| `GetNetworkedEventActionClaimCountByName(playerId: PlayerID, eventId: int, actionName: string): int` | server |  |
| `GetNetWorth(playerId: PlayerID): int` | server |  |
| `GetNthCourierForTeam(courierIndex: int, teamNumber: DOTATeam_t): CDOTA_Unit_Courier, nil` | server |  |
| `GetNthPlayerIDOnTeam(teamNumber: DOTATeam_t, nthPlayer: int): PlayerID` | server |  |
| `GetNumConnectedHumanPlayers(): int` | server | Players on a valid team (radiant, dire, or custom*) who haven't abandoned the game. |
| `GetNumConsumablesPurchased(playerId: PlayerID): int` | server |  |
| `GetNumCouriersForTeam(teamNumber: DOTATeam_t): int` | server |  |
| `GetNumItemsPurchased(playerId: PlayerID): int` | server |  |
| `GetPartyID(playerId: PlayerID): Uint64` | server |  |
| `GetPlayer(playerId: PlayerID): CDOTAPlayerController, nil` | server | Returns player entity for a player with specified id. Player entity represents a single connection, so a different entity might be returned. When player is disconnected nil would be returned. |
| `GetPlayerCount(): int` | server | Includes spectators and players not assigned to a team. |
| `GetPlayerCountForTeam(team: DOTATeam_t): int` | server |  |
| `GetPlayerLoadedCompletely(playerId: PlayerID): bool` | server |  |
| `GetPlayerName(playerId: PlayerID): string` | server |  |
| `GetPreferredCourierForPlayer(playerId: PlayerID): handle` | server |  |
| `GetRawPlayerDamage(playerId: PlayerID): float` | server |  |
| `GetReliableGold(playerId: PlayerID): int` | server |  |
| `GetRespawnSeconds(playerId: PlayerID): int` | server |  |
| `GetRoshanKills(playerId: PlayerID): int` | server |  |
| `GetRunePickups(playerId: PlayerID): int` | server |  |
| `GetSelectedHeroEntity(playerId: PlayerID): CDOTA_BaseNPC_Hero, nil` | server |  |
| `GetSelectedHeroID(playerId: PlayerID): int` | server |  |
| `GetSelectedHeroName(playerId: PlayerID): string` | server |  |
| `GetSteamAccountID(playerId: PlayerID): uint` | server |  |
| `GetSteamID(playerId: PlayerID): Uint64` | server | Get the 64 bit steam ID for a given player. |
| `GetStreak(playerId: PlayerID): int` | server |  |
| `GetStuns(playerId: PlayerID): float` | server |  |
| `GetTeam(playerId: PlayerID): DOTATeam_t` | server |  |
| `GetTeamKills(team: DOTATeam_t): int` | server |  |
| `GetTeamPlayerCount(): int` | server | (Deprecated: use GetNumConnectedHumanPlayers) Players on a valid team (radiant, dire, or custom*) who haven't abandoned the game. |
| `GetTimeOfLastConsumablePurchase(playerId: PlayerID): float` | server |  |
| `GetTimeOfLastDeath(playerId: PlayerID): float` | server |  |
| `GetTimeOfLastItemPurchase(playerId: PlayerID): float` | server |  |
| `GetTotalEarnedGold(playerId: PlayerID): int` | server |  |
| `GetTotalEarnedXP(playerId: PlayerID): int` | server |  |
| `GetTotalGoldSpent(playerId: PlayerID): int` | server |  |
| `GetTowerDamageTaken(playerId: PlayerID, total: bool): float` | server |  |
| `GetTowerKills(playerId: PlayerID): int` | server |  |
| `GetUnitShareMaskForPlayer(playerId: PlayerID, otherPlayerId: PlayerID): int` | server |  |
| `GetUnreliableGold(playerId: PlayerID): int` | server |  |
| `GetXPPerMin(playerId: PlayerID): float` | server |  |
| `HasCustomGameTicketForPlayerID(playerId: PlayerID): bool` | server | Does this player have a custom game ticket for this game? |
| `HasRandomed(playerId: PlayerID): bool` | server |  |
| `HasSelectedHero(playerId: PlayerID): bool` | server |  |
| `HasSetNetworkedEventActionClaimCount(): bool` | server |  |
| `HaveAllPlayersJoined(): bool` | server |  |
| `IncrementAssists(playerId: PlayerID, victimId: PlayerID): nil` | server |  |
| `IncrementClaimedDenies(playerId: PlayerID, value: int): nil` | server |  |
| `IncrementClaimedMisses(playerId: PlayerID, value: int): nil` | server |  |
| `IncrementDeaths(playerId: PlayerID, killerId: PlayerID): nil` | server |  |
| `IncrementDenies(playerId: PlayerID, value: int): nil` | server |  |
| `IncrementKills(playerId: PlayerID, victimId: PlayerID): nil` | server |  |
| `IncrementLastHitMultikill(playerId: PlayerID, count: int): nil` | server |  |
| `IncrementLastHits(playerId: PlayerID, count: int): nil` | server |  |
| `IncrementLastHitStreak(playerId: PlayerID, count: int): nil` | server |  |
| `IncrementMisses(playerId: PlayerID, value: int): nil` | server |  |
| `IncrementNearbyCreepDeaths(playerId: PlayerID, creeps: int): nil` | server |  |
| `IncrementStreak(playerId: PlayerID, count: int): nil` | server |  |
| `IncrementTotalEarnedXP(playerId: PlayerID, xp: int, reason: EDOTA_ModifyXP_Reason): nil` | server |  |
| `IsBroadcaster(playerId: PlayerID): bool` | server |  |
| `IsDisableHelpSetForPlayerID(playerId: PlayerID, otherPlayerId: PlayerID): bool` | server |  |
| `IsFakeClient(playerId: PlayerID): bool` | server |  |
| `IsHeroSelected(heroname: string, ignoreUnrevealedPick: bool): bool` | server |  |
| `IsHeroSharedWithPlayerID(unitOwnerPlayerId: PlayerID, otherPlayerId: PlayerID): bool` | server |  |
| `IsValidPlayer(playerId: int): bool` | server |  |
| `IsValidPlayerID(playerId: int): bool` | server |  |
| `IsValidTeamPlayer(playerId: int): bool` | server |  |
| `IsValidTeamPlayerID(playerId: int): bool` | server |  |
| `ModifyGold(playerId: PlayerID, goldChange: int, reliable: bool, reason: EDOTA_ModifyGold_Reason): int` | server |  |
| `NumPlayers(): int` | server |  |
| `NumTeamPlayers(): int` | server |  |
| `RecordConsumableAbilityChargeChange(playerId: PlayerID, itemDefinitionIndex: int, chargeIncrementOrDecrement: int): nil` | server | Increment or decrement consumable charges (nPlayerID, item_definition_index, nChargeIncrementOrDecrement). |
| `RecordEventActionGrant(playerId: PlayerID, event: int, unActionId: int, unAudit: int, unQuantity: uint, unAuditData: uint): nil` | server |  |
| `RecordEventActionGrantForPrimaryEvent(playerId: PlayerID, actionName: string, unAudit: int, unQuantity: uint, unAuditData: uint): nil` | server |  |
| `ReplaceHeroWith(playerId: PlayerID, heroClass: string, gold: int, xp: int): CDOTA_BaseNPC_Hero` | server | Replaces the player's hero with a new one of the specified class, gold and XP. |
| `ReplaceHeroWithNoTransfer(playerId: PlayerID, heroClass: string, gold: int, xp: int): handle` | server | Replaces the player's hero with a new one of the specified class, gold and XP, without transferring items/abilities if same hero. |
| `ResetBuybackCostTime(playerId: PlayerID): nil` | server |  |
| `ResetTotalEarnedGold(playerId: PlayerID): nil` | server |  |
| `SetBuybackCooldownTime(playerId: PlayerID, buybackCooldown: float): nil` | server |  |
| `SetBuybackGoldLimitTime(playerId: PlayerID, buybackCooldown: float): nil` | server |  |
| `SetCameraTarget(playerId: PlayerID, target: CBaseEntity \| nil): nil` | server | Force the given player's camera to follow the given entity. |
| `SetCanRepick(playerId: PlayerID, canRepick: bool): nil` | server |  |
| `SetCustomBuybackCooldown(playerId: PlayerID, cooldownTime: float): nil` | server | Set the buyback cooldown for this player. |
| `SetCustomBuybackCost(playerId: PlayerID, goldCost: int): nil` | server | Set the buyback cost for this player. |
| `SetCustomIntParam(playerId: PlayerID, param: int): nil` | server |  |
| `SetCustomPlayerColor(playerId: PlayerID, r: int, g: int, b: int): nil` | server | Set custom color for player. |
| `SetCustomTeamAssignment(playerId: PlayerID, teamAssignment: DOTATeam_t): nil` | server | Set custom team assignment for this player. |
| `SetGold(playerId: PlayerID, gold: int, reliable: bool): nil` | server |  |
| `SetHasRandomed(playerId: PlayerID): nil` | server |  |
| `SetLastBuybackTime(playerId: PlayerID, lastBuybackTime: float): nil` | server |  |
| `SetOverrideSelectionEntity(playerId: PlayerID, entity: CDOTA_BaseNPC): nil` | server | Set the forced selection entity for a player. |
| `SetUnitShareMaskForPlayer(playerId: PlayerID, otherPlayerId: PlayerID, flag: int, state: bool): nil` | server |  |
| `SpendGold(playerId: PlayerID, cost: int, reason: EDOTA_ModifyGold_Reason): nil` | server |  |
| `UpdateTeamSlot(playerId: PlayerID, teamNumber: DOTATeam_t, desiredSlot: int): nil` | server |  |
| `WhoSelectedHero(heroFilename: string, ignoreUnrevealedPick: bool): PlayerID` | server |  |

### CDOTA_ShopTrigger

Extends `CBaseTrigger`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetShopType(): DOTA_SHOP_TYPE` | server | Get the DOTA_SHOP_TYPE. |
| `SetShopType(shopType: DOTA_SHOP_TYPE): nil` | server | Set the DOTA_SHOP_TYPE. |

### CDOTA_SimpleObstruction

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `IsEnabled(): bool` | server | Returns whether the obstruction is currently active. |
| `SetEnabled(enabled: bool, force: bool): nil` | server | Enable or disable the obstruction. |

### CDOTA_Unit_Courier

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `RespawnCourier(): nil` | server | Respawn the courier. |
| `UpgradeCourier(level: int): nil` | server | Upgrade the courier ( int param ) times. |

### CDOTA_Unit_CustomGameAnnouncer

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetServerAuthoritative(isServerAuthoritative: bool): nil` | server | Determines whether response criteria is matched on server or client. |

### CDOTA_Unit_CustomGameAnnouncerAghanim

Extends `CDOTA_BaseNPC`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetAnimation(animation: string): nil` | server | Set the animation sequence for this entity. |
| `SetServerAuthoritative(isServerAuthoritative: bool): nil` | server | Determines whether response criteria is matched on server or client. |

### CDOTA_Unit_Nian

Extends `CDOTA_BaseNPC_Creature`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetHorn(): handle` | server | Is the Nian horn? |
| `GetTail(): handle` | server | Is the Nian's tail broken? |
| `IsHornAlive(): bool` | server | Is the Nian's horn broken? |
| `IsTailAlive(): bool` | server | Is the Nian's tail broken? |

### CDOTA_Unit_Scout

Extends `CDOTA_BaseNPC`

_No members._

### CDOTABaseAbility

Client name: `C_DOTABaseAbility` · Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CanAbilityBeUpgraded(): bool` | server |  |
| `CastAbility(): bool` | server |  |
| `ContinueCasting(): bool` | server |  |
| `CreateVisibilityNode(location: Vector, radius: float, duration: float): nil` | server |  |
| `DecrementModifierRefCount(): nil` | server |  |
| `EnableAbilityChargesOnTalentUpgrade(ability: handle, talentName: string): nil` | server |  |
| `EndChannel(interrupted: bool): nil` | server |  |
| `EndCooldown(): nil` | server | Clear the cooldown remaining on this ability. |
| `ForceSetFrozenCooldown(value: int): nil` | server |  |
| `GetAbilityChargeRestoreTime(level: int): float` | server |  |
| `GetAbilityDamage(): int` | server |  |
| `GetAbilityDamageType(): DAMAGE_TYPES` | server |  |
| `GetAbilityIndex(): int` | server |  |
| `GetAbilityKeyValues(): table` | server | Gets the key values definition for this ability. |
| `GetAbilityName(): string` | both | Returns the name of this ability. |
| `GetAbilityTargetFlags(): DOTA_UNIT_TARGET_FLAGS` | server |  |
| `GetAbilityTargetTeam(): DOTA_UNIT_TARGET_TEAM` | server |  |
| `GetAbilityTargetType(): DOTA_UNIT_TARGET_TYPE` | server |  |
| `GetAbilityType(): int` | server |  |
| `GetAltCastState(): bool` | server | Gets the current Alt Cast State. |
| `GetAnimationIgnoresModelScale(): bool` | server |  |
| `GetAOERadius(): float` | server |  |
| `GetAssociatedPrimaryAbilities(): string` | server |  |
| `GetAssociatedSecondaryAbilities(): string` | server |  |
| `GetAutoCastState(): bool` | server |  |
| `GetBackswingTime(): float` | server |  |
| `GetBehavior(): DOTA_ABILITY_BEHAVIOR` | both |  |
| `GetBehaviorInt(): DOTA_ABILITY_BEHAVIOR` | both | Get ability behavior flags as an int for compatability. |
| `GetCaster(): CDOTA_BaseNPC` | both | Get the owner of this ability. |
| `GetCastPoint(): float` | server |  |
| `GetCastPointModifier(): float` | both |  |
| `GetCastRange(location: Vector \| nil, target: CDOTA_BaseNPC \| nil): int` | server | Gets the cast range of the ability. |
| `GetChannelledHealthCostPerSecond(level: int): int` | server |  |
| `GetChannelledManaCostPerSecond(level: int): int` | server |  |
| `GetChannelStartTime(): float` | server |  |
| `GetChannelTime(): float` | server |  |
| `GetCloneSource(): CDOTA_BaseNPC, nil` | server |  |
| `GetConceptRecipientType(): int` | server |  |
| `GetCooldown(level: int): float` | server | Get the cooldown duration for this ability at a given level, not the amount of cooldown actually left. |
| `GetCooldownTime(): float` | server |  |
| `GetCooldownTimeRemaining(): float` | server |  |
| `GetCurrentAbilityCharges(): int` | both | The number of charges remaining on this ability. |
| `GetCursorPosition(): Vector` | server |  |
| `GetCursorTarget(): CDOTA_BaseNPC, nil` | server |  |
| `GetCursorTargetingNothing(): bool` | server |  |
| `GetDuration(): float` | server |  |
| `GetEffectiveCastRange(location: Vector, target: handle): int` | server | Gets the cast range of the ability, taking modifiers into account. |
| `GetEffectiveCooldown(level: int): float` | server |  |
| `GetEffectiveHealthCost(level: int): int` | server |  |
| `GetEffectiveManaCost(level: int): int` | server |  |
| `GetGoldCost(level: int): int` | server |  |
| `GetGoldCostForUpgrade(level: int): int` | server |  |
| `GetHealthCost(level: int): int` | server |  |
| `GetHeroLevelRequiredToUpgrade(): int` | server |  |
| `GetInitialAbilityCharges(level: int): int` | server |  |
| `GetIntrinsicModifierName(): string` | server |  |
| `GetLevel(): int` | both | Get the current level of the ability. |
| `GetLevelSpecialValueFor(name: string, level: int): float` | both | Gets a value from this ability's special value block for passed level. |
| `GetLevelSpecialValueNoOverride(name: string, level: int): float` | both | Gets a value from this ability's special value block for passed level, ignoring MODIFIER_PROPERTY_OVERRIDE_ABILITY_SPECIAL. |
| `GetManaCost(level: int): int` | server |  |
| `GetMaxAbilityCharges(level: int): int` | server |  |
| `GetMaxLevel(): int` | server |  |
| `GetModifierValue(): float` | server |  |
| `GetModifierValueBonus(): float` | server |  |
| `GetPlaybackRateOverride(): float` | server |  |
| `GetSharedCooldownName(): string` | server |  |
| `GetSpecialValueFor(name: string): float` | both | Gets a value from this ability's special value block for its current level. |
| `GetStolenActivityModifier(): string` | server |  |
| `GetToggleState(): bool` | both | Whether or not this ability is toggled. |
| `GetUpgradeRecommended(): bool` | server |  |
| `HeroXPChange(xp: float): bool` | server |  |
| `IncrementModifierRefCount(): nil` | server |  |
| `IsActivated(): bool` | server |  |
| `IsAttributeBonus(): bool` | server |  |
| `IsChanneling(): bool` | server | Returns whether the ability is currently channeling. |
| `IsCooldownReady(): bool` | server |  |
| `IsCosmetic(entity: CBaseEntity): bool` | server |  |
| `IsFullyCastable(): bool` | server | Returns whether the ability can be cast. |
| `IsHidden(): bool` | server |  |
| `IsHiddenAsSecondaryAbility(): bool` | server |  |
| `IsHiddenWhenStolen(): bool` | server |  |
| `IsInAbilityPhase(): bool` | server | Returns whether the ability is currently casting. |
| `IsItem(): bool` | both | Whether or not this ability is an item. |
| `IsOwnersGoldEnough(issuerPlayerId: PlayerID): bool` | server |  |
| `IsOwnersGoldEnoughForUpgrade(): bool` | server |  |
| `IsOwnersManaEnough(): bool` | server |  |
| `IsPassive(): bool` | server |  |
| `IsRefreshable(): bool` | server |  |
| `IsSharedWithTeammates(): bool` | server |  |
| `IsStealable(): bool` | server |  |
| `IsStolen(): bool` | server |  |
| `IsToggle(): bool` | server |  |
| `IsTrained(): bool` | server |  |
| `MarkAbilityButtonDirty(): nil` | server | Mark the ability button for this ability as needing a refresh. |
| `NumModifiersUsingAbility(): int` | server |  |
| `OnAbilityPhaseInterrupted(): nil` | server |  |
| `OnAbilityPhaseStart(): bool` | server |  |
| `OnAbilityPinged(playerId: PlayerID, ctrlHeld: bool): nil` | server |  |
| `OnChannelFinish(interrupted: bool): nil` | server |  |
| `OnChannelThink(interval: float): nil` | server |  |
| `OnHeroCalculateStatBonus(): nil` | server |  |
| `OnHeroLevelUp(): nil` | server |  |
| `OnOwnerDied(): nil` | server |  |
| `OnOwnerSpawned(): nil` | server |  |
| `OnSpellStart(): nil` | server |  |
| `OnToggle(): nil` | server |  |
| `OnUpgrade(): nil` | server |  |
| `PayGoldCost(): nil` | server |  |
| `PayGoldCostForUpgrade(): nil` | server |  |
| `PayHealthCost(): nil` | server |  |
| `PayManaCost(): nil` | server |  |
| `PlaysDefaultAnimWhenStolen(): bool` | server |  |
| `ProcsMagicStick(): bool` | server |  |
| `RefCountsModifiers(): bool` | server |  |
| `RefreshCharges(): nil` | server |  |
| `RefreshIntrinsicModifier(): nil` | server |  |
| `RefundHealthCost(): nil` | server |  |
| `RefundManaCost(): nil` | server |  |
| `RequiresFacing(): bool` | server |  |
| `ResetToggleOnRespawn(): bool` | server |  |
| `SetAbilityIndex(index: int): nil` | server |  |
| `SetActivated(activated: bool): nil` | server |  |
| `SetAltCastState(altCastEnabled: bool): nil` | server | Set Alt Cast State to a specific value (true for on, false for off). |
| `SetChanneling(channeling: bool): nil` | server |  |
| `SetCurrentAbilityCharges(charges: int): nil` | server |  |
| `SetFrozenCooldown(frozenCooldown: bool): nil` | server |  |
| `SetHidden(hidden: bool): nil` | server |  |
| `SetInAbilityPhase(inAbilityPhase: bool): nil` | server |  |
| `SetLevel(level: int): nil` | server | Sets the level of this ability. |
| `SetOverrideCastPoint(castPoint: float): nil` | server |  |
| `SetRefCountsModifiers(refCounts: bool): nil` | server |  |
| `SetStealable(stealable: bool): nil` | server |  |
| `SetStolen(stolen: bool): nil` | server |  |
| `SetUpgradeRecommended(upgradeRecommended: bool): nil` | server |  |
| `ShouldAltCast(): bool` | server | This is what the Alt Cast State of the ability was when it was initially cast. Updated during Execute Orders. |
| `ShouldUseResources(): bool` | server |  |
| `SpeakAbilityConcept(concept: int): nil` | server |  |
| `SpeakTrigger(): unknown` | server |  |
| `StartCooldown(cooldown: float): nil` | server |  |
| `ToggleAbility(): nil` | server |  |
| `ToggleAltCast(): nil` | server | Toggle the Alt Cast State of an Ability. |
| `ToggleAutoCast(): nil` | server |  |
| `UpgradeAbility(supressSpeech: bool): nil` | server |  |
| `UseResources(mana: bool, useHealth: bool, gold: bool, cooldown: bool): nil` | server |  |

### CDOTABaseGameMode

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddAbilityUpgradeToWhitelist(abilityName: string): nil` | server | Const char* pszAbilityName. |
| `AddItemToCustomShop(itemName: string, shopName: string, category: string): nil` | server | Add an item to purchase at a custom shop. |
| `AddRealTimeCombatAnalyzerQuery(queryTable: handle, player: CDOTAPlayerController, queryName: string): CombatAnalyzerQueryID` | server | Begin tracking a sequence of events using the real time combat analyzer. |
| `AllocateFowBlockerRegion(minX: float, minY: float, maxX: float, maxY: float, gridSize: float): CFoWBlockerRegion` | server | Allocates an entity which can be used by custom games to control FoW occlusion volumes. |
| `AreWeatherEffectsDisabled(): bool` | server | Get if weather effects are disabled on the client. |
| `ClearBountyRunePickupFilter(): nil` | server | Clear the script filter that controls bounty rune pickup behavior. |
| `ClearDamageFilter(): nil` | server | Clear the script filter that controls how a unit takes damage. |
| `ClearExecuteOrderFilter(): nil` | server | Clear the script filter that controls when a unit picks up an item. |
| `ClearHealingFilter(): nil` | server | Clear the script filter that controls how a unit heals. |
| `ClearItemAddedToInventoryFilter(): nil` | server | Clear the script filter that controls the item added to inventory filter. |
| `ClearModifierGainedFilter(): nil` | server | Clear the script filter that controls the modifier filter. |
| `ClearModifyExperienceFilter(): nil` | server | Clear the script filter that controls how hero experience is modified. |
| `ClearModifyGoldFilter(): nil` | server | Clear the script filter that controls how hero gold is modified. |
| `ClearRuneSpawnFilter(): nil` | server | Clear the script filter that controls what rune spawns. |
| `ClearTrackingProjectileFilter(): nil` | server | Clear the script filter that controls when tracking projectiles are launched. |
| `DisableClumpingBehaviorByDefault(disabled: bool): nil` | server | Disable npc_dota_creature clumping behavior by default. |
| `DisableHudFlip(disable: bool): nil` | server | Use to disable hud flip for this mod. |
| `EnableAbilityUpgradeWhitelist(enabled: bool): nil` | server | Bool bEnabled. |
| `GetAlwaysShowPlayerInventory(): bool` | server | Show the player hero's inventory in the HUD, regardless of what unit is selected. |
| `GetAlwaysShowPlayerNames(): bool` | server | Get whether player names are always shown, regardless of client setting. |
| `GetAnnouncerDisabled(): bool` | server | Are in-game announcers disabled? |
| `GetAnnouncerGameModeAnnounceDisabled(): bool` | server | Is the announcer announcing the mode / saying Choose Your Hero on start of custom games disabled? |
| `GetCameraDistanceOverride(): float` | server | Set a different camera distance; dota default is 1134. |
| `GetCustomAttributeDerivedStatValue(derivedStatType: AttributeDerivedStats): float` | server | Get current derived stat value constant. |
| `GetCustomBackpackCooldownPercent(): float` | server | Get the current rate cooldown ticks down for items in the backpack. |
| `GetCustomBackpackSwapCooldown(): float` | server | Get the current custom backpack swap cooldown. |
| `GetCustomBuybackCooldownEnabled(): bool` | server | Turns on capability to define custom buyback cooldowns. |
| `GetCustomBuybackCostEnabled(): bool` | server | Turns on capability to define custom buyback costs. |
| `GetCustomDireScore(): int` | server | Get the topbar score display value for dire. |
| `GetCustomGlyphCooldown(): float` | server | Get the current custom glyph cooldown. |
| `GetCustomHeroMaxLevel(): int` | server | Allows definition of the max level heroes can achieve (default is 25). |
| `GetCustomRadiantScore(): int` | server | Get the topbar score display value for radiant. |
| `GetCustomScanCooldown(): float` | server | Get the current custom scan cooldown. |
| `GetDaynightCycleAdvanceRate(): float` | server | Get the rate at which the day/night cycle advances (1.0 = default). |
| `GetEventGameSeed(): int` | server | Get the Game Seed passed from the GC. |
| `GetEventWindowStartTime(): uint` | server | Get the Event Window Start Time passed from the GC. |
| `GetFixedRespawnTime(): float` | server | Gets the fixed respawn time. |
| `GetFogOfWarDisabled(): bool` | server | Turn the fog of war on or off. |
| `GetGoldSoundDisabled(): bool` | server | Turn the sound when gold is acquired off/on. |
| `GetHUDVisible(element: int): bool` | server | Returns the HUD element visibility. |
| `GetMaximumAttackSpeed(): int` | server | Get the maximum attack speed for units. |
| `GetMinimumAttackSpeed(): int` | server | Get the minimum attack speed for units. |
| `GetRecommendedItemsDisabled(): bool` | server | Turn the panel for showing recommended items at the shop off/on. |
| `GetRespawnTimeScale(): float` | server | Returns the scale applied to non-fixed respawn times. |
| `GetStashPurchasingDisabled(): bool` | server | Turn purchasing items to the stash off/on. If purchasing to the stash is off the player must be at a shop to purchase items. |
| `GetStickyItemDisabled(): bool` | server | Hide the sticky item in the quickbuy. |
| `GetTopBarTeamValuesOverride(): bool` | server | Override the values of the team values on the top game bar. |
| `GetTopBarTeamValuesVisible(): bool` | server | Turning on/off the team values on the top game bar. |
| `GetTowerBackdoorProtectionEnabled(): bool` | server | Gets whether tower backdoor protection is enabled or not. |
| `GetUseCustomHeroLevels(): bool` | server | Are custom-defined XP values for hero level ups in use? |
| `GetWaterRuneLastSpawnTime(): float` | server | Gets the time from game start during which water runes spawn. |
| `IsAbilityUpgradeWhitelisted(abilityName: string): bool` | server | Const char* pszAbilityName. |
| `IsBuybackEnabled(): bool` | server | Enables or disables buyback completely. |
| `IsDaynightCycleDisabled(): bool` | server | Is the day/night cycle disabled? |
| `ListenForQueryFailed(function: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'result', 'types': ['CombatAnalyzerQueryResult']}]}, context: table): nil` | server | Set function and context for real time combat analyzer query failed. |
| `ListenForQueryProgressChanged(function: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'result', 'types': ['CombatAnalyzerQueryResult']}]}, context: table): nil` | server | Set function and context for real time combat analyzer query progress changed. |
| `ListenForQuerySucceeded(function: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'result', 'types': ['CombatAnalyzerQueryResult']}]}, context: table): nil` | server | Set function and context for real time combat analyzer query succeeded. |
| `RemoveAbilityUpgradeFromWhitelist(abilityName: string): nil` | server | Const char* pszAbilityName. |
| `RemoveItemFromCustomShop(itemName: string, shopName: string): nil` | server | Remove an item to purchase at a custom shop. |
| `RemoveRealTimeCombatAnalyzerQuery(queryId: CombatAnalyzerQueryID): nil` | server | Stop tracking a combat analyzer query. |
| `SetAbilityTuningValueFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['AbilityTuningValueFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the tuning values that abilities use. (Modify the table and Return true to use new values, return false to use the old values). |
| `SetAllowNeutralItemDrops(enabled: bool): nil` | server | If set to true, neutral items will be dropped on killing neutral monsters.  Otherwise nothing will be dropped. |
| `SetAlwaysShowPlayerInventory(alwaysShow: bool): nil` | server | Show the player hero's inventory in the HUD, regardless of what unit is selected. |
| `SetAlwaysShowPlayerNames(enabled: bool): nil` | server | Set whether player names are always shown, regardless of client setting. |
| `SetAnnouncerDisabled(disabled: bool): nil` | server | Mutes the in-game announcer. |
| `SetAnnouncerGameModeAnnounceDisabled(disabled: bool): nil` | server | Disables the announcer announcing the mode / saying Choose Your Hero on start of custom games. |
| `SetBotsAlwaysPushWithHuman(alwaysPush: bool): nil` | server | Set if the bots should try their best to push with a human player. |
| `SetBotsInLateGame(lateGame: bool): nil` | server | Set if bots should enable their late game behavior. |
| `SetBotsMaxPushTier(maxTier: int): nil` | server | Set the max tier of tower that bots want to push. (-1 to disable). |
| `SetBotThinkingEnabled(enabled: bool): nil` | server | Enables/Disables bots in custom games. Note: this will only work with default heroes in the dota map. |
| `SetBountyRunePickupFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['BountyRunePickupFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a bounty rune is picked up. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetBountyRuneSpawnInterval(interval: float): nil` | server | Set bounty rune spawn rate. |
| `SetBuybackEnabled(enabled: bool): nil` | server | Enables or disables buyback completely. |
| `SetCameraDistanceOverride(cameraDistanceOverride: float): nil` | server | Set a different camera distance; dota default is 1134. |
| `SetCameraSmoothCountOverride(smoothCount: int): nil` | server | Set a different camera smooth count; dota default is 8. |
| `SetCameraZRange(minZ: float, maxZ: float): nil` | server | Sets the camera Z range. |
| `SetCanSellAnywhere(allow: bool): nil` | server | Bool bAllow. |
| `SetCustomAttributeDerivedStatValue(statType: AttributeDerivedStats, newValue: float): nil` | server | Modify derived stat value constants. |
| `SetCustomBackpackCooldownPercent(percent: float): nil` | server | Set the rate cooldown ticks down for items in the backpack. |
| `SetCustomBackpackSwapCooldown(cooldown: float): nil` | server | Set a custom cooldown for swapping items into the backpack. |
| `SetCustomBuybackCooldownEnabled(enabled: bool): nil` | server | Turns on capability to define custom buyback cooldowns. |
| `SetCustomBuybackCostEnabled(enabled: bool): nil` | server | Turns on capability to define custom buyback costs. |
| `SetCustomDireScore(score: int): nil` | server | Sets the topbar score display value for dire. |
| `SetCustomGameForceHero(heroName: string): nil` | server | Force all players to use the specified hero and disable the normal hero selection process. Must be used before hero selection. |
| `SetCustomGlyphCooldown(cooldown: float): nil` | server | Set a custom cooldown for team Glyph ability. |
| `SetCustomHeroMaxLevel(maxLevel: int): nil` | server | Allows definition of the max level heroes can achieve (default is 25). |
| `SetCustomRadiantScore(score: int): nil` | server | Sets the topbar score display value for radiant. |
| `SetCustomScanCooldown(cooldown: float): nil` | server | Set a custom cooldown for team Scan ability. |
| `SetCustomScanMaxCharges(maxCharges: int): nil` | server | Set a custom max charges for team Scan ability. |
| `SetCustomTerrainWeatherEffect(effectName: string): nil` | server | Set the effect used as a custom weather effect, when units are on non-default terrain, in this mode. |
| `SetCustomXPRequiredToReachNextLevel(table: {'kind': 'table', 'key': ['int'], 'value': ['int']}): nil` | server | Allows definition of a table of hero XP values.<br>Requires `SetUseCustomHeroLevels` to be enabled. |
| `SetDamageFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['DamageFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a unit takes damage. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetDaynightCycleAdvanceRate(rate: float): nil` | server | Sets the rate at which the day/night cycle advances (1.0 = default). |
| `SetDaynightCycleDisabled(disable: bool): nil` | server | Enable or disable the day/night cycle. |
| `SetDeathOverlayDisabled(disabled: bool): nil` | server | Specify whether the full screen death overlay effect plays when the selected hero dies. |
| `SetDeathTipsDisabled(disabled: bool): nil` | server | Disables chat tips on death. |
| `SetDefaultStickyItem(item: string): nil` | server | Sets the default sticky item in the quickbuy. |
| `SetDraftingBanningTimeOverride(value: float): nil` | server | Set drafting hero banning time. |
| `SetDraftingHeroPickSelectTimeOverride(value: float): nil` | server | Set drafting hero pick time. |
| `SetExecuteOrderFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['ExecuteOrderFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a unit picks up an item. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetFixedRespawnTime(fixedRespawnTime: float): nil` | server | Set a fixed delay for all players to respawn after. |
| `SetFogOfWarDisabled(disabled: bool): nil` | server | Turn the fog of war on or off. |
| `SetForcedHeroCapOnReset(cap: int): nil` | server | Caps the number of players spawned when the game is reset. Used in tutorials where players are spawned in the script. |
| `SetForcedHUDSkin(value: string): nil` | server | Specify a HUD skin that is forced on for this game mode. |
| `SetForceRightClickAttackDisabled(disabled: bool): nil` | server | Prevent users from using the right click deny setting. |
| `SetFountainConstantManaRegen(constantManaRegen: float): nil` | server | Set the constant rate that the fountain will regen mana. (-1 for default). |
| `SetFountainPercentageHealthRegen(percentageHealthRegen: float): nil` | server | Set the percentage rate that the fountain will regen health. (-1 for default). |
| `SetFountainPercentageManaRegen(percentageManaRegen: float): nil` | server | Set the percentage rate that the fountain will regen mana. (-1 for default). |
| `SetFreeCourierModeEnabled(enabled: bool): nil` | server | If set to true, enable 7.23 free courier mode. |
| `SetFriendlyBuildingMoveToEnabled(enabled: bool): nil` | server | Allows clicks on friendly buildings to be handled normally. |
| `SetGiveFreeTPOnDeath(give: bool): nil` | server | Bool bGive. |
| `SetGoldSoundDisabled(disabled: bool): nil` | server | Turn the sound when gold is acquired off/on. |
| `SetHealingFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['HealingFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a unit heals. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetHudCombatEventsDisabled(disabled: bool): nil` | server | Specify whether the default combat events will show in the HUD. |
| `SetHUDVisible(hudElement: DOTAHUDVisibility_t, visible: bool): nil` | server | Set the HUD element visibility. |
| `SetInnateMeleeDamageBlockAmount(amount: int): nil` | server | Set the amount blocked innately by melee heroes. |
| `SetInnateMeleeDamageBlockPercent(percent: int): nil` | server | Set the percent chance a melee hero will innately block damage. |
| `SetInnateMeleeDamageBlockPerLevelAmount(perLevelAmount: int): nil` | server | Set the amount innately blocked by melee heroes gained per level. |
| `SetItemAddedToInventoryFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['ItemAddedToInventoryFilterEvent']}]}, context: table): nil` | server | Set a filter function to control what happens to items that are added to an inventory, return false to cancel the event. |
| `SetKillableTombstones(enabled: bool): nil` | server | Set whether tombstones can be channeled to be removed by enemy heroes. |
| `SetKillingSpreeAnnouncerDisabled(disabled: bool): nil` | server | Mutes the in-game killing spree announcer. |
| `SetLoseGoldOnDeath(enabled: bool): nil` | server | Use to disable gold loss on death. |
| `SetLuaGameMode(script: handle): nil` | server |  |
| `SetMaximumAttackSpeed(maxSpeed: int): nil` | server | Set the maximum attack speed for units. |
| `SetMinimumAttackSpeed(minSpeed: int): nil` | server | Set the minimum attack speed for units. |
| `SetModifierGainedFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['ModifierGainedFilterEvent']}]}, context: table): nil` | server | Set a filter function to control modifiers that are gained, return false to destroy modifier. |
| `SetModifyExperienceFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['ModifyExperienceFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a hero's experience is modified. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetModifyGoldFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['ModifyGoldFilterEvent']}]}, context: table): nil` | server | Set a filter function to control the behavior when a hero's gold is modified. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetNeutralItemHideUndiscoveredEnabled(enable: bool): nil` | server | When enabled, undiscovered items in the neutral item stash are hidden. |
| `SetNeutralStashEnabled(enable: bool): nil` | server | Allow items to be sent to the neutral stash. |
| `SetNeutralStashTeamViewOnlyEnabled(enable: bool): nil` | server | When enabled, the all neutral items tab cannot be viewed. |
| `SetOverrideSelectionEntity(overrideEntity: CDOTA_BaseNPC \| nil): nil` | server | Set an override for the default selection entity, instead of each player's hero. |
| `SetPauseEnabled(enabled: bool): nil` | server | Set pausing enabled/disabled. |
| `SetPlayerHeroAvailabilityFiltered(filter: bool): nil` | server | Bool bFilter. |
| `SetPowerRuneSpawnInterval(interval: float): nil` | server | Set power rune spawn rate. |
| `SetRandomHeroBonusItemGrantDisabled(disabled: bool): nil` | server | Disables bonus items for randoming a hero. |
| `SetRecommendedItemsDisabled(disabled: bool): nil` | server | Turn the panel for showing recommended items at the shop off/on. |
| `SetRemoveIllusionsOnDeath(remove: bool): nil` | server | Make it so illusions are immediately removed upon death, rather than sticking around for a few seconds. |
| `SetRespawnTimeScale(value: float): nil` | server | Sets the scale applied to non-fixed respawn times. 1 = default DOTA respawn calculations. |
| `SetRuneEnabled(rune: DOTA_RUNES, enabled: bool): nil` | server | Set if a given type of rune is enabled. |
| `SetRuneSpawnFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['RuneSpawnFilterEvent']}]}, context: table): nil` | server | Set a filter function to control what rune spawns. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetSelectionGoldPenaltyEnabled(enabled: bool): nil` | server | Enable/disable gold penalty for late picking. |
| `SetSendToStashEnabled(enable: bool): nil` | server | Allow items to be sent to the stash. |
| `SetStashPurchasingDisabled(disabled: bool): nil` | server | Turn purchasing items to the stash off/on. If purchasing to the stash is off the player must be at a shop to purchase items. |
| `SetStickyItemDisabled(disabled: bool): nil` | server | Hide the sticky item in the quickbuy. |
| `SetTopBarTeamValue(team: DOTATeam_t, value: int): nil` | server | Set the team values on the top game bar. |
| `SetTopBarTeamValuesOverride(override: bool): nil` | server | Override the values of the team values on the top game bar. |
| `SetTopBarTeamValuesVisible(visible: bool): nil` | server | Turning on/off the team values on the top game bar. |
| `SetTowerBackdoorProtectionEnabled(enabled: bool): nil` | server | Enables/Disables tower backdoor protection. |
| `SetTPScrollSlotItemOverride(itemName: string): nil` | server | Sets the item which goes in the TP scroll slot. |
| `SetTrackingProjectileFilter(filterFunc: {'kind': 'function', 'returns': ['bool'], 'args': [{'name': 'event', 'types': ['TrackingProjectileFilterEvent']}]}, context: table): nil` | server | Set a filter function to control when tracking projectiles are launched. (Modify the table and Return true to use new values, return false to cancel the event). |
| `SetUnseenFogOfWarEnabled(enabled: bool): nil` | server | Enable or disable unseen fog of war. When enabled parts of the map the player has never seen will be completely hidden by fog of war. |
| `SetUseCustomHeroLevels(enabled: bool): nil` | server | Turn on custom-defined XP values for hero level ups.  The table should be defined before switching this on. |
| `SetUseDefaultDOTARuneSpawnLogic(enabled: bool): nil` | server | If set to true, use current rune spawn rules.  Either setting respects custom spawn intervals. |
| `SetUseTurboCouriers(enabled: bool): nil` | server | Enables or disables turbo couriers. |
| `SetWaterRuneLastSpawnTime(value: float): nil` | server | Sets the time from game start during which water runes spawn. |
| `SetWeatherEffectsDisabled(disable: bool): nil` | server | Set if weather effects are disabled. |
| `SetXPRuneSpawnInterval(interval: float): nil` | server | Set xp rune spawn rate. |
| `ShouldGiveFreeTPOnDeath(): bool` | server |  |

### CDOTAGameManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetHeroDataByName_Script(heroName: string): table` | both | Get the hero unit. |
| `GetHeroIDByName(heroName: string): int` | both | Get the hero ID given the hero name. |
| `GetHeroLocTokenByID(arg1: int): string` | both | Get the localization token for the given hero ID. |
| `GetHeroNameByID(heroId: int): string` | both | Get the hero name given a hero ID. |
| `GetHeroNameForUnitName(unitName: string): string` | both | Get the hero name given a unit name. |
| `GetHeroUnitNameByID(heroId: int): string` | both | Get the hero unit name given the hero ID. |

### CDOTAGameRules

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddBotPlayerWithEntityScript(heroName: string, playerName: string, team: DOTATeam_t, entityScript: string, arg5: bool): CDOTA_BaseNPC_Hero, nil` | server | Spawn a bot player of the passed hero name, player name, and team. |
| `AddEventMetadataLeaderboardEntry(nameSuffix: string, stars: uint, maxStars: uint, extraData1: uint, extraData2: uint, extraData3: uint, extraData4: uint, extraData5: uint, extraData6: uint): bool` | server | Event-only. |
| `AddEventMetadataLeaderboardEntryRawScore(nameSuffix: string, score: uint, extraData1: uint, extraData2: uint, extraData3: uint, extraData4: uint, extraData5: uint, extraData6: uint): bool` | server | Event-only. |
| `AddHeroIDToBlacklist(arg1: int): nil` | server | Add the hero ID to the hero blacklist if it is not already present. |
| `AddHeroIDToWhitelist(arg1: int): nil` | server | Add the hero ID to the hero whitelist if it is not already present. |
| `AddHeroToBlacklist(arg1: string): nil` | server | Add the hero to the hero blacklist if it is not already present. |
| `AddHeroToPlayerAvailability(arg1: int, arg2: int): nil` | server | Adds hero of given ID to available heroes of player of given ID. |
| `AddHeroToWhitelist(arg1: string): nil` | server | Add the hero to the hero whitelist if it is not already present. |
| `AddItemToWhiteList(itemName: string): nil` | server | Add an item to the whitelist. |
| `AddMinimapDebugPoint(arg1: int, arg2: Vector, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float): nil` | server | Add a point on the minimap. |
| `AddMinimapDebugPointForTeam(arg1: int, arg2: Vector, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float, arg8: int): nil` | server | Add a point on the minimap for a specific team. |
| `BeginNightstalkerNight(duration: float): nil` | server | Begin night stalker night. |
| `BeginTemporaryNight(duration: float, arg2: int): nil` | server | Begin temporary night. |
| `BotPopulate(): nil` | server | Fills all the teams with bots if cheat mode is enabled. |
| `ClearHeroBlacklist(): nil` | server | Clears the hero blacklist. |
| `ClearHeroWhitelist(): nil` | server | Clears the hero whitelist. |
| `ClearPlayerHeroAvailability(arg1: int): nil` | server | Clears available heroes of player of given ID. |
| `ClearRiverPaint(): nil` | server | Clears the current river paint. |
| `Defeated(): nil` | server | Kills the ancient, etc. |
| `DidMatchSignoutTimeOut(): bool` | server | True when we have waited some time after end of the game and not received signout. |
| `EnableCustomGameSetupAutoLaunch(enabled: bool): nil` | server | Enabled (true) or disable (false) auto launch for custom game setup. |
| `ExecuteTeamPing(team: DOTATeam_t, xCoord: float, yCoord: float, entity: CBaseEntity \| nil, type: {'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1} \| {'kind': 'literal', 'value': 2} \| {'kind': 'literal', 'value': 3} \| {'kind': 'literal', 'value': 4} \| {'kind': 'literal', 'value': 5} \| {'kind': 'literal', 'value': 6}): nil` | server | Sends a minimap ping to all players on the team. |
| `FinishCustomGameSetup(): nil` | server | Indicate that the custom game setup phase is complete, and advance to the game. |
| `ForceCreepSpawn(): nil` | server | Spawn the next wave of creeps. |
| `ForceGameStart(): nil` | server | Transition game state to DOTA_GAMERULES_STATE_GAME_IN_PROGRESS. |
| `GetAnnouncer(team: DOTATeam_t): CDOTA_BaseNPC, nil` | server | Get the announcer for a team. |
| `GetBannedHeroes(): {'kind': 'array', 'types': ['string']}` | both | Returns the hero unit names banned in this game, if any. |
| `GetBannedHeroIDs(): table` | both | Returns the hero unit IDs banned in this game, if any. |
| `GetCustomGameDifficulty(): int` | both | Returns the difficulty level of the custom game mode. |
| `GetCustomGameTeamMaxPlayers(team: DOTATeam_t): int` | server | Get whether a team is selectable during game setup. |
| `GetDifficulty(): int` | both | Returns difficulty level of the custom game mode. |
| `GetDOTATime(includePreGame: bool, includeNegativeTime: bool): float` | both | Returns the actual DOTA in-game clock time. |
| `GetDroppedItem(index: int): CDOTA_Item_Physical, nil` | server | Gets the Xth dropped item. |
| `GetGameFrameTime(): float` | both | Returns the number of seconds elapsed since the last frame was renderered. This time doesn't count up when the game is paused. |
| `GetGameModeEntity(): CDOTABaseGameMode` | server | Get the game mode entity. |
| `GetGameSessionConfigValue(arg1: string, arg2: string): string` | server | Get a string value from the game session config (map options). |
| `GetGameTime(): float` | both | Returns the number of seconds elapsed since map start. This time doesn't count up when the game is paused. |
| `GetIetmStockDuration(arg1: int, arg2: string, arg3: int): float` | both | Get the time it takes to add a new item to stock. |
| `GetItemStockCount(team: DOTATeam_t, itemName: string, playerId: PlayerID): int` | both | Get the stock count of the item. |
| `GetItemStockTime(team: DOTATeam_t, itemName: string, playerId: PlayerID): float` | both | Get the time an item will be added to stock. |
| `GetMatchSignoutComplete(): bool` | server | Have we received the post match signout message that includes reward information. |
| `GetNeutralInitialSpawnOffset(): float` | both | Gets the extra offset to initial neutral creep spawn delay. |
| `GetNextBountyRuneSpawnTime(): float` | server | Gets next bounty rune spawn time. |
| `GetNextRuneSpawnTime(): float` | server | Gets next rune spawn time. |
| `GetNianTotalDamageTaken(): int` | server | For New Bloom, get total damage taken by the Nian / Year Beast. |
| `GetPlayerCustomGameAccountRecord(playerId: PlayerID): table` | server | **Deprecated:** Unreleased.<br><br>Gets the player's custom game account record, as it looked at the start of this session. |
| `GetStateTransitionTime(): float` | server | Get time remaining between state changes. |
| `GetTimeOfDay(): float` | server | Get the time of day. |
| `GetWeatherWindDirection(): Vector` | both | Get Weather Wind Direction Vector. |
| `IncreaseItemStock(team: DOTATeam_t, itemName: string, count: int, playerId: PlayerID): nil` | server | Increase an item's stock count, clamped to item max. |
| `IsCheatMode(): bool` | both | Are cheats enabled on the server. |
| `IsDaytime(): bool` | server | Is it day time? |
| `IsDev(): bool` | both |  |
| `IsGamePaused(): bool` | server | Returns whether the game is paused. |
| `IsHeroEnabledViaLists(arg1: string): bool` | both | Is the hero not blacklisted, and is it either whitelisted or the whitelist is empty? |
| `IsHeroRespawnEnabled(): bool` | server | Returns whether hero respawn is enabled. |
| `IsInBanPhase(): bool` | server | Are we in the ban phase of hero pick? |
| `IsItemInWhiteList(itemName: string): bool` | server | Query an item in the whitelist. |
| `IsNightstalkerNight(): bool` | server | Is it night stalker night-time? |
| `IsSuggestAbilitiesEnabled(): bool` | server | Returns whether Dota Plus ability suggestions are enabled or disabled. |
| `IsSuggestItemsEnabled(): bool` | server | Returns whether Dota Plus item suggestions are enabled or disabled. |
| `IsTemporaryNight(): bool` | server | Is it temporarily night-time? |
| `LockCustomGameSetupTeamAssignment(locked: bool): nil` | server | Lock (true) or unlock (false) team assignemnt. If team assignment is locked players cannot change teams. |
| `MakeTeamLose(team: DOTATeam_t): nil` | server | Makes the specified team lose. |
| `ModifyGoldFiltered(playerId: PlayerID, goldChange: int, reliable: bool, reason: EDOTA_ModifyGold_Reason): int` | server | Like ModifyGold, but will use the gold filter if SetFilterMoreGold has been set true. |
| `NumDroppedItems(): int` | server | Returns the number of items currently dropped on the ground. |
| `PlayerHasCustomGameHostPrivileges(player: CDOTAPlayerController): bool` | server | Whether a player has custom game host privileges (shuffle teams, etc.). |
| `Playtesting_UpdateAddOnKeyValues(): nil` | server | Updates custom hero, unit and ability KeyValues in memory with the latest values from disk. |
| `PrepareSpawners(arg1: float): nil` | server | Prepare Dota lane style spawners with a given interval. |
| `RemoveFakeClient(playerId: PlayerID): nil` | server | Removes a fake client. |
| `RemoveHeroFromBlacklist(arg1: string): nil` | server | Remove the hero from the hero blacklist if present. |
| `RemoveHeroFromWhitelist(arg1: string): nil` | server | Remove the hero from the hero whitelist if present. |
| `RemoveHeroIDFromBlacklist(arg1: int): nil` | server | Remove the hero ID from the hero blacklist if present. |
| `RemoveHeroIDFromWhitelist(arg1: int): nil` | server | Remove the hero ID from the hero whitelist if present. |
| `RemoveItemFromWhiteList(itemName: string): nil` | server | Remove an item from the whitelist. |
| `ResetDefeated(): nil` | server | Restart after killing the ancient, etc. |
| `ResetGameTime(): nil` | server | Restart gametime from 0. |
| `ResetPlayer(arg1: int): nil` | server | Resets the player of a given ID. |
| `ResetToCustomGameSetup(): nil` | server | Restart at custom game setup. |
| `ResetToHeroSelection(): nil` | server | Restart the game at hero selection. |
| `Script_GetMatchID(): Uint64` | server | Get the MatchID for this game. |
| `SendCustomMessage(arg1: string, arg2: int, arg3: int): nil` | server | Sends a message on behalf of a player. |
| `SendCustomMessageToTeam(arg1: string, arg2: int, arg3: int, arg4: int): nil` | server | Sends a message on behalf of a player to the specified team. |
| `SetAllowOutpostBonuses(arg1: bool): nil` | server | Allow Outposts granting XP. |
| `SetCreepMinimapIconScale(scale: float): nil` | server | Scale the creep icons on the minimap. |
| `SetCreepSpawningEnabled(arg1: bool): nil` | server | Sets whether the regular Dota creeps spawn. |
| `SetCustomGameAccountRecordSaveFunction(arg1: handle, arg2: handle): nil` | server | **Deprecated:** Unreleased.<br><br>Sets a callback to handle saving custom game account records (callback is passed a Player ID and should return a flat simple table). |
| `SetCustomGameAllowBattleMusic(allow: bool): nil` | server | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowHeroPickMusic(allow: bool): nil` | server | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowMusicAtGameStart(allow: bool): nil` | server | Sets a flag to enable/disable the default music handling code for custom games. |
| `SetCustomGameAllowSecondaryAbilitiesOnOtherUnits(arg1: bool): nil` | server | Sets a flag to enable/disable the casting secondary abilities from units other than the player's own hero. |
| `SetCustomGameBansPerTeam(arg1: int): nil` | server | Set number of hero bans each team gets. |
| `SetCustomGameDifficulty(difficulty: int): nil` | server | Set the difficulty level of the custom game mode. |
| `SetCustomGameEndDelay(delay: float): nil` | server | Sets the game end delay. |
| `SetCustomGameSetupAutoLaunchDelay(delay: float): nil` | server | Set the amount of time to wait for auto launch. |
| `SetCustomGameSetupRemainingTime(remainingTime: float): nil` | server | Set the amount of remaining time, in seconds, for custom game setup. 0 = finish immediately, -1 = wait forever. |
| `SetCustomGameSetupTimeout(timeout: float): nil` | server | Setup (pre-gameplay) phase timeout. 0 = instant, -1 = forever (until FinishCustomGameSetup is called). |
| `SetCustomGameTeamMaxPlayers(team: DOTATeam_t, maxPlayers: int): nil` | server | Set whether a team is selectable during game setup. |
| `SetCustomVictoryMessage(message: string): nil` | server | Sets the victory message. |
| `SetCustomVictoryMessageDuration(duration: float): nil` | server | Sets the victory message duration. |
| `SetEnableAlternateHeroGrids(arg1: bool): nil` | server | Allow alternate hero grids to be used (DOTA+, etc).  True by default. |
| `SetEventMetadataCustomTable(metadataTable: handle): bool` | server | Event-only. |
| `SetEventSignoutCustomTable(metadataTable: handle): bool` | server | Event-only. |
| `SetFilterMoreGold(arg1: bool): nil` | server | Sets whether to filter more gold events than normal. |
| `SetFirstBloodActive(active: bool): nil` | server | Sets whether First Blood has been triggered. |
| `SetGameWinner(team: DOTATeam_t): nil` | server | Makes the specified team win. |
| `SetGlyphCooldown(team: DOTATeam_t, cooldown: float): nil` | server | Set Glyph cooldown for team. |
| `SetGoldPerTick(amount: int): nil` | server | Set the auto gold increase per timed interval. |
| `SetGoldTickTime(time: float): nil` | server | Set the time interval between auto gold increases. |
| `SetHeroMinimapIconScale(scale: float): nil` | server | Scale the hero minimap icons on the minimap. |
| `SetHeroRespawnEnabled(enabled: bool): nil` | server | Control if the normal DOTA hero respawn rules apply. |
| `SetHeroSelectionTime(selectionTime: float): nil` | server | Sets the amount of time players have to pick their hero. |
| `SetHeroSelectPenaltyTime(arg1: float): nil` | server | Sets amount of penalty time before randoming a hero. |
| `SetHideBlacklistedHeroes(arg1: bool): nil` | server | Should blacklisted heroes be hidden, or just dimmed, in hero picking? |
| `SetHideKillMessageHeaders(hideHeaders: bool): nil` | server | Sets whether the multikill, streak, and first-blood banners appear at the top of the screen. |
| `SetIgnoreLobbyTeamsInCustomGame(arg1: bool): nil` | server | Set whether custom and event games should ignore Lobby teams when assigning players to teams. Defaults to true. |
| `SetItemStockCount(count: int, team: DOTATeam_t, itemName: string, playerId: PlayerID): nil` | server | Set the stock count of the item. |
| `SetNeutralInitialSpawnOffset(arg1: float): nil` | server | Sets the extra offset to initial neutral creep spawn delay. |
| `SetNextBountyRuneSpawnTime(arg1: float): nil` | server | Sets next bounty rune spawn time. |
| `SetNextRuneSpawnTime(arg1: float): nil` | server | Sets next rune spawn time. |
| `SetOverlayHealthBarUnit(unit: CDOTA_BaseNPC, style: int): nil` | server | Show this unit's health on the overlay health bar. |
| `SetPostGameColumns(arg1: handle): bool` | server | Set columns to show in post game. |
| `SetPostGameLayout(arg1: int): nil` | server | Configure post game to be single or double column layout. |
| `SetPostGameTeamScores(arg1: handle): bool` | server | Set score value for each team. First element is for DOTA_TEAM_GOODGUYS. |
| `SetPostGameTime(time: float): nil` | server | Sets the amount of time players have between the game ending and the server disconnecting them. |
| `SetPreGameTime(time: float): nil` | server | Sets the amount of time players have between picking their hero and game start. |
| `SetRiverPaint(arg1: int, arg2: float): nil` | server | Paints the river for a duration. |
| `SetRuneMinimapIconScale(minimapRuneIconScale: float): nil` | server | Scale the rune icons on the minimap. |
| `SetRuneSpawnTime(time: float): nil` | server | Sets the amount of time between rune spawns. |
| `SetSafeToLeave(safeToLeave: bool): nil` | server | Mark this game as safe to leave. |
| `SetSameHeroSelectionEnabled(enabled: bool): nil` | server | When true, players can repeatedly pick the same hero. |
| `SetShowcaseTime(time: float): nil` | server | Sets the amount of time players have between the strategy phase and entering the pre-game phase. |
| `SetSpeechUseSpawnInsteadOfRespawnConcept(arg1: bool): nil` | server | Set whether to speak a Spawn concept instead of a Respawn concept on respawn. |
| `SetStartingGold(amount: int): nil` | server | Set the starting gold amount. |
| `SetStrategyTime(time: float): nil` | server | Sets the amount of time players have between the hero selection and entering the showcase phase. |
| `SetSuggestAbilitiesEnabled(arg1: bool): nil` | server | Sets Dota Plus ability suggestions enabled or disabled. |
| `SetSuggestItemsEnabled(arg1: bool): nil` | server | Sets Dota Plus ability item enabled or disabled. |
| `SetTimeOfDay(time: float): nil` | server | Set the time of day. |
| `SetTreeRegrowTime(time: float): nil` | server | Sets the tree regrow time in seconds. |
| `SetUseBaseGoldBountyOnHeroes(useBaseGoldBounties: bool): nil` | server | Heroes will use the basic NPC functionality for determining their bounty, rather than DOTA specific formulas. |
| `SetUseCustomHeroXPValues(useCustomXPValues: bool): nil` | server | Allows heroes in the map to give a specific amount of XP (this value must be set). |
| `SetUseUniversalShopMode(useUniversalShopMode: bool): nil` | server | When true, all items are available at as long as any shop is in range. |
| `SetWeatherWindDirection(arg1: Vector): nil` | server | Set Weather Wind Direction Vector. |
| `SetWhiteListEnabled(whiteListEnabled: bool): nil` | server | Item whitelist functionality enable/disable. |
| `ShouldHideBlacklistedHeroes(): bool` | both | Are blacklisted heroes hidden, or just dimmed, in hero picking? |
| `SpawnAndReleaseCreeps(): nil` | server | Spawn and release the next creep wave from Dota lane style spawners. |
| `SpawnNeutralCreeps(): nil` | server | Spawn and release the next set of neutral camps. |
| `State_Get(): DOTA_GameState` | both | Get the current Gamerules state. |

### CDOTAPlayerController

Client name: `C_DOTAPlayerController` · Extends `CBaseAnimatingActivity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CheckForCourierSpawning(hero: CDOTA_BaseNPC_Hero): handle` | server | Attempt to spawn the appropriate couriers for this mode. |
| `GetActiveAbility(): handle` | client |  |
| `GetAssignedHero(): CDOTA_BaseNPC_Hero` | server | Get the player's hero. |
| `GetClickBehaviors(): unknown` | client |  |
| `GetPlayerID(): PlayerID` | server | Get the player's official PlayerID; notably is -1 when the player isn't yet on a team. |
| `GetQueryUnit(): handle` | client |  |
| `MakeRandomHeroSelection(): nil` | server | Randoms this player's hero. |
| `SetAssignedHeroEntity(hero: handle): nil` | server | Sets this player's hero . |
| `SetKillCamUnit(entity: CDOTA_BaseNPC): nil` | server | Set the kill cam unit for this hero. |
| `SetMusicStatus(musicStatus: int, intensity: float): nil` | server | Set the music status for this player, note this will only really apply if dota_music_battle_enable is off. |
| `SetSelectedHero(heroName: string): nil` | server | Sets this player's hero selection. |
| `ShouldDisplayInWorldUIElements(): bool` | client |  |
| `SpawnCourierAtPosition(location: Vector): CDOTA_Unit_Courier` | server | Spawn a courier for this player at the given position. |

### CDotaQuest

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddSubquest(subquest: handle): nil` | server | Add a subquest to this quest. |
| `CompleteQuest(): nil` | server | Mark this quest complete. |
| `GetSubquest(index: int): handle` | server | Finds a subquest from this quest by index. |
| `GetSubquestByName(name: string): handle` | server | Finds a subquest from this quest by name. |
| `RemoveSubquest(subquest: handle): nil` | server | Remove a subquest from this quest. |
| `SetTextReplaceString(string: string): nil` | server | Set the text replace string for this quest. |
| `SetTextReplaceValue(valueSlot: int, value: int): nil` | server | Set a quest value. |

### CDotaSubquestBase

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CompleteSubquest(): nil` | server | Mark this subquest complete. |
| `SetTextReplaceString(string: string): nil` | server | Set the text replace string for this subquest. |
| `SetTextReplaceValue(valueSlot: int, value: int): nil` | server | Set a subquest value. |

### CDOTATutorial

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddBot(heroName: string, arg2: string, arg3: string, arg4: bool): bool` | server | Add a computer controlled bot. |
| `AddQuest(arg1: string, arg2: int, arg3: string, arg4: string): nil` | server | Add a quest to the quest log. |
| `AddShopWhitelistItem(itemName: string): nil` | server | Add an item to the shop whitelist. |
| `CompleteQuest(arg1: string): nil` | server | Complete a quest,. |
| `CreateLocationTask(arg1: Vector): nil` | server | Add a task to move to a specific location. |
| `EnableCreepAggroViz(arg1: bool): nil` | server | Alert the player when a creep becomes agro to their hero. |
| `EnablePlayerOffscreenTip(arg1: bool): nil` | server | Enable the tip to alert players how to find their hero. |
| `EnableTowerAggroViz(arg1: bool): nil` | server | Alert the player when a tower becomes agro to their hero. |
| `FinishTutorial(): nil` | server | End the tutorial. |
| `ForceGameStart(): nil` | server | Force the start of the game. |
| `IsItemInWhiteList(itemName: string): bool` | server | Is this item currently in the white list. |
| `MoveCameraToLocation(arg1: Vector): nil` | server | Moves the camera to a position. |
| `RemoveShopWhitelistItem(itemName: string): nil` | server | Remove an item from the shop whitelist. |
| `SelectHero(heroName: string): nil` | server | Select a hero for the local player. |
| `SelectPlayerTeam(arg1: string): nil` | server | Select the team for the local player. |
| `SetItemGuide(arg1: string): nil` | server | Set the current item guide. |
| `SetOrModifyPlayerGold(goldAmount: int, setNotModify: bool): nil` | server | Set gold amount for the tutorial player. |
| `SetQuickBuy(itemName: string): nil` | server | Set players quick buy item. |
| `SetShopOpen(open: bool): nil` | server | Set the shop open or closed. |
| `SetTutorialConvar(arg1: string, arg2: string): nil` | server | Set a tutorial convar. |
| `SetTutorialUI(arg1: int): nil` | server | Set the UI to use a reduced version to focus attention to specific elements. |
| `SetWhiteListEnabled(whiteListEnabled: bool): nil` | server | Set if we should whitelist shop items. |
| `StartTutorialMode(): nil` | server | Initialize Tutorial Mode. |
| `UpgradePlayerAbility(abilityName: string): nil` | server | Upgrade a specific ability for the local hero. |

### CDotaTutorialNPCBlocker

Extends `CBaseAnimatingOverlay`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetEnabled(enabled: bool): nil` | server |  |
| `SetOtherBlocker(blocker: handle): nil` | server |  |

### CDOTAVoteSystem

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `StartVote(arg1: handle): nil` | server | Starts a vote, based upon a table of parameters. |

### CEntities

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CreateByClassname(className: string): CBaseEntity` | server | Creates an entity by classname. |
| `FindAllByClassname(className: string): {'kind': 'array', 'types': ['CBaseEntity']}` | server | Finds all entities by class name. Returns an array containing all the found entities. |
| `FindAllByClassnameWithin(arg1: string, location: Vector, arg3: float): table` | server | Find entities by class name within a radius. |
| `FindAllByModel(modelName: string): {'kind': 'array', 'types': ['CBaseEntity']}` | server | Find entities by model name. |
| `FindAllByName(name: string): {'kind': 'array', 'types': ['CBaseEntity']}` | server | Find all entities by name. Returns an array containing all the found entities in it. |
| `FindAllByNameWithin(arg1: string, location: Vector, arg3: float): table` | server | Find entities by name within a radius. |
| `FindAllByTarget(target: string): {'kind': 'array', 'types': ['CBaseEntity']}` | server | Find entities by targetname. |
| `FindAllInSphere(location: Vector, arg2: float): table` | server | Find entities within a radius. |
| `FindByClassname(previous: CBaseEntity \| nil, className: string): CBaseEntity, nil` | server | Find entities by class name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByClassnameNearest(arg1: string, location: Vector, arg3: float): handle` | server | Find entities by class name nearest to a point. |
| `FindByClassnameWithin(arg1: handle, arg2: string, location: Vector, arg4: float): handle` | server | Find entities by class name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByModel(previous: CBaseEntity \| nil, modelName: string): CBaseEntity, nil` | server | Find entities by model name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByModelWithin(arg1: handle, arg2: string, location: Vector, arg4: float): handle` | server | Find entities by model name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByName(previous: CBaseEntity \| nil, name: string): CBaseEntity, nil` | server | Find entities by name. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByNameNearest(arg1: string, location: Vector, arg3: float): handle` | server | Find entities by name nearest to a point. |
| `FindByNameWithin(arg1: handle, arg2: string, location: Vector, arg4: float): handle` | server | Find entities by name within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindByTarget(previous: CBaseEntity \| nil, target: string): CBaseEntity, nil` | server | Find entities by targetname. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `FindInSphere(arg1: handle, location: Vector, arg3: float): handle` | server | Find entities within a radius. Pass 'null' to start an iteration, or reference to a previously found entity to continue a search. |
| `First(): CBaseEntity` | both | Begin an iteration over the list of entities. |
| `GetLocalPlayer(): CDOTAPlayerController` | both | Get the local player controller (backcompat). |
| `GetLocalPlayerController(): handle` | both | Get the local player controller. |
| `GetLocalPlayerPawn(): handle` | both | Get the local player pawn. |
| `Next(previous: CBaseEntity \| nil): CBaseEntity, nil` | both | Continue an iteration over the list of entities, providing reference to a previously found entity. |

### CEntityInstance

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ConnectOutput(arg1: string, arg2: string): nil` | both | Adds an I/O connection that will call the named function on this entity when the specified output fires. |
| `Destroy(): nil` | both |  |
| `DisconnectOutput(arg1: string, arg2: string): nil` | both | Removes a connected script function from an I/O event on this entity. |
| `DisconnectRedirectedOutput(arg1: string, arg2: string, arg3: handle): nil` | both | Removes a connected script function from an I/O event on the passed entity. |
| `entindex(): EntityIndex` | both |  |
| `FireOutput(arg1: string, arg2: handle, arg3: handle, arg4: table, arg5: float): nil` | both | Fire an entity output. |
| `GetClassname(): string` | both |  |
| `GetDebugName(): string` | both | Get the entity name w/help if not defined (i.e. classname/etc). |
| `GetEntityHandle(): ehandle` | both | Get the entity as an EHANDLE. |
| `GetEntityIndex(): EntityIndex` | both |  |
| `GetIntAttr(arg1: string): int` | both | Get Integer Attribute. |
| `GetName(): string` | both | Get the entity name. |
| `GetOrCreatePrivateScriptScope(): handle` | both | Retrieve, creating if necessary, the private per-instance script-side data associated with an entity. |
| `GetOrCreatePublicScriptScope(): handle` | both | Retrieve, creating if necessary, the public script-side data associated with an entity. |
| `GetPrivateScriptScope(): handle` | both | Retrieve the private per-instance script-side data associated with an entity. |
| `GetPublicScriptScope(): handle` | both | Retrieve the public script-side data associated with an entity. |
| `IsNull(): bool` | both | Has underlying C++ entity object been deleted? |
| `RedirectOutput(arg1: string, arg2: string, arg3: handle): nil` | both | Adds an I/O connection that will call the named function on the passed entity when the specified output fires. |
| `RemoveSelf(): nil` | both | Delete this entity. |
| `SetIntAttr(arg1: string, arg2: int): nil` | both | Set Integer Attribute. |

### CEntityScriptFramework

_No members._

### CEnvEntityMaker

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SpawnEntity(): nil` | server | Create an entity at the location of the maker. |
| `SpawnEntityAtEntityOrigin(entity: handle): nil` | server | Create an entity at the location of a specified entity instance. |
| `SpawnEntityAtLocation(vecAlternateOrigin: Vector, vecAlternateAngles: Vector): nil` | server | Create an entity at a specified location and orientaton, orientation is Euler angle in degrees. |
| `SpawnEntityAtNamedEntityOrigin(name: string): nil` | server | Create an entity at the location of a named entity. |

### CFoWBlockerRegion

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddRectangularBlocker(mins: Vector, maxs: Vector, clearRegion: bool): nil` | server | Sets or clears a blocker rectangle. |
| `AddRectangularOutlineBlocker(mins: Vector, maxs: Vector, clearRegion: bool): nil` | server | Sets or clears a blocker rectangle outline. |

### CInfoData

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `QueryColor(tok: string, default: Vector): Vector` | server | Query color data for this key. |
| `QueryFloat(tok: string, default: float): float` | server | Query float data for this key. |
| `QueryInt(tok: string, default: int): int` | server | Query int data for this key. |
| `QueryNumber(tok: string, default: float): float` | server | Query number data for this key. |
| `QueryString(tok: string, default: string): string` | server | Query string data for this key. |
| `QueryVector(tok: string, default: Vector): Vector` | server | Query vector data for this key. |

### CInfoPlayerStartDota

Extends `CPointEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `IsEnabled(): bool` | server | Returns whether the object is currently active. |
| `SetEnabled(enabled: bool): nil` | server | Enable or disable the obstruction. |

### CInfoWorldLayer

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `HideWorldLayer(): nil` | both | Hides this layer. |
| `ShowWorldLayer(): nil` | both | Shows this layer. |

### CLogicRelay

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `Trigger(activator: CBaseEntity \| nil, caller: CBaseEntity \| nil): nil` | both | Triggers the logic_relay. |

### CLogicScript

Extends `CBaseEntity`

_No members._

### CMarkupVolumeTagged

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `HasTag(tagName: unknown): bool` | server | Does this volume have the given tag. |

### CNativeOutputs

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddOutput(arg1: string, arg2: string): nil` | both | Add an output. |
| `Init(arg1: int): nil` | both | Initialize with number of outputs. |

### Convars

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetBool(name: string): bool, nil` | both | Returns the convar as a boolean flag. |
| `GetCommandClient(): CDOTAPlayerController` | both | Returns the player who issued this console command. |
| `GetDOTACommandClient(): CDOTAPlayerController` | both | Returns the DOTA player who issued this console command. |
| `GetFloat(name: string): float, nil` | both | Returns the convar as a float. May return null if no such convar. |
| `GetInt(name: string): int, nil` | both | Returns the convar as an int. May return null if no such convar. |
| `GetStr(name: string): string, nil` | both | Returns the convar as a string. May return null if no such convar. |
| `RegisterCommand(name: string, callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'name', 'types': ['string']}, {'name': '...args', 'types': [{'kind': 'array', 'types': ['string']}]}]}, helpString: string, flags: ConVarFlags): nil` | both | Register a console command. |
| `RegisterConvar(name: string, defaultValue: string, helpString: string, flags: ConVarFlags): nil` | both | Register a new console variable. |
| `SetBool(name: string, value: bool): nil` | both | Sets the value of the convar to the bool. |
| `SetFloat(name: string, value: float): nil` | both | Sets the value of the convar to the float. |
| `SetInt(name: string, value: int): nil` | both | Sets the value of the convar to the int. |
| `SetStr(name: string, value: string): nil` | both | Sets the value of the convar to the string. |

### CParticleSystem

Extends `CBaseModelEntity`

_No members._

### CPhysicsProp

Extends `CBaseAnimatingActivity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `DisableMotion(): nil` | server | Disable motion for the prop. |
| `EnableMotion(): nil` | server | Enable motion for the prop. |

### CPointClientUIWorldPanel

Extends `CBaseModelEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AcceptUserInput(): nil` | server | Tells the panel to accept user input. |
| `AddCSSClasses(classes: string): nil` | server | Adds CSS class(es) to the panel. |
| `IgnoreUserInput(): nil` | server | Tells the panel to ignore user input. |
| `IsGrabbable(): bool` | server | Returns whether this entity is grabbable. |
| `RemoveCSSClasses(classes: string): nil` | server | Remove CSS class(es) from the panel. |

### CPointEntity

Client name: `C_PointEntity` · Extends `CBaseEntity`

_No members._

### CPointTemplate

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `DeleteCreatedSpawnGroups(): nil` | both | Deletes any spawn groups that this point_template has spawned. Note: The point_template will not be deleted by this. |
| `ForceSpawn(): nil` | both | Spawns all of the entities the point_template is pointing at. |
| `GetSpawnedEntities(): handle` | both | Get the list of the most recent spawned entities. |
| `SetSpawnCallback(callbackFunc: handle, callbackScope: handle): nil` | both | Set a callback for when the template spawns entities. The spawned entities will be passed in as an array. |

### CPointWorldText

Client name: `C_PointWorldText` · Extends `CBaseModelEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `SetMessage(message: string): nil` | both | Set the message on this entity. |

### CSceneEntity

Extends `CBaseEntity`

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddBroadcastTeamTarget(arg1: int): nil` | server | Adds a team (by index) to the broadcast list. |
| `Cancel(): nil` | server | Cancel scene playback. |
| `EstimateLength(): float` | server | Returns length of this scene in seconds. |
| `FindNamedEntity(arg1: string): handle` | server | Given an entity reference, such as !target, get actual entity from scene object. |
| `IsPaused(): bool` | server | If this scene is currently paused. |
| `IsPlayingBack(): bool` | server | If this scene is currently playing. |
| `RemoveBroadcastTeamTarget(arg1: int): nil` | server | Removes a team (by index) from the broadcast list. |
| `Start(arg1: handle): nil` | server | Start scene playback, takes activatorEntity as param. |

### CScriptHeroList

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetAllHeroes(): {'kind': 'array', 'types': ['CDOTA_BaseNPC_Hero']}` | server | Returns all the heroes in the world. |
| `GetHero(nth: int): CDOTA_BaseNPC_Hero, nil` | server | Get the Nth hero in the Hero List. |
| `GetHeroCount(): int` | server | Returns the number of heroes in the world. |

### CScriptHTTPRequest

Note: Actual `CScriptHTTPRequest` global exists only after CreateHTTPRequest is called.

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `Send(callback: {'kind': 'function', 'returns': ['nil'], 'args': [{'name': 'response', 'types': ['CScriptHTTPResponse']}]}): bool` | both | Send a HTTP request. |
| `SetHTTPRequestAbsoluteTimeoutMS(milliseconds: uint): bool` | both | Set the total timeout on the request. |
| `SetHTTPRequestGetOrPostParameter(name: string, value: string): bool` | both | Set a POST or GET parameter on the request. |
| `SetHTTPRequestHeaderValue(name: string, value: string): bool` | both | Set a header value on the request. |
| `SetHTTPRequestNetworkActivityTimeout(seconds: uint): bool` | both | Set the network timeout on the request - this timer is reset when any data is received. |
| `SetHTTPRequestRawPostBody(contentType: string, body: string): bool` | both | Set the literal body of a post - invalid after setting a post parameter. |

### CScriptKeyValues

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `GetValue(arg1: string): table` | both | Reads a spawn key. |

### CScriptParticleManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CreateParticle(particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| nil): ParticleID` | both | Creates a new particle effect. |
| `CreateParticleForPlayer(particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| nil, player: CDOTAPlayerController): ParticleID` | both | Creates a new particle effect that only plays for the specified player. |
| `CreateParticleForTeam(particleName: string, particleAttach: ParticleAttachment_t, owner: CBaseEntity \| nil, team: DOTATeam_t): ParticleID` | both | Creates a new particle effect that only plays for the specified team. |
| `DestroyParticle(particle: ParticleID, immediate: bool): nil` | both | Destroy a particle, if bDestroyImmediately destroy it without playing end caps. |
| `GetParticleReplacement(particleName: string, hero: CDOTA_BaseNPC_Hero \| nil): string` | both |  |
| `ReleaseParticleIndex(particle: ParticleID): nil` | both | Frees the specified particle index. |
| `SetParticleAlwaysSimulate(particle: ParticleID): nil` | both |  |
| `SetParticleControl(particle: ParticleID, controlPoint: int, value: Vector): nil` | both | Set the control point data for a control on a particle effect. |
| `SetParticleControlEnt(particle: ParticleID, controlPoint: int, unit: CBaseEntity, particleAttach: ParticleAttachment_t, attachment: string, offset: Vector, lockOrientation: bool): nil` | both |  |
| `SetParticleControlFallback(particle: ParticleID, controlPoint: int, vecPosition: Vector): nil` | both |  |
| `SetParticleControlForward(particle: ParticleID, controlPoint: int, arg3: Vector): nil` | both | [OBSOLETE - Use SetParticleControlTransformForward] (int nFXIndex, int nPoint, vForward). |
| `SetParticleControlOrientation(particle: ParticleID, controlPoint: int, arg3: Vector, arg4: Vector, arg5: Vector): nil` | both | [OBSOLETE - Use SetParticleControlTransform] (int nFXIndex, int nPoint, vForward, vRight, vUp) - Set the orientation for a control on a particle effect (NOTE: This is left handed -- bad!!). |
| `SetParticleControlOrientationFLU(particle: ParticleID, controlPoint: int, arg3: Vector, arg4: Vector, arg5: Vector): nil` | both | [OBSOLETE - Use SetParticleControlTransform] (int nFXIndex, int nPoint, Vector vecForward, Vector vecLeft, Vector vecUp) - Set the orientation for a control on a particle effect. |
| `SetParticleControlTransform(fxIndex: int, point: int, origin: Vector, qAngles: QAngle): nil` | both |  |
| `SetParticleControlTransformForward(fxIndex: int, point: int, origin: Vector, forward: Vector): nil` | both |  |
| `SetParticleFoWProperties(particle: ParticleID, controlPoint: int, controlPoint2: int, radius: float): nil` | both |  |
| `SetParticleShouldCheckFoW(particle: ParticleID, checkFoW: bool): bool` | both |  |

### CScriptPrecacheContext

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddResource(resource: string): nil` | both | Precaches a specific resource. |
| `GetValue(key: string): table` | both | Reads a spawn key. |

### CScriptUniformRandomStream

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `RandomFloat(minVal: float, maxVal: float): float` | both |  |
| `RandomFloatExp(minVal: float, maxVal: float, exponent: float): float` | both |  |
| `RandomInt(minVal: int, maxVal: int): int` | both |  |
| `RollPercentage(percentage: int): bool` | both |  |

### CTakeDamageInfo

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `AddDamage(addAmount: float): nil` | server |  |
| `AddDamageType(damageType: int): nil` | server |  |
| `GetAmmoType(): int` | server |  |
| `GetAttacker(): handle` | server |  |
| `GetDamage(): float` | server |  |
| `GetDamageCustom(): int` | server |  |
| `GetDamageForce(): Vector` | server |  |
| `GetDamagePosition(): Vector` | server |  |
| `GetDamageType(): DAMAGE_TYPES` | server |  |
| `GetInflictor(): handle` | server |  |
| `GetOriginalDamage(): float` | server |  |
| `GetReportedPosition(): Vector` | server |  |
| `GetTotalledDamage(): float` | server |  |
| `HasDamageType(damageType: int): bool` | server |  |
| `ScaleDamage(scaleAmount: float): nil` | server |  |
| `SetAmmoType(ammoType: int): nil` | server |  |
| `SetAttacker(attacker: handle): nil` | server |  |
| `SetDamage(damage: float): nil` | server |  |
| `SetDamageCustom(damageCustom: int): nil` | server |  |
| `SetDamageForce(damageForce: Vector): nil` | server |  |
| `SetDamagePosition(damagePosition: Vector): nil` | server |  |
| `SetDamageType(damageType: int): nil` | server |  |
| `SetOriginalDamage(originalDamage: float): nil` | server |  |
| `SetReportedPosition(reportedPosition: Vector): nil` | server |  |

### GlobalSys

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CommandLineCheck(name: string): table` | both | Returns true if the command line param was used, otherwise false. |
| `CommandLineFloat(arg1: string, arg2: float): table` | both | Returns the command line param as a float. |
| `CommandLineInt(arg1: string, arg2: int): table` | both | Returns the command line param as an int. |
| `CommandLineStr(arg1: string, arg2: string): table` | both | Returns the command line param as a string. |

### GridNav

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `CanFindPath(start: Vector, end: Vector): bool` | server | Determine if it is possible to reach the specified end point from the specified start point. bool. |
| `DestroyTreesAroundPoint(arg1: Vector, arg2: float, arg3: bool): nil` | server | Destroy all trees in the area(vPosition, flRadius, bFullCollision. |
| `FindPathLength(start: Vector, end: Vector): float` | server | Find a path between the two points an return the length of the path. If there is not a path between the points the returned value will be -1. |
| `GetAllTreesAroundPoint(position: Vector, radius: float, fullCollision: bool): {'kind': 'array', 'types': ['CDOTA_MapTree']}` | server | Returns a table full of tree HSCRIPTS. |
| `GridPosToWorldCenterX(arg1: int): float` | server | Get the X position of the center of a given X index. |
| `GridPosToWorldCenterY(arg1: int): float` | server | Get the Y position of the center of a given Y index. |
| `IsBlocked(arg1: Vector): bool` | server | Checks whether the given position is blocked. |
| `IsNearbyTree(position: Vector, radius: float, checkFullTreeRadius: bool): bool` | server | Checks whether there are any trees overlapping the given point. |
| `IsTraversable(arg1: Vector): bool` | server | Checks whether the given position is traversable. |
| `RegrowAllTrees(): nil` | server | Causes all trees in the map to regrow. |
| `WorldToGridPosX(arg1: float): int` | server | Get the X index of a given world X position. |
| `WorldToGridPosY(arg1: float): int` | server | Get the Y index of a given world Y position. |

### ProjectileManager

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `ChangeTrackingProjectileSpeed(ability: CDOTABaseAbility, speed: int): nil` | server | Update speed. |
| `CreateLinearProjectile(options: CreateLinearProjectileOptions): ProjectileID` | server | Creates a linear projectile and returns the projectile ID. |
| `CreateTrackingProjectile(options: CreateTrackingProjectileOptions): ProjectileID` | server | Creates a tracking projectile. |
| `DestroyLinearProjectile(projectile: ProjectileID): nil` | server | Destroys the linear projectile matching the argument ID. |
| `DestroyTrackingProjectile(projectile: ProjectileID): nil` | server | Destroy a tracking projectile early. |
| `GetLinearProjectileLocation(projectile: ProjectileID): Vector` | server | Returns current location of projectile. |
| `GetLinearProjectileRadius(projectile: ProjectileID): float` | server | Returns current radius of projectile. |
| `GetLinearProjectileVelocity(projectile: ProjectileID): Vector` | server | Returns a vector representing the current velocity of the projectile. |
| `GetTrackingProjectileLocation(projectile: ProjectileID): Vector` | server | Returns current location of projectile. |
| `IsValidProjectile(value: int): bool` | server | Is this a valid projectile? |
| `ProjectileDodge(unit: CDOTA_BaseNPC): nil` | server | Makes the specified unit dodge projectiles. |
| `UpdateLinearProjectileDirection(projectile: ProjectileID, direction: Vector, speed: float): nil` | server | Update velocity. |

### QAngle

QAngle class.

**Fields**

| Field | Type | Description |
| --- | --- | --- |
| `x` | `float` | Pitch angle |
| `y` | `float` | Yaw angle |
| `z` | `float` | Roll angle |

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `__add(b: QAngle): QAngle` | both | Overloaded +. Adds angles together. |
| `__eq(b: QAngle): bool` | both | Overloaded ==. Tests for Equality. |
| `__tostring(): string` | both | Overloaded .. Converts the QAngles to strings. |
| `Forward(): Vector` | both | Returns the forward vector. |
| `Left(): Vector` | both | Returns the left vector. |
| `Up(): Vector` | both | Returns the up vector. |

### SteamInfo

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `IsPublicUniverse(): bool` | server | Is the script connected to the public Steam universe. |

### Uint64

Integer with binary operations.

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `__eq(b: Uint64): bool` | server |  |
| `__tostring(): string` | server | Overloaded .. Converts Uint64s to strings. |
| `BitwiseAnd(operand: Uint64): Uint64` | server | Performs bitwise AND between two integers. |
| `BitwiseOr(operand: Uint64): Uint64` | server | Performs bitwise OR between two integers. |
| `BitwiseXor(operand: Uint64): Uint64` | server | Performs bitwise XOR between two integers. |
| `BitwiseNot(): Uint64` | server | Performs bitwise NOT. |
| `SetBit(bitvalue: int): nil` | server | Sets the specified bit. |
| `ClearBit(bitvalue: int): int` | server | Clears the specified bit. |
| `IsBitSet(bitvalue: int): int, nil` | server | Checks if bit is set. |
| `ToggleBit(bitvalue: int): int` | server | Toggles the specified bit. |
| `ToHexString(): string` | server | Returns a hexadecimal string representation of the integer. |

### Vector

3D Vector class.

**Fields**

| Field | Type | Description |
| --- | --- | --- |
| `x` | `float` | X-axis |
| `y` | `float` | Y-axis |
| `z` | `float` | Z-axis |

**Methods**

| Method | Available | Description |
| --- | --- | --- |
| `__add(b: Vector): Vector` | both | Overloaded +. Adds vectors together. |
| `__div(b: Vector): Vector` | both | Overloaded /. Divides vectors. |
| `__eq(b: Vector): bool` | both | Overloaded ==. Tests for Equality. |
| `__len(): float` | both | Overloaded # returns the length of the vector. |
| `__mul(b: Vector \| float): Vector` | both | Overloaded * returns the vectors multiplied together. Can also be used to multiply with scalars. |
| `__sub(b: Vector): Vector` | both | Overloaded -. Subtracts vectors. |
| `__tostring(): string` | both | Overloaded .. Converts vectors to strings. |
| `__unm(): Vector` | both | Overloaded - operator. Reverses the vector. |
| `Cross(b: Vector): Vector` | both | Cross product of two vectors. |
| `Dot(b: Vector): float` | both | Dot product of two vectors. |
| `Length(): float` | both | Length of the Vector. |
| `Length2D(): float` | both | Length of the Vector in the XY plane. |
| `Normalized(): Vector` | both | Returns the vector normalized. |
| `Lerp(b: Vector, t: float): Vector` | both | Linearly interpolates between two vectors.<br>This is most commonly used to find a point some fraction of the way along a line between two endpoints.<br>Same as `this + (b - this) * t`. |
