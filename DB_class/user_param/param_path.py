import os

basic_path = os.getcwd() + '\\DB'
user_path = basic_path + '\\user.pkl'
match_rating_path = basic_path + '\\match_rating.pkl'
match_normal_path = basic_path + '\\match_normal.pkl'
match_user_path = basic_path + '\\match_user.pkl'
item_path = basic_path + '\\items.pkl'
map_path = basic_path + '\\maps.pkl'
position_path = basic_path + '\\position.pkl'
character_path = basic_path + '\\character.pkl'


def item_img_url(item_id):
    return "https://img-api.neople.co.kr/cy/items/" + item_id


def char_img_url(char_id):
    return "https://img-api.neople.co.kr/cy/characters/" + char_id
