import datetime
from CMI_Define.sql_define import *

api = 0
sql = 1

""" field_name = [api_name][sql_name] """
player_id = ["playerId", PLAYER_ID]
nickname = ["nickname", NICKNAME]
grade = ["grade", GRADE]
clan_name = ["clanName", CLAN_NAME]
rating_point = ["ratingPoint", RATING_POINT]
max_rating_point = ["maxRatingPoint", MAX_RATING_POINT]
tier_name = ["tierName", TIER_NAME]
rating_win = ["win", RATING_WIN]
rating_lose = ["lose", RATING_LOSE]
rating_stop = ["stop", RATING_STOP]
normal_win = ["win", NORMAL_WIN]
normal_lose = ["lose", NORMAL_LOSE]
normal_stop = ["stop", NORMAL_STOP]
win_count = ["winCount", WIN_COUNT]
lose_count = ["loseCount", LOSE_COUNT]
stop_count = ["stopCount", STOP_COUNT]
match_id = ["matchId", MATCH_ID]
result = ["result", RESULT]
random = ["random", RANDOM]
party_user_count = ["partyUserCount", PARTY_USER_COUNT]
character_id = ["characterId", CHARACTER_ID]
level = ["level", LEVEL]
kill_count = ["killCount", KILL_COUNT]
death_count = ["deathCount", DEATH_COUNT]
assist_count = ["assistCount", ASSIST_COUNT]
attack_point = ["attackPoint", ATTACK_POINT]
damage_point = ["damagePoint", DAMAGE_POINT]
battle_point = ["battlePoint", BATTLE_POINT]
sight_point = ["sightPoint", SIGHT_POINT]
play_time = ["playTime", PLAY_TIME]
position = ["position", POSITION]
attribute = ["attribute", ATTRIBUTE]
items = ["items", ITEMS]
date = ["date", DATE]
game_type_id = ["gameTypeId", GAME_TYPE_ID]
players = ["players", PLAYERS]
position_name = ["name", POSITION_NAME]
position_explain = ["explain", POSITION_EXPLAIN]
map_id = ["mapId", MAP_ID]
map_name = ["name", MAP_NAME]
item_id = ["itemId", MAP_ID]
item_name = ["itemName", ITEM_NAME]
slot_code = ["slotCode", SLOT_CODE]
slot_name = ["slotName", SLOT_NAME]
rarity_code = ["rarityCode", RARITY_CODE]
rarity_name = ["rarityName", RARITY_NAME]
equip_slot_code = ["equipSlotCode", EQUIP_SLOT_CODE]
equip_slot_name = ["equipSlotName", EQUIP_SLOT_NAME]
season_code = ["seasonCode", SEASON_CODE]
season_name = ["seasonName", SEASON_NAME]
item_explain = ["explain", ITEM_EXPLAIN]
item_explain_detail = ["explainDetail", ITEM_EXPLAIN_DETAIL]
attribute_id = ["id", ATTRIBUTE_ID]
attribute_name = ["attributeName", ATTRIBUTE_NAME]
attribute_explain = ["explain", ATTRIBUTE_EXPLAIN]
character_name = ["characterName", CHARACTER_NAME]
rating = "rating"
normal = "normal"

user_db = {
    player_id[sql]: "",
    nickname[sql]: "",
    grade[sql]: 0,
    clan_name[sql]: "",
    rating_point[sql]: 0,
    max_rating_point[sql]: 0,
    tier_name[sql]: "",
    rating_win[sql]: 0,
    rating_lose[sql]: 0,
    rating_stop[sql]: 0,
    normal_win[sql]: 0,
    normal_lose[sql]: 0,
    normal_stop[sql]: 0
}
match_db = {
    date[sql]: type(datetime),
    match_id[sql]: "",
    map_id[sql]: "",
    map_name[sql]: "",
    game_type_id[sql]: "",
    players[sql]: list  # player id 0-4 are win players, 5-9 are lose players
}
match_detail_db = {
    match_id[sql]: "",
    player_id[sql]: "",
    result[sql]: "",
    random[sql]: bool,
    party_user_count[sql]: 0,
    character_id[sql]: "",
    level[sql]: 0,
    kill_count[sql]: 0,
    death_count[sql]: 0,
    assist_count[sql]: 0,
    attack_point[sql]: 0,
    damage_point[sql]: 0,
    battle_point[sql]: 0,
    sight_point[sql]: 0,
    play_time[sql]: 0,
    position_name[sql]: "",
    attribute[sql]: list,
    items[sql]: list
}
position_db = {
    position_name[sql]: "",
    position_explain[sql]: ""
}
item_db = {
    item_id[sql]: "",
    item_name[sql]: "",
    character_id[sql]: "",
    slot_code[sql]: 0,
    slot_name[sql]: "",
    rarity_code[sql]: 0,
    rarity_name[sql]: "",
    season_code[sql]: 0,
    season_name[sql]: "",
    item_explain[sql]: "",
    item_explain_detail[sql]: ""
}
attribute_db = {
    attribute_id[sql]: "",
    attribute_name[sql]: "",
    attribute_explain[sql]: "",
    position_name[sql]: ""
}
character_db = {
    character_id[sql]: "",
    character_name[sql]: ""
}
item_slot = {
    101: "",
    102: "",
    103: "",
    104: "",
    105: "",
    106: "",
    107: "",
    202: "",
    203: "",
    204: "",
    205: "",
    301: "",
    302: "",
    303: "",
    304: "",
    305: ""
}
tier_list = ["HERO", "LEGEND", "ACE", "JOKER", "GOLD", "SILVER", "BRONZE", "Unranked"]