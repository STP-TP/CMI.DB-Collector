import os

database_path = os.getcwd() + '\\DB'
user_path = database_path + '\\user.pkl'
match_rating_path = database_path + '\\match_rating.pkl'
match_normal_path = database_path + '\\match_normal.pkl'
match_detail_path = database_path + '\\match_detail.pkl'
item_path = database_path + '\\item.pkl'
map_path = database_path + '\\map.pkl'
position_path = database_path + '\\position.pkl'
attribute_path = database_path + '\\attribute.pkl'
character_path = database_path + '\\character.pkl'

log_path = os.getcwd() + '\\LOG'
api_log = '\\api_http_error.json'


def make_dir(param_path):
    try:
        os.makedirs(param_path)
        print("Directory ", param_path, " Created")
    except FileExistsError:
        pass


def item_img_url(item_id):
    return "https://img-api.neople.co.kr/cy/items/" + item_id


def char_img_url(char_id):
    return "https://img-api.neople.co.kr/cy/characters/" + char_id
