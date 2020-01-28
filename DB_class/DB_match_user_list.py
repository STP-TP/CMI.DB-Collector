class GamePosition:
    __name = None
    __explain = None
    __attribute = []

    def setGamePosition(self, name, explain, attribute):
        self.__name = name
        self.__explain = explain
        self.__attribute = attribute


class MatchUserList:
    __random = None
    __party_user_count = None
    __character_id = None
    __level = None
    __kill_cnt = None
    __death_cnt = None
    __assist_cnt = None
    __attack_point = None
    __damage_point = None
    __battle_point = None
    __sight_point = None
    __play_time = None
    __position_name = None
    __position_attribute = []
    __item = None

    def __init__(self, match_id, player_id):
        self.__match_id = match_id
        self.__match_id = player_id

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

    def setPosition(self, position_name):
        self.__position_name = position_name

    def setPositionAttribute(self, att1, att2, att3):
        self.__position_attribute = [att1, att2, att3]

    def setItem(self, item):
        self.__item = item
