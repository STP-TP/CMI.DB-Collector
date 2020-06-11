import pymysql
from DB_class.user_param.param_db import *
from CMI_Define.sql_define import *
import datetime


def convert_datetime_to_str(date_input: datetime):
    return date_input.strftime("%Y%m%d%H%M%S")


class MysqlController:
    def __init__(self, param_host, param_id, param_pw, param_db_name):
        self.conn = pymysql.connect(host=param_host, user=param_id, password=param_pw, db=param_db_name, charset='utf8')
        self.curs = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    '''========================INSERT========================'''

    def insert_attribute(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s, %s) VALUES (%%s, %%s, %%s);"\
                    % (ATTRIBUTE_TABLE,
                       ATTRIBUTE_ID, ATTRIBUTE_NAME, ATTRIBUTE_EXPLAIN)

        self.curs.execute(query, (db_input[attribute_id[sql]], db_input[attribute_name[sql]],
                                  db_input[attribute_explain[sql]]))
        self.conn.commit()

    def insert_character(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s) VALUES (%%s, %%s);" \
                % (CHARACTER_TABLE,
                   CHARACTER_ID, CHARACTER_NAME)

        self.curs.execute(query, (db_input[character_id[sql]], db_input[character_name[sql]]))
        self.conn.commit()

    def insert_item(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s, %s, %s, %s, %s, %s, %s) " \
                "VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s);" \
                % (ITEM_TABLE,
                   ITEM_ID, ITEM_NAME, SLOT_CODE, SLOT_NAME, RARITY_CODE, RARITY_NAME, EQUIP_SLOT_CODE, EQUIP_SLOT_NAME)

        self.curs.execute(query, (db_input[item_id[sql]], db_input[item_name[sql]], int(db_input[slot_code[sql]]),
                                  db_input[slot_name[sql]], int(db_input[rarity_code[sql]]), db_input[rarity_name[sql]],
                                  int(db_input[equip_slot_code[sql]]), db_input[equip_slot_name[sql]]))
        self.conn.commit()

    def insert_match(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s, %s, %s, %s) " \
                "VALUES (%%s, %%s, %%s, %%s, %%s);" \
                % (MATCH_TABLE,
                   DATE, MATCH_ID, MAP_ID, MAP_NAME, GAME_TYPE_ID)

        self.curs.execute(query, (convert_datetime_to_str(db_input[date[sql]]), db_input[match_id[sql]],
                                  db_input[map_id[sql]], db_input[map_name[sql]], db_input[game_type_id[sql]]))
        self.conn.commit()

    def insert_match_detail(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s) " \
                "VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, %%s);" \
                % (MATCH_DETAIL_TABLE,
                   MATCH_ID, PLAYER_ID, RESULT, RANDOM, PARTY_USER_COUNT, CHARACTER_ID, LEVEL,
                   KILL_COUNT, DEATH_COUNT, ASSIST_COUNT, ATTACK_POINT, DAMAGE_POINT, BATTLE_POINT, SIGHT_POINT,
                   PLAY_TIME, POSITION_NAME, ATTRIBUTE_ID_LV1, ATTRIBUTE_ID_LV2, ATTRIBUTE_ID_LV3,
                   ITEM_101, ITEM_102, ITEM_103, ITEM_104, ITEM_105, ITEM_106, ITEM_107,
                   ITEM_202, ITEM_203, ITEM_204, ITEM_205,
                   ITEM_301, ITEM_302, ITEM_303, ITEM_304, ITEM_305)

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
        query = "INSERT IGNORE INTO %s (%s, %s) VALUES (%%s, %%s);" \
                % (POSITION_TABLE,
                   POSITION_NAME, POSITION_EXPLAIN)

        self.curs.execute(query, (db_input["position_name[sql]"], db_input["position_explain[sql]"]))
        self.conn.commit()

    def insert_user(self, db_input):
        query = "INSERT IGNORE INTO %s (%s, %s, %s, %s, %s, %s, %s, " \
                "%s, %s, %s, %s, %s, %s) " \
                "VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s, " \
                "%%s, %%s, %%s, %%s, %%s, %%s);" \
                % (USER_TABLE,
                   PLAYER_ID, NICKNAME, GRADE, CLAN_NAME, RATING_POINT, MAX_RATING_POINT, TIER_NAME,
                   RATING_WIN, RATING_LOSE, RATING_STOP, NORMAL_WIN, NORMAL_LOSE, NORMAL_STOP)

        self.curs.execute(query, (db_input[player_id[sql]], db_input[nickname[sql]], int(db_input[grade[sql]]),
                                  db_input[clan_name[sql]], int(db_input[rating_point[sql]]),
                                  int(db_input[max_rating_point[sql]]), db_input[tier_name[sql]],
                                  int(db_input[rating_win[sql]]), int(db_input[rating_lose[sql]]),
                                  int(db_input[rating_stop[sql]]), int(db_input[normal_win[sql]]),
                                  int(db_input[normal_lose[sql]]), int(db_input[normal_stop[sql]])))
        self.conn.commit()

    '''========================SELECT========================'''

    def select_by_rating(self, str_input):
        player_id_list = []
        query = "SELECT %s FROM %s WHERE %s LIKE '%s%%' ;" \
                % (PLAYER_ID, USER_TABLE, TIER_NAME, str_input)

        self.curs.execute(query)
        res = self.curs.fetchall()
        for row in res:
            player_id_list.append(row[0])
        return player_id_list

    def select_item_id(self):
        item_id_list = []
        for k in item_slot.keys():
            query = "SELECT DISTINCT %s FROM %s WHERE NOT %s = ' ';" \
                    % ("ITEM_%s" % str(k), MATCH_DETAIL_TABLE, "ITEM_%s" % str(k))

            self.curs.execute(query)
            res = self.curs.fetchall()
            for row in res:
                item_id_list.append(row[0])
        return list(set(item_id_list))

    def select_attribute_id(self):
        attribute_id_list = []
        for k in ('lv1', 'lv2', 'lv3'):
            query = "SELECT DISTINCT %s FROM %s;"\
                    % (ATTRIBUTE_ID + "_%s" % k, MATCH_DETAIL_TABLE)

            self.curs.execute(query)
            res = self.curs.fetchall()
            for row in res:
                attribute_id_list.append(row[0])
        return list(set(attribute_id_list))

    def select_search_date(self):
        date_list = {}
        query = "SELECT * FROM %s;" % SEARCH_DATE_TABLE
        self.curs.execute(query)
        res = self.curs.fetchall()
        for row in res:
            date_list[row[0]] = [row[1], row[2]]
        return date_list

    '''========================UPDATE========================'''

    def update_search_date(self, tier, past_date, recent_date):
        query = "UPDATE %s SET %s = %%s, %s = %%s WHERE %s = %%s;"\
                % (SEARCH_DATE_TABLE, PAST_DATE, RECENT_DATE, TIER_NAME)

        self.curs.execute(query, (convert_datetime_to_str(past_date), convert_datetime_to_str(recent_date),
                          tier))
        self.conn.commit()

    def disconnect_db(self):
        self.conn.close()
