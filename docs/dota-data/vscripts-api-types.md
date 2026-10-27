# VScripts API types



12 primitive, 9 nominal and 36 object types.

## Primitive types

| Name | Description |
| --- | --- |
| `bool` |  |
| `double` |  |
| `ehandle` |  |
| `float` |  |
| `handle` |  |
| `int` |  |
| `nil` |  |
| `Quaternion` | There is no known way to create values of this type. |
| `string` |  |
| `table` |  |
| `uint` |  |
| `Vector2D` | There is no known way to create values of this type. |

## Nominal types

| Name | Base type | Description |
| --- | --- | --- |
| `CombatAnalyzerQueryID` | `int` |  |
| `CustomGameEventListenerID` | `int` |  |
| `EntityIndex` | `int` |  |
| `EventListenerID` | `int` |  |
| `ParticleID` | `int` |  |
| `PlayerID` | `int` |  |
| `ProjectileID` | `int` |  |
| `SpawnGroupHandle` | `int` |  |
| `ViewerID` | `int` |  |

## Object types

<details><summary>Object types</summary>

- [AbilityTuningValueFilterEvent](#abilitytuningvaluefilterevent)
- [ApplyDamageOptions](#applydamageoptions)
- [BountyRunePickupFilterEvent](#bountyrunepickupfilterevent)
- [CombatAnalyzerQueryResult](#combatanalyzerqueryresult)
- [CreateBaseProjectileOptions](#createbaseprojectileoptions)
- [CreateIllusionsModifierKeys](#createillusionsmodifierkeys)
- [CreateLinearProjectileOptions](#createlinearprojectileoptions)
- [CreateTrackingProjectileOptions](#createtrackingprojectileoptions)
- [CreateUnitFromTableOptions](#createunitfromtableoptions)
- [CScriptHTTPResponse](#cscripthttpresponse)
- [DamageFilterEvent](#damagefilterevent)
- [EntityBounds](#entitybounds)
- [ExecuteOrderFilterEvent](#executeorderfilterevent)
- [ExecuteOrderOptions](#executeorderoptions)
- [HealingFilterEvent](#healingfilterevent)
- [ItemAddedToInventoryFilterEvent](#itemaddedtoinventoryfilterevent)
- [LocalTime](#localtime)
- [ModifierAbilityEvent](#modifierabilityevent)
- [ModifierAddedEvent](#modifieraddedevent)
- [ModifierAttackEvent](#modifierattackevent)
- [ModifierGainedFilterEvent](#modifiergainedfilterevent)
- [ModifierHealEvent](#modifierhealevent)
- [ModifierInstanceEvent](#modifierinstanceevent)
- [ModifierOverrideAbilitySpecialEvent](#modifieroverrideabilityspecialevent)
- [ModifierUnitEvent](#modifierunitevent)
- [ModifyExperienceFilterEvent](#modifyexperiencefilterevent)
- [ModifyGoldFilterEvent](#modifygoldfilterevent)
- [RuneSpawnFilterEvent](#runespawnfilterevent)
- [SpawnEntityFromTableOptions](#spawnentityfromtableoptions)
- [TraceCollideableInputs](#tracecollideableinputs)
- [TraceCollideableOutputs](#tracecollideableoutputs)
- [TraceHullInputs](#tracehullinputs)
- [TraceHullOutputs](#tracehulloutputs)
- [TraceLineInputs](#tracelineinputs)
- [TraceLineOutputs](#tracelineoutputs)
- [TrackingProjectileFilterEvent](#trackingprojectilefilterevent)

</details>

### AbilityTuningValueFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `entindex_caster_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `value_name_const` | `string` |  |
| `value` | `int` |  |

### ApplyDamageOptions

| Field | Type | Description |
| --- | --- | --- |
| `victim` | `CDOTA_BaseNPC` |  |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `float` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_flags` | `DOTADamageFlag_t \| nil` |  |
| `ability` | `CDOTABaseAbility \| nil` |  |

### BountyRunePickupFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `player_id_const` | `PlayerID` |  |
| `xp_bounty` | `int` |  |
| `gold_bounty` | `int` |  |

### CombatAnalyzerQueryResult

| Field | Type | Description |
| --- | --- | --- |
| `query_id` | `CombatAnalyzerQueryID` |  |

### CreateBaseProjectileOptions

| Field | Type | Description |
| --- | --- | --- |
| `EffectName` | `string \| nil` |  |
| `Ability` | `CDOTABaseAbility \| nil` |  |
| `Source` | `CDOTA_BaseNPC \| nil` |  |
| `bProvidesVision` | `bool \| nil` |  |
| `iVisionRadius` | `uint \| nil` |  |
| `iVisionTeamNumber` | `DOTATeam_t \| nil` |  |
| `ExtraData` | `table \| nil` | Extra data associated with projectile instance, that is passed to `OnProjectileThink_ExtraData` and `OnProjectileHit_ExtraData`. |

### CreateIllusionsModifierKeys

| Field | Type | Description |
| --- | --- | --- |
| `outgoing_damage` | `float \| nil` |  |
| `incoming_damage` | `float \| nil` |  |
| `bounty_base` | `float \| nil` |  |
| `bounty_growth` | `float \| nil` |  |
| `outgoing_damage_structure` | `float \| nil` |  |
| `outgoing_damage_roshan` | `float \| nil` |  |

### CreateLinearProjectileOptions

| Field | Type | Description |
| --- | --- | --- |
| `vSpawnOrigin` | `Vector \| nil` |  |
| `vVelocity` | `Vector \| nil` |  |
| `vAcceleration` | `Vector \| nil` | Velocity change per second. |
| `fMaxSpeed` | `float \| nil` |  |
| `fDistance` | `float \| nil` |  |
| `fStartRadius` | `float \| nil` |  |
| `fEndRadius` | `float \| nil` |  |
| `fExpireTime` | `float \| nil` |  |
| `iUnitTargetTeam` | `DOTA_UNIT_TARGET_TEAM \| nil` |  |
| `iUnitTargetFlags` | `DOTA_UNIT_TARGET_FLAGS \| nil` |  |
| `iUnitTargetType` | `DOTA_UNIT_TARGET_TYPE \| nil` |  |
| `bIgnoreSource` | `bool \| nil` |  |
| `bHasFrontalCone` | `bool \| nil` |  |
| `bDrawsOnMinimap` | `bool \| nil` | @default false |
| `bVisibleToEnemies` | `bool \| nil` | Makes it invisible for all teams. |

### CreateTrackingProjectileOptions

| Field | Type | Description |
| --- | --- | --- |
| `vSourceLoc` | `Vector \| nil` |  |
| `Target` | `CDOTA_BaseNPC \| nil` |  |
| `iMoveSpeed` | `int \| nil` |  |
| `flExpireTime` | `float \| nil` |  |
| `bDodgeable` | `bool \| nil` |  |
| `bIsAttack` | `bool \| nil` |  |
| `bReplaceExisting` | `bool \| nil` | When enabled replaces existing projectile from the ability. Does not destroy the particle.<br>@default false |
| `bIgnoreObstructions` | `bool \| nil` |  |
| `bSuppressTargetCheck` | `bool \| nil` |  |
| `iSourceAttachment` | `DOTAProjectileAttachment_t \| nil` |  |
| `bDrawsOnMinimap` | `bool \| nil` | @default false |
| `bVisibleToEnemies` | `bool \| nil` | @default true |

### CreateUnitFromTableOptions

| Field | Type | Description |
| --- | --- | --- |
| `MapUnitName` | `string` |  |
| `teamnumber` | `DOTATeam_t \| nil` |  |
| `modelscale` | `int \| nil` |  |
| `initial_waypoint` | `string \| nil` | targetname of path_corner or path_track |
| `EnableAutoStyles` | `string \| nil` |  |
| `rendercolor` | `string \| nil` | RGB, example: "255 255 255" |
| `skin` | `int \| nil` |  |
| `NeverMoveToClearSpace` | `bool \| nil` |  |

### CScriptHTTPResponse

| Field | Type | Description |
| --- | --- | --- |
| `Body` | `string` |  |
| `Request` | `CScriptHTTPRequest` |  |
| `StatusCode` | `uint` |  |

### DamageFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `entindex_attacker_const` | `EntityIndex` |  |
| `entindex_victim_const` | `EntityIndex` |  |
| `entindex_inflictor_const` | `EntityIndex \| nil` |  |
| `damagetype_const` | `DAMAGE_TYPES` |  |
| `damage` | `float` |  |

### EntityBounds

| Field | Type | Description |
| --- | --- | --- |
| `Mins` | `Vector` |  |
| `Maxs` | `Vector` |  |

### ExecuteOrderFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `units` | `{'kind': 'table', 'key': ['string'], 'value': ['EntityIndex']}` |  |
| `entindex_target` | `EntityIndex` |  |
| `entindex_ability` | `EntityIndex` |  |
| `issuer_player_id_const` | `PlayerID` |  |
| `sequence_number_const` | `uint` |  |
| `queue` | `{'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1}` |  |
| `order_type` | `dotaunitorder_t` |  |
| `position_x` | `float` |  |
| `position_y` | `float` |  |
| `position_z` | `float` |  |
| `shop_item_name` | `string` |  |

### ExecuteOrderOptions

| Field | Type | Description |
| --- | --- | --- |
| `UnitIndex` | `EntityIndex` |  |
| `OrderType` | `dotaunitorder_t` |  |
| `TargetIndex` | `EntityIndex \| nil` | Only used when targeting units. |
| `AbilityIndex` | `EntityIndex \| nil` | Only used when casting abilities. |
| `Position` | `Vector \| nil` | Only used when targeting the ground. |
| `Queue` | `bool \| nil` | Used for queueing up abilities. |

### HealingFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `entindex_target_const` | `EntityIndex` |  |
| `entindex_inflictor_const` | `EntityIndex \| nil` |  |
| `entindex_healer_const` | `EntityIndex \| nil` |  |
| `heal` | `int` |  |

### ItemAddedToInventoryFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `inventory_parent_entindex_const` | `EntityIndex` |  |
| `item_parent_entindex_const` | `EntityIndex` |  |
| `item_entindex_const` | `EntityIndex` |  |
| `suggested_slot` | `{'kind': 'literal', 'value': -1} \| DOTAScriptInventorySlot_t` |  |

### LocalTime

| Field | Type | Description |
| --- | --- | --- |
| `Minutes` | `int` |  |
| `Seconds` | `int` |  |
| `Hours` | `int` |  |

### ModifierAbilityEvent

| Field | Type | Description |
| --- | --- | --- |
| `ability` | `CDOTABaseAbility` |  |
| `target` | `CDOTA_BaseNPC \| nil` |  |

### ModifierAddedEvent

| Field | Type | Description |
| --- | --- | --- |
| `unit` | `CDOTA_BaseNPC` |  |
| `added_buff` | `CDOTA_Buff` |  |

### ModifierAttackEvent

| Field | Type | Description |
| --- | --- | --- |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `float` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_category` | `DamageCategory_t` |  |
| `damage_flags` | `DOTADamageFlag_t` |  |
| `inflictor` | `CDOTABaseAbility \| nil` |  |
| `original_damage` | `float` |  |
| `ranged_attack` | `bool` |  |
| `target` | `CDOTA_BaseNPC` |  |
| `no_attack_cooldown` | `bool` |  |
| `record` | `int` |  |
| `fail_type` | `attackfail` |  |
| `report_max` | `bool \| nil` |  |

### ModifierGainedFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `entindex_caster_const` | `EntityIndex` |  |
| `entindex_parent_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `name_const` | `string` |  |
| `duration` | `int` | -1 means forever. All other values less or equal to 0 would be equal to 1 frame. |

### ModifierHealEvent

| Field | Type | Description |
| --- | --- | --- |
| `gain` | `int` |  |

### ModifierInstanceEvent

| Field | Type | Description |
| --- | --- | --- |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `float` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_category` | `DamageCategory_t` |  |
| `damage_flags` | `DOTADamageFlag_t` |  |
| `inflictor` | `CDOTABaseAbility \| nil` |  |
| `original_damage` | `float` |  |
| `ranged_attack` | `bool` |  |
| `unit` | `CDOTA_BaseNPC` |  |
| `no_attack_cooldown` | `bool` |  |
| `record` | `int` |  |
| `fail_type` | `attackfail` |  |

### ModifierOverrideAbilitySpecialEvent

| Field | Type | Description |
| --- | --- | --- |
| `ability` | `CDOTABaseAbility` |  |
| `ability_special_value` | `string` |  |
| `ability_special_level` | `int` |  |

### ModifierUnitEvent

| Field | Type | Description |
| --- | --- | --- |
| `new_pos` | `Vector` |  |
| `order_type` | `dotaunitorder_t` |  |
| `unit` | `CDOTA_BaseNPC` |  |

### ModifyExperienceFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `hero_entindex_const` | `EntityIndex` |  |
| `player_id_const` | `PlayerID` |  |
| `reason_const` | `EDOTA_ModifyXP_Reason` |  |
| `experience` | `int` |  |

### ModifyGoldFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `player_id_const` | `PlayerID` |  |
| `reason_const` | `EDOTA_ModifyGold_Reason` |  |
| `reliable` | `{'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1}` |  |
| `gold` | `uint` |  |

### RuneSpawnFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `spawner_entindex_const` | `EntityIndex` |  |
| `rune_type` | `DOTA_RUNES` |  |

### SpawnEntityFromTableOptions

| Field | Type | Description |
| --- | --- | --- |
| `origin` | `string \| Vector \| nil` |  |
| `angles` | `string \| QAngle \| nil` |  |
| `scales` | `string \| Vector \| nil` |  |
| `targetname` | `string \| nil` |  |
| `vscripts` | `string \| nil` |  |

### TraceCollideableInputs

| Field | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `ent` | `CBaseEntity` |  |
| `mins` | `unknown \| nil` |  |
| `maxs` | `unknown \| nil` |  |

### TraceCollideableOutputs

| Field | Type | Description |
| --- | --- | --- |
| `hit` | `bool` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `float` |  |

### TraceHullInputs

| Field | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `min` | `unknown` |  |
| `max` | `unknown` |  |
| `mask` | `unknown \| nil` |  |
| `ignore` | `unknown \| nil` |  |

### TraceHullOutputs

| Field | Type | Description |
| --- | --- | --- |
| `hit` | `bool` |  |
| `startsolid` | `bool` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `float` |  |
| `enthit` | `CBaseEntity \| nil` |  |

### TraceLineInputs

| Field | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `mask` | `unknown \| nil` |  |
| `ignore` | `unknown \| nil` |  |

### TraceLineOutputs

| Field | Type | Description |
| --- | --- | --- |
| `hit` | `bool` |  |
| `startsolid` | `bool` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `float` |  |
| `enthit` | `CBaseEntity \| nil` |  |

### TrackingProjectileFilterEvent

| Field | Type | Description |
| --- | --- | --- |
| `entindex_source_const` | `EntityIndex` |  |
| `entindex_target_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `is_attack` | `{'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1}` |  |
| `dodgeable` | `{'kind': 'literal', 'value': 0} \| {'kind': 'literal', 'value': 1}` |  |
| `max_impact_time` | `int` |  |
| `move_speed` | `int` |  |
| `expire_time` | `int` |  |
