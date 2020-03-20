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
attribute_id = ["id", "attributeId"]
attribute_name = ["attributeName", "attributeName"]
attribute_explain = ["attributeExplain", "attributeExplain"]
character_name = ["characterName", "characterName"]
rating = "rating"
normal = "normal"

user_db = {
    player_id[sql]: str,
    nickname[sql]: str,
    grade[sql]: int,
    clan_name[sql]: str,
    rating_point[sql]: int,
    max_rating_point[sql]: int,
    tier_name[sql]: str,
    rating_win[sql]: int,
    rating_lose[sql]: int,
    rating_stop[sql]: int,
    normal_win[sql]: int,
    normal_lose[sql]: int,
    normal_stop[sql]: int
}
match_db = {
    date[sql]: type(datetime),
    game_type_id[sql]: str,
    match_id[sql]: str,
    players[sql]: list  # player id 0-4 are win players, 5-9 are lose players
}
match_detail_db = {
    match_id[sql]: str,
    player_id[sql]: str,
    result[sql]: str,
    random[sql]: bool,
    party_user_count[sql]: int,
    character_id[sql]: str,
    level[sql]: int,
    kill_count[sql]: int,
    death_count[sql]: int,
    assist_count[sql]: int,
    attack_point[sql]: int,
    damage_point[sql]: int,
    battle_point[sql]: int,
    sight_point[sql]: int,
    play_time[sql]: int,
    position[sql]: str,
    attribute[sql]: list,
    items[sql]: list
}
position_db = {
    position_name[sql]: str,
    position_explain[sql]: str
}
map_db = {
    map_id[sql]: str,
    map_name[sql]: str
}
item_db = {
    item_id[sql]: str,
    item_name[sql]: str,
    slot_code[sql]: str,
    slot_name[sql]: str,
    rarity_code[sql]: str,
    rarity_name[sql]: str,
    equip_slot_code[sql]: str,
    equip_slot_name[sql]: str
}
attribute_db = {
    attribute_id[sql]: str,
    attribute_name[sql]: str,
    attribute_explain[sql]: str
}
character_db = {
    character_id[sql]: str,
    character_name[sql]: str
}
