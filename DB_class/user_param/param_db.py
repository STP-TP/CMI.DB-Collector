import datetime

api = 0
sql = 1

""" field_name = [api_name][sql_name] """
player_id = ["playerId", "playerId"]
nickname = ["nickname", "nickname"]
grade = ["grade", "grade"]
clan_name = ["clanName", "clanName"]
rating_point = ["ratingPoint", "ratingPoint"]
max_rating_point = ["maxRatingPoint", "maxRatingPoint"]
tier_name = ["tierName", "tierName"]
rating_win = ["win", "ratingWin"]
rating_lose = ["lose", "ratingLose"]
rating_stop = ["stop", "ratingStop"]
normal_win = ["win", "normalWin"]
normal_lose = ["lose", "normalLose"]
normal_stop = ["stop", "normalStop"]
win_count = ["winCount", "winCount"]
lose_count = ["loseCount", "loseCount"]
stop_count = ["stopCount", "stopCount"]
match_id = ["matchId", "matchId"]
result = ["result", "result"]
random = ["random", "random"]
party_user_count = ["partyUserCount", "partyUserCount"]
character_id = ["characterId", "characterId"]
level = ["level", "level"]
kill_count = ["killCount", "killCount"]
death_count = ["deathCount", "deathCount"]
assist_count = ["assistCount", "assistCount"]
attack_point = ["attackPoint", "attackPoint"]
damage_point = ["damagePoint", "damagePoint"]
battle_point = ["battlePoint", "battlePoint"]
sight_point = ["sightPoint", "sightPoint"]
play_time = ["playTime", "playTime"]
position = ["position", "position"]
attribute = ["attribute", "attribute"]
items = ["items", "items"]
date = ["date", "date"]
game_type_id = ["gameTypeId", "gameTypeId"]
players = ["players", "players"]
position_name = ["name", "positionName"]
position_explain = ["explain", "explain"]
map_id = ["mapId", "mapId"]
map_name = ["name", "mapName"]
item_id = ["itemId", "itemId"]
item_name = ["itemName", "itemName"]
slot_code = ["slotCode", "slotCode"]
slot_name = ["slotName", "slotName"]
rarity_code = ["rarityCode", "rarityCode"]
rarity_name = ["rarityName", "rarityName"]
equip_slot_code = ["equipSlotCode", "equipSlotCode"]
equip_slot_name = ["equipSlotName", "equipSlotName"]
season_code = ["seasonCode", "seasonCode"]
season_name = ["seasonName", "seasonName"]
item_explain = ["explain", "explain"]
item_explain_detail = ["explainDetail", "explainDetail"]
attribute_id = ["id", "attributeId"]
attribute_name = ["attributeName", "attributeName"]
attribute_explain = ["explain", "attributeExplain"]
character_name = ["characterName", "characterName"]
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