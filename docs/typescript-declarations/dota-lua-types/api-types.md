# Dota Lua API types



9 type aliases and 36 interfaces. Primitive Lua types come from `lua-types`.

## Contents

<details><summary>Type aliases</summary>

- [CombatAnalyzerQueryID](#combatanalyzerqueryid)
- [CustomGameEventListenerID](#customgameeventlistenerid)
- [EntityIndex](#entityindex)
- [EventListenerID](#eventlistenerid)
- [ParticleID](#particleid)
- [PlayerID](#playerid)
- [ProjectileID](#projectileid)
- [SpawnGroupHandle](#spawngrouphandle)
- [ViewerID](#viewerid)

</details>
<details><summary>Interfaces</summary>

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

## Type aliases

### CombatAnalyzerQueryID

```ts
declare type CombatAnalyzerQueryID = number & {
    readonly __tag__: 'CombatAnalyzerQueryID';
};
```

### CustomGameEventListenerID

```ts
declare type CustomGameEventListenerID = number & {
    readonly __tag__: 'CustomGameEventListenerID';
};
```

### EntityIndex

```ts
declare type EntityIndex = number & {
    readonly __tag__: 'EntityIndex';
};
```

### EventListenerID

```ts
declare type EventListenerID = number & {
    readonly __tag__: 'EventListenerID';
};
```

### ParticleID

```ts
declare type ParticleID = number & {
    readonly __tag__: 'ParticleID';
};
```

### PlayerID

```ts
declare type PlayerID =
    | -1
    | 0
    | 1
    | 2
    | 3
    | 4
    | 5
    | 6
    | 7
    | 8
    | 9
    | 10
    | 11
    | 12
    | 13
    | 14
    | 15
    | 16
    | 17
    | 18
    | 19
    | 20
    | 21
    | 22
    | 23;
```

### ProjectileID

```ts
declare type ProjectileID = number & {
    readonly __tag__: 'ProjectileID';
};
```

### SpawnGroupHandle

```ts
declare type SpawnGroupHandle = number & {
    readonly __tag__: 'SpawnGroupHandle';
};
```

### ViewerID

```ts
declare type ViewerID = number & {
    readonly __tag__: 'ViewerID';
};
```

## Interfaces

### AbilityTuningValueFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entindex_caster_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `value_name_const` | `string` |  |
| `value` | `number` |  |

### ApplyDamageOptions

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `victim` | `CDOTA_BaseNPC` |  |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `number` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_flags?` | `DOTADamageFlag_t` |  |
| `ability?` | `CDOTABaseAbility` |  |

### BountyRunePickupFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `player_id_const` | `PlayerID` |  |
| `xp_bounty` | `number` |  |
| `gold_bounty` | `number` |  |

### CombatAnalyzerQueryResult

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `query_id` | `CombatAnalyzerQueryID` |  |

### CreateBaseProjectileOptions

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `EffectName?` | `string` |  |
| `Ability?` | `CDOTABaseAbility` |  |
| `Source?` | `CDOTA_BaseNPC` |  |
| `bProvidesVision?` | `boolean` |  |
| `iVisionRadius?` | `number` |  |
| `iVisionTeamNumber?` | `DOTATeam_t` |  |
| `ExtraData?` | `object` | Extra data associated with projectile instance, that is passed to<br>`OnProjectileThink_ExtraData` and `OnProjectileHit_ExtraData`. |

### CreateIllusionsModifierKeys

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `outgoing_damage?` | `number` |  |
| `incoming_damage?` | `number` |  |
| `bounty_base?` | `number` |  |
| `bounty_growth?` | `number` |  |
| `outgoing_damage_structure?` | `number` |  |
| `outgoing_damage_roshan?` | `number` |  |

### CreateLinearProjectileOptions

Extends `CreateBaseProjectileOptions`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `vSpawnOrigin?` | `Vector` |  |
| `vVelocity?` | `Vector` |  |
| `vAcceleration?` | `Vector` | Velocity change per second. |
| `fMaxSpeed?` | `number` |  |
| `fDistance?` | `number` |  |
| `fStartRadius?` | `number` |  |
| `fEndRadius?` | `number` |  |
| `fExpireTime?` | `number` |  |
| `iUnitTargetTeam?` | `DOTA_UNIT_TARGET_TEAM` |  |
| `iUnitTargetFlags?` | `DOTA_UNIT_TARGET_FLAGS` |  |
| `iUnitTargetType?` | `DOTA_UNIT_TARGET_TYPE` |  |
| `bIgnoreSource?` | `boolean` |  |
| `bHasFrontalCone?` | `boolean` |  |
| `bDrawsOnMinimap?` | `boolean` | **Default:** false<br> |
| `bVisibleToEnemies?` | `boolean` | Makes it invisible for all teams. |

### CreateTrackingProjectileOptions

Extends `CreateBaseProjectileOptions`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `vSourceLoc?` | `Vector` |  |
| `Target?` | `CDOTA_BaseNPC` |  |
| `iMoveSpeed?` | `number` |  |
| `flExpireTime?` | `number` |  |
| `bDodgeable?` | `boolean` |  |
| `bIsAttack?` | `boolean` |  |
| `bReplaceExisting?` | `boolean` | When enabled replaces existing projectile from the ability. Does not destroy<br>the particle.<br><br>**Default:** false<br> |
| `bIgnoreObstructions?` | `boolean` |  |
| `bSuppressTargetCheck?` | `boolean` |  |
| `iSourceAttachment?` | `DOTAProjectileAttachment_t` |  |
| `bDrawsOnMinimap?` | `boolean` | **Default:** false<br> |
| `bVisibleToEnemies?` | `boolean` | **Default:** true<br> |

### CreateUnitFromTableOptions

Extends `SpawnEntityFromTableOptions`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `MapUnitName` | `string` |  |
| `teamnumber?` | `DOTATeam_t` |  |
| `modelscale?` | `number` |  |
| `initial_waypoint?` | `string` | targetname of path_corner or path_track |
| `EnableAutoStyles?` | `string` |  |
| `rendercolor?` | `string` | RGB, example: "255 255 255" |
| `skin?` | `number` |  |
| `NeverMoveToClearSpace?` | `boolean` |  |

### CScriptHTTPResponse

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `Body` | `string` |  |
| `Request` | `CScriptHTTPRequest` |  |
| `StatusCode` | `number` |  |

### DamageFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entindex_attacker_const` | `EntityIndex` |  |
| `entindex_victim_const` | `EntityIndex` |  |
| `entindex_inflictor_const?` | `EntityIndex` |  |
| `damagetype_const` | `DAMAGE_TYPES` |  |
| `damage` | `number` |  |

### EntityBounds

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `Mins` | `Vector` |  |
| `Maxs` | `Vector` |  |

### ExecuteOrderFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `units` | `Record<string, EntityIndex>` |  |
| `entindex_target` | `EntityIndex` |  |
| `entindex_ability` | `EntityIndex` |  |
| `issuer_player_id_const` | `PlayerID` |  |
| `sequence_number_const` | `number` |  |
| `queue` | `0 \| 1` |  |
| `order_type` | `dotaunitorder_t` |  |
| `position_x` | `number` |  |
| `position_y` | `number` |  |
| `position_z` | `number` |  |
| `shop_item_name` | `string` |  |

### ExecuteOrderOptions

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `UnitIndex` | `EntityIndex` |  |
| `OrderType` | `dotaunitorder_t` |  |
| `TargetIndex?` | `EntityIndex` | Only used when targeting units. |
| `AbilityIndex?` | `EntityIndex` | Only used when casting abilities. |
| `Position?` | `Vector` | Only used when targeting the ground. |
| `Queue?` | `boolean` | Used for queueing up abilities. |

### HealingFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entindex_target_const` | `EntityIndex` |  |
| `entindex_inflictor_const?` | `EntityIndex` |  |
| `entindex_healer_const?` | `EntityIndex` |  |
| `heal` | `number` |  |

### ItemAddedToInventoryFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `inventory_parent_entindex_const` | `EntityIndex` |  |
| `item_parent_entindex_const` | `EntityIndex` |  |
| `item_entindex_const` | `EntityIndex` |  |
| `suggested_slot` | `-1 \| DOTAScriptInventorySlot_t` |  |

### LocalTime

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `Minutes` | `number` |  |
| `Seconds` | `number` |  |
| `Hours` | `number` |  |

### ModifierAbilityEvent

Extends `ModifierUnitEvent`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `ability` | `CDOTABaseAbility` |  |
| `target?` | `CDOTA_BaseNPC` |  |

### ModifierAddedEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `unit` | `CDOTA_BaseNPC` |  |
| `added_buff` | `CDOTA_Buff` |  |

### ModifierAttackEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `number` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_category` | `DamageCategory_t` |  |
| `damage_flags` | `DOTADamageFlag_t` |  |
| `inflictor?` | `CDOTABaseAbility` |  |
| `original_damage` | `number` |  |
| `ranged_attack` | `boolean` |  |
| `target` | `CDOTA_BaseNPC` |  |
| `no_attack_cooldown` | `boolean` |  |
| `record` | `number` |  |
| `fail_type` | `attackfail` |  |
| `report_max?` | `boolean` |  |

### ModifierGainedFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entindex_caster_const` | `EntityIndex` |  |
| `entindex_parent_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `name_const` | `string` |  |
| `duration` | `number` | -1 means forever. All other values less or equal to 0 would be equal to 1 frame. |

### ModifierHealEvent

Extends `ModifierUnitEvent`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `gain` | `number` |  |

### ModifierInstanceEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `attacker` | `CDOTA_BaseNPC` |  |
| `damage` | `number` |  |
| `damage_type` | `DAMAGE_TYPES` |  |
| `damage_category` | `DamageCategory_t` |  |
| `damage_flags` | `DOTADamageFlag_t` |  |
| `inflictor?` | `CDOTABaseAbility` |  |
| `original_damage` | `number` |  |
| `ranged_attack` | `boolean` |  |
| `unit` | `CDOTA_BaseNPC` |  |
| `no_attack_cooldown` | `boolean` |  |
| `record` | `number` |  |
| `fail_type` | `attackfail` |  |

### ModifierOverrideAbilitySpecialEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `ability` | `CDOTABaseAbility` |  |
| `ability_special_value` | `string` |  |
| `ability_special_level` | `number` |  |

### ModifierUnitEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `new_pos` | `Vector` |  |
| `order_type` | `dotaunitorder_t` |  |
| `unit` | `CDOTA_BaseNPC` |  |

### ModifyExperienceFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `hero_entindex_const` | `EntityIndex` |  |
| `player_id_const` | `PlayerID` |  |
| `reason_const` | `EDOTA_ModifyXP_Reason` |  |
| `experience` | `number` |  |

### ModifyGoldFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `player_id_const` | `PlayerID` |  |
| `reason_const` | `EDOTA_ModifyGold_Reason` |  |
| `reliable` | `0 \| 1` |  |
| `gold` | `number` |  |

### RuneSpawnFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `spawner_entindex_const` | `EntityIndex` |  |
| `rune_type` | `DOTA_RUNES` |  |

### SpawnEntityFromTableOptions

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `origin?` | `string \| Vector` |  |
| `angles?` | `string \| QAngle` |  |
| `scales?` | `string \| Vector` |  |
| `targetname?` | `string` |  |
| `vscripts?` | `string` |  |

### TraceCollideableInputs

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `ent` | `CBaseEntity` |  |
| `mins?` | `unknown` |  |
| `maxs?` | `unknown` |  |

### TraceCollideableOutputs

Extends `TraceCollideableInputs`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `hit` | `boolean` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `number` |  |

### TraceHullInputs

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `min` | `unknown` |  |
| `max` | `unknown` |  |
| `mask?` | `unknown` |  |
| `ignore?` | `unknown` |  |

### TraceHullOutputs

Extends `TraceHullInputs`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `hit` | `boolean` |  |
| `startsolid` | `boolean` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `number` |  |
| `enthit?` | `CBaseEntity` |  |

### TraceLineInputs

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `startpos` | `Vector` |  |
| `endpos` | `Vector` |  |
| `mask?` | `unknown` |  |
| `ignore?` | `unknown` |  |

### TraceLineOutputs

Extends `TraceLineInputs`

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `hit` | `boolean` |  |
| `startsolid` | `boolean` |  |
| `pos` | `Vector` |  |
| `normal` | `Vector` |  |
| `fraction` | `number` |  |
| `enthit?` | `CBaseEntity` |  |

### TrackingProjectileFilterEvent

**Properties**

| Property | Type | Description |
| --- | --- | --- |
| `entindex_source_const` | `EntityIndex` |  |
| `entindex_target_const` | `EntityIndex` |  |
| `entindex_ability_const` | `EntityIndex` |  |
| `is_attack` | `0 \| 1` |  |
| `dodgeable` | `0 \| 1` |  |
| `max_impact_time` | `number` |  |
| `move_speed` | `number` |  |
| `expire_time` | `number` |  |
