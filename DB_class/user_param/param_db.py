import datetime

player_id = "playerId"
nickname = "nickname"
grade = "grade"
clan_name = "clanName"
rating_point = "ratingPoint"
max_rating_point = "maxRatingPoint"
tier_name = "tierName"
rating_win = "ratingWin"
rating_lose = "ratingLose"
rating_stop = "ratingStop"
normal_win = "normalWin"
normal_lose = "normalLose"
normal_stop = "normalStop"
match_id = "matchId"
result = "result"
party_user_count = "partyUserCount"
character_id = "characterId"
level = "level"
kill_count = "killCount"
death_count = "deathCount"
assist_count = "assistCount"
attack_point = "attackPoint"
damage_point = "damagePoint"
battle_point = "battlePoint"
sight_point = "sightPoint"
play_time = "playTime"
position = "position"
attribute = "attribute"
items = "items"
date = "date"
game_type_id = "gameTypeId"
players = "players"
name = "name"
explain = "explain"
map_id = "mapId"
item_id = "itemId"
item_name = "itemName"
slot_code = "slotCode"
slot_name = "slotName"
rarity_code = "rarityCode"
rarity_name = "rarityName"
equip_slot_code = "equipSlotCode"
equip_slot_name = "equipSlotName"
attribute_id = "attributeId"
attribute_name = "attributeName"
character_name = "characterName"

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
    game_type_id: str,
    match_id: str,
    players: list  # player id 0-4 are win players, 5-9 are lose players
}
match_detail_db = {
    match_id: str,
    player_id: str,
    result: str,
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
    name: str,
    explain: str
}
map_db = {
    map_id: str,
    name: str
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
    explain: str
}
character_db = {
    character_id: str,
    character_name: str
}
