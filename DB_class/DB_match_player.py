import pickle
import DB_class.user_param.param_path as path_define


class MatchPlayer:
    __db_init = False
    __match_player_list = []
    __match_player_info = {
        "date": "",
        "gameTypeId": "",
        "result": "",
        "mapId": "",
        "mapName": "",
        "playerId": "",
        "playerNickname": "",
        "random": "",
        "partyUserCount": "",
        "characterId": "",
        "characterName": "",
        "level": "",
        "killCount": "",
        "deathCount": "",
        "assistCount": "",
        "attackPoint": "",
        "damagePoint": "",
        "battlePoint": "",
        "sightPoint": "",
        "playTime": "",
        "position": "",
        "items": ""
    }

    def __init__(self):
        if not self.__db_init:
            self.loadDB()
            self.__db_init = True

    def setMatchPlayerInfoSearchResult(self, dict_input):
        self.__match_player_info["date"] = dict_input.get("date")
        temp_teams = []
        temp_teams = dict_input.get("teams")
        self.__match_player_info["result"] = temp_teams[0].get("result")
        self.__match_player_info["mapId"] = dict_input.get("date")
        self.__match_player_info["mapName"] = dict_input.get("date")
        self.__match_player_info["playerId"] = dict_input.get("date")
        self.__match_player_info["playerNickname"] = dict_input.get("date")
        self.__match_player_info["random"] = dict_input.get("date")
        self.__match_player_info["partyUserCount"] = dict_input.get("date")
        self.__match_player_info["characterId"] = dict_input.get("date")
        self.__match_player_info["characterName"] = dict_input.get("date")
        self.__match_player_info["level"] = dict_input.get("date")
        self.__match_player_info["killCount"] = dict_input.get("date")
        self.__match_player_info["deathCount"] = dict_input.get("date")
        self.__match_player_info["assistCount"] = dict_input.get("date")
        self.__match_player_info["attackPoint"] = dict_input.get("date")
        self.__match_player_info["damagePoint"] = dict_input.get("date")
        self.__match_player_info["battlePoint"] = dict_input.get("date")
        self.__match_player_info["sightPoint"] = dict_input.get("date")
        self.__match_player_info["playTime"] = dict_input.get("date")
        self.__match_player_info["position"] = dict_input.get("date")
        self.__match_player_info["items"] = dict_input.get("date")


    def setRandom(self, random):
        self.__random = random

    def setPartyUserCount(self, party_cnt):
        self.__party_user_count = party_cnt

    def setCharacterId(self, char_id):
        self.__character_id = char_id

    def setLevel(self, lvl):
        self.__level = lvl

    def setKDACount(self, kill, death, assist):
        self.__kill_cnt = kill
        self.__death_cnt = death
        self.__assist_cnt = assist

    def setPoints(self, attack, damage, battle, sight):
        self.__attack_point = attack
        self.__damage_point = damage
        self.__battle_point = battle
        self.__sight_point = sight

    def setPlayTime(self, time):
        self.__play_time = time

    def setPosition(self, name, explain, attribute_id):
        self.__position = GamePosition(name, explain, attribute_id)

    def setItem(self, item_id_list):
        self.__items = item_id_list
