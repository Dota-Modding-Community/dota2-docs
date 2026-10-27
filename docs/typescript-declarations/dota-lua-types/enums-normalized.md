# Dota Lua normalized enums



63 enums, 50 compatibility aliases and 34 constants.

## Contents

<details><summary>Enums</summary>

- [AbilityBehavior](#abilitybehavior)
- [AbilityLearnResult](#abilitylearnresult)
- [AbilitySpeakTrigger](#abilityspeaktrigger)
- [AbilityTypes](#abilitytypes)
- [ActivateType](#activatetype)
- [AttackRecord](#attackrecord)
- [AttributeDerivedStats](#attributederivedstats)
- [Attributes](#attributes)
- [ClickBehaviors](#clickbehaviors)
- [ConnectionState](#connectionstate)
- [ConVarFlags](#convarflags)
- [CustomCameraEventFlags](#customcameraeventflags)
- [DamageCategory](#damagecategory)
- [DamageFlag](#damageflag)
- [DamageTypes](#damagetypes)
- [DefaultUiElement](#defaultuielement)
- [DotaTeam](#dotateam)
- [EntityEffects](#entityeffects)
- [EntityThinkPhase](#entitythinkphase)
- [FindOrder](#findorder)
- [GameActivity](#gameactivity)
- [GameState](#gamestate)
- [GcTeam](#gcteam)
- [HeroPickState](#heropickstate)
- [HudVisibility](#hudvisibility)
- [InvalidOrders](#invalidorders)
- [InventoryFlags](#inventoryflags)
- [InventorySlot](#inventoryslot)
- [ItemShareability](#itemshareability)
- [LoadoutType](#loadouttype)
- [LuaModifierMotionType](#luamodifiermotiontype)
- [MinimapEventType](#minimapeventtype)
- [ModifierAttribute](#modifierattribute)
- [ModifierFunction](#modifierfunction)
- [ModifierPriority](#modifierpriority)
- [ModifierRemove](#modifierremove)
- [ModifierState](#modifierstate)
- [ModifyGoldReason](#modifygoldreason)
- [ModifyXpReason](#modifyxpreason)
- [MotionControllerPriority](#motioncontrollerpriority)
- [MusicStatus](#musicstatus)
- [OverheadAlert](#overheadalert)
- [ParticleAttachment](#particleattachment)
- [PostGameColumn](#postgamecolumn)
- [PostGameLayout](#postgamelayout)
- [ProjectileAttachment](#projectileattachment)
- [PseudoRandom](#pseudorandom)
- [QuestTextReplaceValue](#questtextreplacevalue)
- [RuneType](#runetype)
- [ShopType](#shoptype)
- [ShowGenericPopupType](#showgenericpopuptype)
- [SourceEngineAnimationEvent](#sourceengineanimationevent)
- [SourceEngineDamageTypes](#sourceenginedamagetypes)
- [SourceEngineSoundData](#sourceenginesounddata)
- [SpeechType](#speechtype)
- [SubquestTextReplaceValue](#subquesttextreplacevalue)
- [UnitAttackCapability](#unitattackcapability)
- [UnitFilterResult](#unitfilterresult)
- [UnitMoveCapability](#unitmovecapability)
- [UnitOrder](#unitorder)
- [UnitTargetFlags](#unittargetflags)
- [UnitTargetTeam](#unittargetteam)
- [UnitTargetType](#unittargettype)

</details>
<details><summary>Compatibility aliases</summary>

- [ABILITY_TYPES](#ability_types)
- [AbilityLearnResult_t](#abilitylearnresult_t)
- [attackfail](#attackfail)
- [CLICK_BEHAVIORS](#click_behaviors)
- [DAMAGE_TYPES](#damage_types)
- [DamageCategory_t](#damagecategory_t)
- [DOTA_ABILITY_BEHAVIOR](#dota_ability_behavior)
- [DOTA_GameState](#dota_gamestate)
- [DOTA_GC_TEAM](#dota_gc_team)
- [DOTA_HeroPickState](#dota_heropickstate)
- [DOTA_INVALID_ORDERS](#dota_invalid_orders)
- [DOTA_MOTION_CONTROLLER_PRIORITY](#dota_motion_controller_priority)
- [DOTA_OVERHEAD_ALERT](#dota_overhead_alert)
- [DOTA_RUNES](#dota_runes)
- [DOTA_SHOP_TYPE](#dota_shop_type)
- [DOTA_UNIT_TARGET_FLAGS](#dota_unit_target_flags)
- [DOTA_UNIT_TARGET_TEAM](#dota_unit_target_team)
- [DOTA_UNIT_TARGET_TYPE](#dota_unit_target_type)
- [DOTAAbilitySpeakTrigger_t](#dotaabilityspeaktrigger_t)
- [DOTAConnectionState_t](#dotaconnectionstate_t)
- [DOTACustomCameraEventFlags_t](#dotacustomcameraeventflags_t)
- [DOTADamageFlag_t](#dotadamageflag_t)
- [DotaDefaultUIElement_t](#dotadefaultuielement_t)
- [DOTAHUDVisibility_t](#dotahudvisibility_t)
- [DOTAInventoryFlags_t](#dotainventoryflags_t)
- [DOTAMinimapEvent_t](#dotaminimapevent_t)
- [DOTAModifierAttribute_t](#dotamodifierattribute_t)
- [DOTAMusicStatus_t](#dotamusicstatus_t)
- [DOTAPostGameColumn_t](#dotapostgamecolumn_t)
- [DOTAPostGameLayout_t](#dotapostgamelayout_t)
- [DOTAProjectileAttachment_t](#dotaprojectileattachment_t)
- [DOTAScriptInventorySlot_t](#dotascriptinventoryslot_t)
- [DOTASlotType_t](#dotaslottype_t)
- [DOTASpeechType_t](#dotaspeechtype_t)
- [DOTATeam_t](#dotateam_t)
- [DOTAUnitAttackCapability_t](#dotaunitattackcapability_t)
- [DOTAUnitMoveCapability_t](#dotaunitmovecapability_t)
- [dotaunitorder_t](#dotaunitorder_t)
- [EDOTA_ModifyGold_Reason](#edota_modifygold_reason)
- [EDOTA_ModifyXP_Reason](#edota_modifyxp_reason)
- [EShareAbility](#eshareability)
- [GameActivity_t](#gameactivity_t)
- [LuaModifierType](#luamodifiertype)
- [modifierfunction](#modifierfunction)
- [modifierpriority](#modifierpriority)
- [modifierremove](#modifierremove)
- [modifierstate](#modifierstate)
- [ParticleAttachment_t](#particleattachment_t)
- [quest_text_replace_values_t](#quest_text_replace_values_t)
- [subquest_text_replace_values_t](#subquest_text_replace_values_t)

</details>

## Constants

| Name | Type / value | Description |
| --- | --- | --- |
| `DOTA_DEFAULT_MAX_TEAM` | `5` | Default number of players per team. |
| `DOTA_DEFAULT_MAX_TEAM_PLAYERS` | `10` | Default number of non-spectator players supported. |
| `DOTA_DEFAULT_UI_ELEMENT_COUNT` | `32` |  |
| `DOTA_HEROPICK_STATE_COUNT` | `62` |  |
| `DOTA_HUD_VISIBILITY_COUNT` | `32` |  |
| `DOTA_ITEM_INVENTORY_SIZE` | `9` |  |
| `DOTA_ITEM_MAX` | `25` |  |
| `DOTA_ITEM_STASH_MAX` | `15` |  |
| `DOTA_ITEM_STASH_MIN` | `9` |  |
| `DOTA_ITEM_STASH_SIZE` | `6` |  |
| `DOTA_LOADOUT_TYPE_COUNT` | `103` |  |
| `DOTA_MAX_ABILITIES` | `40` |  |
| `DOTA_MAX_PLAYER_TEAMS` | `10` | Max number of player teams supported. |
| `DOTA_MAX_PLAYERS` | `64` | Max number of players connected to the server including spectators. |
| `DOTA_MAX_SPECTATOR_LOBBY_SIZE` | `15` | Max number of viewers in a spectator lobby. |
| `DOTA_MAX_SPECTATOR_TEAM_SIZE` | `40` | How many spectators can watch. |
| `DOTA_MAX_TEAM` | `24` | Max number of players per team. |
| `DOTA_MAX_TEAM_PLAYERS` | `24` | Max number of non-spectator players supported. |
| `DOTA_PLAYER_LOADOUT_END` | `101` |  |
| `DOTA_PLAYER_LOADOUT_START` | `70` |  |
| `DOTA_PROJECTILE_ATTACHMENT_LAST` | `6` |  |
| `DOTA_RUNE_COUNT` | `10` |  |
| `DOTA_TEAM_COUNT` | `15` |  |
| `DOTA_TEAM_CUSTOM_COUNT` | `8` |  |
| `DOTA_TEAM_CUSTOM_MAX` | `13` |  |
| `DOTA_TEAM_CUSTOM_MIN` | `6` |  |
| `DOTA_TEAM_FIRST` | `2` |  |
| `DOTA_UNIT_ATTACK_CAPABILITY_BIT_COUNT` | `3` |  |
| `FIND_UNITS_EVERYWHERE` | `-1` |  |
| `MAX_PATTACH_TYPES` | `16` |  |
| `MODIFIER_FUNCTION_LAST` | `399` |  |
| `MODIFIER_STATE_LAST` | `64` |  |
| `QUEST_NUM_TEXT_REPLACE_VALUES` | `4` |  |
| `SPAWN_GROUP_HANDLE_INVALID` | `0` |  |

## Enums

### AbilityBehavior

| Member | Value |
| --- | --- |
| `LAST_RESORT_POINT` | `-2147483648` |
| `AFFECTED_BY_MUTE` | `0` |
| `ALT_CASTABLE` | `0` |
| `CAN_SELF_CAST` | `0` |
| `DONT_PROC_OTHER_ABILITIES` | `0` |
| `FORCE_KEYBIND` | `0` |
| `FORCE_NO_INNATE_UI` | `0` |
| `FREE_DRAW_TARGETING` | `0` |
| `IGNORE_INVISIBLE` | `0` |
| `IGNORE_MUTED` | `0` |
| `IGNORE_SILENCE` | `0` |
| `INNATE_UI` | `0` |
| `IS_FAKE_ITEM` | `0` |
| `ITEM_IMBUE` | `0` |
| `NONE` | `0` |
| `OVERSHOOT` | `0` |
| `SHOW_IN_GUIDES` | `0` |
| `SKIP_FOR_KEYBINDS` | `0` |
| `SUPPRESS_ASSOCIATED_CONSUMABLE` | `0` |
| `UNLOCKED_BY_EFFECT_INDEX` | `0` |
| `UNSWAPPABLE` | `0` |
| `HIDDEN` | `1` |
| `PASSIVE` | `2` |
| `NO_TARGET` | `4` |
| `UNIT_TARGET` | `8` |
| `POINT` | `16` |
| `AOE` | `32` |
| `NOT_LEARNABLE` | `64` |
| `CHANNELLED` | `128` |
| `ITEM` | `256` |
| `TOGGLE` | `512` |
| `DIRECTIONAL` | `1024` |
| `IMMEDIATE` | `2048` |
| `AUTOCAST` | `4096` |
| `OPTIONAL_UNIT_TARGET` | `8192` |
| `OPTIONAL_POINT` | `16384` |
| `OPTIONAL_NO_TARGET` | `32768` |
| `AURA` | `65536` |
| `ATTACK` | `131072` |
| `DONT_RESUME_MOVEMENT` | `262144` |
| `ROOT_DISABLES` | `524288` |
| `UNRESTRICTED` | `1048576` |
| `IGNORE_PSEUDO_QUEUE` | `2097152` |
| `IGNORE_CHANNEL` | `4194304` |
| `DONT_CANCEL_MOVEMENT` | `8388608` |
| `DONT_ALERT_TARGET` | `16777216` |
| `DONT_RESUME_ATTACK` | `33554432` |
| `NORMAL_WHEN_STOLEN` | `67108864` |
| `IGNORE_BACKSWING` | `134217728` |
| `RUNE_TARGET` | `268435456` |
| `DONT_CANCEL_CHANNEL` | `536870912` |
| `VECTOR_TARGETING` | `1073741824` |

### AbilityLearnResult

| Member | Value |
| --- | --- |
| `CAN_BE_UPGRADED` | `0` |
| `CANNOT_BE_UPGRADED_NOT_UPGRADABLE` | `1` |
| `CANNOT_BE_UPGRADED_AT_MAX` | `2` |
| `CANNOT_BE_UPGRADED_REQUIRES_LEVEL` | `3` |
| `NOT_LEARNABLE` | `4` |

### AbilitySpeakTrigger

| Member | Value |
| --- | --- |
| `START_ACTION_PHASE` | `0` |
| `CAST` | `1` |

### AbilityTypes

| Member | Value |
| --- | --- |
| `BASIC` | `0` |
| `ULTIMATE` | `1` |
| `ATTRIBUTES` | `2` |
| `HIDDEN` | `3` |

### ActivateType

| Member | Value |
| --- | --- |
| `INITIAL_CREATION` | `0` |
| `DATAUPDATE_CREATION` | `1` |
| `ONRESTORE` | `2` |

### AttackRecord

| Member | Value |
| --- | --- |
| `FAIL_NO` | `0` |
| `FAIL_TERRAIN_MISS` | `1` |
| `FAIL_SOURCE_MISS` | `2` |
| `FAIL_TARGET_EVADED` | `3` |
| `FAIL_TARGET_INVULNERABLE` | `4` |
| `FAIL_TARGET_OUT_OF_RANGE` | `5` |
| `CANNOT_FAIL` | `6` |
| `FAIL_BLOCKED_BY_OBSTRUCTION` | `7` |

### AttributeDerivedStats

| Member | Value |
| --- | --- |
| `STRENGTH_DAMAGE` | `0` |
| `STRENGTH_HP` | `1` |
| `STRENGTH_HP_REGEN` | `2` |
| `AGILITY_DAMAGE` | `3` |
| `AGILITY_ARMOR` | `4` |
| `AGILITY_ATTACK_SPEED` | `5` |
| `INTELLIGENCE_DAMAGE` | `6` |
| `INTELLIGENCE_MANA` | `7` |
| `INTELLIGENCE_MANA_REGEN` | `8` |
| `INTELLIGENCE_MAGIC_RESIST` | `9` |
| `ALL_DAMAGE` | `10` |

### Attributes

| Member | Value |
| --- | --- |
| `INVALID` | `-1` |
| `STRENGTH` | `0` |
| `AGILITY` | `1` |
| `INTELLECT` | `2` |
| `ALL` | `3` |
| `MAX` | `4` |

### ClickBehaviors

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `MOVE` | `1` |
| `ATTACK` | `2` |
| `CAST` | `3` |
| `DROP_ITEM` | `4` |
| `DROP_SHOP_ITEM` | `5` |
| `DRAG` | `6` |
| `LEARN_ABILITY` | `7` |
| `PATROL` | `8` |
| `VECTOR_CAST` | `9` |
| `UNUSED` | `10` |
| `RADAR` | `11` |
| `LAST` | `12` |

### ConnectionState

| Member | Value |
| --- | --- |
| `UNKNOWN` | `0` |
| `NOT_YET_CONNECTED` | `1` |
| `CONNECTED` | `2` |
| `DISCONNECTED` | `3` |
| `ABANDONED` | `4` |
| `LOADING` | `5` |
| `FAILED` | `6` |

### ConVarFlags

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `DEVELOPMENTONLY` | `2` |
| `HIDDEN` | `16` |
| `PROTECTED` | `32` |
| `SPONLY` | `64` |
| `ARCHIVE` | `128` |
| `NOTIFY` | `256` |
| `USERINFO` | `512` |
| `UNLOGGED` | `2048` |
| `REPLICATED` | `8192` |
| `CHEAT` | `16384` |
| `PER_USER` | `32768` |
| `DEMO` | `65536` |
| `DONTRECORD` | `131072` |
| `VCONSOLE_SET_FOCUS` | `134217728` |

### CustomCameraEventFlags

| Member | Value |
| --- | --- |
| `ZOOM` | `1` |
| `POSITION` | `2` |
| `POSITION_PLAYER_HERO` | `4` |
| `PITCH` | `8` |
| `YAW` | `16` |
| `LOCK` | `32` |
| `UNLOCK` | `64` |
| `RESET_DEFAULT` | `128` |
| `SPECIFIC_PLAYER` | `256` |
| `FADE_OUT` | `512` |
| `FADE_IN` | `1024` |
| `LETTERBOX_ON` | `2048` |
| `LETTERBOX_OFF` | `4096` |

### DamageCategory

| Member | Value |
| --- | --- |
| `SPELL` | `0` |
| `ATTACK` | `1` |
| `BARRIER` | `2` |

### DamageFlag

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `IGNORES_MAGIC_ARMOR` | `1` |
| `IGNORES_PHYSICAL_ARMOR` | `2` |
| `BYPASSES_INVULNERABILITY` | `4` |
| `BYPASSES_PHYSICAL_BLOCK` | `8` |
| `REFLECTION` | `16` |
| `HPLOSS` | `32` |
| `NO_DIRECTOR_EVENT` | `64` |
| `NON_LETHAL` | `128` |
| `NO_DAMAGE_MULTIPLIERS` | `512` |
| `NO_SPELL_AMPLIFICATION` | `1024` |
| `DONT_DISPLAY_DAMAGE_IF_SOURCE_HIDDEN` | `2048` |
| `NO_SPELL_LIFESTEAL` | `4096` |
| `PROPERTY_FIRE` | `8192` |
| `IGNORES_BASE_PHYSICAL_ARMOR` | `16384` |
| `SECONDARY_PROJECTILE_ATTACK` | `32768` |
| `FORCE_SPELL_AMPLIFICATION` | `65536` |
| `MAGIC_AUTO_ATTACK` | `131072` |
| `ATTACK_MODIFIER` | `262144` |
| `BYPASSES_ALL_BLOCK` | `524288` |
| `NO_REFLECTION` | `1048576` |

### DamageTypes

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `PHYSICAL` | `1` |
| `MAGICAL` | `2` |
| `PURE` | `4` |
| `ALL` | `7` |
| `HP_REMOVAL` | `8` |
| `ABILITY_DEFINED` | `16` |

### DefaultUiElement

| Member | Value |
| --- | --- |
| `INVALID` | `-1` |
| `TOP_TIMEOFDAY` | `0` |
| `TOP_HEROES` | `1` |
| `FLYOUT_SCOREBOARD` | `2` |
| `ACTION_PANEL` | `3` |
| `ACTION_MINIMAP` | `4` |
| `INVENTORY_PANEL` | `5` |
| `INVENTORY_SHOP` | `6` |
| `INVENTORY_ITEMS` | `7` |
| `INVENTORY_QUICKBUY` | `8` |
| `INVENTORY_COURIER` | `9` |
| `INVENTORY_PROTECT` | `10` |
| `INVENTORY_GOLD` | `11` |
| `SHOP_SUGGESTEDITEMS` | `12` |
| `SHOP_COMMONITEMS` | `13` |
| `HERO_SELECTION_TEAMS` | `14` |
| `HERO_SELECTION_GAME_NAME` | `15` |
| `HERO_SELECTION_CLOCK` | `16` |
| `HERO_SELECTION_HEADER` | `17` |
| `TOP_MENU_BUTTONS` | `18` |
| `TOP_BAR_BACKGROUND` | `19` |
| `TOP_BAR_RADIANT_TEAM` | `20` |
| `TOP_BAR_DIRE_TEAM` | `21` |
| `TOP_BAR_SCORE` | `22` |
| `ENDGAME` | `23` |
| `ENDGAME_CHAT` | `24` |
| `QUICK_STATS` | `25` |
| `PREGAME_STRATEGYUI` | `26` |
| `KILLCAM` | `27` |
| `FIGHT_RECAP` | `28` |
| `TOP_BAR` | `29` |
| `CUSTOMUI_BEHIND_HUD_ELEMENTS` | `30` |
| `AGHANIMS_STATUS` | `31` |

### DotaTeam

| Member | Value |
| --- | --- |
| `GOODGUYS` | `2` |
| `BADGUYS` | `3` |
| `NEUTRALS` | `4` |
| `NOTEAM` | `5` |
| `CUSTOM_1` | `6` |
| `CUSTOM_2` | `7` |
| `CUSTOM_3` | `8` |
| `CUSTOM_4` | `9` |
| `CUSTOM_5` | `10` |
| `CUSTOM_6` | `11` |
| `CUSTOM_7` | `12` |
| `CUSTOM_8` | `13` |
| `DRAFT_POOL` | `14` |

### EntityEffects

| Member | Value |
| --- | --- |
| `EF_NODRAW` | `32` |

### EntityThinkPhase

| Member | Value |
| --- | --- |
| `RESIM` | `0` |
| `RESENSING` | `1` |
| `OSTSENSING` | `2` |

### FindOrder

| Member | Value |
| --- | --- |
| `ANY` | `0` |
| `CLOSEST` | `1` |
| `FARTHEST` | `2` |

### GameActivity

| Member | Value |
| --- | --- |
| `RESET` | `0` |
| `IDLE` | `1` |
| `TRANSITION` | `2` |
| `COVER` | `3` |
| `COVER_MED` | `4` |
| `COVER_LOW` | `5` |
| `WALK` | `6` |
| `WALK_AIM` | `7` |
| `WALK_CROUCH` | `8` |
| `WALK_CROUCH_AIM` | `9` |
| `RUN` | `10` |
| `RUN_AIM` | `11` |
| `RUN_CROUCH` | `12` |
| `RUN_CROUCH_AIM` | `13` |
| `RUN_PROTECTED` | `14` |
| `SCRIPT_CUSTOM_MOVE` | `15` |
| `RANGE_ATTACK_1` | `16` |
| `RANGE_ATTACK_2` | `17` |
| `RANGE_ATTACK_1_LOW` | `18` |
| `RANGE_ATTACK_2_LOW` | `19` |
| `DIESIMPLE` | `20` |
| `DIEBACKWARD` | `21` |
| `DIEFORWARD` | `22` |
| `DIEVIOLENT` | `23` |
| `DIERAGDOLL` | `24` |
| `FLY` | `25` |
| `HOVER` | `26` |
| `GLIDE` | `27` |
| `SWIM` | `28` |
| `JUMP` | `29` |
| `HOP` | `30` |
| `LEAP` | `31` |
| `LAND` | `32` |
| `CLIMB_UP` | `33` |
| `CLIMB_DOWN` | `34` |
| `CLIMB_DISMOUNT` | `35` |
| `SHIPLADDER_UP` | `36` |
| `SHIPLADDER_DOWN` | `37` |
| `STRAFE_LEFT` | `38` |
| `STRAFE_RIGHT` | `39` |
| `ROLL_LEFT` | `40` |
| `ROLL_RIGHT` | `41` |
| `TURN_LEFT` | `42` |
| `TURN_RIGHT` | `43` |
| `CROUCH` | `44` |
| `CROUCHIDLE` | `45` |
| `STAND` | `46` |
| `USE` | `47` |
| `ALIEN_BURROW_IDLE` | `48` |
| `ALIEN_BURROW_OUT` | `49` |
| `SIGNAL_1` | `50` |
| `SIGNAL_2` | `51` |
| `SIGNAL_3` | `52` |
| `SIGNAL_ADVANCE` | `53` |
| `SIGNAL_FORWARD` | `54` |
| `SIGNAL_GROUP` | `55` |
| `SIGNAL_HALT` | `56` |
| `SIGNAL_LEFT` | `57` |
| `SIGNAL_RIGHT` | `58` |
| `SIGNAL_TAKECOVER` | `59` |
| `LOOKBACK_RIGHT` | `60` |
| `LOOKBACK_LEFT` | `61` |
| `COWER` | `62` |
| `SMALL_FLINCH` | `63` |
| `BIG_FLINCH` | `64` |
| `MELEE_ATTACK_1` | `65` |
| `MELEE_ATTACK_2` | `66` |
| `RELOAD` | `67` |
| `RELOAD_START` | `68` |
| `RELOAD_FINISH` | `69` |
| `RELOAD_LOW` | `70` |
| `ARM` | `71` |
| `DISARM` | `72` |
| `DROP_WEAPON` | `73` |
| `DROP_WEAPON_SHOTGUN` | `74` |
| `PICKUP_GROUND` | `75` |
| `PICKUP_RACK` | `76` |
| `IDLE_ANGRY` | `77` |
| `IDLE_RELAXED` | `78` |
| `IDLE_STIMULATED` | `79` |
| `IDLE_AGITATED` | `80` |
| `IDLE_STEALTH` | `81` |
| `IDLE_HURT` | `82` |
| `WALK_RELAXED` | `83` |
| `WALK_STIMULATED` | `84` |
| `WALK_AGITATED` | `85` |
| `WALK_STEALTH` | `86` |
| `RUN_RELAXED` | `87` |
| `RUN_STIMULATED` | `88` |
| `RUN_AGITATED` | `89` |
| `RUN_STEALTH` | `90` |
| `IDLE_AIM_RELAXED` | `91` |
| `IDLE_AIM_STIMULATED` | `92` |
| `IDLE_AIM_AGITATED` | `93` |
| `IDLE_AIM_STEALTH` | `94` |
| `WALK_AIM_RELAXED` | `95` |
| `WALK_AIM_STIMULATED` | `96` |
| `WALK_AIM_AGITATED` | `97` |
| `WALK_AIM_STEALTH` | `98` |
| `RUN_AIM_RELAXED` | `99` |
| `RUN_AIM_STIMULATED` | `100` |
| `RUN_AIM_AGITATED` | `101` |
| `RUN_AIM_STEALTH` | `102` |
| `CROUCHIDLE_STIMULATED` | `103` |
| `CROUCHIDLE_AIM_STIMULATED` | `104` |
| `CROUCHIDLE_AGITATED` | `105` |
| `WALK_HURT` | `106` |
| `RUN_HURT` | `107` |
| `SPECIAL_ATTACK_1` | `108` |
| `SPECIAL_ATTACK_2` | `109` |
| `COMBAT_IDLE` | `110` |
| `WALK_SCARED` | `111` |
| `RUN_SCARED` | `112` |
| `VICTORY_DANCE` | `113` |
| `DIE_HEADSHOT` | `114` |
| `DIE_CHESTSHOT` | `115` |
| `DIE_GUTSHOT` | `116` |
| `DIE_BACKSHOT` | `117` |
| `FLINCH_HEAD` | `118` |
| `FLINCH_CHEST` | `119` |
| `FLINCH_STOMACH` | `120` |
| `FLINCH_LEFTARM` | `121` |
| `FLINCH_RIGHTARM` | `122` |
| `FLINCH_LEFTLEG` | `123` |
| `FLINCH_RIGHTLEG` | `124` |
| `FLINCH_PHYSICS` | `125` |
| `FLINCH_HEAD_BACK` | `126` |
| `FLINCH_CHEST_BACK` | `127` |
| `FLINCH_STOMACH_BACK` | `128` |
| `FLINCH_CROUCH_FRONT` | `129` |
| `FLINCH_CROUCH_BACK` | `130` |
| `FLINCH_CROUCH_LEFT` | `131` |
| `FLINCH_CROUCH_RIGHT` | `132` |
| `IDLE_ON_FIRE` | `133` |
| `WALK_ON_FIRE` | `134` |
| `RUN_ON_FIRE` | `135` |
| `STEP_LEFT` | `141` |
| `STEP_RIGHT` | `142` |
| `STEP_BACK` | `143` |
| `STEP_FORE` | `144` |
| `GESTURE_RANGE_ATTACK_1` | `145` |
| `GESTURE_RANGE_ATTACK_2` | `146` |
| `GESTURE_MELEE_ATTACK_1` | `147` |
| `GESTURE_MELEE_ATTACK_2` | `148` |
| `GESTURE_RANGE_ATTACK_1_LOW` | `149` |
| `GESTURE_RANGE_ATTACK_2_LOW` | `150` |
| `MELEE_ATTACK_SWING_GESTURE` | `151` |
| `GESTURE_SMALL_FLINCH` | `152` |
| `GESTURE_BIG_FLINCH` | `153` |
| `GESTURE_FLINCH_BLAST` | `154` |
| `GESTURE_FLINCH_BLAST_SHOTGUN` | `155` |
| `GESTURE_FLINCH_BLAST_DAMAGED` | `156` |
| `GESTURE_FLINCH_BLAST_DAMAGED_SHOTGUN` | `157` |
| `GESTURE_FLINCH_HEAD` | `158` |
| `GESTURE_FLINCH_CHEST` | `159` |
| `GESTURE_FLINCH_STOMACH` | `160` |
| `GESTURE_FLINCH_LEFTARM` | `161` |
| `GESTURE_FLINCH_RIGHTARM` | `162` |
| `GESTURE_FLINCH_LEFTLEG` | `163` |
| `GESTURE_FLINCH_RIGHTLEG` | `164` |
| `GESTURE_TURN_LEFT` | `165` |
| `GESTURE_TURN_RIGHT` | `166` |
| `GESTURE_TURN_LEFT_45` | `167` |
| `GESTURE_TURN_RIGHT_45` | `168` |
| `GESTURE_TURN_LEFT_90` | `169` |
| `GESTURE_TURN_RIGHT_90` | `170` |
| `GESTURE_TURN_LEFT_45_FLAT` | `171` |
| `GESTURE_TURN_RIGHT_45_FLAT` | `172` |
| `GESTURE_TURN_LEFT_90_FLAT` | `173` |
| `GESTURE_TURN_RIGHT_90_FLAT` | `174` |
| `BARNACLE_HIT` | `175` |
| `BARNACLE_PULL` | `176` |
| `BARNACLE_CHOMP` | `177` |
| `BARNACLE_CHEW` | `178` |
| `DO_NOT_DISTURB` | `179` |
| `SPECIFIC_SEQUENCE` | `180` |
| `VM_DEPLOY` | `181` |
| `VM_RELOAD_EMPTY` | `182` |
| `VM_DRAW` | `183` |
| `VM_HOLSTER` | `184` |
| `VM_IDLE` | `185` |
| `VM_FIDGET` | `186` |
| `VM_PULLBACK` | `187` |
| `VM_PULLBACK_HIGH` | `188` |
| `VM_PULLBACK_LOW` | `189` |
| `VM_THROW` | `190` |
| `VM_DROP` | `191` |
| `VM_PULLPIN` | `192` |
| `VM_PRIMARYATTACK` | `193` |
| `VM_SECONDARYATTACK` | `194` |
| `VM_RELOAD` | `195` |
| `VM_DRYFIRE` | `196` |
| `VM_HITLEFT` | `197` |
| `VM_HITLEFT_2` | `198` |
| `VM_HITRIGHT` | `199` |
| `VM_HITRIGHT_2` | `200` |
| `VM_HITCENTER` | `201` |
| `VM_HITCENTER_2` | `202` |
| `VM_MISSLEFT` | `203` |
| `VM_MISSLEFT_2` | `204` |
| `VM_MISSRIGHT` | `205` |
| `VM_MISSRIGHT_2` | `206` |
| `VM_MISSCENTER` | `207` |
| `VM_MISSCENTER_2` | `208` |
| `VM_HAULBACK` | `209` |
| `VM_SWINGHARD` | `210` |
| `VM_SWINGMISS` | `211` |
| `VM_SWINGHIT` | `212` |
| `VM_IDLE_TO_LOWERED` | `213` |
| `VM_IDLE_LOWERED` | `214` |
| `VM_LOWERED_TO_IDLE` | `215` |
| `VM_RECOIL_1` | `216` |
| `VM_RECOIL_2` | `217` |
| `VM_RECOIL_3` | `218` |
| `VM_PICKUP` | `219` |
| `VM_RELEASE` | `220` |
| `VM_MAUL_LOOP` | `221` |
| `VM_ATTACH_SILENCER` | `222` |
| `VM_DETACH_SILENCER` | `223` |
| `SLAM_STICKWALL_IDLE` | `224` |
| `SLAM_STICKWALL_ND_IDLE` | `225` |
| `SLAM_STICKWALL_ATTACH` | `226` |
| `SLAM_STICKWALL_ATTACH_2` | `227` |
| `SLAM_STICKWALL_ND_ATTACH` | `228` |
| `SLAM_STICKWALL_ND_ATTACH_2` | `229` |
| `SLAM_STICKWALL_DETONATE` | `230` |
| `SLAM_STICKWALL_DETONATOR_HOLSTER` | `231` |
| `SLAM_STICKWALL_DRAW` | `232` |
| `SLAM_STICKWALL_ND_DRAW` | `233` |
| `SLAM_STICKWALL_TO_THROW` | `234` |
| `SLAM_STICKWALL_TO_THROW_ND` | `235` |
| `SLAM_STICKWALL_TO_TRIPMINE_ND` | `236` |
| `SLAM_THROW_IDLE` | `237` |
| `SLAM_THROW_ND_IDLE` | `238` |
| `SLAM_THROW_THROW` | `239` |
| `SLAM_THROW_THROW_2` | `240` |
| `SLAM_THROW_THROW_ND` | `241` |
| `SLAM_THROW_THROW_ND_2` | `242` |
| `SLAM_THROW_DRAW` | `243` |
| `SLAM_THROW_ND_DRAW` | `244` |
| `SLAM_THROW_TO_STICKWALL` | `245` |
| `SLAM_THROW_TO_STICKWALL_ND` | `246` |
| `SLAM_THROW_DETONATE` | `247` |
| `SLAM_THROW_DETONATOR_HOLSTER` | `248` |
| `SLAM_THROW_TO_TRIPMINE_ND` | `249` |
| `SLAM_TRIPMINE_IDLE` | `250` |
| `SLAM_TRIPMINE_DRAW` | `251` |
| `SLAM_TRIPMINE_ATTACH` | `252` |
| `SLAM_TRIPMINE_ATTACH_2` | `253` |
| `SLAM_TRIPMINE_TO_STICKWALL_ND` | `254` |
| `SLAM_TRIPMINE_TO_THROW_ND` | `255` |
| `SLAM_DETONATOR_IDLE` | `256` |
| `SLAM_DETONATOR_DRAW` | `257` |
| `SLAM_DETONATOR_DETONATE` | `258` |
| `SLAM_DETONATOR_HOLSTER` | `259` |
| `SLAM_DETONATOR_STICKWALL_DRAW` | `260` |
| `SLAM_DETONATOR_THROW_DRAW` | `261` |
| `SHOTGUN_RELOAD_START` | `262` |
| `SHOTGUN_RELOAD_FINISH` | `263` |
| `SHOTGUN_PUMP` | `264` |
| `SMG_2_IDLE_2` | `265` |
| `SMG_2_FIRE_2` | `266` |
| `SMG_2_DRAW_2` | `267` |
| `SMG_2_RELOAD_2` | `268` |
| `SMG_2_DRYFIRE_2` | `269` |
| `SMG_2_TOAUTO` | `270` |
| `SMG_2_TOBURST` | `271` |
| `PHYSCANNON_UPGRADE` | `272` |
| `RANGE_ATTACK_AR_1` | `273` |
| `RANGE_ATTACK_AR_2` | `274` |
| `RANGE_ATTACK_AR_2_LOW` | `275` |
| `RANGE_ATTACK_AR_2_GRENADE` | `276` |
| `RANGE_ATTACK_HMG_1` | `277` |
| `RANGE_ATTACK_ML` | `278` |
| `RANGE_ATTACK_SMG_1` | `279` |
| `RANGE_ATTACK_SMG_1_LOW` | `280` |
| `RANGE_ATTACK_SMG_2` | `281` |
| `RANGE_ATTACK_SHOTGUN` | `282` |
| `RANGE_ATTACK_SHOTGUN_LOW` | `283` |
| `RANGE_ATTACK_PISTOL` | `284` |
| `RANGE_ATTACK_PISTOL_LOW` | `285` |
| `RANGE_ATTACK_SLAM` | `286` |
| `RANGE_ATTACK_TRIPWIRE` | `287` |
| `RANGE_ATTACK_THROW` | `288` |
| `RANGE_ATTACK_SNIPER_RIFLE` | `289` |
| `RANGE_ATTACK_RPG` | `290` |
| `MELEE_ATTACK_SWING` | `291` |
| `RANGE_AIM_LOW` | `292` |
| `RANGE_AIM_SMG_1_LOW` | `293` |
| `RANGE_AIM_PISTOL_LOW` | `294` |
| `RANGE_AIM_AR_2_LOW` | `295` |
| `COVER_PISTOL_LOW` | `296` |
| `COVER_SMG_1_LOW` | `297` |
| `GESTURE_RANGE_ATTACK_AR_1` | `298` |
| `GESTURE_RANGE_ATTACK_AR_2` | `299` |
| `GESTURE_RANGE_ATTACK_AR_2_GRENADE` | `300` |
| `GESTURE_RANGE_ATTACK_HMG_1` | `301` |
| `GESTURE_RANGE_ATTACK_ML` | `302` |
| `GESTURE_RANGE_ATTACK_SMG_1` | `303` |
| `GESTURE_RANGE_ATTACK_SMG_1_LOW` | `304` |
| `GESTURE_RANGE_ATTACK_SMG_2` | `305` |
| `GESTURE_RANGE_ATTACK_SHOTGUN` | `306` |
| `GESTURE_RANGE_ATTACK_PISTOL` | `307` |
| `GESTURE_RANGE_ATTACK_PISTOL_LOW` | `308` |
| `GESTURE_RANGE_ATTACK_SLAM` | `309` |
| `GESTURE_RANGE_ATTACK_TRIPWIRE` | `310` |
| `GESTURE_RANGE_ATTACK_THROW` | `311` |
| `GESTURE_RANGE_ATTACK_SNIPER_RIFLE` | `312` |
| `GESTURE_MELEE_ATTACK_SWING` | `313` |
| `IDLE_RIFLE` | `314` |
| `IDLE_SMG_1` | `315` |
| `IDLE_ANGRY_SMG_1` | `316` |
| `IDLE_PISTOL` | `317` |
| `IDLE_ANGRY_PISTOL` | `318` |
| `IDLE_ANGRY_SHOTGUN` | `319` |
| `IDLE_STEALTH_PISTOL` | `320` |
| `IDLE_PACKAGE` | `321` |
| `WALK_PACKAGE` | `322` |
| `IDLE_SUITCASE` | `323` |
| `WALK_SUITCASE` | `324` |
| `IDLE_SMG_1_RELAXED` | `325` |
| `IDLE_SMG_1_STIMULATED` | `326` |
| `WALK_RIFLE_RELAXED` | `327` |
| `RUN_RIFLE_RELAXED` | `328` |
| `WALK_RIFLE_STIMULATED` | `329` |
| `RUN_RIFLE_STIMULATED` | `330` |
| `IDLE_AIM_RIFLE_STIMULATED` | `331` |
| `WALK_AIM_RIFLE_STIMULATED` | `332` |
| `RUN_AIM_RIFLE_STIMULATED` | `333` |
| `IDLE_SHOTGUN_RELAXED` | `334` |
| `IDLE_SHOTGUN_STIMULATED` | `335` |
| `IDLE_SHOTGUN_AGITATED` | `336` |
| `WALK_ANGRY` | `337` |
| `POLICE_HARASS_1` | `338` |
| `POLICE_HARASS_2` | `339` |
| `IDLE_MANNEDGUN` | `340` |
| `IDLE_MELEE` | `341` |
| `IDLE_ANGRY_MELEE` | `342` |
| `IDLE_RPG_RELAXED` | `343` |
| `IDLE_RPG` | `344` |
| `IDLE_ANGRY_RPG` | `345` |
| `COVER_LOW_RPG` | `346` |
| `WALK_RPG` | `347` |
| `RUN_RPG` | `348` |
| `WALK_CROUCH_RPG` | `349` |
| `RUN_CROUCH_RPG` | `350` |
| `WALK_RPG_RELAXED` | `351` |
| `RUN_RPG_RELAXED` | `352` |
| `WALK_RIFLE` | `353` |
| `WALK_AIM_RIFLE` | `354` |
| `WALK_CROUCH_RIFLE` | `355` |
| `WALK_CROUCH_AIM_RIFLE` | `356` |
| `RUN_RIFLE` | `357` |
| `RUN_AIM_RIFLE` | `358` |
| `RUN_CROUCH_RIFLE` | `359` |
| `RUN_CROUCH_AIM_RIFLE` | `360` |
| `RUN_STEALTH_PISTOL` | `361` |
| `WALK_AIM_SHOTGUN` | `362` |
| `RUN_AIM_SHOTGUN` | `363` |
| `WALK_PISTOL` | `364` |
| `RUN_PISTOL` | `365` |
| `WALK_AIM_PISTOL` | `366` |
| `RUN_AIM_PISTOL` | `367` |
| `WALK_STEALTH_PISTOL` | `368` |
| `WALK_AIM_STEALTH_PISTOL` | `369` |
| `RUN_AIM_STEALTH_PISTOL` | `370` |
| `RELOAD_PISTOL` | `371` |
| `RELOAD_PISTOL_LOW` | `372` |
| `RELOAD_SMG_1` | `373` |
| `RELOAD_SMG_1_LOW` | `374` |
| `RELOAD_SHOTGUN` | `375` |
| `RELOAD_SHOTGUN_LOW` | `376` |
| `GESTURE_RELOAD` | `377` |
| `GESTURE_RELOAD_PISTOL` | `378` |
| `GESTURE_RELOAD_SMG_1` | `379` |
| `GESTURE_RELOAD_SHOTGUN` | `380` |
| `BUSY_LEAN_LEFT` | `381` |
| `BUSY_LEAN_LEFT_ENTRY` | `382` |
| `BUSY_LEAN_LEFT_EXIT` | `383` |
| `BUSY_LEAN_BACK` | `384` |
| `BUSY_LEAN_BACK_ENTRY` | `385` |
| `BUSY_LEAN_BACK_EXIT` | `386` |
| `BUSY_SIT_GROUND` | `387` |
| `BUSY_SIT_GROUND_ENTRY` | `388` |
| `BUSY_SIT_GROUND_EXIT` | `389` |
| `BUSY_SIT_CHAIR` | `390` |
| `BUSY_SIT_CHAIR_ENTRY` | `391` |
| `BUSY_SIT_CHAIR_EXIT` | `392` |
| `BUSY_STAND` | `393` |
| `BUSY_QUEUE` | `394` |
| `DUCK_DODGE` | `395` |
| `DIE_BARNACLE_SWALLOW` | `396` |
| `GESTURE_BARNACLE_STRANGLE` | `397` |
| `DIE_FRONTSIDE` | `402` |
| `DIE_RIGHTSIDE` | `403` |
| `DIE_BACKSIDE` | `404` |
| `DIE_LEFTSIDE` | `405` |
| `DIE_CROUCH_FRONTSIDE` | `406` |
| `DIE_CROUCH_RIGHTSIDE` | `407` |
| `DIE_CROUCH_BACKSIDE` | `408` |
| `DIE_CROUCH_LEFTSIDE` | `409` |
| `DIE_INCAP` | `410` |
| `DIE_STANDING` | `411` |
| `OPEN_DOOR` | `412` |
| `DI_ALYX_ZOMBIE_MELEE` | `413` |
| `DI_ALYX_ZOMBIE_TORSO_MELEE` | `414` |
| `DI_ALYX_HEADCRAB_MELEE` | `415` |
| `DI_ALYX_ANTLION` | `416` |
| `DI_ALYX_ZOMBIE_SHOTGUN_64` | `417` |
| `DI_ALYX_ZOMBIE_SHOTGUN_26` | `418` |
| `READINESS_RELAXED_TO_STIMULATED` | `419` |
| `READINESS_RELAXED_TO_STIMULATED_WALK` | `420` |
| `READINESS_AGITATED_TO_STIMULATED` | `421` |
| `READINESS_STIMULATED_TO_RELAXED` | `422` |
| `READINESS_PISTOL_RELAXED_TO_STIMULATED` | `423` |
| `READINESS_PISTOL_RELAXED_TO_STIMULATED_WALK` | `424` |
| `READINESS_PISTOL_AGITATED_TO_STIMULATED` | `425` |
| `READINESS_PISTOL_STIMULATED_TO_RELAXED` | `426` |
| `IDLE_CARRY` | `427` |
| `WALK_CARRY` | `428` |
| `STARTDYING` | `429` |
| `DYINGLOOP` | `430` |
| `DYINGTODEAD` | `431` |
| `RIDE_MANNED_GUN` | `432` |
| `VM_SPRINT_ENTER` | `433` |
| `VM_SPRINT_IDLE` | `434` |
| `VM_SPRINT_LEAVE` | `435` |
| `FIRE_START` | `436` |
| `FIRE_LOOP` | `437` |
| `FIRE_END` | `438` |
| `CROUCHING_GRENADEIDLE` | `439` |
| `CROUCHING_GRENADEREADY` | `440` |
| `CROUCHING_PRIMARYATTACK` | `441` |
| `OVERLAY_GRENADEIDLE` | `442` |
| `OVERLAY_GRENADEREADY` | `443` |
| `OVERLAY_PRIMARYATTACK` | `444` |
| `OVERLAY_SHIELD_UP` | `445` |
| `OVERLAY_SHIELD_DOWN` | `446` |
| `OVERLAY_SHIELD_UP_IDLE` | `447` |
| `OVERLAY_SHIELD_ATTACK` | `448` |
| `OVERLAY_SHIELD_KNOCKBACK` | `449` |
| `SHIELD_UP` | `450` |
| `SHIELD_DOWN` | `451` |
| `SHIELD_UP_IDLE` | `452` |
| `SHIELD_ATTACK` | `453` |
| `SHIELD_KNOCKBACK` | `454` |
| `CROUCHING_SHIELD_UP` | `455` |
| `CROUCHING_SHIELD_DOWN` | `456` |
| `CROUCHING_SHIELD_UP_IDLE` | `457` |
| `CROUCHING_SHIELD_ATTACK` | `458` |
| `CROUCHING_SHIELD_KNOCKBACK` | `459` |
| `TURNRIGHT_45` | `460` |
| `TURNLEFT_45` | `461` |
| `TURN` | `462` |
| `OBJ_ASSEMBLING` | `463` |
| `OBJ_DISMANTLING` | `464` |
| `OBJ_STARTUP` | `465` |
| `OBJ_RUNNING` | `466` |
| `OBJ_IDLE` | `467` |
| `OBJ_PLACING` | `468` |
| `OBJ_DETERIORATING` | `469` |
| `OBJ_UPGRADING` | `470` |
| `DEPLOY` | `471` |
| `DEPLOY_IDLE` | `472` |
| `UNDEPLOY` | `473` |
| `CROSSBOW_DRAW_UNLOADED` | `474` |
| `GAUSS_SPINUP` | `475` |
| `GAUSS_SPINCYCLE` | `476` |
| `VM_PRIMARYATTACK_SILENCED` | `477` |
| `VM_RELOAD_SILENCED` | `478` |
| `VM_DRYFIRE_SILENCED` | `479` |
| `VM_IDLE_SILENCED` | `480` |
| `VM_DRAW_SILENCED` | `481` |
| `VM_IDLE_EMPTY_LEFT` | `482` |
| `VM_DRYFIRE_LEFT` | `483` |
| `VM_IS_DRAW` | `484` |
| `VM_IS_HOLSTER` | `485` |
| `VM_IS_IDLE` | `486` |
| `VM_IS_PRIMARYATTACK` | `487` |
| `PLAYER_IDLE_FIRE` | `488` |
| `PLAYER_CROUCH_FIRE` | `489` |
| `PLAYER_CROUCH_WALK_FIRE` | `490` |
| `PLAYER_WALK_FIRE` | `491` |
| `PLAYER_RUN_FIRE` | `492` |
| `IDLETORUN` | `493` |
| `RUNTOIDLE` | `494` |
| `VM_DRAW_DEPLOYED` | `495` |
| `HL_2_MP_IDLE_MELEE` | `496` |
| `HL_2_MP_RUN_MELEE` | `497` |
| `HL_2_MP_IDLE_CROUCH_MELEE` | `498` |
| `HL_2_MP_WALK_CROUCH_MELEE` | `499` |
| `HL_2_MP_GESTURE_RANGE_ATTACK_MELEE` | `500` |
| `HL_2_MP_GESTURE_RELOAD_MELEE` | `501` |
| `HL_2_MP_JUMP_MELEE` | `502` |
| `MP_STAND_IDLE` | `503` |
| `MP_CROUCH_IDLE` | `504` |
| `MP_CROUCH_DEPLOYED_IDLE` | `505` |
| `MP_CROUCH_DEPLOYED` | `506` |
| `MP_DEPLOYED_IDLE` | `507` |
| `MP_RUN` | `508` |
| `MP_WALK` | `509` |
| `MP_AIRWALK` | `510` |
| `MP_CROUCHWALK` | `511` |
| `MP_SPRINT` | `512` |
| `MP_JUMP` | `513` |
| `MP_JUMP_START` | `514` |
| `MP_JUMP_FLOAT` | `515` |
| `MP_JUMP_LAND` | `516` |
| `MP_DOUBLEJUMP` | `517` |
| `MP_SWIM` | `518` |
| `MP_DEPLOYED` | `519` |
| `MP_SWIM_DEPLOYED` | `520` |
| `MP_VCD` | `521` |
| `MP_ATTACK_STAND_PRIMARYFIRE` | `522` |
| `MP_ATTACK_STAND_PRIMARYFIRE_DEPLOYED` | `523` |
| `MP_ATTACK_STAND_SECONDARYFIRE` | `524` |
| `MP_ATTACK_STAND_GRENADE` | `525` |
| `MP_ATTACK_CROUCH_PRIMARYFIRE` | `526` |
| `MP_ATTACK_CROUCH_PRIMARYFIRE_DEPLOYED` | `527` |
| `MP_ATTACK_CROUCH_SECONDARYFIRE` | `528` |
| `MP_ATTACK_CROUCH_GRENADE` | `529` |
| `MP_ATTACK_SWIM_PRIMARYFIRE` | `530` |
| `MP_ATTACK_SWIM_SECONDARYFIRE` | `531` |
| `MP_ATTACK_SWIM_GRENADE` | `532` |
| `MP_ATTACK_AIRWALK_PRIMARYFIRE` | `533` |
| `MP_ATTACK_AIRWALK_SECONDARYFIRE` | `534` |
| `MP_ATTACK_AIRWALK_GRENADE` | `535` |
| `MP_RELOAD_STAND` | `536` |
| `MP_RELOAD_STAND_LOOP` | `537` |
| `MP_RELOAD_STAND_END` | `538` |
| `MP_RELOAD_CROUCH` | `539` |
| `MP_RELOAD_CROUCH_LOOP` | `540` |
| `MP_RELOAD_CROUCH_END` | `541` |
| `MP_RELOAD_SWIM` | `542` |
| `MP_RELOAD_SWIM_LOOP` | `543` |
| `MP_RELOAD_SWIM_END` | `544` |
| `MP_RELOAD_AIRWALK` | `545` |
| `MP_RELOAD_AIRWALK_LOOP` | `546` |
| `MP_RELOAD_AIRWALK_END` | `547` |
| `MP_ATTACK_STAND_PREFIRE` | `548` |
| `MP_ATTACK_STAND_POSTFIRE` | `549` |
| `MP_ATTACK_STAND_STARTFIRE` | `550` |
| `MP_ATTACK_CROUCH_PREFIRE` | `551` |
| `MP_ATTACK_CROUCH_POSTFIRE` | `552` |
| `MP_ATTACK_SWIM_PREFIRE` | `553` |
| `MP_ATTACK_SWIM_POSTFIRE` | `554` |
| `MP_STAND_PRIMARY` | `555` |
| `MP_CROUCH_PRIMARY` | `556` |
| `MP_RUN_PRIMARY` | `557` |
| `MP_WALK_PRIMARY` | `558` |
| `MP_AIRWALK_PRIMARY` | `559` |
| `MP_CROUCHWALK_PRIMARY` | `560` |
| `MP_JUMP_PRIMARY` | `561` |
| `MP_JUMP_START_PRIMARY` | `562` |
| `MP_JUMP_FLOAT_PRIMARY` | `563` |
| `MP_JUMP_LAND_PRIMARY` | `564` |
| `MP_SWIM_PRIMARY` | `565` |
| `MP_DEPLOYED_PRIMARY` | `566` |
| `MP_SWIM_DEPLOYED_PRIMARY` | `567` |
| `MP_ATTACK_STAND_PRIMARY` | `568` |
| `MP_ATTACK_STAND_PRIMARY_DEPLOYED` | `569` |
| `MP_ATTACK_CROUCH_PRIMARY` | `570` |
| `MP_ATTACK_CROUCH_PRIMARY_DEPLOYED` | `571` |
| `MP_ATTACK_SWIM_PRIMARY` | `572` |
| `MP_ATTACK_AIRWALK_PRIMARY` | `573` |
| `MP_RELOAD_STAND_PRIMARY` | `574` |
| `MP_RELOAD_STAND_PRIMARY_LOOP` | `575` |
| `MP_RELOAD_STAND_PRIMARY_END` | `576` |
| `MP_RELOAD_CROUCH_PRIMARY` | `577` |
| `MP_RELOAD_CROUCH_PRIMARY_LOOP` | `578` |
| `MP_RELOAD_CROUCH_PRIMARY_END` | `579` |
| `MP_RELOAD_SWIM_PRIMARY` | `580` |
| `MP_RELOAD_SWIM_PRIMARY_LOOP` | `581` |
| `MP_RELOAD_SWIM_PRIMARY_END` | `582` |
| `MP_RELOAD_AIRWALK_PRIMARY` | `583` |
| `MP_RELOAD_AIRWALK_PRIMARY_LOOP` | `584` |
| `MP_RELOAD_AIRWALK_PRIMARY_END` | `585` |
| `MP_ATTACK_STAND_GRENADE_PRIMARY` | `586` |
| `MP_ATTACK_CROUCH_GRENADE_PRIMARY` | `587` |
| `MP_ATTACK_SWIM_GRENADE_PRIMARY` | `588` |
| `MP_ATTACK_AIRWALK_GRENADE_PRIMARY` | `589` |
| `MP_STAND_SECONDARY` | `590` |
| `MP_CROUCH_SECONDARY` | `591` |
| `MP_RUN_SECONDARY` | `592` |
| `MP_WALK_SECONDARY` | `593` |
| `MP_AIRWALK_SECONDARY` | `594` |
| `MP_CROUCHWALK_SECONDARY` | `595` |
| `MP_JUMP_SECONDARY` | `596` |
| `MP_JUMP_START_SECONDARY` | `597` |
| `MP_JUMP_FLOAT_SECONDARY` | `598` |
| `MP_JUMP_LAND_SECONDARY` | `599` |
| `MP_SWIM_SECONDARY` | `600` |
| `MP_ATTACK_STAND_SECONDARY` | `601` |
| `MP_ATTACK_CROUCH_SECONDARY` | `602` |
| `MP_ATTACK_SWIM_SECONDARY` | `603` |
| `MP_ATTACK_AIRWALK_SECONDARY` | `604` |
| `MP_RELOAD_STAND_SECONDARY` | `605` |
| `MP_RELOAD_STAND_SECONDARY_LOOP` | `606` |
| `MP_RELOAD_STAND_SECONDARY_END` | `607` |
| `MP_RELOAD_CROUCH_SECONDARY` | `608` |
| `MP_RELOAD_CROUCH_SECONDARY_LOOP` | `609` |
| `MP_RELOAD_CROUCH_SECONDARY_END` | `610` |
| `MP_RELOAD_SWIM_SECONDARY` | `611` |
| `MP_RELOAD_SWIM_SECONDARY_LOOP` | `612` |
| `MP_RELOAD_SWIM_SECONDARY_END` | `613` |
| `MP_RELOAD_AIRWALK_SECONDARY` | `614` |
| `MP_RELOAD_AIRWALK_SECONDARY_LOOP` | `615` |
| `MP_RELOAD_AIRWALK_SECONDARY_END` | `616` |
| `MP_ATTACK_STAND_GRENADE_SECONDARY` | `617` |
| `MP_ATTACK_CROUCH_GRENADE_SECONDARY` | `618` |
| `MP_ATTACK_SWIM_GRENADE_SECONDARY` | `619` |
| `MP_ATTACK_AIRWALK_GRENADE_SECONDARY` | `620` |
| `MP_STAND_MELEE` | `621` |
| `MP_CROUCH_MELEE` | `622` |
| `MP_RUN_MELEE` | `623` |
| `MP_WALK_MELEE` | `624` |
| `MP_AIRWALK_MELEE` | `625` |
| `MP_CROUCHWALK_MELEE` | `626` |
| `MP_JUMP_MELEE` | `627` |
| `MP_JUMP_START_MELEE` | `628` |
| `MP_JUMP_FLOAT_MELEE` | `629` |
| `MP_JUMP_LAND_MELEE` | `630` |
| `MP_SWIM_MELEE` | `631` |
| `MP_ATTACK_STAND_MELEE` | `632` |
| `MP_ATTACK_STAND_MELEE_SECONDARY` | `633` |
| `MP_ATTACK_CROUCH_MELEE` | `634` |
| `MP_ATTACK_CROUCH_MELEE_SECONDARY` | `635` |
| `MP_ATTACK_SWIM_MELEE` | `636` |
| `MP_ATTACK_AIRWALK_MELEE` | `637` |
| `MP_ATTACK_STAND_GRENADE_MELEE` | `638` |
| `MP_ATTACK_CROUCH_GRENADE_MELEE` | `639` |
| `MP_ATTACK_SWIM_GRENADE_MELEE` | `640` |
| `MP_ATTACK_AIRWALK_GRENADE_MELEE` | `641` |
| `MP_STAND_ITEM_1` | `642` |
| `MP_CROUCH_ITEM_1` | `643` |
| `MP_RUN_ITEM_1` | `644` |
| `MP_WALK_ITEM_1` | `645` |
| `MP_AIRWALK_ITEM_1` | `646` |
| `MP_CROUCHWALK_ITEM_1` | `647` |
| `MP_JUMP_ITEM_1` | `648` |
| `MP_JUMP_START_ITEM_1` | `649` |
| `MP_JUMP_FLOAT_ITEM_1` | `650` |
| `MP_JUMP_LAND_ITEM_1` | `651` |
| `MP_SWIM_ITEM_1` | `652` |
| `MP_ATTACK_STAND_ITEM_1` | `653` |
| `MP_ATTACK_STAND_ITEM_1_SECONDARY` | `654` |
| `MP_ATTACK_CROUCH_ITEM_1` | `655` |
| `MP_ATTACK_CROUCH_ITEM_1_SECONDARY` | `656` |
| `MP_ATTACK_SWIM_ITEM_1` | `657` |
| `MP_ATTACK_AIRWALK_ITEM_1` | `658` |
| `MP_STAND_ITEM_2` | `659` |
| `MP_CROUCH_ITEM_2` | `660` |
| `MP_RUN_ITEM_2` | `661` |
| `MP_WALK_ITEM_2` | `662` |
| `MP_AIRWALK_ITEM_2` | `663` |
| `MP_CROUCHWALK_ITEM_2` | `664` |
| `MP_JUMP_ITEM_2` | `665` |
| `MP_JUMP_START_ITEM_2` | `666` |
| `MP_JUMP_FLOAT_ITEM_2` | `667` |
| `MP_JUMP_LAND_ITEM_2` | `668` |
| `MP_SWIM_ITEM_2` | `669` |
| `MP_ATTACK_STAND_ITEM_2` | `670` |
| `MP_ATTACK_STAND_ITEM_2_SECONDARY` | `671` |
| `MP_ATTACK_CROUCH_ITEM_2` | `672` |
| `MP_ATTACK_CROUCH_ITEM_2_SECONDARY` | `673` |
| `MP_ATTACK_SWIM_ITEM_2` | `674` |
| `MP_ATTACK_AIRWALK_ITEM_2` | `675` |
| `MP_GESTURE_FLINCH` | `676` |
| `MP_GESTURE_FLINCH_PRIMARY` | `677` |
| `MP_GESTURE_FLINCH_SECONDARY` | `678` |
| `MP_GESTURE_FLINCH_MELEE` | `679` |
| `MP_GESTURE_FLINCH_ITEM_1` | `680` |
| `MP_GESTURE_FLINCH_ITEM_2` | `681` |
| `MP_GESTURE_FLINCH_HEAD` | `682` |
| `MP_GESTURE_FLINCH_CHEST` | `683` |
| `MP_GESTURE_FLINCH_STOMACH` | `684` |
| `MP_GESTURE_FLINCH_LEFTARM` | `685` |
| `MP_GESTURE_FLINCH_RIGHTARM` | `686` |
| `MP_GESTURE_FLINCH_LEFTLEG` | `687` |
| `MP_GESTURE_FLINCH_RIGHTLEG` | `688` |
| `MP_GRENADE_1_DRAW` | `689` |
| `MP_GRENADE_1_IDLE` | `690` |
| `MP_GRENADE_1_ATTACK` | `691` |
| `MP_GRENADE_2_DRAW` | `692` |
| `MP_GRENADE_2_IDLE` | `693` |
| `MP_GRENADE_2_ATTACK` | `694` |
| `MP_PRIMARY_GRENADE_1_DRAW` | `695` |
| `MP_PRIMARY_GRENADE_1_IDLE` | `696` |
| `MP_PRIMARY_GRENADE_1_ATTACK` | `697` |
| `MP_PRIMARY_GRENADE_2_DRAW` | `698` |
| `MP_PRIMARY_GRENADE_2_IDLE` | `699` |
| `MP_PRIMARY_GRENADE_2_ATTACK` | `700` |
| `MP_SECONDARY_GRENADE_1_DRAW` | `701` |
| `MP_SECONDARY_GRENADE_1_IDLE` | `702` |
| `MP_SECONDARY_GRENADE_1_ATTACK` | `703` |
| `MP_SECONDARY_GRENADE_2_DRAW` | `704` |
| `MP_SECONDARY_GRENADE_2_IDLE` | `705` |
| `MP_SECONDARY_GRENADE_2_ATTACK` | `706` |
| `MP_MELEE_GRENADE_1_DRAW` | `707` |
| `MP_MELEE_GRENADE_1_IDLE` | `708` |
| `MP_MELEE_GRENADE_1_ATTACK` | `709` |
| `MP_MELEE_GRENADE_2_DRAW` | `710` |
| `MP_MELEE_GRENADE_2_IDLE` | `711` |
| `MP_MELEE_GRENADE_2_ATTACK` | `712` |
| `MP_ITEM_1_GRENADE_1_DRAW` | `713` |
| `MP_ITEM_1_GRENADE_1_IDLE` | `714` |
| `MP_ITEM_1_GRENADE_1_ATTACK` | `715` |
| `MP_ITEM_1_GRENADE_2_DRAW` | `716` |
| `MP_ITEM_1_GRENADE_2_IDLE` | `717` |
| `MP_ITEM_1_GRENADE_2_ATTACK` | `718` |
| `MP_ITEM_2_GRENADE_1_DRAW` | `719` |
| `MP_ITEM_2_GRENADE_1_IDLE` | `720` |
| `MP_ITEM_2_GRENADE_1_ATTACK` | `721` |
| `MP_ITEM_2_GRENADE_2_DRAW` | `722` |
| `MP_ITEM_2_GRENADE_2_IDLE` | `723` |
| `MP_ITEM_2_GRENADE_2_ATTACK` | `724` |
| `MP_STAND_BUILDING` | `725` |
| `MP_CROUCH_BUILDING` | `726` |
| `MP_RUN_BUILDING` | `727` |
| `MP_WALK_BUILDING` | `728` |
| `MP_AIRWALK_BUILDING` | `729` |
| `MP_CROUCHWALK_BUILDING` | `730` |
| `MP_JUMP_BUILDING` | `731` |
| `MP_JUMP_START_BUILDING` | `732` |
| `MP_JUMP_FLOAT_BUILDING` | `733` |
| `MP_JUMP_LAND_BUILDING` | `734` |
| `MP_SWIM_BUILDING` | `735` |
| `MP_ATTACK_STAND_BUILDING` | `736` |
| `MP_ATTACK_CROUCH_BUILDING` | `737` |
| `MP_ATTACK_SWIM_BUILDING` | `738` |
| `MP_ATTACK_AIRWALK_BUILDING` | `739` |
| `MP_ATTACK_STAND_GRENADE_BUILDING` | `740` |
| `MP_ATTACK_CROUCH_GRENADE_BUILDING` | `741` |
| `MP_ATTACK_SWIM_GRENADE_BUILDING` | `742` |
| `MP_ATTACK_AIRWALK_GRENADE_BUILDING` | `743` |
| `MP_STAND_PDA` | `744` |
| `MP_CROUCH_PDA` | `745` |
| `MP_RUN_PDA` | `746` |
| `MP_WALK_PDA` | `747` |
| `MP_AIRWALK_PDA` | `748` |
| `MP_CROUCHWALK_PDA` | `749` |
| `MP_JUMP_PDA` | `750` |
| `MP_JUMP_START_PDA` | `751` |
| `MP_JUMP_FLOAT_PDA` | `752` |
| `MP_JUMP_LAND_PDA` | `753` |
| `MP_SWIM_PDA` | `754` |
| `MP_ATTACK_STAND_PDA` | `755` |
| `MP_ATTACK_SWIM_PDA` | `756` |
| `MP_GESTURE_VC_HANDMOUTH` | `757` |
| `MP_GESTURE_VC_FINGERPOINT` | `758` |
| `MP_GESTURE_VC_FISTPUMP` | `759` |
| `MP_GESTURE_VC_THUMBSUP` | `760` |
| `MP_GESTURE_VC_NODYES` | `761` |
| `MP_GESTURE_VC_NODNO` | `762` |
| `MP_GESTURE_VC_HANDMOUTH_PRIMARY` | `763` |
| `MP_GESTURE_VC_FINGERPOINT_PRIMARY` | `764` |
| `MP_GESTURE_VC_FISTPUMP_PRIMARY` | `765` |
| `MP_GESTURE_VC_THUMBSUP_PRIMARY` | `766` |
| `MP_GESTURE_VC_NODYES_PRIMARY` | `767` |
| `MP_GESTURE_VC_NODNO_PRIMARY` | `768` |
| `MP_GESTURE_VC_HANDMOUTH_SECONDARY` | `769` |
| `MP_GESTURE_VC_FINGERPOINT_SECONDARY` | `770` |
| `MP_GESTURE_VC_FISTPUMP_SECONDARY` | `771` |
| `MP_GESTURE_VC_THUMBSUP_SECONDARY` | `772` |
| `MP_GESTURE_VC_NODYES_SECONDARY` | `773` |
| `MP_GESTURE_VC_NODNO_SECONDARY` | `774` |
| `MP_GESTURE_VC_HANDMOUTH_MELEE` | `775` |
| `MP_GESTURE_VC_FINGERPOINT_MELEE` | `776` |
| `MP_GESTURE_VC_FISTPUMP_MELEE` | `777` |
| `MP_GESTURE_VC_THUMBSUP_MELEE` | `778` |
| `MP_GESTURE_VC_NODYES_MELEE` | `779` |
| `MP_GESTURE_VC_NODNO_MELEE` | `780` |
| `MP_GESTURE_VC_HANDMOUTH_ITEM_1` | `781` |
| `MP_GESTURE_VC_FINGERPOINT_ITEM_1` | `782` |
| `MP_GESTURE_VC_FISTPUMP_ITEM_1` | `783` |
| `MP_GESTURE_VC_THUMBSUP_ITEM_1` | `784` |
| `MP_GESTURE_VC_NODYES_ITEM_1` | `785` |
| `MP_GESTURE_VC_NODNO_ITEM_1` | `786` |
| `MP_GESTURE_VC_HANDMOUTH_ITEM_2` | `787` |
| `MP_GESTURE_VC_FINGERPOINT_ITEM_2` | `788` |
| `MP_GESTURE_VC_FISTPUMP_ITEM_2` | `789` |
| `MP_GESTURE_VC_THUMBSUP_ITEM_2` | `790` |
| `MP_GESTURE_VC_NODYES_ITEM_2` | `791` |
| `MP_GESTURE_VC_NODNO_ITEM_2` | `792` |
| `MP_GESTURE_VC_HANDMOUTH_BUILDING` | `793` |
| `MP_GESTURE_VC_FINGERPOINT_BUILDING` | `794` |
| `MP_GESTURE_VC_FISTPUMP_BUILDING` | `795` |
| `MP_GESTURE_VC_THUMBSUP_BUILDING` | `796` |
| `MP_GESTURE_VC_NODYES_BUILDING` | `797` |
| `MP_GESTURE_VC_NODNO_BUILDING` | `798` |
| `MP_GESTURE_VC_HANDMOUTH_PDA` | `799` |
| `MP_GESTURE_VC_FINGERPOINT_PDA` | `800` |
| `MP_GESTURE_VC_FISTPUMP_PDA` | `801` |
| `MP_GESTURE_VC_THUMBSUP_PDA` | `802` |
| `MP_GESTURE_VC_NODYES_PDA` | `803` |
| `MP_GESTURE_VC_NODNO_PDA` | `804` |
| `VM_UNUSABLE` | `805` |
| `VM_UNUSABLE_TO_USABLE` | `806` |
| `VM_USABLE_TO_UNUSABLE` | `807` |
| `PRIMARY_VM_DRAW` | `808` |
| `PRIMARY_VM_HOLSTER` | `809` |
| `PRIMARY_VM_IDLE` | `810` |
| `PRIMARY_VM_PULLBACK` | `811` |
| `PRIMARY_VM_PRIMARYATTACK` | `812` |
| `PRIMARY_VM_SECONDARYATTACK` | `813` |
| `PRIMARY_VM_RELOAD` | `814` |
| `PRIMARY_VM_DRYFIRE` | `815` |
| `PRIMARY_VM_IDLE_TO_LOWERED` | `816` |
| `PRIMARY_VM_IDLE_LOWERED` | `817` |
| `PRIMARY_VM_LOWERED_TO_IDLE` | `818` |
| `SECONDARY_VM_DRAW` | `819` |
| `SECONDARY_VM_HOLSTER` | `820` |
| `SECONDARY_VM_IDLE` | `821` |
| `SECONDARY_VM_PULLBACK` | `822` |
| `SECONDARY_VM_PRIMARYATTACK` | `823` |
| `SECONDARY_VM_SECONDARYATTACK` | `824` |
| `SECONDARY_VM_RELOAD` | `825` |
| `SECONDARY_VM_DRYFIRE` | `826` |
| `SECONDARY_VM_IDLE_TO_LOWERED` | `827` |
| `SECONDARY_VM_IDLE_LOWERED` | `828` |
| `SECONDARY_VM_LOWERED_TO_IDLE` | `829` |
| `MELEE_VM_DRAW` | `830` |
| `MELEE_VM_HOLSTER` | `831` |
| `MELEE_VM_IDLE` | `832` |
| `MELEE_VM_PULLBACK` | `833` |
| `MELEE_VM_PRIMARYATTACK` | `834` |
| `MELEE_VM_SECONDARYATTACK` | `835` |
| `MELEE_VM_RELOAD` | `836` |
| `MELEE_VM_DRYFIRE` | `837` |
| `MELEE_VM_IDLE_TO_LOWERED` | `838` |
| `MELEE_VM_IDLE_LOWERED` | `839` |
| `MELEE_VM_LOWERED_TO_IDLE` | `840` |
| `PDA_VM_DRAW` | `841` |
| `PDA_VM_HOLSTER` | `842` |
| `PDA_VM_IDLE` | `843` |
| `PDA_VM_PULLBACK` | `844` |
| `PDA_VM_PRIMARYATTACK` | `845` |
| `PDA_VM_SECONDARYATTACK` | `846` |
| `PDA_VM_RELOAD` | `847` |
| `PDA_VM_DRYFIRE` | `848` |
| `PDA_VM_IDLE_TO_LOWERED` | `849` |
| `PDA_VM_IDLE_LOWERED` | `850` |
| `PDA_VM_LOWERED_TO_IDLE` | `851` |
| `ITEM_1_VM_DRAW` | `852` |
| `ITEM_1_VM_HOLSTER` | `853` |
| `ITEM_1_VM_IDLE` | `854` |
| `ITEM_1_VM_PULLBACK` | `855` |
| `ITEM_1_VM_PRIMARYATTACK` | `856` |
| `ITEM_1_VM_SECONDARYATTACK` | `857` |
| `ITEM_1_VM_RELOAD` | `858` |
| `ITEM_1_VM_DRYFIRE` | `859` |
| `ITEM_1_VM_IDLE_TO_LOWERED` | `860` |
| `ITEM_1_VM_IDLE_LOWERED` | `861` |
| `ITEM_1_VM_LOWERED_TO_IDLE` | `862` |
| `ITEM_2_VM_DRAW` | `863` |
| `ITEM_2_VM_HOLSTER` | `864` |
| `ITEM_2_VM_IDLE` | `865` |
| `ITEM_2_VM_PULLBACK` | `866` |
| `ITEM_2_VM_PRIMARYATTACK` | `867` |
| `ITEM_2_VM_SECONDARYATTACK` | `868` |
| `ITEM_2_VM_RELOAD` | `869` |
| `ITEM_2_VM_DRYFIRE` | `870` |
| `ITEM_2_VM_IDLE_TO_LOWERED` | `871` |
| `ITEM_2_VM_IDLE_LOWERED` | `872` |
| `ITEM_2_VM_LOWERED_TO_IDLE` | `873` |
| `RELOAD_SUCCEED` | `874` |
| `RELOAD_FAIL` | `875` |
| `WALK_AIM_AUTOGUN` | `876` |
| `RUN_AIM_AUTOGUN` | `877` |
| `IDLE_AUTOGUN` | `878` |
| `IDLE_AIM_AUTOGUN` | `879` |
| `RELOAD_AUTOGUN` | `880` |
| `CROUCH_IDLE_AUTOGUN` | `881` |
| `RANGE_ATTACK_AUTOGUN` | `882` |
| `JUMP_AUTOGUN` | `883` |
| `IDLE_AIM_PISTOL` | `884` |
| `WALK_AIM_DUAL` | `885` |
| `RUN_AIM_DUAL` | `886` |
| `IDLE_DUAL` | `887` |
| `IDLE_AIM_DUAL` | `888` |
| `RELOAD_DUAL` | `889` |
| `CROUCH_IDLE_DUAL` | `890` |
| `RANGE_ATTACK_DUAL` | `891` |
| `JUMP_DUAL` | `892` |
| `IDLE_AIM_SHOTGUN` | `893` |
| `CROUCH_IDLE_SHOTGUN` | `894` |
| `IDLE_AIM_RIFLE` | `895` |
| `CROUCH_IDLE_RIFLE` | `896` |
| `RANGE_ATTACK_RIFLE` | `897` |
| `SLEEP` | `898` |
| `WAKE` | `899` |
| `FLICK_LEFT` | `900` |
| `FLICK_LEFT_MIDDLE` | `901` |
| `FLICK_RIGHT_MIDDLE` | `902` |
| `FLICK_RIGHT` | `903` |
| `SPINAROUND` | `904` |
| `PREP_TO_FIRE` | `905` |
| `FIRE` | `906` |
| `FIRE_RECOVER` | `907` |
| `SPRAY` | `908` |
| `PREP_EXPLODE` | `909` |
| `EXPLODE` | `910` |
| `SCRIPT_CUSTOM_0` | `911` |
| `SCRIPT_CUSTOM_1` | `912` |
| `SCRIPT_CUSTOM_2` | `913` |
| `SCRIPT_CUSTOM_3` | `914` |
| `SCRIPT_CUSTOM_4` | `915` |
| `SCRIPT_CUSTOM_5` | `916` |
| `SCRIPT_CUSTOM_6` | `917` |
| `SCRIPT_CUSTOM_7` | `918` |
| `SCRIPT_CUSTOM_8` | `919` |
| `SCRIPT_CUSTOM_9` | `920` |
| `SCRIPT_CUSTOM_10` | `921` |
| `SCRIPT_CUSTOM_11` | `922` |
| `SCRIPT_CUSTOM_12` | `923` |
| `SCRIPT_CUSTOM_13` | `924` |
| `SCRIPT_CUSTOM_14` | `925` |
| `SCRIPT_CUSTOM_15` | `926` |
| `SCRIPT_CUSTOM_16` | `927` |
| `SCRIPT_CUSTOM_17` | `928` |
| `SCRIPT_CUSTOM_18` | `929` |
| `SCRIPT_CUSTOM_19` | `930` |
| `SCRIPT_CUSTOM_20` | `931` |
| `SCRIPT_CUSTOM_21` | `932` |
| `SCRIPT_CUSTOM_22` | `933` |
| `SCRIPT_CUSTOM_23` | `934` |
| `SCRIPT_CUSTOM_24` | `935` |
| `SCRIPT_CUSTOM_25` | `936` |
| `SCRIPT_CUSTOM_26` | `937` |
| `SCRIPT_CUSTOM_27` | `938` |
| `SCRIPT_CUSTOM_28` | `939` |
| `SCRIPT_CUSTOM_29` | `940` |
| `SCRIPT_CUSTOM_30` | `941` |
| `SCRIPT_CUSTOM_31` | `942` |
| `VR_PISTOL_LAST_SHOT` | `943` |
| `VR_PISTOL_SLIDE_RELEASE` | `944` |
| `VR_PISTOL_CLIP_OUT_CHAMBERED` | `945` |
| `VR_PISTOL_CLIP_OUT_SLIDE_BACK` | `946` |
| `VR_PISTOL_CLIP_IN_CHAMBERED` | `947` |
| `VR_PISTOL_CLIP_IN_SLIDE_BACK` | `948` |
| `VR_PISTOL_IDLE_SLIDE_BACK` | `949` |
| `VR_PISTOL_IDLE_SLIDE_BACK_CLIP_READY` | `950` |
| `RAGDOLL_RECOVERY_FRONT` | `951` |
| `RAGDOLL_RECOVERY_BACK` | `952` |
| `RAGDOLL_RECOVERY_LEFT` | `953` |
| `RAGDOLL_RECOVERY_RIGHT` | `954` |
| `GRABBITYGLOVES_GRAB` | `955` |
| `GRABBITYGLOVES_RELEASE` | `956` |
| `GRABBITYGLOVES_GRAB_IDLE` | `957` |
| `GRABBITYGLOVES_ACTIVE` | `958` |
| `GRABBITYGLOVES_ACTIVE_IDLE` | `959` |
| `GRABBITYGLOVES_DEACTIVATE` | `960` |
| `GRABBITYGLOVES_PULL` | `961` |
| `HEADCRAB_SMOKE_BOMB` | `962` |
| `HEADCRAB_SPIT` | `963` |
| `ZOMBIE_TRIP` | `964` |
| `ZOMBIE_LUNGE` | `965` |
| `NEUTRAL_REF_POSE` | `966` |
| `ANTLION_SCUTTLE_FORWARD` | `967` |
| `ANTLION_SCUTTLE_BACK` | `968` |
| `ANTLION_SCUTTLE_LEFT` | `969` |
| `ANTLION_SCUTTLE_RIGHT` | `970` |
| `VR_PISTOL_EMPTY_CLIP_IN_SLIDE_BACK` | `971` |
| `VR_SHOTGUN_IDLE` | `972` |
| `VR_SHOTGUN_OPEN_CHAMBER` | `973` |
| `VR_SHOTGUN_RELOAD_1` | `974` |
| `VR_SHOTGUN_RELOAD_2` | `975` |
| `VR_SHOTGUN_RELOAD_3` | `976` |
| `VR_SHOTGUN_CLOSE_CHAMBER` | `977` |
| `VR_SHOTGUN_TRIGGER_SQUEEZE` | `978` |
| `VR_SHOTGUN_SHOOT` | `979` |
| `VR_SHOTGUN_SLIDE_BACK` | `980` |
| `VR_SHOTGUN_SLIDE_FORWARD` | `981` |
| `VR_PISTOL_LONG_CLIP_IN_CHAMBERED` | `982` |
| `VR_PISTOL_LONG_CLIP_IN_SLIDE_BACK` | `983` |
| `VR_PISTOL_BURST_TOGGLE` | `984` |
| `VR_PISTOL_LOW_KICK` | `985` |
| `VR_PISTOL_BURST_ATTACK` | `986` |
| `VR_SHOTGUN_GRENADE_TWIST` | `987` |
| `DIE_STAND` | `988` |
| `DIE_STAND_HEADSHOT` | `989` |
| `DIE_CROUCH` | `990` |
| `DIE_CROUCH_HEADSHOT` | `991` |
| `CSGO_NULL` | `992` |
| `CSGO_DEFUSE` | `993` |
| `CSGO_DEFUSE_WITH_KIT` | `994` |
| `CSGO_FLASHBANG_REACTION` | `995` |
| `CSGO_FIRE_PRIMARY` | `996` |
| `CSGO_FIRE_PRIMARY_OPT_1` | `997` |
| `CSGO_FIRE_PRIMARY_OPT_2` | `998` |
| `CSGO_FIRE_SECONDARY` | `999` |
| `CSGO_FIRE_SECONDARY_OPT_1` | `1000` |
| `CSGO_FIRE_SECONDARY_OPT_2` | `1001` |
| `CSGO_RELOAD` | `1002` |
| `CSGO_RELOAD_START` | `1003` |
| `CSGO_RELOAD_LOOP` | `1004` |
| `CSGO_RELOAD_END` | `1005` |
| `CSGO_OPERATE` | `1006` |
| `CSGO_DEPLOY` | `1007` |
| `CSGO_CATCH` | `1008` |
| `CSGO_SILENCER_DETACH` | `1009` |
| `CSGO_SILENCER_ATTACH` | `1010` |
| `CSGO_TWITCH` | `1011` |
| `CSGO_TWITCH_BUYZONE` | `1012` |
| `CSGO_PLANT_BOMB` | `1013` |
| `CSGO_IDLE_TURN_BALANCEADJUST` | `1014` |
| `CSGO_IDLE_ADJUST_STOPPEDMOVING` | `1015` |
| `CSGO_ALIVE_LOOP` | `1016` |
| `CSGO_FLINCH` | `1017` |
| `CSGO_FLINCH_HEAD` | `1018` |
| `CSGO_FLINCH_MOLOTOV` | `1019` |
| `CSGO_JUMP` | `1020` |
| `CSGO_FALL` | `1021` |
| `CSGO_CLIMB_LADDER` | `1022` |
| `CSGO_LAND_LIGHT` | `1023` |
| `CSGO_LAND_HEAVY` | `1024` |
| `CSGO_EXIT_LADDER_TOP` | `1025` |
| `CSGO_EXIT_LADDER_BOTTOM` | `1026` |
| `CSGO_PARACHUTE` | `1027` |
| `CSGO_TAUNT` | `1028` |
| `DOTA_IDLE` | `1500` |
| `DOTA_IDLE_RARE` | `1501` |
| `DOTA_RUN` | `1502` |
| `DOTA_ATTACK` | `1503` |
| `DOTA_ATTACK_2` | `1504` |
| `DOTA_ATTACK_EVENT` | `1505` |
| `DOTA_DIE` | `1506` |
| `DOTA_FLINCH` | `1507` |
| `DOTA_FLAIL` | `1508` |
| `DOTA_DISABLED` | `1509` |
| `DOTA_CAST_ABILITY_1` | `1510` |
| `DOTA_CAST_ABILITY_2` | `1511` |
| `DOTA_CAST_ABILITY_3` | `1512` |
| `DOTA_CAST_ABILITY_4` | `1513` |
| `DOTA_CAST_ABILITY_5` | `1514` |
| `DOTA_CAST_ABILITY_6` | `1515` |
| `DOTA_OVERRIDE_ABILITY_1` | `1516` |
| `DOTA_OVERRIDE_ABILITY_2` | `1517` |
| `DOTA_OVERRIDE_ABILITY_3` | `1518` |
| `DOTA_OVERRIDE_ABILITY_4` | `1519` |
| `DOTA_CHANNEL_ABILITY_1` | `1520` |
| `DOTA_CHANNEL_ABILITY_2` | `1521` |
| `DOTA_CHANNEL_ABILITY_3` | `1522` |
| `DOTA_CHANNEL_ABILITY_4` | `1523` |
| `DOTA_CHANNEL_ABILITY_5` | `1524` |
| `DOTA_CHANNEL_ABILITY_6` | `1525` |
| `DOTA_CHANNEL_END_ABILITY_1` | `1526` |
| `DOTA_CHANNEL_END_ABILITY_2` | `1527` |
| `DOTA_CHANNEL_END_ABILITY_3` | `1528` |
| `DOTA_CHANNEL_END_ABILITY_4` | `1529` |
| `DOTA_CHANNEL_END_ABILITY_5` | `1530` |
| `DOTA_CHANNEL_END_ABILITY_6` | `1531` |
| `DOTA_CONSTANT_LAYER` | `1532` |
| `DOTA_CAPTURE` | `1533` |
| `DOTA_SPAWN` | `1534` |
| `DOTA_KILLTAUNT` | `1535` |
| `DOTA_TAUNT` | `1536` |
| `DOTA_THIRST` | `1537` |
| `DOTA_CAST_DRAGONBREATH` | `1538` |
| `DOTA_ECHO_SLAM` | `1539` |
| `DOTA_CAST_ABILITY_1_END` | `1540` |
| `DOTA_CAST_ABILITY_2_END` | `1541` |
| `DOTA_CAST_ABILITY_3_END` | `1542` |
| `DOTA_CAST_ABILITY_4_END` | `1543` |
| `MIRANA_LEAP_END` | `1544` |
| `WAVEFORM_START` | `1545` |
| `WAVEFORM_END` | `1546` |
| `DOTA_CAST_ABILITY_ROT` | `1547` |
| `DOTA_DIE_SPECIAL` | `1548` |
| `DOTA_RATTLETRAP_BATTERYASSAULT` | `1549` |
| `DOTA_RATTLETRAP_POWERCOGS` | `1550` |
| `DOTA_RATTLETRAP_HOOKSHOT_START` | `1551` |
| `DOTA_RATTLETRAP_HOOKSHOT_LOOP` | `1552` |
| `DOTA_RATTLETRAP_HOOKSHOT_END` | `1553` |
| `STORM_SPIRIT_OVERLOAD_RUN_OVERRIDE` | `1554` |
| `DOTA_TINKER_REARM_1` | `1555` |
| `DOTA_TINKER_REARM_2` | `1556` |
| `DOTA_TINKER_REARM_3` | `1557` |
| `TINY_AVALANCHE` | `1558` |
| `TINY_TOSS` | `1559` |
| `TINY_GROWL` | `1560` |
| `DOTA_WEAVERBUG_ATTACH` | `1561` |
| `DOTA_CAST_WILD_AXES_END` | `1562` |
| `DOTA_CAST_LIFE_BREAK_START` | `1563` |
| `DOTA_CAST_LIFE_BREAK_END` | `1564` |
| `DOTA_NIGHTSTALKER_TRANSITION` | `1565` |
| `DOTA_LIFESTEALER_RAGE` | `1566` |
| `DOTA_LIFESTEALER_OPEN_WOUNDS` | `1567` |
| `DOTA_SAND_KING_BURROW_IN` | `1568` |
| `DOTA_SAND_KING_BURROW_OUT` | `1569` |
| `DOTA_EARTHSHAKER_TOTEM_ATTACK` | `1570` |
| `DOTA_WHEEL_LAYER` | `1571` |
| `DOTA_ALCHEMIST_CHEMICAL_RAGE_START` | `1572` |
| `DOTA_ALCHEMIST_CONCOCTION` | `1573` |
| `DOTA_JAKIRO_LIQUIDFIRE_START` | `1574` |
| `DOTA_JAKIRO_LIQUIDFIRE_LOOP` | `1575` |
| `DOTA_LIFESTEALER_INFEST` | `1576` |
| `DOTA_LIFESTEALER_INFEST_END` | `1577` |
| `DOTA_LASSO_LOOP` | `1578` |
| `DOTA_ALCHEMIST_CONCOCTION_THROW` | `1579` |
| `DOTA_ALCHEMIST_CHEMICAL_RAGE_END` | `1580` |
| `DOTA_CAST_COLD_SNAP` | `1581` |
| `DOTA_CAST_GHOST_WALK` | `1582` |
| `DOTA_CAST_TORNADO` | `1583` |
| `DOTA_CAST_EMP` | `1584` |
| `DOTA_CAST_ALACRITY` | `1585` |
| `DOTA_CAST_CHAOS_METEOR` | `1586` |
| `DOTA_CAST_SUN_STRIKE` | `1587` |
| `DOTA_CAST_FORGE_SPIRIT` | `1588` |
| `DOTA_CAST_ICE_WALL` | `1589` |
| `DOTA_CAST_DEAFENING_BLAST` | `1590` |
| `DOTA_VICTORY` | `1591` |
| `DOTA_DEFEAT` | `1592` |
| `DOTA_SPIRIT_BREAKER_CHARGE_POSE` | `1593` |
| `DOTA_SPIRIT_BREAKER_CHARGE_END` | `1594` |
| `DOTA_TELEPORT` | `1595` |
| `DOTA_TELEPORT_END` | `1596` |
| `DOTA_CAST_REFRACTION` | `1597` |
| `DOTA_CAST_ABILITY_7` | `1598` |
| `DOTA_CANCEL_SIREN_SONG` | `1599` |
| `DOTA_CHANNEL_ABILITY_7` | `1600` |
| `DOTA_LOADOUT` | `1601` |
| `DOTA_FORCESTAFF_END` | `1602` |
| `DOTA_POOF_END` | `1603` |
| `DOTA_SLARK_POUNCE` | `1604` |
| `DOTA_MAGNUS_SKEWER_START` | `1605` |
| `DOTA_MAGNUS_SKEWER_END` | `1606` |
| `DOTA_MEDUSA_STONE_GAZE` | `1607` |
| `DOTA_RELAX_START` | `1608` |
| `DOTA_RELAX_LOOP` | `1609` |
| `DOTA_RELAX_END` | `1610` |
| `DOTA_CENTAUR_STAMPEDE` | `1611` |
| `DOTA_BELLYACHE_START` | `1612` |
| `DOTA_BELLYACHE_LOOP` | `1613` |
| `DOTA_BELLYACHE_END` | `1614` |
| `DOTA_ROQUELAIRE_LAND` | `1615` |
| `DOTA_ROQUELAIRE_LAND_IDLE` | `1616` |
| `DOTA_GREEVIL_CAST` | `1617` |
| `DOTA_GREEVIL_OVERRIDE_ABILITY` | `1618` |
| `DOTA_GREEVIL_HOOK_START` | `1619` |
| `DOTA_GREEVIL_HOOK_END` | `1620` |
| `DOTA_GREEVIL_BLINK_BONE` | `1621` |
| `DOTA_IDLE_SLEEPING` | `1622` |
| `DOTA_INTRO` | `1623` |
| `DOTA_GESTURE_POINT` | `1624` |
| `DOTA_GESTURE_ACCENT` | `1625` |
| `DOTA_SLEEPING_END` | `1626` |
| `DOTA_AMBUSH` | `1627` |
| `DOTA_ITEM_LOOK` | `1628` |
| `DOTA_STARTLE` | `1629` |
| `DOTA_FRUSTRATION` | `1630` |
| `DOTA_TELEPORT_REACT` | `1631` |
| `DOTA_TELEPORT_END_REACT` | `1632` |
| `DOTA_SHRUG` | `1633` |
| `DOTA_RELAX_LOOP_END` | `1634` |
| `DOTA_PRESENT_ITEM` | `1635` |
| `DOTA_IDLE_IMPATIENT` | `1636` |
| `DOTA_SHARPEN_WEAPON` | `1637` |
| `DOTA_SHARPEN_WEAPON_OUT` | `1638` |
| `DOTA_IDLE_SLEEPING_END` | `1639` |
| `DOTA_BRIDGE_DESTROY` | `1640` |
| `DOTA_TAUNT_SNIPER` | `1641` |
| `DOTA_DEATH_BY_SNIPER` | `1642` |
| `DOTA_LOOK_AROUND` | `1643` |
| `DOTA_CAGED_CREEP_RAGE` | `1644` |
| `DOTA_CAGED_CREEP_RAGE_OUT` | `1645` |
| `DOTA_CAGED_CREEP_SMASH` | `1646` |
| `DOTA_CAGED_CREEP_SMASH_OUT` | `1647` |
| `DOTA_IDLE_IMPATIENT_SWORD_TAP` | `1648` |
| `DOTA_INTRO_LOOP` | `1649` |
| `DOTA_BRIDGE_THREAT` | `1650` |
| `DOTA_DAGON` | `1651` |
| `DOTA_CAST_ABILITY_2_ES_ROLL_START` | `1652` |
| `DOTA_CAST_ABILITY_2_ES_ROLL` | `1653` |
| `DOTA_CAST_ABILITY_2_ES_ROLL_END` | `1654` |
| `DOTA_NIAN_PIN_START` | `1655` |
| `DOTA_NIAN_PIN_LOOP` | `1656` |
| `DOTA_NIAN_PIN_END` | `1657` |
| `DOTA_LEAP_STUN` | `1658` |
| `DOTA_LEAP_SWIPE` | `1659` |
| `DOTA_NIAN_INTRO_LEAP` | `1660` |
| `DOTA_AREA_DENY` | `1661` |
| `DOTA_NIAN_PIN_TO_STUN` | `1662` |
| `DOTA_RAZE_1` | `1663` |
| `DOTA_RAZE_2` | `1664` |
| `DOTA_RAZE_3` | `1665` |
| `DOTA_UNDYING_DECAY` | `1666` |
| `DOTA_UNDYING_SOUL_RIP` | `1667` |
| `DOTA_UNDYING_TOMBSTONE` | `1668` |
| `DOTA_WHIRLING_AXES_RANGED` | `1669` |
| `DOTA_SHALLOW_GRAVE` | `1670` |
| `DOTA_COLD_FEET` | `1671` |
| `DOTA_ICE_VORTEX` | `1672` |
| `DOTA_CHILLING_TOUCH` | `1673` |
| `DOTA_ENFEEBLE` | `1674` |
| `DOTA_FATAL_BONDS` | `1675` |
| `DOTA_MIDNIGHT_PULSE` | `1676` |
| `DOTA_ANCESTRAL_SPIRIT` | `1677` |
| `DOTA_THUNDER_STRIKE` | `1678` |
| `DOTA_KINETIC_FIELD` | `1679` |
| `DOTA_STATIC_STORM` | `1680` |
| `DOTA_MINI_TAUNT` | `1681` |
| `DOTA_ARCTIC_BURN_END` | `1682` |
| `DOTA_LOADOUT_RARE` | `1683` |
| `DOTA_SWIM` | `1684` |
| `DOTA_FLEE` | `1685` |
| `DOTA_TROT` | `1686` |
| `DOTA_SHAKE` | `1687` |
| `DOTA_SWIM_IDLE` | `1688` |
| `DOTA_WAIT_IDLE` | `1689` |
| `DOTA_GREET` | `1690` |
| `DOTA_TELEPORT_COOP_START` | `1691` |
| `DOTA_TELEPORT_COOP_WAIT` | `1692` |
| `DOTA_TELEPORT_COOP_END` | `1693` |
| `DOTA_TELEPORT_COOP_EXIT` | `1694` |
| `DOTA_SHOPKEEPER_PET_INTERACT` | `1695` |
| `DOTA_ITEM_PICKUP` | `1696` |
| `DOTA_ITEM_DROP` | `1697` |
| `DOTA_CAPTURE_PET` | `1698` |
| `DOTA_PET_WARD_OBSERVER` | `1699` |
| `DOTA_PET_WARD_SENTRY` | `1700` |
| `DOTA_PET_LEVEL` | `1701` |
| `DOTA_CAST_BURROW_END` | `1702` |
| `DOTA_LIFESTEALER_ASSIMILATE` | `1703` |
| `DOTA_LIFESTEALER_EJECT` | `1704` |
| `DOTA_ATTACK_EVENT_BASH` | `1705` |
| `DOTA_CAPTURE_RARE` | `1706` |
| `DOTA_AW_MAGNETIC_FIELD` | `1707` |
| `DOTA_CAST_GHOST_SHIP` | `1708` |
| `DOTA_FXANIM` | `1709` |
| `DOTA_VICTORY_START` | `1710` |
| `DOTA_DEFEAT_START` | `1711` |
| `DOTA_DP_SPIRIT_SIPHON` | `1712` |
| `DOTA_TRICKS_END` | `1713` |
| `DOTA_ES_STONE_CALLER` | `1714` |
| `DOTA_MK_STRIKE` | `1715` |
| `DOTA_VERSUS` | `1716` |
| `DOTA_CAPTURE_CARD` | `1717` |
| `DOTA_MK_SPRING_SOAR` | `1718` |
| `DOTA_MK_SPRING_END` | `1719` |
| `DOTA_MK_TREE_SOAR` | `1720` |
| `DOTA_MK_TREE_END` | `1721` |
| `DOTA_MK_FUR_ARMY` | `1722` |
| `DOTA_MK_SPRING_CAST` | `1723` |
| `DOTA_NECRO_GHOST_SHROUD` | `1724` |
| `DOTA_OVERRIDE_ARCANA` | `1725` |
| `DOTA_SLIDE` | `1726` |
| `DOTA_SLIDE_LOOP` | `1727` |
| `DOTA_GENERIC_CHANNEL_1` | `1728` |
| `DOTA_GS_SOUL_CHAIN` | `1729` |
| `DOTA_GS_INK_CREATURE` | `1730` |
| `DOTA_TRANSITION` | `1731` |
| `DOTA_BLINK_DAGGER` | `1732` |
| `DOTA_BLINK_DAGGER_END` | `1733` |
| `DOTA_CUSTOM_TOWER_ATTACK` | `1734` |
| `DOTA_CUSTOM_TOWER_IDLE` | `1735` |
| `DOTA_CUSTOM_TOWER_DIE` | `1736` |
| `DOTA_CAST_COLD_SNAP_ORB` | `1737` |
| `DOTA_CAST_GHOST_WALK_ORB` | `1738` |
| `DOTA_CAST_TORNADO_ORB` | `1739` |
| `DOTA_CAST_EMP_ORB` | `1740` |
| `DOTA_CAST_ALACRITY_ORB` | `1741` |
| `DOTA_CAST_CHAOS_METEOR_ORB` | `1742` |
| `DOTA_CAST_SUN_STRIKE_ORB` | `1743` |
| `DOTA_CAST_FORGE_SPIRIT_ORB` | `1744` |
| `DOTA_CAST_ICE_WALL_ORB` | `1745` |
| `DOTA_CAST_DEAFENING_BLAST_ORB` | `1746` |
| `DOTA_NOTICE` | `1747` |
| `DOTA_CAST_ABILITY_2_ALLY` | `1748` |
| `DOTA_SHUFFLE_L` | `1749` |
| `DOTA_SHUFFLE_R` | `1750` |
| `DOTA_OVERRIDE_LOADOUT` | `1751` |
| `DOTA_TAUNT_SPECIAL` | `1752` |
| `DOTA_TELEPORT_START` | `1753` |
| `DOTA_GENERIC_CHANNEL_1_START` | `1754` |
| `DOTA_CUSTOM_TOWER_IDLE_RARE` | `1755` |
| `DOTA_CUSTOM_TOWER_TAUNT` | `1756` |
| `DOTA_CUSTOM_TOWER_HIGH_FIVE` | `1757` |
| `DOTA_ATTACK_SPECIAL` | `1758` |
| `DOTA_TRANSITION_IDLE` | `1759` |
| `DOTA_PIERCE_THE_VEIL` | `1760` |
| `DOTA_RUN_RARE` | `1761` |
| `DOTA_VIPER_DIVE` | `1762` |
| `DOTA_VIPER_DIVE_END` | `1763` |
| `DOTA_MK_STRIKE_END` | `1764` |
| `DOTA_SHADOW_VAULT` | `1765` |
| `DOTA_KEZ_KATANA_ULT_START` | `1766` |
| `DOTA_KEZ_KATANA_ULT_CHAIN_A` | `1767` |
| `DOTA_KEZ_KATANA_ULT_CHAIN_B` | `1768` |
| `DOTA_KEZ_KATANA_ULT_END` | `1769` |
| `DOTA_KEZ_KATANA_IMPALE` | `1770` |
| `DOTA_KEZ_KATANA_IMPALE_FAST` | `1771` |
| `DOTA_UNICYCLE` | `1772` |
| `DOTA_UNICYCLE_END` | `1773` |
| `DOTA_LARGO_ULT_STRUM_SUCCESS` | `1774` |
| `DOTA_LARGO_ULT_STRUM_FAIL` | `1775` |
| `DOTA_MVP_SCREEN` | `1776` |
| `DOTA_LARGO_ULT_TOGGLE_ON` | `1777` |
| `DOTA_LARGO_ULT_TOGGLE_OFF` | `1778` |
| `DOTA_RUN_STATUE` | `1779` |
| `DOTA_CAST_1_STATUE` | `1780` |
| `DOTA_CAST_2_STATUE` | `1781` |
| `DOTA_STUN_STATUE` | `1782` |
| `DOTA_FLAIL_STATUE` | `1783` |
| `DOTA_SPAWN_STATUE` | `1784` |
| `DOTA_TELEPORT_END_STATUE` | `1785` |
| `DOTA_ATTACK_STATUE` | `1786` |
| `DOTA_FORCESTAFF_STATUE` | `1787` |
| `DOTA_TELEPORT_STATUE` | `1788` |
| `DOTA_VICTORY_STATUE` | `1789` |
| `DOTA_TAUNT_STATUE` | `1790` |
| `DOTA_IDLE_STATUE` | `1791` |
| `DOTA_DISABLED_END` | `1792` |
| `DOTA_VOODOO_REST` | `1793` |
| `DOTA_CYCLONE` | `1794` |
| `DOTA_IMPALE` | `1795` |
| `DOTA_TORRENT` | `1796` |
| `DOTA_RADIANT_CREEP_HAMMER` | `1798` |
| `DOTA_RELAX_IN` | `1799` |
| `DOTA_RELAX_OUT` | `1800` |
| `DOTA_CAST_FENCE` | `1801` |
| `DOTA_SPWN` | `1802` |
| `DOTA_CAST_3_STATUE` | `1803` |
| `DOTA_CAST_4_STATUE` | `1804` |
| `DOTA_CAST_5_STATUE` | `1805` |

### GameState

| Member | Value |
| --- | --- |
| `INIT` | `0` |
| `WAIT_FOR_PLAYERS_TO_LOAD` | `1` |
| `CUSTOM_GAME_SETUP` | `2` |
| `PLAYER_DRAFT` | `3` |
| `HERO_SELECTION` | `4` |
| `STRATEGY_TIME` | `5` |
| `TEAM_SHOWCASE` | `6` |
| `WAIT_FOR_MAP_TO_LOAD` | `7` |
| `PRE_GAME` | `8` |
| `SCENARIO_SETUP` | `9` |
| `GAME_IN_PROGRESS` | `10` |
| `POST_GAME` | `11` |
| `DISCONNECT` | `12` |

### GcTeam

| Member | Value |
| --- | --- |
| `GOOD_GUYS` | `0` |
| `BAD_GUYS` | `1` |
| `BROADCASTER` | `2` |
| `SPECTATOR` | `3` |
| `PLAYER_POOL` | `4` |
| `NOTEAM` | `5` |
| `CUSTOM_1` | `6` |
| `CUSTOM_2` | `7` |
| `CUSTOM_3` | `8` |
| `CUSTOM_4` | `9` |
| `CUSTOM_5` | `10` |
| `CUSTOM_6` | `11` |
| `CUSTOM_7` | `12` |
| `CUSTOM_8` | `13` |
| `NEUTRALS` | `14` |

### HeroPickState

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `AP_SELECT` | `1` |
| `SD_SELECT` | `2` |
| `INTRO_SELECT_UNUSED` | `3` |
| `RD_SELECT_UNUSED` | `4` |
| `CM_INTRO` | `5` |
| `CM_CAPTAINPICK` | `6` |
| `CM_BAN1` | `7` |
| `CM_BAN2` | `8` |
| `CM_BAN3` | `9` |
| `CM_BAN4` | `10` |
| `CM_BAN5` | `11` |
| `CM_BAN6` | `12` |
| `CM_BAN7` | `13` |
| `CM_BAN8` | `14` |
| `CM_BAN9` | `15` |
| `CM_BAN10` | `16` |
| `CM_BAN11` | `17` |
| `CM_BAN12` | `18` |
| `CM_BAN13` | `19` |
| `CM_BAN14` | `20` |
| `CM_SELECT1` | `21` |
| `CM_SELECT2` | `22` |
| `CM_SELECT3` | `23` |
| `CM_SELECT4` | `24` |
| `CM_SELECT5` | `25` |
| `CM_SELECT6` | `26` |
| `CM_SELECT7` | `27` |
| `CM_SELECT8` | `28` |
| `CM_SELECT9` | `29` |
| `CM_SELECT10` | `30` |
| `CM_PICK` | `31` |
| `AR_SELECT` | `32` |
| `MO_SELECT` | `33` |
| `FH_SELECT` | `34` |
| `CD_INTRO` | `35` |
| `CD_CAPTAINPICK` | `36` |
| `CD_BAN1` | `37` |
| `CD_BAN2` | `38` |
| `CD_BAN3` | `39` |
| `CD_BAN4` | `40` |
| `CD_BAN5` | `41` |
| `CD_BAN6` | `42` |
| `CD_SELECT1` | `43` |
| `CD_SELECT2` | `44` |
| `CD_SELECT3` | `45` |
| `CD_SELECT4` | `46` |
| `CD_SELECT5` | `47` |
| `CD_SELECT6` | `48` |
| `CD_SELECT7` | `49` |
| `CD_SELECT8` | `50` |
| `CD_SELECT9` | `51` |
| `CD_SELECT10` | `52` |
| `CD_PICK` | `53` |
| `BD_SELECT` | `54` |
| `ABILITY_DRAFT_SELECT` | `55` |
| `ARDM_SELECT` | `56` |
| `ALL_DRAFT_SELECT` | `57` |
| `CUSTOMGAME_SELECT` | `58` |
| `SELECT_PENALTY` | `59` |
| `CUSTOM_PICK_RULES` | `60` |
| `SCENARIO_PICK` | `61` |

### HudVisibility

| Member | Value |
| --- | --- |
| `VISIBILITY_INVALID` | `-1` |
| `VISIBILITY_TOP_TIMEOFDAY` | `0` |
| `VISIBILITY_TOP_HEROES` | `1` |
| `VISIBILITY_TOP_SCOREBOARD` | `2` |
| `VISIBILITY_ACTION_PANEL` | `3` |
| `VISIBILITY_ACTION_MINIMAP` | `4` |
| `VISIBILITY_INVENTORY_PANEL` | `5` |
| `VISIBILITY_INVENTORY_SHOP` | `6` |
| `VISIBILITY_INVENTORY_ITEMS` | `7` |
| `VISIBILITY_INVENTORY_QUICKBUY` | `8` |
| `VISIBILITY_INVENTORY_COURIER` | `9` |
| `VISIBILITY_INVENTORY_PROTECT` | `10` |
| `VISIBILITY_INVENTORY_GOLD` | `11` |
| `VISIBILITY_SHOP_SUGGESTEDITEMS` | `12` |
| `VISIBILITY_SHOP_COMMONITEMS` | `13` |
| `VISIBILITY_HERO_SELECTION_TEAMS` | `14` |
| `VISIBILITY_HERO_SELECTION_GAME_NAME` | `15` |
| `VISIBILITY_HERO_SELECTION_CLOCK` | `16` |
| `VISIBILITY_HERO_SELECTION_HEADER` | `17` |
| `VISIBILITY_TOP_MENU_BUTTONS` | `18` |
| `VISIBILITY_TOP_BAR_BACKGROUND` | `19` |
| `VISIBILITY_TOP_BAR_RADIANT_TEAM` | `20` |
| `VISIBILITY_TOP_BAR_DIRE_TEAM` | `21` |
| `VISIBILITY_TOP_BAR_SCORE` | `22` |
| `VISIBILITY_ENDGAME` | `23` |
| `VISIBILITY_ENDGAME_CHAT` | `24` |
| `VISIBILITY_QUICK_STATS` | `25` |
| `VISIBILITY_PREGAME_STRATEGYUI` | `26` |
| `VISIBILITY_KILLCAM` | `27` |
| `VISIBILITY_FIGHT_RECAP` | `28` |
| `VISIBILITY_TOP_BAR` | `29` |
| `CUSTOMUI_BEHIND_HUD_ELEMENTS` | `30` |
| `VISIBILITY_AGHANIMS_STATUS` | `31` |

### InvalidOrders

| Member | Value |
| --- | --- |
| `ORDER_SUCCESS` | `-1` |
| `INVALID_ORDER_NOT_CONTROLLABLE_BY_PLAYER` | `0` |
| `INVALID_ORDER_UNIT_IS_NOT_NPC` | `1` |
| `INVALID_ORDER_BAD_ABILITY_ENTITY` | `2` |
| `INVALID_ORDER_UNRECOGNIZED_ORDER` | `3` |
| `INVALID_ORDER_ABILITY_REQUIRED` | `4` |
| `INVALID_ORDER_NPC_TARGET_REQUIRED` | `5` |
| `INVALID_ORDER_TARGET_TREE_INDEX_NOT_A_TREE` | `6` |
| `INVALID_ORDER_TARGET_ENTITY_INDEX_OUT_OF_RANGE` | `7` |
| `INVALID_ORDER_ABILITY_NOT_AN_ITEM` | `8` |
| `INVALID_ORDER_PHYSICAL_ITEM_TARGET_REQUIRED` | `9` |
| `INVALID_ORDER_RUNE_TARGET_REQUIRED` | `10` |
| `INVALID_ORDER_ABILITY_NOT_OWNED_BY_UNIT` | `11` |
| `INVALID_ORDER_ABILITY_CANT_BE_UPGRADED` | `12` |
| `INVALID_ORDER_NO_POINTS_FOR_ABILITY_UPGRADE` | `13` |
| `INVALID_ORDER_NOT_ENOUGH_MANA` | `14` |
| `INVALID_ORDER_ABILITY_IN_COOLDOWN` | `15` |
| `INVALID_ORDER_ABILITY_NOT_LEARNED` | `16` |
| `INVALID_ORDER_CANT_CAST_PASSIVE_ABILITY` | `17` |
| `INVALID_ORDER_PHANTOM_TARGET` | `18` |
| `INVALID_ORDER_DEAD_TARGET` | `19` |
| `INVALID_ORDER_UNIT_IS_DEAD` | `20` |
| `INVALID_ORDER_TARGET_MAGIC_IMMUNE_ENEMY` | `21` |
| `INVALID_ORDER_TARGET_INVULNERABLE` | `22` |
| `INVALID_ORDER_TARGET_ATTACK_IMMUNE` | `23` |
| `INVALID_ORDER_UNIT_SILENCED` | `24` |
| `INVALID_ORDER_ABILITY_CANT_BE_TOGGLED` | `25` |
| `INVALID_ORDER_TARGET_CANT_BE_SEEN` | `26` |
| `INVALID_ORDER_TARGET_INVISIBLE` | `27` |
| `INVALID_ORDER_HERO_CANT_BE_DENIED` | `28` |
| `INVALID_ORDER_CANT_CAST_ON_TEAMMATE` | `29` |
| `INVALID_ORDER_CANT_CAST_ON_ENEMY` | `30` |
| `INVALID_ORDER_UNIT_CANT_MOVE` | `31` |
| `INVALID_ORDER_CANT_CAST_ON_ATTACK_IMMUNE` | `32` |
| `INVALID_ORDER_PURCHASE_INVALID_ITEM` | `33` |
| `INVALID_ORDER_ITEM_NOT_IN_INVENTORY` | `34` |
| `INVALID_ORDER_ITEM_NOT_IN_UNIT_INVENTORY` | `35` |
| `INVALID_ORDER_TARGET_UNSELECTABLE` | `36` |
| `INVALID_ORDER_ITEM_NOT_IN_ACTIVE_INVENTORY` | `37` |
| `INVALID_ORDER_UNIT_CANT_PICK_UP_RUNES` | `38` |
| `INVALID_ORDER_UNIT_CANT_MANIPULATE_ITEMS` | `39` |
| `INVALID_ORDER_UNIT_IS_ILLUSION` | `40` |
| `INVALID_ORDER_UNIT_CANT_ATTACK` | `41` |
| `INVALID_ORDER_ITEM_CANT_BE_DROPPED` | `42` |
| `INVALID_ORDER_TARGET_TREE_NOT_ACTIVE` | `43` |
| `INVALID_ORDER_ABILITY_CANT_AUTO_CAST` | `44` |
| `INVALID_ORDER_TARGET_POSITION_OFF_MAP` | `45` |
| `INVALID_ORDER_UNIT_CANT_MOVE_TARGET_OUT_OF_RANGE` | `46` |
| `INVALID_ORDER_CANT_CAST_ON_HERO` | `47` |
| `INVALID_ORDER_CANT_CAST_ON_OTHER` | `48` |
| `INVALID_ORDER_CANT_CAST_ON_BUILDING` | `49` |
| `INVALID_ORDER_CANT_CAST_ON_ANCIENT` | `50` |
| `INVALID_ORDER_ITEM_CANT_BE_MOVED_TO_STASH` | `51` |
| `INVALID_ORDER_ITEM_CANT_BE_MOVED_TO_SLOT` | `52` |
| `INVALID_ORDER_CANT_CAST_ON_MECHANICAL` | `53` |
| `INVALID_ORDER_CANT_ACCEPT_ATTACK_TARGET` | `54` |
| `INVALID_ORDER_CANT_CAST_NO_CHARGES` | `55` |
| `INVALID_ORDER_CANT_CAST_ON_CREEP` | `56` |
| `INVALID_ORDER_TARGET_CANT_TAKE_ITEMS` | `57` |
| `INVALID_ORDER_CANT_GIVE_ITEM_TO_ENEMY` | `58` |
| `INVALID_ORDER_CANT_CAST_ON_COURIER` | `59` |
| `INVALID_ORDER_ABILITY_IS_HIDDEN` | `60` |
| `INVALID_ORDER_ITEM_IN_COOLDOWN` | `61` |
| `INVALID_ORDER_SECRET_SHOP_NOT_IN_RANGE` | `62` |
| `INVALID_ORDER_NOT_ENOUGH_GOLD` | `63` |
| `INVALID_ORDER_PURCHASE_AUTOCOMBINE_RECIPE` | `64` |
| `INVALID_ORDER_CANT_DENY_HEALTH_TOO_HIGH` | `65` |
| `INVALID_ORDER_SIDE_SHOP_NOT_IN_RANGE` | `66` |
| `INVALID_ORDER_HOME_SHOP_NOT_IN_RANGE` | `67` |
| `INVALID_ORDER_CANT_PICK_UP_ITEM` | `68` |
| `INVALID_ORDER_CANT_SELL_NO_SHOP_IN_RANGE` | `69` |
| `INVALID_ORDER_CANT_SELL_ITEM` | `70` |
| `INVALID_ORDER_CANT_SELL_ITEM_WHILE_DEAD` | `71` |
| `INVALID_ORDER_TARGET_CANT_BE_DENIED` | `72` |
| `INVALID_ORDER_ABILITY_DISABLED_BY_ROOT` | `73` |
| `INVALID_ORDER_UNIT_COMMAND_RESTRICTED` | `74` |
| `INVALID_ORDER_UNIT_MUTED` | `75` |
| `INVALID_ORDER_CANT_CAST_ON_SUMMONED` | `76` |
| `INVALID_ORDER_TARGET_MAGIC_IMMUNE_ALLY` | `77` |
| `INVALID_ORDER_CANT_PURCHASE_DISALLOWED_ITEM` | `78` |
| `INVALID_ORDER_CANT_CAST_ON_DOMINATED` | `79` |
| `INVALID_ORDER_CAST_CUSTOM` | `80` |
| `INVALID_ORDER_ITEM_NOT_DISASSEMBLABLE` | `81` |
| `INVALID_ORDER_ITEM_OUT_OF_STOCK` | `82` |
| `INVALID_ORDER_ABILITY_CANT_BE_UPGRADED_AT_MAX` | `83` |
| `INVALID_ORDER_ABILITY_INACTIVE` | `84` |
| `INVALID_ORDER_ITEM_NOT_IN_MAIN_INVENTORY` | `85` |
| `INVALID_ORDER_CANT_GLYPH` | `86` |
| `INVALID_ORDER_CANT_DRAG_CHANNELING_ITEM` | `87` |
| `INVALID_ORDER_CANT_BUYBACK_UNIT_NOT_A_HERO` | `88` |
| `INVALID_ORDER_CANT_BUYBACK_UNIT_NOT_DEAD` | `89` |
| `INVALID_ORDER_CANT_BUYBACK_NOT_ENOUGH_GOLD` | `90` |
| `INVALID_ORDER_CANT_BUYBACK_IN_COOLDOWN` | `91` |
| `INVALID_ORDER_CANT_DISASSEMBLE_STASH_OUT_OF_RANGE` | `92` |
| `INVALID_ORDER_CANT_EJECT_ITEM_NOT_IN_STASH` | `93` |
| `INVALID_ORDER_GAME_IS_PAUSED` | `94` |
| `INVALID_ORDER_CANT_CAST_ON_CONSIDERED_HERO` | `95` |
| `INVALID_ORDER_CANT_SHOP_AUTO_BUY_ENABLED` | `96` |
| `INVALID_ORDER_ONLY_DELIBERATE_CHANNELING_CANCEL` | `97` |
| `INVALID_ORDER_CANT_BUYBACK_DEVILS_BARGAIN` | `98` |
| `INVALID_ORDER_CANT_BUYBACK_DISABLED_BY_GAME_MODE` | `99` |
| `INVALID_ORDER_CANT_ABILITY_PING_BAD_TEAM` | `100` |
| `INVALID_ORDER_ABILITY_NOT_POSITIONED` | `101` |
| `INVALID_ORDER_ABILITY_NOT_TARGETTED` | `102` |
| `INVALID_ORDER_ABILITY_REQUIRES_TARGET` | `103` |
| `INVALID_ORDER_CANT_RADAR` | `104` |
| `INVALID_ORDER_NO_COURIER` | `105` |
| `INVALID_ORDER_CUSTOM_SHOP_NOT_IN_RANGE` | `106` |
| `INVALID_ORDER_CANT_CAST_RIVER_PAINT` | `107` |
| `INVALID_ORDER_UNIT_OBSTRUCTED` | `108` |
| `INVALID_ORDER_CANT_CAST_DRAG_REQUIRED` | `109` |
| `INVALID_ORDER_ABILITY_DISABLED_BY_TETHER` | `110` |
| `INVALID_ORDER_ABILITY_NOT_UNLOCKED` | `111` |
| `INVALID_ORDER_CANT_FOUNTAIN_DROP_UNIT_NOT_DEAD` | `112` |
| `INVALID_ORDER_ITEM_NOT_IN_NEUTRAL_ITEM_STASH` | `113` |
| `INVALID_ORDER_ITEM_ALREADY_PURCHASED` | `114` |
| `INVALID_ORDER_BEYOND_PHYSICAL_ITEM_LIMIT` | `115` |
| `INVALID_ORDER_ABILITY_PING_DEAD_ALLY` | `116` |
| `INVALID_ORDER_CANT_LOCKCOMBINE_NEUTRAL_ITEMS` | `117` |
| `INVALID_ORDER_ABILITY_CANT_ALT_CAST` | `118` |
| `INVALID_ORDER_ITEM_CANNOT_BE_CONSUMED` | `119` |
| `INVALID_ORDER_CANT_BUYBACK_CEASELESS_DIRGE` | `120` |
| `INVALID_ORDER_CANT_ATTACK_BUILDINGS` | `121` |
| `INVALID_ORDER_PURCHASE_LEVEL` | `122` |
| `INVALID_ORDER_COUNT` | `123` |

### InventoryFlags

| Member | Value |
| --- | --- |
| `ALLOW_NONE` | `0` |
| `ALLOW_MAIN` | `1` |
| `ALLOW_STASH` | `2` |
| `ALL_ACCESS` | `3` |
| `ALLOW_DROP_ON_GROUND` | `4` |
| `ALLOW_DROP_AT_FOUNTAIN` | `8` |
| `LIMIT_DROP_ON_GROUND` | `16` |

### InventorySlot

| Member | Value |
| --- | --- |
| `SLOT_1` | `0` |
| `SLOT_2` | `1` |
| `SLOT_3` | `2` |
| `SLOT_4` | `3` |
| `SLOT_5` | `4` |
| `SLOT_6` | `5` |
| `SLOT_7` | `6` |
| `SLOT_8` | `7` |
| `SLOT_9` | `8` |
| `STASH_1` | `9` |
| `STASH_2` | `10` |
| `STASH_3` | `11` |
| `STASH_4` | `12` |
| `STASH_5` | `13` |
| `STASH_6` | `14` |
| `TP_SCROLL` | `15` |
| `NEUTRAL_ACTIVE_SLOT` | `16` |
| `NEUTRAL_PASSIVE_SLOT` | `17` |
| `TRANSIENT_ITEM` | `23` |
| `TRANSIENT_RECIPE` | `24` |
| `TRANSIENT_CAST_ITEM` | `26` |

### ItemShareability

| Member | Value |
| --- | --- |
| `FULLY_SHAREABLE` | `0` |
| `PARTIALLY_SHAREABLE` | `1` |
| `NOT_SHAREABLE` | `2` |

### LoadoutType

| Member | Value |
| --- | --- |
| `TYPE_INVALID` | `-1` |
| `TYPE_WEAPON` | `0` |
| `TYPE_OFFHAND_WEAPON` | `1` |
| `TYPE_WEAPON_2` | `2` |
| `TYPE_OFFHAND_WEAPON_2` | `3` |
| `TYPE_HEAD` | `4` |
| `TYPE_SHOULDER` | `5` |
| `TYPE_ARMS` | `6` |
| `TYPE_ARMOR` | `7` |
| `TYPE_BELT` | `8` |
| `TYPE_NECK` | `9` |
| `TYPE_BACK` | `10` |
| `TYPE_GLOVES` | `11` |
| `TYPE_LEGS` | `12` |
| `TYPE_TAIL` | `13` |
| `TYPE_MISC` | `14` |
| `TYPE_COSTUME` | `15` |
| `TYPE_HERO_BASE` | `16` |
| `TYPE_BODY_HEAD` | `17` |
| `TYPE_MOUNT` | `18` |
| `TYPE_SUMMON` | `19` |
| `TYPE_SHAPESHIFT` | `20` |
| `TYPE_TAUNT` | `21` |
| `TYPE_HERO_EFFIGY` | `22` |
| `TYPE_AMBIENT_EFFECTS` | `23` |
| `TYPE_ABILITY_ATTACK` | `24` |
| `TYPE_ABILITY_1` | `25` |
| `TYPE_ABILITY_2` | `26` |
| `TYPE_ABILITY_3` | `27` |
| `TYPE_ABILITY_4` | `28` |
| `TYPE_ABILITY_ULTIMATE` | `29` |
| `TYPE_ABILITY_EFFECTS_1` | `30` |
| `TYPE_ABILITY_EFFECTS_2` | `31` |
| `TYPE_ABILITY_EFFECTS_3` | `32` |
| `TYPE_ABILITY_EFFECTS_4` | `33` |
| `TYPE_ABILITY_EFFECTS_5` | `34` |
| `TYPE_ABILITY_EFFECTS_6` | `35` |
| `TYPE_ABILITY_EFFECTS_7` | `36` |
| `TYPE_ABILITY_EFFECTS_8` | `37` |
| `TYPE_ABILITY_EFFECTS_9` | `38` |
| `TYPE_VOICE` | `39` |
| `PERSONA_1_START` | `40` |
| `TYPE_WEAPON_PERSONA_1` | `40` |
| `TYPE_OFFHAND_WEAPON_PERSONA_1` | `41` |
| `TYPE_WEAPON_2_PERSONA_1` | `42` |
| `TYPE_OFFHAND_WEAPON_2_PERSONA_1` | `43` |
| `TYPE_HEAD_PERSONA_1` | `44` |
| `TYPE_SHOULDER_PERSONA_1` | `45` |
| `TYPE_ARMS_PERSONA_1` | `46` |
| `TYPE_ARMOR_PERSONA_1` | `47` |
| `TYPE_BELT_PERSONA_1` | `48` |
| `TYPE_NECK_PERSONA_1` | `49` |
| `TYPE_BACK_PERSONA_1` | `50` |
| `TYPE_LEGS_PERSONA_1` | `51` |
| `TYPE_GLOVES_PERSONA_1` | `52` |
| `TYPE_TAIL_PERSONA_1` | `53` |
| `TYPE_MISC_PERSONA_1` | `54` |
| `TYPE_BODY_HEAD_PERSONA_1` | `55` |
| `TYPE_MOUNT_PERSONA_1` | `56` |
| `TYPE_SUMMON_PERSONA_1` | `57` |
| `TYPE_SHAPESHIFT_PERSONA_1` | `58` |
| `TYPE_TAUNT_PERSONA_1` | `59` |
| `TYPE_HERO_EFFIGY_PERSONA_1` | `60` |
| `TYPE_AMBIENT_EFFECTS_PERSONA_1` | `61` |
| `TYPE_ABILITY_ATTACK_PERSONA_1` | `62` |
| `TYPE_ABILITY_1_PERSONA_1` | `63` |
| `TYPE_ABILITY_2_PERSONA_1` | `64` |
| `TYPE_ABILITY_3_PERSONA_1` | `65` |
| `TYPE_ABILITY_4_PERSONA_1` | `66` |
| `TYPE_ABILITY_ULTIMATE_PERSONA_1` | `67` |
| `PERSONA_1_END` | `68` |
| `TYPE_VOICE_PERSONA_1` | `68` |
| `TYPE_PERSONA_SELECTOR` | `69` |
| `TYPE_COURIER` | `70` |
| `TYPE_ANNOUNCER` | `71` |
| `TYPE_MEGA_KILLS` | `72` |
| `TYPE_MUSIC` | `73` |
| `TYPE_WARD` | `74` |
| `TYPE_HUD_SKIN` | `75` |
| `TYPE_LOADING_SCREEN` | `76` |
| `TYPE_WEATHER` | `77` |
| `TYPE_HEROIC_STATUE` | `78` |
| `TYPE_MULTIKILL_BANNER` | `79` |
| `TYPE_CURSOR_PACK` | `80` |
| `TYPE_TELEPORT_EFFECT` | `81` |
| `TYPE_BLINK_EFFECT` | `82` |
| `TYPE_EMBLEM` | `83` |
| `TYPE_TERRAIN` | `84` |
| `TYPE_RADIANT_CREEPS` | `85` |
| `TYPE_DIRE_CREEPS` | `86` |
| `TYPE_RADIANT_TOWER` | `87` |
| `TYPE_DIRE_TOWER` | `88` |
| `TYPE_VERSUS_SCREEN` | `89` |
| `TYPE_STREAK_EFFECT` | `90` |
| `TYPE_KILL_EFFECT` | `91` |
| `TYPE_DEATH_EFFECT` | `92` |
| `TYPE_HEAD_EFFECT` | `93` |
| `TYPE_MAP_EFFECT` | `94` |
| `TYPE_COURIER_EFFECT` | `95` |
| `TYPE_RADIANT_SIEGE_CREEPS` | `96` |
| `TYPE_DIRE_SIEGE_CREEPS` | `97` |
| `TYPE_ROSHAN` | `98` |
| `TYPE_TORMENTOR` | `99` |
| `TYPE_ANCIENT` | `100` |
| `TYPE_PET_EFFIGY` | `101` |
| `TYPE_NONE` | `102` |

### LuaModifierMotionType

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `HORIZONTAL` | `1` |
| `VERTICAL` | `2` |
| `BOTH` | `3` |
| `INVALID` | `4` |

### MinimapEventType

| Member | Value |
| --- | --- |
| `ANCIENT_UNDER_ATTACK` | `2` |
| `BASE_UNDER_ATTACK` | `4` |
| `BASE_GLYPHED` | `8` |
| `TEAMMATE_UNDER_ATTACK` | `16` |
| `TEAMMATE_TELEPORTING` | `32` |
| `TEAMMATE_DIED` | `64` |
| `TUTORIAL_TASK_ACTIVE` | `128` |
| `TUTORIAL_TASK_FINISHED` | `256` |
| `HINT_LOCATION` | `512` |
| `ENEMY_TELEPORTING` | `1024` |
| `CANCEL_TELEPORTING` | `2048` |
| `RADAR` | `4096` |
| `RADAR_TARGET` | `8192` |
| `MOVE_TO_TARGET` | `16384` |

### ModifierAttribute

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `PERMANENT` | `1` |
| `MULTIPLE` | `2` |
| `IGNORE_INVULNERABLE` | `4` |
| `AURA_PRIORITY` | `8` |
| `IGNORE_DODGE` | `16` |
| `DUPLICATED` | `32` |

### ModifierFunction

| Member | Value |
| --- | --- |
| `PREATTACK_BONUS_DAMAGE` | `0` |
| `PREATTACK_BONUS_DAMAGE_TARGET` | `1` |
| `PREATTACK_BONUS_DAMAGE_PROC` | `2` |
| `PREATTACK_BONUS_DAMAGE_POST_CRIT` | `3` |
| `BASEATTACK_BONUSDAMAGE` | `4` |
| `PROCATTACK_BONUS_DAMAGE_PHYSICAL` | `5` |
| `PROCATTACK_CONVERT_PHYSICAL_TO_MAGICAL` | `6` |
| `PROCATTACK_BONUS_DAMAGE_MAGICAL` | `7` |
| `PROCATTACK_BONUS_DAMAGE_PURE` | `8` |
| `PROCATTACK_BONUS_DAMAGE_MAGICAL_TARGET` | `9` |
| `PROCATTACK_FEEDBACK` | `10` |
| `OVERRIDE_ATTACK_DAMAGE` | `11` |
| `PRE_ATTACK` | `12` |
| `INVISIBILITY_LEVEL` | `13` |
| `INVISIBILITY_ATTACK_BEHAVIOR_EXCEPTION` | `14` |
| `PERSISTENT_INVISIBILITY` | `15` |
| `MOVESPEED_BONUS_CONSTANT` | `16` |
| `MOVESPEED_BASE_OVERRIDE` | `17` |
| `MOVESPEED_MIN_OVERRIDE` | `18` |
| `MOVESPEED_MAX_OVERRIDE` | `19` |
| `MOVESPEED_BONUS_PERCENTAGE` | `20` |
| `MOVESPEED_BONUS_PERCENTAGE_UNIQUE` | `21` |
| `MOVESPEED_BONUS_UNIQUE` | `22` |
| `MOVESPEED_BONUS_UNIQUE_2` | `23` |
| `MOVESPEED_BONUS_CONSTANT_UNIQUE` | `24` |
| `MOVESPEED_BONUS_CONSTANT_UNIQUE_2` | `25` |
| `MOVESPEED_ABSOLUTE` | `26` |
| `MOVESPEED_ABSOLUTE_MIN` | `27` |
| `MOVESPEED_ABSOLUTE_MAX` | `28` |
| `IGNORE_MOVESPEED_LIMIT` | `29` |
| `MOVESPEED_LIMIT` | `30` |
| `ATTACKSPEED_BASE_OVERRIDE` | `31` |
| `FIXED_ATTACK_RATE` | `32` |
| `ATTACKSPEED_BONUS_CONSTANT` | `33` |
| `IGNORE_ATTACKSPEED_LIMIT` | `34` |
| `COOLDOWN_REDUCTION_CONSTANT` | `35` |
| `MANACOST_REDUCTION_CONSTANT` | `36` |
| `HEALTHCOST_REDUCTION_CONSTANT` | `37` |
| `BASE_ATTACK_TIME_CONSTANT` | `38` |
| `BASE_ATTACK_TIME_CONSTANT_ADJUST` | `39` |
| `BASE_ATTACK_TIME_PERCENTAGE` | `40` |
| `ATTACK_POINT_CONSTANT` | `41` |
| `BONUSDAMAGEOUTGOING_PERCENTAGE` | `42` |
| `DAMAGEOUTGOING_PERCENTAGE` | `43` |
| `DAMAGEOUTGOING_PERCENTAGE_ILLUSION` | `44` |
| `DAMAGEOUTGOING_PERCENTAGE_ILLUSION_AMPLIFY` | `45` |
| `TOTALDAMAGEOUTGOING_PERCENTAGE` | `46` |
| `SPELL_AMPLIFY_PERCENTAGE` | `47` |
| `SPELL_AMPLIFY_PERCENTAGE_UNIQUE` | `48` |
| `SPELL_AMPLIFY_PERCENTAGE_TARGET` | `49` |
| `HEAL_AMPLIFY_PERCENTAGE_SOURCE` | `50` |
| `HEAL_AMPLIFY_PERCENTAGE_TARGET` | `51` |
| `HP_REGEN_AMPLIFY_PERCENTAGE` | `52` |
| `LIFESTEAL_AMPLIFY_PERCENTAGE` | `53` |
| `SPELL_LIFESTEAL_AMPLIFY_PERCENTAGE` | `54` |
| `SPELL_LIFESTEAL_AMPLIFY_PERCENTAGE_UNIQUE` | `55` |
| `MP_REGEN_AMPLIFY_PERCENTAGE` | `56` |
| `MP_REGEN_AMPLIFY_PERCENTAGE_UNIQUE` | `57` |
| `MANA_DRAIN_AMPLIFY_PERCENTAGE` | `58` |
| `MP_RESTORE_AMPLIFY_PERCENTAGE` | `59` |
| `BASEDAMAGEOUTGOING_PERCENTAGE` | `60` |
| `BASEDAMAGEOUTGOING_PERCENTAGE_UNIQUE` | `61` |
| `INCOMING_DAMAGE_PERCENTAGE` | `62` |
| `INCOMING_PHYSICAL_DAMAGE_PERCENTAGE` | `63` |
| `INCOMING_PHYSICAL_DAMAGE_CONSTANT` | `64` |
| `INCOMING_SPELL_DAMAGE_CONSTANT` | `65` |
| `EVASION_CONSTANT` | `66` |
| `NEGATIVE_EVASION_CONSTANT` | `67` |
| `STATUS_RESISTANCE` | `68` |
| `STATUS_RESISTANCE_STACKING` | `69` |
| `STATUS_RESISTANCE_CASTER` | `70` |
| `AVOID_DAMAGE` | `71` |
| `AVOID_SPELL` | `72` |
| `MISS_PERCENTAGE` | `73` |
| `PHYSICAL_ARMOR_BASE_PERCENTAGE` | `74` |
| `PHYSICAL_ARMOR_TOTAL_PERCENTAGE` | `75` |
| `PHYSICAL_ARMOR_BONUS` | `76` |
| `PHYSICAL_ARMOR_BONUS_UNIQUE` | `77` |
| `PHYSICAL_ARMOR_BONUS_UNIQUE_ACTIVE` | `78` |
| `PHYSICAL_ARMOR_BONUS_POST` | `79` |
| `MIN_PHYSICAL_ARMOR` | `80` |
| `IGNORE_PHYSICAL_ARMOR` | `81` |
| `MAGICAL_RESISTANCE_BASE_REDUCTION` | `82` |
| `MAGICAL_RESISTANCE_DIRECT_MODIFICATION` | `83` |
| `MAGICAL_RESISTANCE_BONUS` | `84` |
| `MAGICAL_RESISTANCE_BONUS_ILLUSIONS` | `85` |
| `MAGICAL_RESISTANCE_BONUS_UNIQUE` | `86` |
| `MAGICAL_RESISTANCE_DECREPIFY_UNIQUE` | `87` |
| `BASE_MANA_REGEN` | `88` |
| `MANA_REGEN_CONSTANT` | `89` |
| `MANA_REGEN_CONSTANT_UNIQUE` | `90` |
| `MANA_REGEN_TOTAL_PERCENTAGE` | `91` |
| `HEALTH_REGEN_CONSTANT` | `92` |
| `HEALTH_REGEN_PERCENTAGE` | `93` |
| `HEALTH_REGEN_PERCENTAGE_UNIQUE` | `94` |
| `HEALTH_BONUS` | `95` |
| `MANA_BONUS` | `96` |
| `EXTRA_STRENGTH_BONUS` | `97` |
| `EXTRA_HEALTH_BONUS` | `98` |
| `EXTRA_MANA_BONUS` | `99` |
| `EXTRA_MANA_BONUS_PERCENTAGE` | `100` |
| `EXTRA_HEALTH_PERCENTAGE` | `101` |
| `EXTRA_MANA_PERCENTAGE` | `102` |
| `STATS_STRENGTH_BONUS` | `103` |
| `STATS_AGILITY_BONUS` | `104` |
| `STATS_INTELLECT_BONUS` | `105` |
| `STATS_STRENGTH_BONUS_PERCENTAGE` | `106` |
| `STATS_AGILITY_BONUS_PERCENTAGE` | `107` |
| `STATS_INTELLECT_BONUS_PERCENTAGE` | `108` |
| `STATS_INTELLECT_NONE` | `109` |
| `CAST_RANGE_BONUS` | `110` |
| `CAST_RANGE_BONUS_PERCENTAGE` | `111` |
| `CAST_RANGE_BONUS_TARGET` | `112` |
| `CAST_RANGE_BONUS_STACKING` | `113` |
| `ATTACK_RANGE_BASE_OVERRIDE` | `114` |
| `ATTACK_RANGE_BONUS` | `115` |
| `ATTACK_RANGE_BONUS_UNIQUE` | `116` |
| `ATTACK_RANGE_BONUS_PERCENTAGE` | `117` |
| `MAX_ATTACK_RANGE` | `118` |
| `PROJECTILE_SPEED_BONUS` | `119` |
| `PROJECTILE_SPEED_BONUS_PERCENTAGE` | `120` |
| `PROJECTILE_NAME` | `121` |
| `REINCARNATION` | `122` |
| `REINCARNATION_SUPPRESS_FX` | `123` |
| `RESPAWNTIME` | `124` |
| `RESPAWNTIME_PERCENTAGE` | `125` |
| `RESPAWNTIME_STACKING` | `126` |
| `COOLDOWN_PERCENTAGE` | `127` |
| `COOLDOWN_PERCENTAGE_ONGOING` | `128` |
| `CASTTIME_PERCENTAGE` | `129` |
| `ATTACK_ANIM_TIME_PERCENTAGE` | `130` |
| `MANACOST_PERCENTAGE` | `131` |
| `MANACOST_PERCENTAGE_STACKING` | `132` |
| `HEALTHCOST_PERCENTAGE` | `133` |
| `HEALTHCOST_PERCENTAGE_STACKING` | `134` |
| `DEATHGOLDCOST` | `135` |
| `PERCENTAGE_DEATHGOLDCOST` | `136` |
| `EXP_RATE_BOOST` | `137` |
| `GOLD_RATE_BOOST` | `138` |
| `KILL_ASSIST_GOLD_BOOST` | `139` |
| `CONVERT_EXP_TO_GOLD_PCT` | `140` |
| `PREATTACK_CRITICALSTRIKE` | `141` |
| `PREATTACK_TARGET_CRITICALSTRIKE` | `142` |
| `MAGICAL_CONSTANT_BLOCK` | `143` |
| `PHYSICAL_CONSTANT_BLOCK` | `144` |
| `PHYSICAL_CONSTANT_BLOCK_SPECIAL` | `145` |
| `PHYSICAL_CONSTANT_BLOCK_BONUS` | `146` |
| `INNATE_DAMAGE_BLOCK_PCT_OVERRIDE` | `147` |
| `TOTAL_CONSTANT_BLOCK_UNAVOIDABLE_PRE_ARMOR` | `148` |
| `TOTAL_CONSTANT_BLOCK` | `149` |
| `OVERRIDE_ANIMATION` | `150` |
| `OVERRIDE_ANIMATION_RATE` | `151` |
| `ABSORB_SPELL` | `152` |
| `REFLECT_SPELL` | `153` |
| `DISABLE_AUTOATTACK` | `154` |
| `BONUS_DAY_VISION` | `155` |
| `BONUS_DAY_VISION_PERCENTAGE` | `156` |
| `BONUS_NIGHT_VISION` | `157` |
| `BONUS_NIGHT_VISION_UNIQUE` | `158` |
| `BONUS_VISION_PERCENTAGE` | `159` |
| `FIXED_DAY_VISION` | `160` |
| `FIXED_NIGHT_VISION` | `161` |
| `MIN_HEALTH` | `162` |
| `MIN_MANA` | `163` |
| `ABSOLUTE_NO_DAMAGE_PHYSICAL` | `164` |
| `ABSOLUTE_NO_DAMAGE_MAGICAL` | `165` |
| `ABSOLUTE_NO_DAMAGE_PURE` | `166` |
| `IS_ILLUSION` | `167` |
| `ILLUSION_LABEL` | `168` |
| `STRONG_ILLUSION` | `169` |
| `SUPER_ILLUSION` | `170` |
| `SUPER_ILLUSION_WITH_ULTIMATE` | `171` |
| `XP_DURING_DEATH` | `172` |
| `TURN_RATE_PERCENTAGE` | `173` |
| `TURN_RATE_OVERRIDE` | `174` |
| `DISABLE_HEALING` | `175` |
| `DISABLE_MANA_GAIN` | `176` |
| `ALWAYS_ALLOW_ATTACK` | `177` |
| `ALWAYS_ETHEREAL_ATTACK` | `178` |
| `OVERRIDE_ATTACK_MAGICAL` | `179` |
| `UNIT_STATS_NEEDS_REFRESH` | `180` |
| `BOUNTY_CREEP_MULTIPLIER` | `181` |
| `BOUNTY_OTHER_MULTIPLIER` | `182` |
| `UNIT_DISALLOW_UPGRADING` | `183` |
| `DODGE_PROJECTILE` | `184` |
| `TRIGGER_COSMETIC_AND_END_ATTACK` | `185` |
| `PRIMARY_STAT_DAMAGE_MULTIPLIER` | `186` |
| `PREATTACK_DEADLY_BLOW` | `187` |
| `ALWAYS_AUTOATTACK_WHILE_HOLD_POSITION` | `188` |
| `PHYSICAL_ARMOR_PIERCING_PERCENTAGE_TARGET` | `189` |
| `MAGICAL_ARMOR_PIERCING_PERCENTAGE_TARGET` | `190` |
| `CRITICAL_STRIKE_BONUS` | `191` |
| `CONVERT_ATTACK_PHYSICAL_TO_PURE` | `192` |
| `BUFF_AMPLIFICATION` | `193` |
| `ON_SPELL_TARGET_READY` | `194` |
| `ON_ATTACK_RECORD` | `195` |
| `ON_ATTACK_START` | `196` |
| `ON_ATTACK` | `197` |
| `ON_ATTACK_LANDED` | `198` |
| `ON_ATTACK_FAIL` | `199` |
| `ON_ATTACK_ALLIED` | `200` |
| `ON_PROJECTILE_DODGE` | `201` |
| `ON_ORDER` | `202` |
| `ON_ORDER_RECEIVED` | `203` |
| `ON_UNIT_MOVED` | `204` |
| `ON_ABILITY_START` | `205` |
| `ON_ABILITY_EXECUTED` | `206` |
| `ON_ABILITY_FULLY_CAST` | `207` |
| `ON_BREAK_INVISIBILITY` | `208` |
| `ON_ABILITY_END_CHANNEL` | `209` |
| `ON_PROCESS_UPGRADE` | `210` |
| `ON_REFRESH` | `211` |
| `ON_TAKEDAMAGE` | `212` |
| `ON_DEATH_PREVENTED` | `213` |
| `ON_STATE_CHANGED` | `214` |
| `ON_ORB_EFFECT` | `215` |
| `ON_PROCESS_CLEAVE` | `216` |
| `ON_DAMAGE_CALCULATED` | `217` |
| `ON_MAGIC_DAMAGE_CALCULATED` | `218` |
| `ON_ATTACKED` | `219` |
| `ON_DEATH` | `220` |
| `ON_DEATH_COMPLETED` | `221` |
| `ON_RESPAWN` | `222` |
| `ON_SPENT_MANA` | `223` |
| `ON_SPENT_HEALTH` | `224` |
| `ON_SPENT_ITEM_CHARGE` | `225` |
| `ON_TELEPORTING` | `226` |
| `ON_TELEPORTED` | `227` |
| `ON_SET_LOCATION` | `228` |
| `ON_HEALTH_GAINED` | `229` |
| `ON_MANA_GAINED` | `230` |
| `ON_TAKEDAMAGE_KILLCREDIT` | `231` |
| `ON_HERO_KILLED` | `232` |
| `ON_HEAL_RECEIVED` | `233` |
| `ON_REDIRECT_HEALTH_GAIN` | `234` |
| `ON_BUILDING_KILLED` | `235` |
| `ON_MODEL_CHANGED` | `236` |
| `ON_MODIFIER_ADDED` | `237` |
| `ON_MODIFIER_REMOVED` | `238` |
| `ON_SCEPTER_UPGRADE_SELECTED` | `239` |
| `ON_SHARD_UPGRADE_SELECTED` | `240` |
| `TOOLTIP` | `241` |
| `MODEL_CHANGE` | `242` |
| `MODEL_SCALE` | `243` |
| `MODEL_SCALE_ANIMATE_TIME` | `244` |
| `MODEL_SCALE_USE_IN_OUT_EASE` | `245` |
| `MODEL_SCALE_CONSTANT` | `246` |
| `IS_SCEPTER` | `247` |
| `IS_SHARD` | `248` |
| `RADAR_COOLDOWN_REDUCTION` | `249` |
| `TRANSLATE_ACTIVITY_MODIFIERS` | `250` |
| `TRANSLATE_ATTACK_SOUND` | `251` |
| `LIFETIME_FRACTION` | `252` |
| `PROVIDES_FOW_POSITION` | `253` |
| `SPELLS_REQUIRE_HP` | `254` |
| `CONVERT_MANA_COST_TO_HEALTH_COST` | `255` |
| `FORCE_DRAW_MINIMAP` | `256` |
| `DISABLE_TURNING` | `257` |
| `IGNORE_CAST_ANGLE` | `258` |
| `CHANGE_ABILITY_VALUE` | `259` |
| `OVERRIDE_ABILITY_SPECIAL` | `260` |
| `OVERRIDE_ABILITY_SPECIAL_VALUE` | `261` |
| `ABILITY_LAYOUT` | `262` |
| `ON_DOMINATED` | `263` |
| `ON_KILL` | `264` |
| `ON_ASSIST` | `265` |
| `TEMPEST_DOUBLE` | `266` |
| `PRESERVE_PARTICLES_ON_MODEL_CHANGE` | `267` |
| `ON_ATTACK_FINISHED` | `268` |
| `IGNORE_COOLDOWN` | `269` |
| `CAN_ATTACK_TREES` | `270` |
| `VISUAL_Z_DELTA` | `271` |
| `VISUAL_Z_SPEED_BASE_OVERRIDE` | `272` |
| `INCOMING_DAMAGE_ILLUSION` | `273` |
| `DONT_GIVE_VISION_OF_ATTACKER` | `274` |
| `TOOLTIP2` | `275` |
| `ON_ATTACK_RECORD_DESTROY` | `276` |
| `ON_PROJECTILE_OBSTRUCTION_HIT` | `277` |
| `SUPPRESS_TELEPORT` | `278` |
| `ON_ATTACK_CANCELLED` | `279` |
| `SUPPRESS_CLEAVE` | `280` |
| `BOT_ATTACK_SCORE_BONUS` | `281` |
| `ATTACKSPEED_REDUCTION_PERCENTAGE` | `282` |
| `MOVESPEED_REDUCTION_PERCENTAGE` | `283` |
| `ATTACK_WHILE_MOVING_TARGET` | `284` |
| `ATTACKSPEED_PERCENTAGE` | `285` |
| `ON_ATTEMPT_PROJECTILE_DODGE` | `286` |
| `COOLDOWN_PERCENTAGE_STACKING` | `287` |
| `SPELL_REDIRECT_TARGET` | `288` |
| `TURN_RATE_CONSTANT` | `289` |
| `PACK_RAT` | `290` |
| `PHYSICALDAMAGEOUTGOING_PERCENTAGE` | `291` |
| `KNOCKBACK_AMPLIFICATION_PERCENTAGE` | `292` |
| `HEALTHBAR_PIPS` | `293` |
| `INCOMING_DAMAGE_CONSTANT` | `294` |
| `SPELL_APPLIED_SUCCESSFULLY` | `295` |
| `AVOID_DAMAGE_AFTER_REDUCTIONS` | `296` |
| `FAIL_ATTACK` | `297` |
| `PREREDUCE_INCOMING_DAMAGE_MULT` | `298` |
| `SUPPRESS_FULLSCREEN_DEATH_FX` | `299` |
| `INCOMING_DAMAGE_CONSTANT_POST` | `300` |
| `DAMAGEOUTGOING_PERCENTAGE_MULTIPLICATIVE` | `301` |
| `TICK_GOLD_MULTIPLIER` | `302` |
| `SLOW_RESISTANCE_UNIQUE` | `303` |
| `SLOW_RESISTANCE_STACKING` | `304` |
| `SLOW_RESISTANCE_APPLIES_TO_ATTACKS` | `305` |
| `AOE_BONUS_PERCENTAGE` | `306` |
| `PROJECTILE_SPEED` | `307` |
| `PROJECTILE_SPEED_TARGET` | `308` |
| `BECOME_STRENGTH` | `309` |
| `BECOME_AGILITY` | `310` |
| `BECOME_INTELLIGENCE` | `311` |
| `BECOME_UNIVERSAL` | `312` |
| `ON_FORCE_PROC_MAGIC_STICK` | `313` |
| `ON_DAMAGE_HPLOSS` | `314` |
| `SHARE_XPRUNE` | `315` |
| `XP_FOUNTAIN_COUNTDOWN_TIME_OVERRIDE` | `316` |
| `NO_FREE_TP_SCROLL_ON_DEATH` | `317` |
| `HAS_BONUS_NEUTRAL_ITEM_CHOICE` | `318` |
| `HAS_BONUS_NEUTRAL_ITEM_PASSIVE` | `319` |
| `PRESERVE_NEUTRAL_ITEM_PASSIVES` | `320` |
| `FORCE_MAX_HEALTH` | `321` |
| `FORCE_MAX_MANA` | `322` |
| `AOE_BONUS_CONSTANT` | `323` |
| `AOE_BONUS_CONSTANT_STACKING` | `324` |
| `ON_TAKEDAMAGE_POST_UNAVOIDABLE_BLOCK` | `325` |
| `ON_MUTE_DAMAGE_ABILITIES` | `326` |
| `SUPPRESS_CRIT` | `327` |
| `ABILITY_POINTS` | `328` |
| `BUYBACK_PENALTY_PERCENT` | `329` |
| `ITEM_SELLBACK_COST` | `330` |
| `DISASSEMBLE_ANYTHING` | `331` |
| `FIXED_MANA_REGEN` | `332` |
| `BONUS_UPHILL_MISS_CHANCE` | `333` |
| `CREEP_DENY_PERCENT` | `334` |
| `ATTACKSPEED_ABSOLUTE_MAX` | `335` |
| `FOW_TEAM` | `336` |
| `ON_HERO_BEGIN_DYING` | `337` |
| `BONUS_LOTUS_HEAL` | `338` |
| `BASE_HP_REGEN_PER_STR_BONUS_PERCENTAGE` | `339` |
| `BASE_ARMOR_PER_AGI_BONUS_PERCENTAGE` | `340` |
| `BASE_ATTACKSPEED_PER_AGI_BONUS_PERCENTAGE` | `341` |
| `BASE_MP_REGEN_PER_INT_BONUS_PERCENTAGE` | `342` |
| `BASE_MRES_PER_INT_BONUS_PERCENTAGE` | `343` |
| `ON_DAY_STARTED` | `344` |
| `ON_NIGHT_STARTED` | `345` |
| `CREATE_BONUS_ILLUSION_CHANCE` | `346` |
| `CREATE_BONUS_ILLUSION_COUNT` | `347` |
| `PSEUDORANDOM_BONUS` | `348` |
| `ATTACK_HEIGHT_BONUS` | `349` |
| `SKIP_ATTACK_REGULATOR` | `350` |
| `MISS_PERCENTAGE_TARGET` | `351` |
| `ADDITIONAL_NEUTRAL_ITEM_DROPS` | `352` |
| `KILL_STREAK_BONUS_GOLD_PERCENTAGE` | `353` |
| `HP_REGEN_MULTIPLIER_PRE_AMPLIFICATION` | `354` |
| `HEROFACET_OVERRIDE` | `355` |
| `ON_TREE_CUT_DOWN` | `356` |
| `ON_CLEAVE_ATTACK_LANDED` | `357` |
| `MIN_ATTRIBUTE_LEVEL` | `358` |
| `TIER_TOKEN_REROLL` | `359` |
| `VISION_DEGREES_RESTRICTION` | `360` |
| `TOTAL_CONSTANT_BLOCK_STACKING` | `361` |
| `INVENTORY_SLOT_RESTRICTED` | `362` |
| `ON_TIER_TOKEN_REROLLED` | `363` |
| `REDIRECT_SPELL` | `364` |
| `BASEATTACK_POSTBONUS` | `365` |
| `ON_FOW_TEAM_CHANGED` | `366` |
| `SUPPRESS_ATTACK_PROCS` | `367` |
| `ON_ABILITY_TOGGLED` | `368` |
| `AVOID_ATTACK_PROCS` | `369` |
| `ON_RUNE_SPAWN` | `370` |
| `PHYSICAL_LIFESTEAL` | `371` |
| `MAGICAL_LIFESTEAL` | `372` |
| `ON_PURE_DAMAGE_CALCULATED` | `373` |
| `NEUTRAL_TRINKET_OPTIONS` | `374` |
| `NEUTRAL_ENHANCEMENT_OPTIONS` | `375` |
| `MOVESPEED_MAX_BONUS_CONSTANT` | `376` |
| `MOVESPEED_POST_MULTIPLIER_BONUS_CONSTANT` | `377` |
| `FORBID_ILLUSIONS` | `378` |
| `MANACOST_OVERRIDE` | `379` |
| `RESTORATION_AMPLIFICATION` | `380` |
| `RESTORATION_AMPLIFICATION_UNIQUE` | `381` |
| `HEAL_AMPLIFY_PERCENTAGE_SOURCE_UNIQUE` | `382` |
| `REDIRECT_HEALTH_GAIN` | `383` |
| `SUPPRESS_INCOMING_CRIT` | `384` |
| `UPGRADE_NEUTRAL_ARTIFACTS` | `385` |
| `SUPPRESS_INVALID_MOVE_ATTACK_ORDERS` | `386` |
| `CONSUMABLE_USE_SPEED` | `387` |
| `REQUIRED_LEVEL` | `388` |
| `ON_MODIFIER_REFRESHED` | `389` |
| `ON_ABILITY_SWAPPED` | `390` |
| `OVERRIDE_CREEP_BOUNTY` | `391` |
| `OVERRIDE_BASE_DAMAGE` | `392` |
| `UNTARGETABLE_FROM` | `393` |
| `UNTARGETABLE_TO` | `394` |
| `SUPER_ILLUSION_WITH_ITEMS` | `395` |
| `ON_PURGE` | `396` |
| `ON_ILLUSION_CREATED` | `397` |
| `HEROLEVELSCALE` | `398` |
| `INVALID` | `65535` |

### ModifierPriority

| Member | Value |
| --- | --- |
| `LOW` | `0` |
| `NORMAL` | `1` |
| `HIGH` | `2` |
| `ULTRA` | `3` |
| `SUPER_ULTRA` | `4` |

### ModifierRemove

| Member | Value |
| --- | --- |
| `ALL` | `0` |
| `ENEMY` | `1` |
| `ALLY` | `2` |

### ModifierState

| Member | Value |
| --- | --- |
| `ROOTED` | `0` |
| `DISARMED` | `1` |
| `ATTACK_IMMUNE` | `2` |
| `SILENCED` | `3` |
| `MUTED` | `4` |
| `STUNNED` | `5` |
| `HEXED` | `6` |
| `INVISIBLE` | `7` |
| `INVULNERABLE` | `8` |
| `MAGIC_IMMUNE` | `9` |
| `PROVIDES_VISION` | `10` |
| `NIGHTMARED` | `11` |
| `BLOCK_DISABLED` | `12` |
| `EVADE_DISABLED` | `13` |
| `UNSELECTABLE` | `14` |
| `CANNOT_TARGET_ENEMIES` | `15` |
| `CANNOT_TARGET_BUILDINGS` | `16` |
| `CANNOT_MISS` | `17` |
| `SPECIALLY_DENIABLE` | `18` |
| `FROZEN` | `19` |
| `COMMAND_RESTRICTED` | `20` |
| `NOT_ON_MINIMAP` | `21` |
| `LOW_ATTACK_PRIORITY` | `22` |
| `NO_HEALTH_BAR` | `23` |
| `NO_HEALTH_BAR_FOR_ENEMIES` | `24` |
| `NO_HEALTH_BAR_FOR_OTHER_PLAYERS` | `25` |
| `FLYING` | `26` |
| `NO_UNIT_COLLISION` | `27` |
| `NO_TEAM_MOVE_TO` | `28` |
| `NO_TEAM_SELECT` | `29` |
| `PASSIVES_DISABLED` | `30` |
| `DOMINATED` | `31` |
| `BLIND` | `32` |
| `OUT_OF_GAME` | `33` |
| `FAKE_ALLY` | `34` |
| `FLYING_FOR_PATHING_PURPOSES_ONLY` | `35` |
| `TRUESIGHT_IMMUNE` | `36` |
| `UNTARGETABLE` | `37` |
| `UNTARGETABLE_ALLIED` | `38` |
| `UNTARGETABLE_ENEMY` | `39` |
| `UNTARGETABLE_SELF` | `40` |
| `IGNORING_MOVE_AND_ATTACK_ORDERS` | `41` |
| `ALLOW_PATHING_THROUGH_TREES` | `42` |
| `NOT_ON_MINIMAP_FOR_ENEMIES` | `43` |
| `UNSLOWABLE` | `44` |
| `TETHERED` | `45` |
| `IGNORING_STOP_ORDERS` | `46` |
| `FEARED` | `47` |
| `TAUNTED` | `48` |
| `CANNOT_BE_MOTION_CONTROLLED` | `49` |
| `FORCED_FLYING_VISION` | `50` |
| `ATTACK_ALLIES` | `51` |
| `ALLOW_PATHING_THROUGH_CLIFFS` | `52` |
| `ALLOW_PATHING_THROUGH_POWER_COGS` | `53` |
| `SPECIALLY_UNDENIABLE` | `54` |
| `ALLOW_PATHING_THROUGH_OBSTRUCTIONS` | `55` |
| `DEBUFF_IMMUNE` | `56` |
| `ALLOW_PATHING_THROUGH_BASE_BLOCKER` | `57` |
| `IGNORING_MOVE_ORDERS` | `58` |
| `ATTACKS_ARE_MELEE` | `59` |
| `CAN_USE_BACKPACK_ITEMS` | `60` |
| `CASTS_IGNORE_CHANNELING` | `61` |
| `ATTACKS_DONT_REVEAL` | `62` |
| `NEUTRALS_DONT_ATTACK` | `63` |

### ModifyGoldReason

| Member | Value |
| --- | --- |
| `UNSPECIFIED` | `0` |
| `DEATH` | `1` |
| `BUYBACK` | `2` |
| `PURCHASE_CONSUMABLE` | `3` |
| `PURCHASE_ITEM` | `4` |
| `ABANDONED_REDISTRIBUTE` | `5` |
| `SELL_ITEM` | `6` |
| `ABILITY_COST` | `7` |
| `CHEAT_COMMAND` | `8` |
| `SELECTION_PENALTY` | `9` |
| `GAME_TICK` | `10` |
| `BUILDING` | `11` |
| `HERO_KILL` | `12` |
| `CREEP_KILL` | `13` |
| `NEUTRAL_KILL` | `14` |
| `ROSHAN_KILL` | `15` |
| `COURIER_KILL` | `16` |
| `BOUNTY_RUNE` | `17` |
| `SHARED_GOLD` | `18` |
| `ABILITY_GOLD` | `19` |
| `WARD_KILL` | `20` |
| `COURIER_KILLED_BY_THIS_PLAYER` | `21` |

### ModifyXpReason

| Member | Value |
| --- | --- |
| `UNSPECIFIED` | `0` |
| `HERO_KILL` | `1` |
| `CREEP_KILL` | `2` |
| `ROSHAN_KILL` | `3` |
| `TOME_OF_KNOWLEDGE` | `4` |
| `OUTPOST` | `5` |
| `CATCH_UP` | `6` |
| `HERO_ABILITY` | `7` |
| `MAX` | `8` |

### MotionControllerPriority

| Member | Value |
| --- | --- |
| `LOWEST` | `0` |
| `LOW` | `1` |
| `MEDIUM` | `2` |
| `HIGH` | `3` |
| `HIGHEST` | `4` |
| `ULTRA` | `5` |

### MusicStatus

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `EXPLORATION` | `1` |
| `BATTLE` | `2` |
| `PRE_GAME_EXPLORATION` | `3` |
| `DEAD` | `4` |
| `LAST` | `5` |

### OverheadAlert

| Member | Value |
| --- | --- |
| `GOLD` | `0` |
| `DENY` | `1` |
| `CRITICAL` | `2` |
| `XP` | `3` |
| `BONUS_SPELL_DAMAGE` | `4` |
| `MISS` | `5` |
| `DAMAGE` | `6` |
| `EVADE` | `7` |
| `BLOCK` | `8` |
| `BONUS_POISON_DAMAGE` | `9` |
| `HEAL` | `10` |
| `MANA_ADD` | `11` |
| `MANA_LOSS` | `12` |
| `MAGICAL_BLOCK` | `16` |
| `INCOMING_DAMAGE` | `17` |
| `OUTGOING_DAMAGE` | `18` |
| `DISABLE_RESIST` | `19` |
| `DEATH` | `20` |
| `BLOCKED` | `21` |
| `ITEM_RECEIVED` | `22` |
| `SHARD` | `23` |
| `DEADLY_BLOW` | `24` |
| `FORCE_MISS` | `25` |
| `AEGIS` | `26` |
| `DISPEL` | `27` |
| `BONUS_PURE_DAMAGE` | `28` |

### ParticleAttachment

| Member | Value |
| --- | --- |
| `INVALID` | `-1` |
| `ABSORIGIN` | `0` |
| `ABSORIGIN_FOLLOW` | `1` |
| `CUSTOMORIGIN` | `2` |
| `CUSTOMORIGIN_FOLLOW` | `3` |
| `POINT` | `4` |
| `POINT_FOLLOW` | `5` |
| `EYES_FOLLOW` | `6` |
| `OVERHEAD_FOLLOW` | `7` |
| `WORLDORIGIN` | `8` |
| `ROOTBONE_FOLLOW` | `9` |
| `RENDERORIGIN_FOLLOW` | `10` |
| `MAIN_VIEW` | `11` |
| `WATERWAKE` | `12` |
| `CENTER_FOLLOW` | `13` |
| `CUSTOM_GAME_STATE_1` | `14` |
| `HEALTHBAR` | `15` |

### PostGameColumn

| Member | Value |
| --- | --- |
| `LEVEL` | `0` |
| `ITEMS` | `1` |
| `KILLS` | `2` |
| `DEATHS` | `3` |
| `ASSISTS` | `4` |
| `NET_WORTH` | `5` |
| `LAST_HITS` | `6` |
| `DENIES` | `7` |
| `DAMAGE` | `8` |
| `HEALING` | `9` |
| `MAX` | `10` |

### PostGameLayout

| Member | Value |
| --- | --- |
| `DOUBLE_COLUMN` | `0` |
| `SINGLE_COLUMN` | `1` |
| `MAX` | `2` |

### ProjectileAttachment

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `ATTACK_1` | `1` |
| `ATTACK_2` | `2` |
| `HITLOCATION` | `3` |
| `ATTACK_3` | `4` |
| `ATTACK_4` | `5` |

### PseudoRandom

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `MAGNUS_SHARD` | `1` |
| `PHANTOMASSASSIN_CRIT` | `2` |
| `PHANTOMASSASSIN_DAGGER` | `3` |
| `PHANTOMLANCER_JUXTAPOSE` | `4` |
| `TINY_CRAGGY` | `5` |
| `COLD_REBUKE` | `6` |
| `WOLF_CRIT` | `7` |
| `AXE_HELIX` | `8` |
| `AXE_HELIX_ATTACK` | `9` |
| `LEGION_MOMENT` | `10` |
| `SLARDAR_BASH` | `11` |
| `OD_ESSENCE` | `12` |
| `DROW_MARKSMANSHIP` | `13` |
| `OGRE_MAGI_FIREBLAST` | `14` |
| `OGRE_ITEM_MULTICAST` | `15` |
| `SPIRITBREAKER_GREATERBASH` | `16` |
| `LONE_DRUID_ENTANGLE` | `17` |
| `FACELESS_BASH` | `18` |
| `FACELESS_EVADE_SPELL` | `19` |
| `FACELESS_EVADE_ATTACK` | `20` |
| `FACELESS_VOID_BACKTRACK` | `21` |
| `BREWMASTER_CRIT` | `22` |
| `BREWMASTER_CINDER_BREW` | `23` |
| `SNIPER_HEADSHOT` | `24` |
| `ATOS` | `25` |
| `JUGG_CRIT` | `26` |
| `DAZZLE_SCEPTER` | `27` |
| `CHAOS_CRIT` | `28` |
| `LYCAN_CRIT` | `29` |
| `TUSK_CRIT` | `30` |
| `CM_FREEZING_FIELD` | `31` |
| `GENERIC_BASHER` | `32` |
| `SKELETONKING_CRIT` | `33` |
| `SKELETONKING_CRIT_MORTAL` | `34` |
| `ITEM_GREATERCRIT` | `35` |
| `ITEM_LESSERCRIT` | `36` |
| `ITEM_BASHER` | `37` |
| `ITEM_SOLAR_CREST` | `38` |
| `ITEM_JAVELIN_ACCURACY` | `39` |
| `ITEM_TRIDENT` | `40` |
| `ITEM_ABYSSAL` | `41` |
| `ITEM_ABYSSAL_BLOCK` | `42` |
| `ITEM_STOUT` | `43` |
| `ITEM_VANGUARD` | `44` |
| `ITEM_CRIMSON_GUARD` | `45` |
| `ITEM_PMS` | `46` |
| `ITEM_HALBRED_MAIM` | `47` |
| `ITEM_SANGEYASHA_MAIM` | `48` |
| `ITEM_SANGEKAYA_MAIM` | `49` |
| `ITEM_SANGE_MAIM` | `50` |
| `ITEM_BUTTERFLY` | `51` |
| `ITEM_MAELSTROM` | `52` |
| `ITEM_MJOLLNIR` | `53` |
| `ITEM_MJOLLNIR_STATIC` | `54` |
| `ITEM_MKB` | `55` |
| `ITEM_SILVER_EDGE` | `56` |
| `ITEM_NAGINATA` | `57` |
| `TROLL_BASH` | `58` |
| `RIKI_SMOKE_SCREEN` | `59` |
| `CHAOS_DOUBLE_CRIT` | `60` |
| `CHAOS_TRIPLE_CRIT` | `61` |
| `GENERIC_EVASION` | `62` |
| `GENERIC_HEIGHT_MISS` | `63` |
| `GENERIC_MISS` | `64` |
| `ARMADILLO_HEARTPIERCER` | `65` |
| `MARS_SHIELD` | `66` |
| `CHAOS_KNIGHT_INNATE_REFUND` | `67` |
| `NEUTRAL_DROP_TIER_1` | `68` |
| `NEUTRAL_DROP_TIER_2` | `69` |
| `NEUTRAL_DROP_TIER_3` | `70` |
| `NEUTRAL_DROP_TIER_4` | `71` |
| `NEUTRAL_DROP_TIER_5` | `72` |
| `MARS_BULWARK` | `73` |
| `MUERTA_GUNSLINGER` | `74` |
| `TROLL_FERVOR_SHARD` | `75` |
| `SNAPFIRE_GLANCING` | `76` |
| `PANGOLIER_PARRY` | `77` |
| `HOODWINK_REDIRECT` | `78` |
| `KEZ_SAI` | `79` |
| `CHAOS_KNIGHT_HAVOC` | `80` |
| `LARGO_FROGSTOMP` | `81` |
| `NAGA_RIPTIDE` | `82` |
| `CUSTOM_GENERIC` | `83` |
| `CUSTOM_GAME_1` | `84` |
| `CUSTOM_GAME_2` | `85` |
| `CUSTOM_GAME_3` | `86` |
| `CUSTOM_GAME_4` | `87` |
| `CUSTOM_GAME_5` | `88` |
| `CUSTOM_GAME_6` | `89` |
| `CUSTOM_GAME_7` | `90` |
| `CUSTOM_GAME_8` | `91` |
| `CUSTOM_GAME_9` | `92` |

### QuestTextReplaceValue

| Member | Value |
| --- | --- |
| `CURRENT_VALUE` | `0` |
| `TARGET_VALUE` | `1` |
| `ROUND` | `2` |
| `REWARD` | `3` |

### RuneType

| Member | Value |
| --- | --- |
| `INVALID` | `-1` |
| `DOUBLEDAMAGE` | `0` |
| `HASTE` | `1` |
| `ILLUSION` | `2` |
| `INVISIBILITY` | `3` |
| `REGENERATION` | `4` |
| `BOUNTY` | `5` |
| `ARCANE` | `6` |
| `WATER` | `7` |
| `XP` | `8` |
| `SHIELD` | `9` |

### ShopType

| Member | Value |
| --- | --- |
| `HOME` | `0` |
| `SIDE` | `1` |
| `SECRET` | `2` |
| `GROUND` | `3` |
| `SIDE_2` | `4` |
| `SECRET_2` | `5` |
| `CUSTOM` | `6` |
| `NEUTRALS` | `7` |
| `NONE` | `8` |

### ShowGenericPopupType

| Member | Value |
| --- | --- |
| `TINT_SCREEN` | `1` |
| `SHOW_NO_OTHER_DIALOGS` | `2` |

### SourceEngineAnimationEvent

https://developer.valvesoftware.com/wiki/Animation_Events#Server_events

| Member | Value |
| --- | --- |
| `EMPTY` | `0` |
| `CL_PLAYSOUND` | `1` |
| `CL_PLAYSOUND_ATTACHMENT` | `2` |
| `CL_PLAYSOUND_POSITION` | `3` |
| `SV_PLAYSOUND` | `4` |
| `CL_STOPSOUND` | `5` |
| `CL_PLAYSOUND_LOOPING` | `6` |
| `CL_CREATE_PARTICLE_EFFECT` | `7` |
| `CL_STOP_PARTICLE_EFFECT` | `8` |
| `CL_CREATE_PARTICLE_EFFECT_CFG` | `9` |
| `SV_CREATE_PARTICLE_EFFECT_CFG` | `10` |
| `SV_STOP_PARTICLE_EFFECT` | `11` |
| `FOOTSTEP` | `12` |
| `CL_STOP_RAGDOLL_CONTROL` | `13` |
| `CL_ENABLE_BODYGROUP` | `14` |
| `CL_DISABLE_BODYGROUP` | `15` |
| `BODYGROUP_SET_VALUE` | `16` |
| `WEAPON_PERFORM_ATTACK` | `17` |
| `FIRE_INPUT` | `18` |
| `CL_CLOTH_ATTR` | `19` |
| `CL_CLOTH_GROUND_OFFSET` | `20` |
| `CL_CLOTH_STIFFEN` | `21` |
| `CL_CLOTH_EFFECT` | `22` |
| `CL_CREATE_ANIM_SCOPE_PROP` | `23` |
| `SV_IKLOCK` | `24` |
| `PULSE_GRAPH` | `25` |
| `DISABLE_PLATFORM` | `26` |
| `ENABLE_PLATFORM_PLAYER_FOLLOWS_YAW` | `27` |
| `ENABLE_PLATFORM_PLAYER_IGNORES_YAW` | `28` |
| `DESTRUCTIBLE_PART_DESTROY` | `29` |
| `CL_SUPPRESS_EVENTS_WITH_TAG` | `30` |
| `CL_HIDE_PARTICLE_EFFECT` | `31` |
| `CL_SHOW_PARTICLE_EFFECT` | `32` |
| `CL_ADD_PARTICLE_EFFECT_CP` | `33` |
| `CL_SPEECH` | `34` |
| `CL_PANORAMA_EVENT` | `35` |
| `CL_DOTA_PLAY_STATUS_EFFECT` | `36` |
| `CL_DOTA_STOP_STATUS_EFFECT` | `37` |
| `CL_DOTA_NPC_CREATE_PARTICLE_EFFECT` | `38` |
| `CL_DOTA_RUBICK_ARCANA_CREATE_PARTICLE_EFFECT` | `39` |
| `DOTA_PET_ITEM_PICKUP` | `40` |
| `DOTA_PET_ITEM_DROP` | `41` |
| `DOTA_SUPPRESS_CONSTANT_LAYER` | `42` |
| `DOTA_PLAY_SOUND_ATTACK_SPECIAL` | `43` |
| `DOTA_CREATE_CLINKZ_ATTACK` | `44` |
| `DOTA_PLAY_SOUND_ATTACK_BACKSTAB` | `45` |
| `DOTA_DIE_PHANTOM_DEATH_PARTICLES` | `46` |
| `DOTA_SWITCH_ATTACK_COMBO` | `47` |
| `EF_NODRAW` | `48` |
| `EF_DRAW` | `49` |
| `DOTA_PLAY_SOUND_ATTACK` | `50` |
| `CL_CREATE_PARTICLE_BRASS` | `51` |

### SourceEngineDamageTypes

https://developer.valvesoftware.com/wiki/Damage_types

| Member | Value |
| --- | --- |
| `GENERIC` | `0` |
| `CRUSH` | `1` |
| `BULLET` | `2` |
| `SLASH` | `4` |
| `BURN` | `8` |
| `VEHICLE` | `16` |
| `FALL` | `32` |
| `BLAST` | `64` |
| `CLUB` | `128` |
| `SHOCK` | `256` |
| `SONIC` | `512` |
| `ENERGYBEAM` | `1024` |
| `PREVENT_PHYSICS_FORCE` | `2048` |
| `NEVERGIB` | `4096` |
| `ALWAYSGIB` | `8192` |
| `DROWN` | `16384` |
| `PARALYZE` | `32768` |
| `NERVEGAS` | `65536` |
| `POISON` | `131072` |
| `RADIATION` | `262144` |

### SourceEngineSoundData

https://developer.valvesoftware.com/wiki/Weapon_script#SoundData

| Member | Value |
| --- | --- |
| `EMPTY` | `0` |
| `SINGLE_SHOT` | `2` |
| `DOUBLE_SHOT` | `3` |
| `MELEE_MISS` | `4` |
| `MELEE_HIT` | `5` |
| `MELEE_HIT_WORLD` | `6` |
| `SPECIAL_1` | `9` |
| `SPECIAL_2` | `10` |
| `SPECIAL_3` | `11` |

### SpeechType

| Member | Value |
| --- | --- |
| `USER_INVALID` | `0` |
| `USER_SINGLE` | `1` |
| `USER_TEAM` | `2` |
| `USER_TEAM_NEARBY` | `3` |
| `USER_NEARBY` | `4` |
| `USER_ALL` | `5` |
| `GOOD_TEAM` | `6` |
| `BAD_TEAM` | `7` |
| `SPECTATOR` | `8` |
| `USER_TEAM_NOSPECTATOR` | `9` |
| `RECIPIENT_TYPE_MAX` | `10` |

### SubquestTextReplaceValue

| Member | Value |
| --- | --- |
| `TEXT_REPLACE_CURRENT_VALUE` | `0` |
| `TEXT_REPLACE_TARGET_VALUE` | `1` |
| `NUM_TEXT_REPLACES` | `2` |

### UnitAttackCapability

| Member | Value |
| --- | --- |
| `NO_ATTACK` | `0` |
| `MELEE_ATTACK` | `1` |
| `RANGED_ATTACK` | `2` |
| `RANGED_ATTACK_DIRECTIONAL` | `4` |

### UnitFilterResult

| Member | Value |
| --- | --- |
| `SUCCESS` | `0` |
| `FAIL_FRIENDLY` | `1` |
| `FAIL_ENEMY` | `2` |
| `FAIL_HERO` | `3` |
| `FAIL_CONSIDERED_HERO` | `4` |
| `FAIL_CREEP` | `5` |
| `FAIL_BUILDING` | `6` |
| `FAIL_COURIER` | `7` |
| `FAIL_OTHER` | `8` |
| `FAIL_ANCIENT` | `9` |
| `FAIL_ILLUSION` | `10` |
| `FAIL_SUMMONED` | `11` |
| `FAIL_DOMINATED` | `12` |
| `FAIL_MELEE` | `13` |
| `FAIL_RANGED` | `14` |
| `FAIL_DEAD` | `15` |
| `FAIL_MAGIC_IMMUNE_ALLY` | `16` |
| `FAIL_MAGIC_IMMUNE_ENEMY` | `17` |
| `FAIL_INVULNERABLE` | `18` |
| `FAIL_IN_FOW` | `19` |
| `FAIL_INVISIBLE` | `20` |
| `FAIL_NOT_PLAYER_CONTROLLED` | `21` |
| `FAIL_ATTACK_IMMUNE` | `22` |
| `FAIL_CUSTOM` | `23` |
| `FAIL_INVALID_LOCATION` | `24` |
| `FAIL_DISABLE_HELP` | `25` |
| `FAIL_OUT_OF_WORLD` | `26` |
| `FAIL_NIGHTMARED` | `27` |
| `FAIL_OBSTRUCTED` | `28` |

### UnitMoveCapability

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `GROUND` | `1` |
| `FLY` | `2` |

### UnitOrder

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `MOVE_TO_POSITION` | `1` |
| `MOVE_TO_TARGET` | `2` |
| `ATTACK_MOVE` | `3` |
| `ATTACK_TARGET` | `4` |
| `CAST_POSITION` | `5` |
| `CAST_TARGET` | `6` |
| `CAST_TARGET_TREE` | `7` |
| `CAST_NO_TARGET` | `8` |
| `CAST_TOGGLE` | `9` |
| `HOLD_POSITION` | `10` |
| `TRAIN_ABILITY` | `11` |
| `DROP_ITEM` | `12` |
| `GIVE_ITEM` | `13` |
| `PICKUP_ITEM` | `14` |
| `PICKUP_RUNE` | `15` |
| `PURCHASE_ITEM` | `16` |
| `SELL_ITEM` | `17` |
| `DISASSEMBLE_ITEM` | `18` |
| `MOVE_ITEM` | `19` |
| `CAST_TOGGLE_AUTO` | `20` |
| `STOP` | `21` |
| `TAUNT` | `22` |
| `BUYBACK` | `23` |
| `GLYPH` | `24` |
| `EJECT_ITEM_FROM_STASH` | `25` |
| `CAST_RUNE` | `26` |
| `PING_ABILITY` | `27` |
| `MOVE_TO_DIRECTION` | `28` |
| `PATROL` | `29` |
| `VECTOR_TARGET_POSITION` | `30` |
| `RADAR` | `31` |
| `SET_ITEM_COMBINE_LOCK` | `32` |
| `CONTINUE` | `33` |
| `VECTOR_TARGET_CANCELED` | `34` |
| `CAST_RIVER_PAINT` | `35` |
| `PREGAME_ADJUST_ITEM_ASSIGNMENT` | `36` |
| `DROP_ITEM_AT_FOUNTAIN` | `37` |
| `TAKE_ITEM_FROM_NEUTRAL_ITEM_STASH` | `38` |
| `MOVE_RELATIVE` | `39` |
| `CAST_TOGGLE_ALT` | `40` |
| `CONSUME_ITEM` | `41` |
| `SET_ITEM_MARK_FOR_SELL` | `42` |

### UnitTargetFlags

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `RANGED_ONLY` | `2` |
| `MELEE_ONLY` | `4` |
| `DEAD` | `8` |
| `MAGIC_IMMUNE_ENEMIES` | `16` |
| `NOT_MAGIC_IMMUNE_ALLIES` | `32` |
| `INVULNERABLE` | `64` |
| `FOW_VISIBLE` | `128` |
| `NO_INVIS` | `256` |
| `CAN_BE_SEEN` | `384` |
| `NOT_ANCIENTS` | `512` |
| `PLAYER_CONTROLLED` | `1024` |
| `NOT_DOMINATED` | `2048` |
| `NOT_SUMMONED` | `4096` |
| `NOT_ILLUSIONS` | `8192` |
| `NOT_ATTACK_IMMUNE` | `16384` |
| `MANA_ONLY` | `32768` |
| `CHECK_DISABLE_HELP` | `65536` |
| `NOT_CREEP_HERO` | `131072` |
| `OUT_OF_WORLD` | `262144` |
| `NOT_NIGHTMARED` | `524288` |
| `PREFER_ENEMIES` | `1048576` |
| `RESPECT_OBSTRUCTIONS` | `2097152` |

### UnitTargetTeam

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `FRIENDLY` | `1` |
| `ENEMY` | `2` |
| `BOTH` | `3` |
| `CUSTOM` | `4` |

### UnitTargetType

| Member | Value |
| --- | --- |
| `NONE` | `0` |
| `HERO` | `1` |
| `CREEP` | `2` |
| `BUILDING` | `4` |
| `COURIER` | `16` |
| `BASIC` | `18` |
| `HEROES_AND_CREEPS` | `19` |
| `OTHER` | `32` |
| `ALL` | `55` |
| `TREE` | `64` |
| `CUSTOM` | `128` |
| `SELF` | `256` |

## Compatibility aliases

| Alias | Target | Description |
| --- | --- | --- |
| <a name="ability_types"></a>`ABILITY_TYPES` | `AbilityTypes` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="abilitylearnresult_t"></a>`AbilityLearnResult_t` | `AbilityLearnResult` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="attackfail"></a>`attackfail` | `AttackRecord` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="click_behaviors"></a>`CLICK_BEHAVIORS` | `ClickBehaviors` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="damage_types"></a>`DAMAGE_TYPES` | `DamageTypes` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="damagecategory_t"></a>`DamageCategory_t` | `DamageCategory` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_ability_behavior"></a>`DOTA_ABILITY_BEHAVIOR` | `AbilityBehavior` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_gamestate"></a>`DOTA_GameState` | `GameState` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_gc_team"></a>`DOTA_GC_TEAM` | `GcTeam` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_heropickstate"></a>`DOTA_HeroPickState` | `HeroPickState` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_invalid_orders"></a>`DOTA_INVALID_ORDERS` | `InvalidOrders` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_motion_controller_priority"></a>`DOTA_MOTION_CONTROLLER_PRIORITY` | `MotionControllerPriority` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_overhead_alert"></a>`DOTA_OVERHEAD_ALERT` | `OverheadAlert` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_runes"></a>`DOTA_RUNES` | `RuneType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_shop_type"></a>`DOTA_SHOP_TYPE` | `ShopType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_unit_target_flags"></a>`DOTA_UNIT_TARGET_FLAGS` | `UnitTargetFlags` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_unit_target_team"></a>`DOTA_UNIT_TARGET_TEAM` | `UnitTargetTeam` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dota_unit_target_type"></a>`DOTA_UNIT_TARGET_TYPE` | `UnitTargetType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaabilityspeaktrigger_t"></a>`DOTAAbilitySpeakTrigger_t` | `AbilitySpeakTrigger` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaconnectionstate_t"></a>`DOTAConnectionState_t` | `ConnectionState` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotacustomcameraeventflags_t"></a>`DOTACustomCameraEventFlags_t` | `CustomCameraEventFlags` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotadamageflag_t"></a>`DOTADamageFlag_t` | `DamageFlag` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotadefaultuielement_t"></a>`DotaDefaultUIElement_t` | `DefaultUiElement` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotahudvisibility_t"></a>`DOTAHUDVisibility_t` | `HudVisibility` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotainventoryflags_t"></a>`DOTAInventoryFlags_t` | `InventoryFlags` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaminimapevent_t"></a>`DOTAMinimapEvent_t` | `MinimapEventType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotamodifierattribute_t"></a>`DOTAModifierAttribute_t` | `ModifierAttribute` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotamusicstatus_t"></a>`DOTAMusicStatus_t` | `MusicStatus` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotapostgamecolumn_t"></a>`DOTAPostGameColumn_t` | `PostGameColumn` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotapostgamelayout_t"></a>`DOTAPostGameLayout_t` | `PostGameLayout` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaprojectileattachment_t"></a>`DOTAProjectileAttachment_t` | `ProjectileAttachment` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotascriptinventoryslot_t"></a>`DOTAScriptInventorySlot_t` | `InventorySlot` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaslottype_t"></a>`DOTASlotType_t` | `LoadoutType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaspeechtype_t"></a>`DOTASpeechType_t` | `SpeechType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotateam_t"></a>`DOTATeam_t` | `DotaTeam` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaunitattackcapability_t"></a>`DOTAUnitAttackCapability_t` | `UnitAttackCapability` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaunitmovecapability_t"></a>`DOTAUnitMoveCapability_t` | `UnitMoveCapability` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="dotaunitorder_t"></a>`dotaunitorder_t` | `UnitOrder` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="edota_modifygold_reason"></a>`EDOTA_ModifyGold_Reason` | `ModifyGoldReason` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="edota_modifyxp_reason"></a>`EDOTA_ModifyXP_Reason` | `ModifyXpReason` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="eshareability"></a>`EShareAbility` | `ItemShareability` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="gameactivity_t"></a>`GameActivity_t` | `GameActivity` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="luamodifiertype"></a>`LuaModifierType` | `LuaModifierMotionType` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="modifierfunction"></a>`modifierfunction` | `ModifierFunction` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="modifierpriority"></a>`modifierpriority` | `ModifierPriority` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="modifierremove"></a>`modifierremove` | `ModifierRemove` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="modifierstate"></a>`modifierstate` | `ModifierState` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="particleattachment_t"></a>`ParticleAttachment_t` | `ParticleAttachment` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="quest_text_replace_values_t"></a>`quest_text_replace_values_t` | `QuestTextReplaceValue` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
| <a name="subquest_text_replace_values_t"></a>`subquest_text_replace_values_t` | `SubquestTextReplaceValue` | **Deprecated:** Non-normalized enum name. Defined only for library compatibility.<br> |
