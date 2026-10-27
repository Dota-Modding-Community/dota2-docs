# Dota game event declarations



365 typed game events.

<details><summary>Events</summary>

- [account_all_hero_challenge_changed](#account_all_hero_challenge_changed)
- [achievement_earned](#achievement_earned)
- [achievement_event](#achievement_event)
- [achievement_write_failed](#achievement_write_failed)
- [aegis_event](#aegis_event)
- [antiaddiction_toast](#antiaddiction_toast)
- [bindpanel_close](#bindpanel_close)
- [bindpanel_open](#bindpanel_open)
- [bonus_updated](#bonus_updated)
- [booster_state_updated](#booster_state_updated)
- [bot_takeover](#bot_takeover)
- [bought_back](#bought_back)
- [break_breakable](#break_breakable)
- [break_prop](#break_prop)
- [broken_breakable](#broken_breakable)
- [cart_updated](#cart_updated)
- [chat_members_changed](#chat_members_changed)
- [chat_new_message](#chat_new_message)
- [client_disconnect](#client_disconnect)
- [client_reload_game_keyvalues](#client_reload_game_keyvalues)
- [clientside_lesson_closed](#clientside_lesson_closed)
- [colorblind_mode_changed](#colorblind_mode_changed)
- [community_cached_names_updated](#community_cached_names_updated)
- [custom_game_friends_played_updated](#custom_game_friends_played_updated)
- [custom_game_lobby_list_updated](#custom_game_lobby_list_updated)
- [custom_game_mode_list_updated](#custom_game_mode_list_updated)
- [custom_game_player_count_updated](#custom_game_player_count_updated)
- [custom_games_friends_play_updated](#custom_games_friends_play_updated)
- [dashboard_caches_cleared](#dashboard_caches_cleared)
- [dashboard_switched_section](#dashboard_switched_section)
- [defeated](#defeated)
- [demo_skip](#demo_skip)
- [demo_start](#demo_start)
- [demo_stop](#demo_stop)
- [difficulty_changed](#difficulty_changed)
- [door_close](#door_close)
- [dota_ability_changed](#dota_ability_changed)
- [dota_ability_channel_finished](#dota_ability_channel_finished)
- [dota_action_item](#dota_action_item)
- [dota_action_success](#dota_action_success)
- [dota_ad_ban](#dota_ad_ban)
- [dota_ad_ban_count](#dota_ad_ban_count)
- [dota_ad_hero_collision](#dota_ad_hero_collision)
- [dota_ad_nominated_ban](#dota_ad_nominated_ban)
- [dota_ad_randomed](#dota_ad_randomed)
- [dota_alchemist_granted_scepter](#dota_alchemist_granted_scepter)
- [dota_ancient_decoration_event](#dota_ancient_decoration_event)
- [dota_assist_earned](#dota_assist_earned)
- [dota_banner_planted](#dota_banner_planted)
- [dota_barracks_kill](#dota_barracks_kill)
- [dota_blessing_chosen](#dota_blessing_chosen)
- [dota_bounty](#dota_bounty)
- [dota_buyback](#dota_buyback)
- [dota_candy](#dota_candy)
- [dota_challenge_socache_updated](#dota_challenge_socache_updated)
- [dota_chase_hero](#dota_chase_hero)
- [dota_chat_assassin_announce](#dota_chat_assassin_announce)
- [dota_chat_assassin_denied](#dota_chat_assassin_denied)
- [dota_chat_assassin_success](#dota_chat_assassin_success)
- [dota_chat_ban_notification](#dota_chat_ban_notification)
- [dota_chat_event](#dota_chat_event)
- [dota_chat_first_blood](#dota_chat_first_blood)
- [dota_chat_informational](#dota_chat_informational)
- [dota_chat_kill_streak](#dota_chat_kill_streak)
- [dota_chat_timed_reward](#dota_chat_timed_reward)
- [dota_coin_wager](#dota_coin_wager)
- [dota_combat_event_message](#dota_combat_event_message)
- [dota_combatlog](#dota_combatlog)
- [dota_courier_lost](#dota_courier_lost)
- [dota_courier_respawned](#dota_courier_respawned)
- [dota_courier_transfer_item](#dota_courier_transfer_item)
- [dota_crafting_xp](#dota_crafting_xp)
- [dota_creature_gained_level](#dota_creature_gained_level)
- [dota_custom_camera_pitch_updated](#dota_custom_camera_pitch_updated)
- [dota_custom_camera_updated](#dota_custom_camera_updated)
- [dota_effigy_kill](#dota_effigy_kill)
- [dota_enemy_money_changed](#dota_enemy_money_changed)
- [dota_event_game_camera_position_updated](#dota_event_game_camera_position_updated)
- [dota_event_game_camera_zoom_updated](#dota_event_game_camera_zoom_updated)
- [dota_favorite_heroes_updated](#dota_favorite_heroes_updated)
- [dota_force_portrait_update](#dota_force_portrait_update)
- [dota_game_state_change](#dota_game_state_change)
- [dota_glyph_used](#dota_glyph_used)
- [dota_hero_ability_points_changed](#dota_hero_ability_points_changed)
- [dota_hero_entered_shop](#dota_hero_entered_shop)
- [dota_hero_inventory_item_change](#dota_hero_inventory_item_change)
- [dota_hero_on_gain_aggro](#dota_hero_on_gain_aggro)
- [dota_hero_random](#dota_hero_random)
- [dota_hero_swap](#dota_hero_swap)
- [dota_hero_teleport_to_unit](#dota_hero_teleport_to_unit)
- [dota_hero_undoselection](#dota_hero_undoselection)
- [dota_holdout_revive_complete](#dota_holdout_revive_complete)
- [dota_holdout_revive_eliminated](#dota_holdout_revive_eliminated)
- [dota_hud_error_message](#dota_hud_error_message)
- [dota_hud_skin_changed](#dota_hud_skin_changed)
- [dota_illusions_created](#dota_illusions_created)
- [dota_inventory_changed](#dota_inventory_changed)
- [dota_inventory_changed_query_unit](#dota_inventory_changed_query_unit)
- [dota_inventory_item_added](#dota_inventory_item_added)
- [dota_inventory_item_changed](#dota_inventory_item_changed)
- [dota_inventory_player_got_item](#dota_inventory_player_got_item)
- [dota_item_auto_purchase](#dota_item_auto_purchase)
- [dota_item_combined](#dota_item_combined)
- [dota_item_drag_begin](#dota_item_drag_begin)
- [dota_item_drag_end](#dota_item_drag_end)
- [dota_item_gifted](#dota_item_gifted)
- [dota_item_physical_destroyed](#dota_item_physical_destroyed)
- [dota_item_picked_up](#dota_item_picked_up)
- [dota_item_placed_in_neutral_stash](#dota_item_placed_in_neutral_stash)
- [dota_item_purchase](#dota_item_purchase)
- [dota_item_purchased](#dota_item_purchased)
- [dota_item_spawned](#dota_item_spawned)
- [dota_item_spotted](#dota_item_spotted)
- [dota_item_used](#dota_item_used)
- [dota_link_clicked](#dota_link_clicked)
- [dota_local_quickbuy_changed](#dota_local_quickbuy_changed)
- [dota_match_done](#dota_match_done)
- [dota_match_done_client](#dota_match_done_client)
- [dota_match_signout](#dota_match_signout)
- [dota_miniboss_kill](#dota_miniboss_kill)
- [dota_money_changed](#dota_money_changed)
- [dota_neutral_creep_camp_cleared](#dota_neutral_creep_camp_cleared)
- [dota_neutral_item_sent_to_stash](#dota_neutral_item_sent_to_stash)
- [dota_no_battle_points](#dota_no_battle_points)
- [dota_non_player_begin_cast](#dota_non_player_begin_cast)
- [dota_non_player_used_ability](#dota_non_player_used_ability)
- [dota_npc_goal_reached](#dota_npc_goal_reached)
- [dota_on_hero_finish_spawn](#dota_on_hero_finish_spawn)
- [dota_pause_event](#dota_pause_event)
- [dota_player_begin_cast](#dota_player_begin_cast)
- [dota_player_connection_state_changed](#dota_player_connection_state_changed)
- [dota_player_deny](#dota_player_deny)
- [dota_player_details_changed](#dota_player_details_changed)
- [dota_player_gained_level](#dota_player_gained_level)
- [dota_player_hero_selection_dirty](#dota_player_hero_selection_dirty)
- [dota_player_kill](#dota_player_kill)
- [dota_player_killed](#dota_player_killed)
- [dota_player_learned_ability](#dota_player_learned_ability)
- [dota_player_pick_hero](#dota_player_pick_hero)
- [dota_player_reconnected](#dota_player_reconnected)
- [dota_player_selected_custom_team](#dota_player_selected_custom_team)
- [dota_player_shop_changed](#dota_player_shop_changed)
- [dota_player_show_killcam](#dota_player_show_killcam)
- [dota_player_show_minikillcam](#dota_player_show_minikillcam)
- [dota_player_spawned](#dota_player_spawned)
- [dota_player_take_tower_damage](#dota_player_take_tower_damage)
- [dota_player_team_changed](#dota_player_team_changed)
- [dota_player_update_assigned_hero](#dota_player_update_assigned_hero)
- [dota_player_update_hero_selection](#dota_player_update_hero_selection)
- [dota_player_update_killcam_unit](#dota_player_update_killcam_unit)
- [dota_player_update_query_unit](#dota_player_update_query_unit)
- [dota_player_update_selected_unit](#dota_player_update_selected_unit)
- [dota_player_used_ability](#dota_player_used_ability)
- [dota_portrait_ability_layout_changed](#dota_portrait_ability_layout_changed)
- [dota_portrait_unit_modifiers_changed](#dota_portrait_unit_modifiers_changed)
- [dota_portrait_unit_stats_changed](#dota_portrait_unit_stats_changed)
- [dota_protector_spawned](#dota_protector_spawned)
- [dota_quest_completed](#dota_quest_completed)
- [dota_quest_started](#dota_quest_started)
- [dota_quick_buy_changed](#dota_quick_buy_changed)
- [dota_rank_wager](#dota_rank_wager)
- [dota_rd_chat_turn](#dota_rd_chat_turn)
- [dota_report_submitted](#dota_report_submitted)
- [dota_reset_suggested_items](#dota_reset_suggested_items)
- [dota_river_painted](#dota_river_painted)
- [dota_roshan_kill](#dota_roshan_kill)
- [dota_roshan_roar](#dota_roshan_roar)
- [dota_rubick_ability_steal](#dota_rubick_ability_steal)
- [dota_rune_activated_server](#dota_rune_activated_server)
- [dota_rune_deny](#dota_rune_deny)
- [dota_rune_pickup](#dota_rune_pickup)
- [dota_rune_spotted](#dota_rune_spotted)
- [dota_scan_found_enemy](#dota_scan_found_enemy)
- [dota_scan_used](#dota_scan_used)
- [dota_set_quick_buy](#dota_set_quick_buy)
- [dota_shop_item_drag_begin](#dota_shop_item_drag_begin)
- [dota_shop_item_drag_end](#dota_shop_item_drag_end)
- [dota_shrine_kill](#dota_shrine_kill)
- [dota_spectate_hero](#dota_spectate_hero)
- [dota_spectator_talent_changed](#dota_spectator_talent_changed)
- [dota_stone_of_recall_used](#dota_stone_of_recall_used)
- [dota_super_creeps](#dota_super_creeps)
- [dota_team_kill_credit](#dota_team_kill_credit)
- [dota_team_neutral_stash_items_acknowledged_changed](#dota_team_neutral_stash_items_acknowledged_changed)
- [dota_team_neutral_stash_items_changed](#dota_team_neutral_stash_items_changed)
- [dota_team_player_list_changed](#dota_team_player_list_changed)
- [dota_tournament_item_event](#dota_tournament_item_event)
- [dota_tower_deny](#dota_tower_deny)
- [dota_tower_kill](#dota_tower_kill)
- [dota_tutorial_lesson_start](#dota_tutorial_lesson_start)
- [dota_tutorial_shop_toggled](#dota_tutorial_shop_toggled)
- [dota_tutorial_task_advance](#dota_tutorial_task_advance)
- [dota_unit_aghshard_status_change](#dota_unit_aghshard_status_change)
- [dota_unit_event](#dota_unit_event)
- [dota_wager_token](#dota_wager_token)
- [dota_ward_killed](#dota_ward_killed)
- [dota_watch_tower_captured](#dota_watch_tower_captured)
- [dota_workshop_filecanceled](#dota_workshop_filecanceled)
- [dota_workshop_fileselected](#dota_workshop_fileselected)
- [dota_year_beast_killed](#dota_year_beast_killed)
- [drop_rate_modified](#drop_rate_modified)
- [dynamic_shadow_light_changed](#dynamic_shadow_light_changed)
- [enable_china_logomark](#enable_china_logomark)
- [entity_hurt](#entity_hurt)
- [entity_killed](#entity_killed)
- [entity_visible](#entity_visible)
- [event_ticket_modified](#event_ticket_modified)
- [fantasy_league_changed](#fantasy_league_changed)
- [fantasy_score_info_changed](#fantasy_score_info_changed)
- [fantasy_updated](#fantasy_updated)
- [file_downloaded](#file_downloaded)
- [finale_start](#finale_start)
- [flare_ignite_npc](#flare_ignite_npc)
- [friend_lobby_list_updated](#friend_lobby_list_updated)
- [frosty_points_updated](#frosty_points_updated)
- [full_ui_unlocked](#full_ui_unlocked)
- [game_end_visible](#game_end_visible)
- [game_message](#game_message)
- [game_newmap](#game_newmap)
- [game_rules_shutdown](#game_rules_shutdown)
- [game_rules_state_change](#game_rules_state_change)
- [gameinstructor_draw](#gameinstructor_draw)
- [gameinstructor_nodraw](#gameinstructor_nodraw)
- [gameui_activated](#gameui_activated)
- [gameui_hidden](#gameui_hidden)
- [gc_chat_channel_list_updated](#gc_chat_channel_list_updated)
- [gc_connected](#gc_connected)
- [gc_mismatched_version](#gc_mismatched_version)
- [gc_user_session_created](#gc_user_session_created)
- [guild_data_updated](#guild_data_updated)
- [guild_open_parties_updated](#guild_open_parties_updated)
- [halloween_high_score_received](#halloween_high_score_received)
- [halloween_high_score_request_failed](#halloween_high_score_request_failed)
- [halloween_phase_end](#halloween_phase_end)
- [helicopter_grenade_punt_miss](#helicopter_grenade_punt_miss)
- [hero_picker_hidden](#hero_picker_hidden)
- [hero_picker_shown](#hero_picker_shown)
- [hero_selected](#hero_selected)
- [hero_selector_preview_set](#hero_selector_preview_set)
- [hide_highlight_hud_element](#hide_highlight_hud_element)
- [highlight_hud_element](#highlight_hud_element)
- [hltv_cameraman](#hltv_cameraman)
- [hltv_chase](#hltv_chase)
- [hltv_chat](#hltv_chat)
- [hltv_fixed](#hltv_fixed)
- [hltv_message](#hltv_message)
- [hltv_rank_camera](#hltv_rank_camera)
- [hltv_rank_entity](#hltv_rank_entity)
- [hltv_replay](#hltv_replay)
- [hltv_replay_status](#hltv_replay_status)
- [hltv_status](#hltv_status)
- [hltv_title](#hltv_title)
- [hltv_versioninfo](#hltv_versioninfo)
- [hostname_changed](#hostname_changed)
- [hud_flip_changed](#hud_flip_changed)
- [instructor_close_lesson](#instructor_close_lesson)
- [instructor_server_hint_create](#instructor_server_hint_create)
- [instructor_server_hint_stop](#instructor_server_hint_stop)
- [instructor_start_lesson](#instructor_start_lesson)
- [intro_video_finished](#intro_video_finished)
- [inventory_updated](#inventory_updated)
- [item_preview_closed](#item_preview_closed)
- [item_purchased](#item_purchased)
- [item_schema_initialized](#item_schema_initialized)
- [joined_chat_channel](#joined_chat_channel)
- [keybind_changed](#keybind_changed)
- [last_hit](#last_hit)
- [league_admin_info_updated](#league_admin_info_updated)
- [league_series_info_updated](#league_series_info_updated)
- [left_chat_channel](#left_chat_channel)
- [live_games_updated](#live_games_updated)
- [live_leagues_updated](#live_leagues_updated)
- [lobby_invites_updated](#lobby_invites_updated)
- [lobby_updated](#lobby_updated)
- [local_player_controller_team](#local_player_controller_team)
- [local_player_pawn_changed](#local_player_pawn_changed)
- [local_player_team](#local_player_team)
- [map_shutdown](#map_shutdown)
- [map_transition](#map_transition)
- [match_details_updated](#match_details_updated)
- [match_history_updated](#match_history_updated)
- [matchmaking_status_visibility_changed](#matchmaking_status_visibility_changed)
- [microtransaction_success](#microtransaction_success)
- [modifier_event](#modifier_event)
- [news_updated](#news_updated)
- [nommed_tree](#nommed_tree)
- [npc_replaced](#npc_replaced)
- [npc_spawn_finished](#npc_spawn_finished)
- [npc_spawned](#npc_spawned)
- [particle_system_start](#particle_system_start)
- [particle_system_stop](#particle_system_stop)
- [party_invites_updated](#party_invites_updated)
- [party_updated](#party_updated)
- [persona_updated](#persona_updated)
- [physgun_pickup](#physgun_pickup)
- [player_activate](#player_activate)
- [player_changename](#player_changename)
- [player_chat](#player_chat)
- [player_completed_game](#player_completed_game)
- [player_connect](#player_connect)
- [player_connect_full](#player_connect_full)
- [player_death](#player_death)
- [player_disconnect](#player_disconnect)
- [player_footstep](#player_footstep)
- [player_full_update](#player_full_update)
- [player_fullyjoined](#player_fullyjoined)
- [player_hintmessage](#player_hintmessage)
- [player_hurt](#player_hurt)
- [player_info](#player_info)
- [player_info_individual_updated](#player_info_individual_updated)
- [player_info_updated](#player_info_updated)
- [player_is_experienced](#player_is_experienced)
- [player_is_notexperienced](#player_is_notexperienced)
- [player_reconnected](#player_reconnected)
- [player_report_counts_updated](#player_report_counts_updated)
- [player_spawn](#player_spawn)
- [player_stats_updated](#player_stats_updated)
- [player_team](#player_team)
- [practice_lobby_visibility_changed](#practice_lobby_visibility_changed)
- [prizepool_received](#prizepool_received)
- [profile_closed](#profile_closed)
- [profile_opened](#profile_opened)
- [ragdoll_dissolved](#ragdoll_dissolved)
- [recent_matches_updated](#recent_matches_updated)
- [reset_defeated](#reset_defeated)
- [rich_presence_updated](#rich_presence_updated)
- [richpresence_custom_updated](#richpresence_custom_updated)
- [round_end](#round_end)
- [round_freeze_end](#round_freeze_end)
- [round_start](#round_start)
- [round_start_post_nav](#round_start_post_nav)
- [round_start_pre_entity](#round_start_pre_entity)
- [scaleform_file_download_complete](#scaleform_file_download_complete)
- [server_cvar](#server_cvar)
- [server_message](#server_message)
- [server_pre_shutdown](#server_pre_shutdown)
- [server_shutdown](#server_shutdown)
- [server_spawn](#server_spawn)
- [set_instructor_group_enabled](#set_instructor_group_enabled)
- [spec_aegis_reclaim_time](#spec_aegis_reclaim_time)
- [spec_item_pickup](#spec_item_pickup)
- [spec_mode_updated](#spec_mode_updated)
- [spec_target_updated](#spec_target_updated)
- [store_pricesheet_updated](#store_pricesheet_updated)
- [team_data_updated](#team_data_updated)
- [team_details_updated](#team_details_updated)
- [team_info](#team_info)
- [team_score](#team_score)
- [team_showcase_ui_update](#team_showcase_ui_update)
- [teamplay_broadcast_audio](#teamplay_broadcast_audio)
- [teamplay_round_start](#teamplay_round_start)
- [tournament_state_updated](#tournament_state_updated)
- [tree_cut](#tree_cut)
- [ugc_details_arrived](#ugc_details_arrived)
- [ugc_download_requested](#ugc_download_requested)
- [ugc_installed](#ugc_installed)
- [ugc_subscribed](#ugc_subscribed)
- [ugc_unsubscribed](#ugc_unsubscribed)
- [user_data_downloaded](#user_data_downloaded)
- [vote_cast_no](#vote_cast_no)
- [vote_cast_yes](#vote_cast_yes)
- [vote_changed](#vote_changed)
- [vote_failed](#vote_failed)
- [vote_passed](#vote_passed)
- [vote_started](#vote_started)

</details>

### account_all_hero_challenge_changed

Type: `AccountAllHeroChallengeChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `account_id` | `number` |  |

### achievement_earned

Type: `AchievementEarnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player` | `EntityIndex` | Entindex of the player. |
| `achievement` | `number` | Achievement ID. |

### achievement_event

Type: `AchievementEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `achievement_name` | `string` | Non-localized name of achievement. |
| `cur_val` | `number` | # of steps toward achievement. |
| `max_val` | `number` | Total # of steps in achievement. |

### achievement_write_failed

Type: `object`

_No typed fields._

### aegis_event

Type: `AegisEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |
| `chat_message_type` | `number` |  |

### antiaddiction_toast

Type: `AntiaddictionToastEvent`

| Field | Type | Description |
| --- | --- | --- |
| `message` | `string` |  |
| `duration` | `number` |  |

### bindpanel_close

Type: `object`

_No typed fields._

### bindpanel_open

Type: `object`

_No typed fields._

### bonus_updated

Type: `BonusUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `numadvanced` | `number` |  |
| `numbronze` | `number` |  |
| `numsilver` | `number` |  |
| `numgold` | `number` |  |

### booster_state_updated

Type: `object`

_No typed fields._

### bot_takeover

Type: `BotTakeoverEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `botid` | `EntityIndex` |  |
| `p` | `number` |  |
| `y` | `number` |  |
| `r` | `number` |  |

### bought_back

Type: `BoughtBackEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |

### break_breakable

Type: `BreakBreakableEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `userid` | `EntityIndex` |  |
| `material` | `number` | BREAK_GLASS, BREAK_WOOD, etc. |

### break_prop

Type: `BreakPropEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `userid` | `EntityIndex` |  |
| `player_held` | `0 \| 1` |  |
| `player_thrown` | `0 \| 1` |  |
| `player_dropped` | `0 \| 1` |  |

### broken_breakable

Type: `BrokenBreakableEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `userid` | `EntityIndex` |  |
| `material` | `number` | BREAK_GLASS, BREAK_WOOD, etc. |

### cart_updated

Type: `object`

_No typed fields._

### chat_members_changed

Type: `ChatMembersChangedEvent`

The specified channel has had players leave or join.

| Field | Type | Description |
| --- | --- | --- |
| `channel` | `number` |  |

### chat_new_message

Type: `ChatNewMessageEvent`

The specified channel contains new messages.

| Field | Type | Description |
| --- | --- | --- |
| `channel` | `number` |  |

### client_disconnect

Type: `ClientDisconnectEvent`

| Field | Type | Description |
| --- | --- | --- |
| `reason_code` | `number` |  |
| `reason_desc` | `string` |  |

### client_reload_game_keyvalues

Type: `object`

_No typed fields._

### clientside_lesson_closed

Type: `ClientsideLessonClosedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `lesson_name` | `string` |  |

### colorblind_mode_changed

Type: `object`

_No typed fields._

### community_cached_names_updated

Type: `object`

_No typed fields._

### custom_game_friends_played_updated

Type: `CustomGameFriendsPlayedUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `custom_game_id` | `number` |  |

### custom_game_lobby_list_updated

Type: `object`

_No typed fields._

### custom_game_mode_list_updated

Type: `object`

_No typed fields._

### custom_game_player_count_updated

Type: `CustomGamePlayerCountUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `custom_game_id` | `number` |  |

### custom_games_friends_play_updated

Type: `object`

_No typed fields._

### dashboard_caches_cleared

Type: `object`

_No typed fields._

### dashboard_switched_section

Type: `DashboardSwitchedSectionEvent`

| Field | Type | Description |
| --- | --- | --- |
| `section` | `number` |  |

### defeated

Type: `DefeatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |

### demo_skip

Type: `DemoSkipEvent`

| Field | Type | Description |
| --- | --- | --- |
| `playback_tick` | `number` | Current playback tick. |
| `skipto_tick` | `number` | Tick we're going to. |
| `user_message_list` | `any` | CSVCMsgList_UserMessages. |
| `dota_hero_chase_list` | `any` | CSVCMsgList_GameEvents. |

### demo_start

Type: `DemoStartEvent`

| Field | Type | Description |
| --- | --- | --- |
| `dota_combatlog_list` | `any` | CSVCMsgList_GameEvents that are combat log events. |
| `dota_hero_chase_list` | `any` | CSVCMsgList_GameEvents. |
| `dota_pick_hero_list` | `any` | CSVCMsgList_GameEvents. |

### demo_stop

Type: `object`

_No typed fields._

### difficulty_changed

Type: `DifficultyChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `newDifficulty` | `number` |  |
| `oldDifficulty` | `number` |  |
| `strDifficulty` | `string` | New difficulty as string. |

### door_close

Type: `DoorCloseEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Who closed the door. |
| `checkpoint` | `0 \| 1` | Is the door a checkpoint door. |

### dota_ability_changed

Type: `DotaAbilityChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entityIndex` | `EntityIndex` |  |

### dota_ability_channel_finished

Type: `DotaAbilityChannelFinishedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `abilityname` | `string` |  |
| `interrupted` | `0 \| 1` |  |
| `caster_entindex` | `EntityIndex` |  |

### dota_action_item

Type: `DotaActionItemEvent`

| Field | Type | Description |
| --- | --- | --- |
| `reason` | `number` |  |
| `itemdef` | `number` |  |
| `message` | `number` |  |

### dota_action_success

Type: `object`

_No typed fields._

### dota_ad_ban

Type: `DotaAdBanEvent`

| Field | Type | Description |
| --- | --- | --- |
| `heroid` | `number` |  |

### dota_ad_ban_count

Type: `DotaAdBanCountEvent`

| Field | Type | Description |
| --- | --- | --- |
| `count` | `number` |  |

### dota_ad_hero_collision

Type: `DotaAdHeroCollisionEvent`

| Field | Type | Description |
| --- | --- | --- |
| `heroid` | `number` |  |
| `playerid1` | `PlayerID` |  |
| `playerid2` | `PlayerID` |  |

### dota_ad_nominated_ban

Type: `DotaAdNominatedBanEvent`

| Field | Type | Description |
| --- | --- | --- |
| `heroid` | `number` |  |

### dota_ad_randomed

Type: `DotaAdRandomedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |

### dota_alchemist_granted_scepter

Type: `DotaAlchemistGrantedScepterEvent`

| Field | Type | Description |
| --- | --- | --- |
| `alchemist_userid` | `EntityIndex` |  |
| `grantee_userid` | `EntityIndex` |  |

### dota_ancient_decoration_event

Type: `DotaAncientDecorationEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `teamnumber` | `number` |  |
| `eventname` | `string` |  |

### dota_assist_earned

Type: `DotaAssistEarnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex_hero` | `EntityIndex` |  |
| `playerid_victim` | `PlayerID` |  |

### dota_banner_planted

Type: `DotaBannerPlantedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_barracks_kill

Type: `DotaBarracksKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `barracks_id` | `number` |  |
| `barracks_type` | `number` |  |
| `teamnumber` | `number` |  |
| `killer_userid` | `EntityIndex` |  |
| `killer_team` | `number` |  |
| `gold` | `number` |  |
| `pos_x` | `number` |  |
| `pos_y` | `number` |  |
| `pos_z` | `number` |  |

### dota_blessing_chosen

Type: `DotaBlessingChosenEvent`

| Field | Type | Description |
| --- | --- | --- |
| `blessing_receipient_id` | `number` |  |
| `blessing` | `number` |  |

### dota_bounty

Type: `DotaBountyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `target` | `number` |  |
| `bounty_event` | `number` |  |

### dota_buyback

Type: `DotaBuybackEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `player_id` | `number` |  |

### dota_candy

Type: `DotaCandyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `candy_event` | `number` |  |

### dota_challenge_socache_updated

Type: `object`

_No typed fields._

### dota_chase_hero

Type: `DotaChaseHeroEvent`

Shot of a single entity.

| Field | Type | Description |
| --- | --- | --- |
| `target1` | `number` | Primary traget index. |
| `target2` | `number` | Secondary traget index or 0. |
| `type` | `number` |  |
| `priority` | `number` |  |
| `gametime` | `number` |  |
| `highlight` | `0 \| 1` | If set, a result of highlight reel mode. |
| `target1playerid` | `PlayerID` |  |
| `target2playerid` | `PlayerID` |  |
| `eventtype` | `number` | EDOTAHeroChaseEventType. |

### dota_chat_assassin_announce

Type: `DotaChatAssassinAnnounceEvent`

| Field | Type | Description |
| --- | --- | --- |
| `assassin_id` | `number` |  |
| `target_id` | `number` |  |
| `message` | `number` |  |

### dota_chat_assassin_denied

Type: `DotaChatAssassinDeniedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `assassin_id` | `number` |  |
| `target_id` | `number` |  |
| `message` | `number` |  |

### dota_chat_assassin_success

Type: `DotaChatAssassinSuccessEvent`

| Field | Type | Description |
| --- | --- | --- |
| `assassin_id` | `number` |  |
| `target_id` | `number` |  |
| `message` | `number` |  |

### dota_chat_ban_notification

Type: `DotaChatBanNotificationEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |

### dota_chat_event

Type: `DotaChatEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `gold` | `number` |  |
| `message` | `number` |  |

### dota_chat_first_blood

Type: `DotaChatFirstBloodEvent`

| Field | Type | Description |
| --- | --- | --- |
| `gold` | `number` |  |
| `killer_id` | `number` |  |
| `victim_id` | `number` |  |

### dota_chat_informational

Type: `DotaChatInformationalEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `type` | `number` |  |

### dota_chat_kill_streak

Type: `DotaChatKillStreakEvent`

| Field | Type | Description |
| --- | --- | --- |
| `gold` | `number` |  |
| `killer_id` | `number` |  |
| `killer_streak` | `number` |  |
| `killer_multikill` | `number` |  |
| `victim_id` | `number` |  |
| `victim_streak` | `number` |  |

### dota_chat_timed_reward

Type: `DotaChatTimedRewardEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `itmedef` | `number` |  |
| `message` | `number` |  |

### dota_coin_wager

Type: `DotaCoinWagerEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `message` | `number` |  |
| `coins` | `number` |  |

### dota_combat_event_message

Type: `DotaCombatEventMessageEvent`

| Field | Type | Description |
| --- | --- | --- |
| `message` | `string` |  |
| `teamnumber` | `number` |  |
| `player_id` | `number` |  |
| `player_id2` | `number` |  |
| `value` | `number` |  |
| `value1` | `number` |  |
| `value2` | `number` |  |
| `value3` | `number` |  |
| `int_value` | `number` |  |
| `int_value2` | `number` |  |
| `ability_name` | `string` |  |
| `locstring_value` | `string` |  |
| `locstring_value2` | `string` |  |
| `string_replace_token` | `string` |  |

### dota_combatlog

Type: `DotaCombatlogEvent`

| Field | Type | Description |
| --- | --- | --- |
| `type` | `number` |  |
| `sourcename` | `number` |  |
| `targetname` | `number` |  |
| `attackername` | `number` |  |
| `inflictorname` | `number` |  |
| `attackerillusion` | `0 \| 1` |  |
| `targetillusion` | `0 \| 1` |  |
| `value` | `number` |  |
| `health` | `number` |  |
| `timestamp` | `number` |  |
| `targetsourcename` | `number` |  |
| `timestampraw` | `number` |  |
| `attackerhero` | `0 \| 1` |  |
| `targethero` | `0 \| 1` |  |
| `ability_toggle_on` | `0 \| 1` |  |
| `ability_toggle_off` | `0 \| 1` |  |
| `ability_level` | `number` |  |
| `gold_reason` | `number` |  |
| `xp_reason` | `number` |  |

### dota_courier_lost

Type: `DotaCourierLostEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killerid` | `number` |  |
| `teamnumber` | `number` |  |
| `bounty_gold` | `number` |  |

### dota_courier_respawned

Type: `DotaCourierRespawnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_courier_transfer_item

Type: `DotaCourierTransferItemEvent`

| Field | Type | Description |
| --- | --- | --- |
| `hero_entindex` | `EntityIndex` |  |
| `courier_entindex` | `EntityIndex` |  |
| `item_entindex` | `EntityIndex` |  |

### dota_crafting_xp

Type: `DotaCraftingXpEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `type` | `number` |  |
| `xp` | `number` |  |

### dota_creature_gained_level

Type: `DotaCreatureGainedLevelEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `level` | `number` |  |

### dota_custom_camera_pitch_updated

Type: `DotaCustomCameraPitchUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `pitch` | `number` |  |

### dota_custom_camera_updated

Type: `DotaCustomCameraUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `flags` | `number` | DOTACustomCameraEventFlags_t. |
| `zoom` | `number` |  |
| `x` | `number` |  |
| `y` | `number` |  |
| `extra_yaw` | `number` |  |
| `pitch` | `number` |  |
| `duration` | `number` |  |
| `player_id` | `number` | Only used if associated flag is set. |

### dota_effigy_kill

Type: `DotaEffigyKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `owner_userid` | `EntityIndex` |  |

### dota_enemy_money_changed

Type: `object`

_No typed fields._

### dota_event_game_camera_position_updated

Type: `DotaEventGameCameraPositionUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `x` | `number` |  |
| `y` | `number` |  |
| `duration` | `number` | 0 - instantaneous camera update. |

### dota_event_game_camera_zoom_updated

Type: `DotaEventGameCameraZoomUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `zoom` | `number` |  |
| `duration` | `number` | 0 - instantaneous camera update. |

### dota_favorite_heroes_updated

Type: `object`

_No typed fields._

### dota_force_portrait_update

Type: `object`

_No typed fields._

### dota_game_state_change

Type: `DotaGameStateChangeEvent`

| Field | Type | Description |
| --- | --- | --- |
| `old_state` | `number` |  |
| `new_state` | `number` |  |

### dota_glyph_used

Type: `DotaGlyphUsedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_hero_ability_points_changed

Type: `object`

_No typed fields._

### dota_hero_entered_shop

Type: `DotaHeroEnteredShopEvent`

| Field | Type | Description |
| --- | --- | --- |
| `shop_type` | `number` |  |
| `shop_entindex` | `EntityIndex` |  |
| `hero_entindex` | `EntityIndex` |  |

### dota_hero_inventory_item_change

Type: `DotaHeroInventoryItemChangeEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `number` |  |
| `hero_entindex` | `EntityIndex` |  |
| `item_entindex` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |
| `removed` | `0 \| 1` |  |
| `dropped` | `0 \| 1` |  |
| `sold` | `0 \| 1` |  |
| `in_sellback_windown` | `0 \| 1` |  |

### dota_hero_on_gain_aggro

Type: `DotaHeroOnGainAggroEvent`

An NPC has gained aggro (is attacking) a hero.

| Field | Type | Description |
| --- | --- | --- |
| `entindex_attacker` | `EntityIndex` |  |
| `entindex_hero` | `EntityIndex` |  |

### dota_hero_random

Type: `DotaHeroRandomEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `heroid` | `number` |  |

### dota_hero_swap

Type: `DotaHeroSwapEvent`

| Field | Type | Description |
| --- | --- | --- |
| `playerid1` | `PlayerID` |  |
| `playerid2` | `PlayerID` |  |

### dota_hero_teleport_to_unit

Type: `DotaHeroTeleportToUnitEvent`

| Field | Type | Description |
| --- | --- | --- |
| `hero_entindex` | `EntityIndex` |  |
| `unit_entindex` | `EntityIndex` |  |

### dota_hero_undoselection

Type: `DotaHeroUndoselectionEvent`

| Field | Type | Description |
| --- | --- | --- |
| `playerid1` | `PlayerID` |  |

### dota_holdout_revive_complete

Type: `DotaHoldoutReviveCompleteEvent`

| Field | Type | Description |
| --- | --- | --- |
| `caster` | `number` |  |
| `target` | `number` |  |
| `channel_time` | `number` |  |

### dota_holdout_revive_eliminated

Type: `DotaHoldoutReviveEliminatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `caster` | `number` |  |
| `target` | `number` |  |
| `channel_time` | `number` |  |

### dota_hud_error_message

Type: `DotaHudErrorMessageEvent`

| Field | Type | Description |
| --- | --- | --- |
| `reason` | `number` |  |
| `message` | `string` |  |
| `sequenceNumber` | `number` |  |

### dota_hud_skin_changed

Type: `DotaHudSkinChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `skin` | `string` |  |
| `style` | `number` |  |

### dota_illusions_created

Type: `DotaIllusionsCreatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `original_entindex` | `EntityIndex` |  |

### dota_inventory_changed

Type: `object`

_No typed fields._

### dota_inventory_changed_query_unit

Type: `object`

_No typed fields._

### dota_inventory_item_added

Type: `DotaInventoryItemAddedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `item_slot` | `number` |  |
| `inventory_player_id` | `PlayerID` |  |
| `itemname` | `string` |  |
| `item_entindex` | `EntityIndex` |  |
| `inventory_parent_entindex` | `EntityIndex` |  |
| `is_courier` | `0 \| 1` |  |

### dota_inventory_item_changed

Type: `DotaInventoryItemChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entityIndex` | `EntityIndex` |  |

### dota_inventory_player_got_item

Type: `DotaInventoryPlayerGotItemEvent`

| Field | Type | Description |
| --- | --- | --- |
| `itemname` | `string` |  |

### dota_item_auto_purchase

Type: `DotaItemAutoPurchaseEvent`

| Field | Type | Description |
| --- | --- | --- |
| `item_id` | `number` |  |

### dota_item_combined

Type: `DotaItemCombinedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `itemname` | `string` |  |
| `itemcost` | `number` |  |

### dota_item_drag_begin

Type: `object`

_No typed fields._

### dota_item_drag_end

Type: `object`

_No typed fields._

### dota_item_gifted

Type: `DotaItemGiftedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |
| `sourceid` | `number` |  |

### dota_item_physical_destroyed

Type: `DotaItemPhysicalDestroyedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `itemname` | `string` |  |
| `PlayerID` | `PlayerID` |  |
| `ItemEntityIndex` | `EntityIndex` |  |
| `HeroEntityIndex` | `EntityIndex` |  |

### dota_item_picked_up

Type: `DotaItemPickedUpEvent`

| Field | Type | Description |
| --- | --- | --- |
| `itemname` | `string` |  |
| `PlayerID` | `PlayerID` |  |
| `ItemEntityIndex` | `EntityIndex` |  |
| `HeroEntityIndex` | `EntityIndex` |  |

### dota_item_placed_in_neutral_stash

Type: `DotaItemPlacedInNeutralStashEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |

### dota_item_purchase

Type: `DotaItemPurchaseEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |

### dota_item_purchased

Type: `DotaItemPurchasedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `itemname` | `string` |  |
| `itemcost` | `number` |  |

### dota_item_spawned

Type: `DotaItemSpawnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `item_ent_index` | `EntityIndex` |  |
| `player_id` | `number` |  |

### dota_item_spotted

Type: `DotaItemSpottedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `item_ability_id` | `number` |  |

### dota_item_used

Type: `DotaItemUsedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `itemname` | `string` |  |

### dota_link_clicked

Type: `DotaLinkClickedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `link` | `string` |  |
| `nav` | `0 \| 1` | Internal to item panel - preserve the nav stack. |
| `nav_back` | `0 \| 1` | Internal to item panel - preserve the nav stack. |
| `recipe` | `number` |  |
| `shop` | `number` | Show the item in a particular shop. |

### dota_local_quickbuy_changed

Type: `object`

_No typed fields._

### dota_match_done

Type: `DotaMatchDoneEvent`

| Field | Type | Description |
| --- | --- | --- |
| `winningteam` | `number` | The ID of the winning team. |

### dota_match_done_client

Type: `object`

_No typed fields._

### dota_match_signout

Type: `object`

_No typed fields._

### dota_miniboss_kill

Type: `DotaMinibossKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `shard_recipient_id` | `number` |  |
| `teamnumber` | `number` |  |
| `gold` | `number` |  |

### dota_money_changed

Type: `object`

_No typed fields._

### dota_neutral_creep_camp_cleared

Type: `DotaNeutralCreepCampClearedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `camp_name` | `string` |  |
| `camp_type` | `number` |  |
| `killer_player_id` | `number` |  |

### dota_neutral_item_sent_to_stash

Type: `DotaNeutralItemSentToStashEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |
| `itemname` | `string` |  |
| `item_entindex` | `EntityIndex` |  |

### dota_no_battle_points

Type: `DotaNoBattlePointsEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `reason` | `number` |  |

### dota_non_player_begin_cast

Type: `DotaNonPlayerBeginCastEvent`

| Field | Type | Description |
| --- | --- | --- |
| `abilityname` | `string` |  |
| `caster_entindex` | `EntityIndex` |  |

### dota_non_player_used_ability

Type: `DotaNonPlayerUsedAbilityEvent`

| Field | Type | Description |
| --- | --- | --- |
| `abilityname` | `string` |  |
| `caster_entindex` | `EntityIndex` |  |

### dota_npc_goal_reached

Type: `DotaNpcGoalReachedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `npc_entindex` | `EntityIndex` | Entity index of the npc which was following a path and has reached a goal<br>entity. |
| `goal_entindex` | `EntityIndex` | Entity index of the path goal entity which has been reached. |
| `next_goal_entindex` | `EntityIndex` | Entity index of the next goal entity on the path (if any) which the npc will<br>now be pathing towards. |

### dota_on_hero_finish_spawn

Type: `DotaOnHeroFinishSpawnEvent`

| Field | Type | Description |
| --- | --- | --- |
| `heroindex` | `number` |  |
| `hero` | `string` |  |

### dota_pause_event

Type: `DotaPauseEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `value` | `number` |  |
| `message` | `number` |  |

### dota_player_begin_cast

Type: `DotaPlayerBeginCastEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `abilityname` | `string` |  |
| `caster_entindex` | `EntityIndex` |  |

### dota_player_connection_state_changed

Type: `object`

_No typed fields._

### dota_player_deny

Type: `DotaPlayerDenyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_userid` | `EntityIndex` |  |
| `victim_userid` | `EntityIndex` |  |

### dota_player_details_changed

Type: `object`

_No typed fields._

### dota_player_gained_level

Type: `DotaPlayerGainedLevelEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player` | `number` |  |
| `player_id` | `PlayerID` |  |
| `level` | `number` |  |
| `hero_entindex` | `EntityIndex` |  |
| `PlayerID` | `PlayerID` |  |

### dota_player_hero_selection_dirty

Type: `object`

_No typed fields._

### dota_player_kill

Type: `DotaPlayerKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `victim_userid` | `EntityIndex` |  |
| `killer1_userid` | `EntityIndex` |  |
| `killer2_userid` | `EntityIndex` |  |
| `killer3_userid` | `EntityIndex` |  |
| `killer4_userid` | `EntityIndex` |  |
| `killer5_userid` | `EntityIndex` |  |
| `bounty` | `number` |  |
| `neutral` | `number` |  |
| `greevil` | `number` |  |

### dota_player_killed

Type: `DotaPlayerKilledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `HeroKill` | `0 \| 1` |  |
| `TowerKill` | `0 \| 1` |  |

### dota_player_learned_ability

Type: `DotaPlayerLearnedAbilityEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `player` | `number` |  |
| `abilityname` | `string` |  |

### dota_player_pick_hero

Type: `DotaPlayerPickHeroEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player` | `number` |  |
| `heroindex` | `number` |  |
| `hero` | `string` |  |

### dota_player_reconnected

Type: `DotaPlayerReconnectedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `number` |  |

### dota_player_selected_custom_team

Type: `DotaPlayerSelectedCustomTeamEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` | Player id of the player who select a team. |
| `team_id` | `number` | Id of the team the player selected. |
| `success` | `0 \| 1` | Was the player successfully assigned to the selected team. |

### dota_player_shop_changed

Type: `DotaPlayerShopChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `prevshopmask` | `number` |  |
| `shopmask` | `number` |  |

### dota_player_show_killcam

Type: `DotaPlayerShowKillcamEvent`

| Field | Type | Description |
| --- | --- | --- |
| `nodes` | `number` |  |
| `player` | `number` |  |

### dota_player_show_minikillcam

Type: `DotaPlayerShowMinikillcamEvent`

| Field | Type | Description |
| --- | --- | --- |
| `nodes` | `number` |  |
| `player` | `number` |  |

### dota_player_spawned

Type: `DotaPlayerSpawnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |

### dota_player_take_tower_damage

Type: `DotaPlayerTakeTowerDamageEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `damage` | `number` |  |

### dota_player_team_changed

Type: `object`

_No typed fields._

### dota_player_update_assigned_hero

Type: `DotaPlayerUpdateAssignedHeroEvent`

| Field | Type | Description |
| --- | --- | --- |
| `playerid` | `PlayerID` |  |

### dota_player_update_hero_selection

Type: `DotaPlayerUpdateHeroSelectionEvent`

| Field | Type | Description |
| --- | --- | --- |
| `tabcycle` | `0 \| 1` |  |

### dota_player_update_killcam_unit

Type: `object`

_No typed fields._

### dota_player_update_query_unit

Type: `object`

_No typed fields._

### dota_player_update_selected_unit

Type: `object`

_No typed fields._

### dota_player_used_ability

Type: `DotaPlayerUsedAbilityEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `abilityname` | `string` |  |
| `caster_entindex` | `EntityIndex` |  |

### dota_portrait_ability_layout_changed

Type: `object`

_No typed fields._

### dota_portrait_unit_modifiers_changed

Type: `DotaPortraitUnitModifiersChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `modifier_affects_abilities` | `0 \| 1` |  |

### dota_portrait_unit_stats_changed

Type: `object`

_No typed fields._

### dota_protector_spawned

Type: `DotaProtectorSpawnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `number` |  |

### dota_quest_completed

Type: `DotaQuestCompletedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `questIndex` | `number` | Entity index. |

### dota_quest_started

Type: `DotaQuestStartedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `questIndex` | `number` | Entity index. |

### dota_quick_buy_changed

Type: `DotaQuickBuyChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `item` | `string` |  |
| `recipe` | `number` |  |

### dota_rank_wager

Type: `DotaRankWagerEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |

### dota_rd_chat_turn

Type: `DotaRdChatTurnEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |

### dota_report_submitted

Type: `DotaReportSubmittedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `result` | `number` |  |
| `report_flags` | `number` |  |
| `message` | `string` |  |

### dota_reset_suggested_items

Type: `object`

_No typed fields._

### dota_river_painted

Type: `DotaRiverPaintedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `riverid` | `number` |  |

### dota_roshan_kill

Type: `DotaRoshanKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |
| `gold` | `number` |  |

### dota_roshan_roar

Type: `DotaRoshanRoarEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_rubick_ability_steal

Type: `DotaRubickAbilityStealEvent`

| Field | Type | Description |
| --- | --- | --- |
| `abilityIndex` | `number` |  |
| `abilityLevel` | `number` |  |

### dota_rune_activated_server

Type: `DotaRuneActivatedServerEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `rune` | `number` |  |

### dota_rune_deny

Type: `DotaRuneDenyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `rune` | `number` |  |

### dota_rune_pickup

Type: `DotaRunePickupEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `type` | `number` |  |
| `rune` | `number` |  |
| `bounty_amount` | `number` |  |

### dota_rune_spotted

Type: `DotaRuneSpottedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `rune` | `number` |  |
| `map_location` | `string` |  |
| `rune_team` | `number` |  |

### dota_scan_found_enemy

Type: `DotaScanFoundEnemyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_scan_used

Type: `DotaScanUsedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_set_quick_buy

Type: `DotaSetQuickBuyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `item` | `string` |  |
| `recipe` | `number` |  |
| `toggle` | `0 \| 1` |  |

### dota_shop_item_drag_begin

Type: `object`

_No typed fields._

### dota_shop_item_drag_end

Type: `object`

_No typed fields._

### dota_shrine_kill

Type: `DotaShrineKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_userid` | `EntityIndex` |  |
| `teamnumber` | `number` |  |
| `gold` | `number` |  |

### dota_spectate_hero

Type: `DotaSpectateHeroEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |

### dota_spectator_talent_changed

Type: `DotaSpectatorTalentChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `abilityname` | `string` |  |
| `playerid` | `PlayerID` |  |

### dota_stone_of_recall_used

Type: `DotaStoneOfRecallUsedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `caster_userid` | `EntityIndex` |  |

### dota_super_creeps

Type: `DotaSuperCreepsEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_team_kill_credit

Type: `DotaTeamKillCreditEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_userid` | `EntityIndex` |  |
| `victim_userid` | `EntityIndex` |  |
| `teamnumber` | `number` |  |
| `herokills` | `number` |  |

### dota_team_neutral_stash_items_acknowledged_changed

Type: `DotaTeamNeutralStashItemsAcknowledgedChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_team_neutral_stash_items_changed

Type: `DotaTeamNeutralStashItemsChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamnumber` | `number` |  |

### dota_team_player_list_changed

Type: `object`

_No typed fields._

### dota_tournament_item_event

Type: `DotaTournamentItemEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `winner_count` | `number` |  |
| `event_type` | `number` |  |

### dota_tower_deny

Type: `DotaTowerDenyEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_userid` | `EntityIndex` |  |
| `teamnumber` | `number` |  |
| `gold` | `number` |  |
| `tier` | `number` |  |
| `pos_x` | `number` |  |
| `pos_y` | `number` |  |
| `pos_z` | `number` |  |

### dota_tower_kill

Type: `DotaTowerKillEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_userid` | `EntityIndex` |  |
| `teamnumber` | `number` |  |
| `gold` | `number` |  |
| `tier` | `number` |  |
| `pos_x` | `number` |  |
| `pos_y` | `number` |  |
| `pos_z` | `number` |  |

### dota_tutorial_lesson_start

Type: `object`

_No typed fields._

### dota_tutorial_shop_toggled

Type: `DotaTutorialShopToggledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `shop_opened` | `0 \| 1` |  |

### dota_tutorial_task_advance

Type: `object`

_No typed fields._

### dota_unit_aghshard_status_change

Type: `DotaUnitAghshardStatusChangeEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `has_scepter` | `0 \| 1` |  |
| `has_shard` | `0 \| 1` |  |

### dota_unit_event

Type: `DotaUnitEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `victim` | `number` |  |
| `attacker` | `number` |  |
| `basepriority` | `number` |  |
| `priority` | `number` |  |
| `eventtype` | `number` | EDOTAHeroChaseEventType. |

### dota_wager_token

Type: `DotaWagerTokenEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `message` | `number` |  |
| `amount` | `number` |  |

### dota_ward_killed

Type: `DotaWardKilledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `type` | `number` |  |
| `bounty_amount` | `number` |  |

### dota_watch_tower_captured

Type: `DotaWatchTowerCapturedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `team_number` | `number` |  |
| `old_team_number` | `number` |  |

### dota_workshop_filecanceled

Type: `object`

_No typed fields._

### dota_workshop_fileselected

Type: `DotaWorkshopFileselectedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `filename` | `string` |  |

### dota_year_beast_killed

Type: `DotaYearBeastKilledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `killer_player_id` | `PlayerID` |  |
| `message` | `number` |  |
| `beast_id` | `number` |  |

### drop_rate_modified

Type: `object`

_No typed fields._

### dynamic_shadow_light_changed

Type: `object`

_No typed fields._

### enable_china_logomark

Type: `object`

_No typed fields._

### entity_hurt

Type: `EntityHurtEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex_killed` | `EntityIndex` |  |
| `entindex_attacker` | `EntityIndex` |  |
| `entindex_inflictor` | `EntityIndex` |  |
| `damagebits` | `number` |  |
| `damage` | `number` |  |

### entity_killed

Type: `EntityKilledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex_killed` | `EntityIndex` |  |
| `entindex_attacker` | `EntityIndex` |  |
| `entindex_inflictor` | `EntityIndex` |  |
| `damagebits` | `number` |  |

### entity_visible

Type: `EntityVisibleEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | The player who sees the entity. |
| `subject` | `number` | Entindex of the entity they see. |
| `classname` | `string` | Classname of the entity they see. |
| `entityname` | `string` | Name of the entity they see. |

### event_ticket_modified

Type: `object`

_No typed fields._

### fantasy_league_changed

Type: `object`

_No typed fields._

### fantasy_score_info_changed

Type: `object`

_No typed fields._

### fantasy_updated

Type: `object`

_No typed fields._

### file_downloaded

Type: `FileDownloadedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `success` | `0 \| 1` |  |
| `local_filename` | `string` |  |
| `remote_url` | `string` |  |

### finale_start

Type: `FinaleStartEvent`

| Field | Type | Description |
| --- | --- | --- |
| `rushes` | `number` |  |

### flare_ignite_npc

Type: `FlareIgniteNpcEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` | Entity ignited. |

### friend_lobby_list_updated

Type: `object`

_No typed fields._

### frosty_points_updated

Type: `object`

_No typed fields._

### full_ui_unlocked

Type: `object`

_No typed fields._

### game_end_visible

Type: `object`

_No typed fields._

### game_message

Type: `GameMessageEvent`

A message send by game logic to everyone.

| Field | Type | Description |
| --- | --- | --- |
| `target` | `number` | 0 = console, 1 = HUD. |
| `text` | `string` | The message text. |

### game_newmap

Type: `GameNewmapEvent`

Send when new map is completely loaded.

| Field | Type | Description |
| --- | --- | --- |
| `mapname` | `string` | Map name. |
| `transition` | `0 \| 1` | True if this is a transition from one map to another. |

### game_rules_shutdown

Type: `object`

_No typed fields._

### game_rules_state_change

Type: `object`

_No typed fields._

### gameinstructor_draw

Type: `object`

_No typed fields._

### gameinstructor_nodraw

Type: `object`

_No typed fields._

### gameui_activated

Type: `object`

_No typed fields._

### gameui_hidden

Type: `object`

_No typed fields._

### gc_chat_channel_list_updated

Type: `object`

_No typed fields._

### gc_connected

Type: `object`

_No typed fields._

### gc_mismatched_version

Type: `object`

_No typed fields._

### gc_user_session_created

Type: `object`

_No typed fields._

### guild_data_updated

Type: `object`

_No typed fields._

### guild_open_parties_updated

Type: `object`

_No typed fields._

### halloween_high_score_received

Type: `object`

_No typed fields._

### halloween_high_score_request_failed

Type: `object`

_No typed fields._

### halloween_phase_end

Type: `HalloweenPhaseEndEvent`

| Field | Type | Description |
| --- | --- | --- |
| `phase` | `number` |  |
| `team` | `number` |  |

### helicopter_grenade_punt_miss

Type: `object`

_No typed fields._

### hero_picker_hidden

Type: `object`

_No typed fields._

### hero_picker_shown

Type: `object`

_No typed fields._

### hero_selected

Type: `HeroSelectedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |
| `team_number` | `number` |  |
| `hero_unit` | `string` |  |

### hero_selector_preview_set

Type: `HeroSelectorPreviewSetEvent`

| Field | Type | Description |
| --- | --- | --- |
| `setindex` | `number` |  |

### hide_highlight_hud_element

Type: `object`

_No typed fields._

### highlight_hud_element

Type: `HighlightHudElementEvent`

| Field | Type | Description |
| --- | --- | --- |
| `elementname` | `string` |  |
| `duration` | `number` |  |

### hltv_cameraman

Type: `HltvCameramanEvent`

A spectator/player is a cameraman.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Camera man entity index. |

### hltv_chase

Type: `HltvChaseEvent`

Shot of a single entity.

| Field | Type | Description |
| --- | --- | --- |
| `target1` | `EntityIndex` | Primary traget index. |
| `target2` | `EntityIndex` | Secondary traget index or 0. |
| `distance` | `number` | Camera distance. |
| `theta` | `number` | View angle horizontal. |
| `phi` | `number` | View angle vertical. |
| `inertia` | `number` | Camera inertia. |
| `ineye` | `number` | Diretcor suggests to show ineye. |

### hltv_chat

Type: `HltvChatEvent`

A HLTV chat msg sent by spectators.

| Field | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |
| `steamID` | `number` | Steam id. |
| `name` | `string` |  |

### hltv_fixed

Type: `HltvFixedEvent`

Show from fixed view.

| Field | Type | Description |
| --- | --- | --- |
| `posx` | `number` | Camera position in world. |
| `posy` | `number` |  |
| `posz` | `number` |  |
| `theta` | `number` | Camera angles. |
| `phi` | `number` |  |
| `offset` | `number` |  |
| `fov` | `number` |  |
| `target` | `EntityIndex` | Follow this player. |

### hltv_message

Type: `HltvMessageEvent`

A HLTV message send by moderators.

| Field | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |

### hltv_rank_camera

Type: `HltvRankCameraEvent`

A camera ranking.

| Field | Type | Description |
| --- | --- | --- |
| `index` | `number` | Fixed camera index. |
| `rank` | `number` | Ranking, how interesting is this camera view. |
| `target` | `EntityIndex` | Best/closest target entity. |

### hltv_rank_entity

Type: `HltvRankEntityEvent`

An entity ranking.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Player slot. |
| `rank` | `number` | Ranking, how interesting is this entity to view. |
| `target` | `EntityIndex` | Best/closest target entity. |

### hltv_replay

Type: `HltvReplayEvent`

| Field | Type | Description |
| --- | --- | --- |
| `delay` | `number` | Number of seconds in killer replay delay. |
| `reason` | `number` | Reason for replay    (ReplayEventType_t). |

### hltv_replay_status

Type: `HltvReplayStatusEvent`

| Field | Type | Description |
| --- | --- | --- |
| `reason` | `number` | Reason for hltv replay status change (). |

### hltv_status

Type: `HltvStatusEvent`

General HLTV status.

| Field | Type | Description |
| --- | --- | --- |
| `clients` | `number` | Number of HLTV spectators. |
| `slots` | `number` | Number of HLTV slots. |
| `proxies` | `number` | Number of HLTV proxies. |
| `master` | `string` | Disptach master IP:port. |

### hltv_title

Type: `HltvTitleEvent`

| Field | Type | Description |
| --- | --- | --- |
| `text` | `string` |  |

### hltv_versioninfo

Type: `HltvVersioninfoEvent`

| Field | Type | Description |
| --- | --- | --- |
| `version` | `number` |  |

### hostname_changed

Type: `HostnameChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `hostname` | `string` |  |

### hud_flip_changed

Type: `HudFlipChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `flipped` | `0 \| 1` |  |

### instructor_close_lesson

Type: `InstructorCloseLessonEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | The player who this lesson is intended for. |
| `hint_name` | `string` | Name of the lesson to start.  Must match instructor_lesson.txt. |

### instructor_server_hint_create

Type: `InstructorServerHintCreateEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID of the player that triggered the hint. |
| `hint_entindex` | `EntityIndex` | Entity id of the env_instructor_hint that fired the event. |
| `hint_name` | `string` | What to name the hint. For referencing it again later (e.g. a kill command for<br>the hint instead of a timeout). |
| `hint_replace_key` | `string` | Type name so that messages of the same type will replace each other. |
| `hint_target` | `number` | Entity id that the hint should display at. |
| `hint_activator_userid` | `EntityIndex` | Playerslot of the activator. |
| `hint_timeout` | `number` | How long in seconds until the hint automatically times out, 0 = never. |
| `hint_icon_onscreen` | `string` | The hint icon to use when the hint is onscreen. e.g. "icon_alert_red". |
| `hint_icon_offscreen` | `string` | The hint icon to use when the hint is offscreen. e.g. "icon_alert". |
| `hint_caption` | `string` | The hint caption. e.g. "#ThisIsDangerous". |
| `hint_activator_caption` | `string` | The hint caption that only the activator sees e.g. "#YouPushedItGood". |
| `hint_color` | `string` | The hint color in "r,g,b" format where each component is 0-255. |
| `hint_icon_offset` | `number` | How far on the z axis to offset the hint from entity origin. |
| `hint_range` | `number` | Range before the hint is culled. |
| `hint_flags` | `number` | Hint flags. |
| `hint_binding` | `string` | Bindings to use when use_binding is the onscreen icon. |
| `hint_allow_nodraw_target` | `0 \| 1` | If false, the hint will dissappear if the target entity is invisible. |
| `hint_nooffscreen` | `0 \| 1` | If true, the hint will not show when outside the player view. |
| `hint_forcecaption` | `0 \| 1` | If true, the hint caption will show even if the hint is occluded. |
| `hint_local_player_only` | `0 \| 1` | If true, only the local player will see the hint. |
| `hint_start_sound` | `string` | Game sound to play. |
| `hint_layoutfile` | `string` | Path for Panorama layout file. |
| `hint_vr_panel_type` | `number` | Attachment type for the Panorama panel. |
| `hint_vr_height_offset` | `number` | Height offset for attached panels. |
| `hint_vr_offset_x` | `number` | Offset for attached panels. |
| `hint_vr_offset_y` | `number` | Offset for attached panels. |
| `hint_vr_offset_z` | `number` | Offset for attached panels. |

### instructor_server_hint_stop

Type: `InstructorServerHintStopEvent`

| Field | Type | Description |
| --- | --- | --- |
| `hint_name` | `string` | The hint to stop. Will stop ALL hints with this name. |
| `hint_entindex` | `EntityIndex` | Entity id of the env_instructor_hint that fired the event. |

### instructor_start_lesson

Type: `InstructorStartLessonEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | The player who this lesson is intended for. |
| `hint_name` | `string` | Name of the lesson to start.  Must match instructor_lesson.txt. |
| `hint_target` | `number` | Entity id that the hint should display at. Leave empty if controller target. |
| `vr_movement_type` | `number` |  |
| `vr_single_controller` | `0 \| 1` |  |
| `vr_controller_type` | `number` |  |

### intro_video_finished

Type: `object`

_No typed fields._

### inventory_updated

Type: `InventoryUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `itemdef` | `number` |  |
| `itemid` | `number` |  |

### item_preview_closed

Type: `object`

_No typed fields._

### item_purchased

Type: `ItemPurchasedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `itemid` | `number` |  |

### item_schema_initialized

Type: `object`

_No typed fields._

### joined_chat_channel

Type: `JoinedChatChannelEvent`

| Field | Type | Description |
| --- | --- | --- |
| `channelName` | `string` |  |

### keybind_changed

Type: `object`

_No typed fields._

### last_hit

Type: `LastHitEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `EntKilled` | `number` |  |
| `FirstBlood` | `0 \| 1` |  |
| `HeroKill` | `0 \| 1` |  |
| `TowerKill` | `0 \| 1` |  |

### league_admin_info_updated

Type: `object`

_No typed fields._

### league_series_info_updated

Type: `object`

_No typed fields._

### left_chat_channel

Type: `LeftChatChannelEvent`

| Field | Type | Description |
| --- | --- | --- |
| `channelName` | `string` |  |

### live_games_updated

Type: `object`

_No typed fields._

### live_leagues_updated

Type: `object`

_No typed fields._

### lobby_invites_updated

Type: `object`

_No typed fields._

### lobby_updated

Type: `object`

_No typed fields._

### local_player_controller_team

Type: `object`

_No typed fields._

### local_player_pawn_changed

Type: `object`

_No typed fields._

### local_player_team

Type: `object`

_No typed fields._

### map_shutdown

Type: `object`

_No typed fields._

### map_transition

Type: `object`

_No typed fields._

### match_details_updated

Type: `MatchDetailsUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `matchID` | `number` |  |

### match_history_updated

Type: `MatchHistoryUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `SteamID` | `number` |  |

### matchmaking_status_visibility_changed

Type: `object`

_No typed fields._

### microtransaction_success

Type: `MicrotransactionSuccessEvent`

| Field | Type | Description |
| --- | --- | --- |
| `txnid` | `number` |  |

### modifier_event

Type: `ModifierEventEvent`

| Field | Type | Description |
| --- | --- | --- |
| `eventname` | `string` |  |
| `caster` | `number` |  |
| `ability` | `number` |  |

### news_updated

Type: `object`

_No typed fields._

### nommed_tree

Type: `NommedTreeEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |

### npc_replaced

Type: `NpcReplacedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `old_entindex` | `EntityIndex` |  |
| `new_entindex` | `EntityIndex` |  |

### npc_spawn_finished

Type: `NpcSpawnFinishedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |

### npc_spawned

Type: `NpcSpawnedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |
| `is_respawn` | `number` |  |

### particle_system_start

Type: `ParticleSystemStartEvent`

| Field | Type | Description |
| --- | --- | --- |
| `targetname` | `string` |  |

### particle_system_stop

Type: `ParticleSystemStopEvent`

| Field | Type | Description |
| --- | --- | --- |
| `targetname` | `string` |  |
| `immediate` | `0 \| 1` |  |

### party_invites_updated

Type: `object`

_No typed fields._

### party_updated

Type: `object`

_No typed fields._

### persona_updated

Type: `PersonaUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `SteamID` | `number` |  |

### physgun_pickup

Type: `PhysgunPickupEvent`

| Field | Type | Description |
| --- | --- | --- |
| `target` | `EntityIndex` | Entity picked up. |

### player_activate

Type: `PlayerActivateEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server. |

### player_changename

Type: `PlayerChangenameEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server. |
| `oldname` | `string` | Players old (current) name. |
| `newname` | `string` | Players new name. |

### player_chat

Type: `PlayerChatEvent`

A public player chat.

| Field | Type | Description |
| --- | --- | --- |
| `teamonly` | `0 \| 1` | True if team only chat. |
| `userid` | `EntityIndex` | Chatting player. |
| `playerid` | `PlayerID` | Chatting player ID. |
| `text` | `string` | Chat text. |

### player_completed_game

Type: `PlayerCompletedGameEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |
| `Winner` | `number` |  |

### player_connect

Type: `PlayerConnectEvent`

A new client connected.

| Field | Type | Description |
| --- | --- | --- |
| `name` | `string` | Player name. |
| `userid` | `EntityIndex` | User ID on server (unique on server). |
| `networkid` | `string` | Player network (i.e steam) id. |
| `xuid` | `number` | Steam id. |
| `bot` | `0 \| 1` |  |
| `index` | `number` | Player slot (entity index-1). |

### player_connect_full

Type: `PlayerConnectFullEvent`

Player has sent final message in the connection sequence.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server (unique on server). |
| `index` | `number` |  |
| `PlayerID` | `PlayerID` |  |

### player_death

Type: `PlayerDeathEvent`

A game event, name may be 32 charaters long.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID who died. |
| `attacker` | `EntityIndex` | User ID who killed. |

### player_disconnect

Type: `PlayerDisconnectEvent`

A client was disconnected.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server. |
| `reason` | `number` | See networkdisconnect enum protobuf. |
| `name` | `string` | Player name. |
| `networkid` | `string` | Player network (i.e steam) id. |
| `xuid` | `number` | Steam id. |
| `PlayerID` | `PlayerID` |  |

### player_footstep

Type: `PlayerFootstepEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |

### player_full_update

Type: `PlayerFullUpdateEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server. |
| `count` | `number` | Number of this full update. |

### player_fullyjoined

Type: `PlayerFullyjoinedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | User ID on server. |
| `name` | `string` | Player name. |

### player_hintmessage

Type: `PlayerHintmessageEvent`

| Field | Type | Description |
| --- | --- | --- |
| `hintmessage` | `string` | Localizable string of a hint. |

### player_hurt

Type: `PlayerHurtEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Player who was hurt. |
| `attacker` | `EntityIndex` | Player who attacked. |
| `health` | `number` | Remaining health points. |

### player_info

Type: `PlayerInfoEvent`

A player changed his name.

| Field | Type | Description |
| --- | --- | --- |
| `name` | `string` | Player name. |
| `userid` | `EntityIndex` | User ID on server (unique on server). |
| `steamid` | `number` | Player network (i.e steam) id. |
| `bot` | `0 \| 1` | True if player is a AI bot. |

### player_info_individual_updated

Type: `PlayerInfoIndividualUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `account_id` | `number` |  |

### player_info_updated

Type: `object`

_No typed fields._

### player_is_experienced

Type: `object`

_No typed fields._

### player_is_notexperienced

Type: `object`

_No typed fields._

### player_reconnected

Type: `PlayerReconnectedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `PlayerID` | `PlayerID` |  |

### player_report_counts_updated

Type: `PlayerReportCountsUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `positive_remaining` | `number` |  |
| `negative_remaining` | `number` |  |
| `positive_total` | `number` |  |
| `negative_total` | `number` |  |

### player_spawn

Type: `PlayerSpawnEvent`

Player spawned in game.

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |

### player_stats_updated

Type: `PlayerStatsUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `forceupload` | `0 \| 1` |  |

### player_team

Type: `PlayerTeamEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` |  |
| `team` | `number` | Team id. |
| `oldteam` | `number` | Old team id. |
| `disconnect` | `0 \| 1` | Team change because player disconnects. |
| `silent` | `0 \| 1` |  |
| `name` | `string` |  |
| `isbot` | `0 \| 1` |  |

### practice_lobby_visibility_changed

Type: `object`

_No typed fields._

### prizepool_received

Type: `PrizepoolReceivedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `success` | `0 \| 1` |  |
| `prizepool` | `number` |  |
| `leagueid` | `number` |  |

### profile_closed

Type: `object`

_No typed fields._

### profile_opened

Type: `object`

_No typed fields._

### ragdoll_dissolved

Type: `RagdollDissolvedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `entindex` | `EntityIndex` |  |

### recent_matches_updated

Type: `RecentMatchesUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `Page` | `number` |  |

### reset_defeated

Type: `object`

_No typed fields._

### rich_presence_updated

Type: `object`

_No typed fields._

### richpresence_custom_updated

Type: `object`

_No typed fields._

### round_end

Type: `RoundEndEvent`

| Field | Type | Description |
| --- | --- | --- |
| `winner` | `number` | Winner team/user i. |
| `reason` | `number` | Reson why team won. |
| `message` | `string` | End round message. |
| `time` | `number` |  |

### round_freeze_end

Type: `object`

_No typed fields._

### round_start

Type: `RoundStartEvent`

| Field | Type | Description |
| --- | --- | --- |
| `timelimit` | `number` | Round time limit in seconds. |
| `fraglimit` | `number` | Frag limit in seconds. |
| `objective` | `string` | Round objective. |

### round_start_post_nav

Type: `object`

_No typed fields._

### round_start_pre_entity

Type: `object`

_No typed fields._

### scaleform_file_download_complete

Type: `ScaleformFileDownloadCompleteEvent`

| Field | Type | Description |
| --- | --- | --- |
| `success` | `0 \| 1` |  |
| `local_filename` | `string` |  |
| `remote_url` | `string` |  |

### server_cvar

Type: `ServerCvarEvent`

A server console var has changed.

| Field | Type | Description |
| --- | --- | --- |
| `cvarname` | `string` | Cvar name, eg "mp_roundtime". |
| `cvarvalue` | `string` | New cvar value. |

### server_message

Type: `ServerMessageEvent`

A generic server message.

| Field | Type | Description |
| --- | --- | --- |
| `text` | `string` | The message text. |

### server_pre_shutdown

Type: `ServerPreShutdownEvent`

Server is about to be shut down.

| Field | Type | Description |
| --- | --- | --- |
| `reason` | `string` | Reason why server is about to be shut down. |

### server_shutdown

Type: `ServerShutdownEvent`

Server shut down.

| Field | Type | Description |
| --- | --- | --- |
| `reason` | `string` | Reason why server was shut down. |

### server_spawn

Type: `ServerSpawnEvent`

Send once a server starts.

| Field | Type | Description |
| --- | --- | --- |
| `hostname` | `string` | Public host name. |
| `address` | `string` | Hostame, IP or DNS name. |
| `port` | `number` | Server port. |
| `game` | `string` | Game dir. |
| `mapname` | `string` | Map name. |
| `addonname` | `string` | Addon name. |
| `maxplayers` | `number` | Max players. |
| `os` | `string` | WIN32, LINUX. |
| `dedicated` | `0 \| 1` | True if dedicated server. |
| `password` | `0 \| 1` | True if password protected. |

### set_instructor_group_enabled

Type: `SetInstructorGroupEnabledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `group` | `string` |  |
| `enabled` | `number` |  |

### spec_aegis_reclaim_time

Type: `SpecAegisReclaimTimeEvent`

| Field | Type | Description |
| --- | --- | --- |
| `reclaim_time` | `number` |  |

### spec_item_pickup

Type: `SpecItemPickupEvent`

| Field | Type | Description |
| --- | --- | --- |
| `player_id` | `PlayerID` |  |
| `item_name` | `string` |  |
| `purchase` | `0 \| 1` |  |
| `gift` | `0 \| 1` |  |
| `gift_player_id` | `PlayerID` |  |

### spec_mode_updated

Type: `SpecModeUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Spectating player. |

### spec_target_updated

Type: `SpecTargetUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `userid` | `EntityIndex` | Spectating player. |
| `target` | `EntityIndex` | Ehandle of the target. |

### store_pricesheet_updated

Type: `object`

_No typed fields._

### team_data_updated

Type: `object`

_No typed fields._

### team_details_updated

Type: `TeamDetailsUpdatedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `teamID` | `number` |  |

### team_info

Type: `TeamInfoEvent`

Info about team.

| Field | Type | Description |
| --- | --- | --- |
| `teamid` | `number` | Unique team id. |
| `teamname` | `string` | Team name eg "Team Blue". |

### team_score

Type: `TeamScoreEvent`

Team score changed.

| Field | Type | Description |
| --- | --- | --- |
| `teamid` | `number` | Team id. |
| `score` | `number` | Total team score. |

### team_showcase_ui_update

Type: `TeamShowcaseUiUpdateEvent`

| Field | Type | Description |
| --- | --- | --- |
| `show` | `0 \| 1` |  |
| `account_id` | `number` |  |
| `hero_entindex` | `EntityIndex` |  |
| `display_ui_on_left` | `0 \| 1` |  |

### teamplay_broadcast_audio

Type: `TeamplayBroadcastAudioEvent`

Emits a sound to everyone on a team.

| Field | Type | Description |
| --- | --- | --- |
| `team` | `number` | Unique team id. |
| `sound` | `string` | Name of the sound to emit. |

### teamplay_round_start

Type: `TeamplayRoundStartEvent`

Round restart.

| Field | Type | Description |
| --- | --- | --- |
| `full_reset` | `0 \| 1` | Is this a full reset of the map. |

### tournament_state_updated

Type: `object`

_No typed fields._

### tree_cut

Type: `TreeCutEvent`

| Field | Type | Description |
| --- | --- | --- |
| `tree_x` | `number` |  |
| `tree_y` | `number` |  |

### ugc_details_arrived

Type: `UgcDetailsArrivedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `published_file_id` | `number` |  |

### ugc_download_requested

Type: `UgcDownloadRequestedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `published_file_id` | `number` |  |

### ugc_installed

Type: `UgcInstalledEvent`

| Field | Type | Description |
| --- | --- | --- |
| `published_file_id` | `number` |  |

### ugc_subscribed

Type: `UgcSubscribedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `published_file_id` | `number` |  |

### ugc_unsubscribed

Type: `UgcUnsubscribedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `published_file_id` | `number` |  |

### user_data_downloaded

Type: `object`

Fired when achievements/stats are downloaded from Steam or XBox Live.

_No typed fields._

### vote_cast_no

Type: `VoteCastNoEvent`

| Field | Type | Description |
| --- | --- | --- |
| `team` | `number` |  |
| `entityid` | `number` | Entity id of the voter. |

### vote_cast_yes

Type: `VoteCastYesEvent`

| Field | Type | Description |
| --- | --- | --- |
| `team` | `number` |  |
| `entityid` | `number` | Entity id of the voter. |

### vote_changed

Type: `VoteChangedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `yesVotes` | `number` |  |
| `noVotes` | `number` |  |
| `potentialVotes` | `number` |  |

### vote_failed

Type: `VoteFailedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `team` | `number` |  |
| `reliable` | `1` | This event is reliable. |

### vote_passed

Type: `VotePassedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `details` | `string` |  |
| `param1` | `string` |  |
| `team` | `number` |  |
| `reliable` | `1` | This event is reliable. |

### vote_started

Type: `VoteStartedEvent`

| Field | Type | Description |
| --- | --- | --- |
| `issue` | `string` |  |
| `param1` | `string` |  |
| `votedata` | `string` |  |
| `team` | `number` |  |
| `initiator` | `number` | Entity id of the player who initiated the vote. |
| `reliable` | `1` | This event is reliable. |
