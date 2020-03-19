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
    player_id: str,
    nickname: str,
    grade: int,
    clan_name: str,
    rating_point: int,
    max_rating_point: int,
    tier_name: str,
    rating_win: str,
    rating_lose: str,
    rating_stop: str,
    normal_win: str,
    normal_lose: str,
    normal_stop: str
}
match_db = {
    date: type(datetime),
    match_id: str,
    map_id: str,
    map_name: str,
    game_type_id: str,
    players: list  # player id 0-4 are win players, 5-9 are lose players
}
match_detail_db = {
    match_id: str,
    player_id: str,
    result: str,
    random: bool,
    party_user_count: int,
    character_id: str,
    level: int,
    kill_count: int,
    death_count: int,
    assist_count: int,
    attack_point: int,
    damage_point: int,
    battle_point: int,
    sight_point: int,
    play_time: int,
    position: str,
    attribute: list,
    items: list
}
position_db = {
    position_name: str,
    position_explain: str
}
item_db = {
    item_id: str,
    item_name: str,
    slot_code: str,
    slot_name: str,
    rarity_code: str,
    rarity_name: str,
    equip_slot_code: str,
    equip_slot_name: str
}
attribute_db = {
    attribute_id: str,
    attribute_name: str,
    attribute_explain: str
}
character_db = {
    character_id: str,
    character_name: str
}
