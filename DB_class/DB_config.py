import pymysql
from DB_class.user_param.param_db import *
import datetime


def convert_datetime_to_str(date_input):
    return date_input.strftime("%Y%m%d%H%M%S")


class MysqlController:
    def __init__(self, param_host, param_id, param_pw, param_db_name):
        MysqlController.conn = pymysql.connect(host=param_host, user=param_id, password=param_pw, db=param_db_name,
                                               charset='utf8')
        self.curs = self.conn.cursor()

    def insert_attribute(self, db_input):
        query = '''
        INSERT IGNORE INTO attributeTbl (attributeID, attributeName, attributeExplain) VALUES (%s, %s, %s)
        '''
        self.curs.execute(query, (db_input[attribute_id[sql]], db_input[attribute_name[sql]],
                                  db_input[attribute_explain[sql]]))
        self.conn.commit()

    def insert_character(self, db_input):
        query = '''
        INSERT IGNORE INTO characterTbl (characterID, characterName) VALUES (%s, %s)
        '''
        self.curs.execute(query, (db_input[character_id[sql]], db_input[character_name[sql]]))
        self.conn.commit()

    def insert_item(self, db_input):
        query = '''
        INSERT IGNORE INTO itemTbl (itemID, itemName, slotCode, slotName, rarityCode, rarityName, equipSlotCode,
         equipSlotName)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)   
        '''
        self.curs.execute(query, (db_input[item_id[sql]], db_input[item_name[sql]], int(db_input[slot_code[sql]]),
                                  db_input[slot_name[sql]], int(db_input[rarity_code[sql]]), db_input[rarity_name[sql]],
                                  int(db_input[equip_slot_code[sql]]), db_input[equip_slot_name[sql]]))
        self.conn.commit()

    def insert_match(self, db_input):
        query = '''
        INSERT IGNORE INTO matchTbl (date, matchID, mapID, mapName, gametypeID) VALUES (%s, %s, %s, %s, %s)
        '''
        self.curs.execute(query, (convert_datetime_to_str(db_input[date[sql]]), db_input[match_id[sql]],
                                  db_input[map_id[sql]], db_input[map_name[sql]], db_input[game_type_id[sql]]))
        self.conn.commit()

    def insert_match_detail(self, db_input):
        query = '''INSERT IGNORE INTO match_detailTbl (matchID, playerID, result, random, partyUserCount, characterID,
         level, killCount, deathCount, assistCount, attackPoint, damagePoint, battlePoint, sightPoint, playTime,
         positionName, attributeID_lv1, attributeID_lv2, attributeID_lv3, item_101, item_102, item_103, item_104,
         item_105, item_106, item_107, item_202, item_203, item_204, item_205, item_301, item_302, item_303, item_304,
         item_305) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        self.curs.execute(query, (db_input[match_id[sql]], db_input[player_id[sql]], db_input[result[sql]],
                                  db_input[random[sql]], int(db_input[party_user_count[sql]]),
                                  db_input[character_id[sql]], int(db_input[level[sql]]),
                                  int(db_input[kill_count[sql]]), int(db_input[death_count[sql]]),
                                  int(db_input[assist_count[sql]]), int(db_input[attack_point[sql]]),
                                  int(db_input[damage_point[sql]]), int(db_input[battle_point[sql]]),
                                  int(db_input[sight_point[sql]]), int(db_input[play_time[sql]]),
                                  db_input[position_name[sql]], db_input[attribute[sql]][0], db_input[attribute[sql]][1],
                                  db_input[attribute[sql]][2], db_input[items[sql]][0][1], db_input[items[sql]][1][1],
                                  db_input[items[sql]][2][1], db_input[items[sql]][3][1], db_input[items[sql]][4][1],
                                  db_input[items[sql]][5][1], db_input[items[sql]][6][1], db_input[items[sql]][7][1],
                                  db_input[items[sql]][8][1], db_input[items[sql]][9][1], db_input[items[sql]][10][1],
                                  db_input[items[sql]][11][1], db_input[items[sql]][12][1], db_input[items[sql]][13][1],
                                  db_input[items[sql]][14][1], db_input[items[sql]][15][1]))
        self.conn.commit()

    def insert_position(self, db_input):
        query = '''INSERT IGNORE INTO positionTbl (positionName, positionExplain) VALUES (%s, %s)
        '''
        self.curs.execute(query, (db_input["position_name[sql]"], db_input["position_explain[sql]"]))
        self.conn.commit()

    def insert_user(self, db_input):
        query = '''INSERT INTO userTbl (playerID, nickname, grade, clanName, ratingPoint, maxRatingPoint, tierName,
         ratingWin, ratingLose, ratingStop, normalWin, normalLose, normalStop) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE playerID = VALUES(playerID), nickname = VALUES(nickname), grade = VALUES(grade),
        clanName = VALUES(clanName), ratingPoint = VALUES(ratingPoint), maxRatingPoint = VALUES(maxRatingPoint),
        tierName = VALUES(tierName), ratingWin = VALUES(ratingWin), ratingLose = VALUES(ratingLose),
        ratingStop = VALUES(ratingStop), normalWin = VALUES(normalWin), normalLose = VALUES(normalLose),
        normalStop = VALUES(normalStop);
        '''
        self.curs.execute(query, (db_input[player_id[sql]], db_input[nickname[sql]], int(db_input[grade[sql]]),
                                  db_input[clan_name[sql]], int(db_input[rating_point[sql]]),
                                  int(db_input[max_rating_point[sql]]), db_input[tier_name[sql]],
                                  int(db_input[rating_win[sql]]), int(db_input[rating_lose[sql]]),
                                  int(db_input[rating_stop[sql]]), int(db_input[normal_win[sql]]),
                                  int(db_input[normal_lose[sql]]), int(db_input[normal_stop[sql]])))
        self.conn.commit()

    def disconnect_db(self):
        self.conn.close()

#testSQL = MysqlController('localhost', 'root', 'vmfhwprxm2@', 'modeldb')
