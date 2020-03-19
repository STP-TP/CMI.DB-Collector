import pymysql
from DB_class.user_param.param_db import *
import datetime


def convert_datetime_to_str(date):
    return date.strftime("%Y%m%d%H%M%S")


class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()

    def insert_attribute(self, db_input):
        sql = 'INSERT INTO attributeTbl VALUES (%s, %s, %s)'
        self.curs.execute(sql,(db_input["attribute_id"][sql], db_input["attribute_name"][sql],
                               db_input["attribute_explain"][sql]))
        self.conn.commit()

    def insert_character(self, db_input):
        sql = 'INSERT INTO characterTbl VALUES (%s, %s)'
        self.curs.execute(sql, (db_input["character_id"][sql], db_input["character_name"][sql]))
        self.conn.commit()

    def insert_match(self, db_input):
        sql = 'INSERT INTO matchTbl VALUES (%s, %s, %s, %s, %s)'
        self.curs.execute(sql, (convert_datetime_to_str(db_input["date"][sql]), db_input["match_id"][sql],
                                db_input["map_id"][sql], db_input["map_name"][sql], db_input["game_type_id"][sql]))
        self.conn.commit()

    def insert_match_detail(self, db_input):
        sql = 'INSERT INTO match_detailTbl VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
              '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, )'
        self.curs.execute(sql, (db_input["match_id"][sql], db_input["player_id"][sql], db_input["result"][sql],
                                db_input["random"][sql], db_input["random"][sql], db_input["random"][sql],
                                ))
        self.conn.commit()

    def insert_position(self, db_input):
        sql = 'INSERT INTO positionTbl VALUES (%s, %s)'
        self.curs.execute(sql, (db_input["position_name"][sql], db_input["position_explain"][sql]))
        self.conn.commit()

    def insert_user(self, db_input):
        sql = 'INSERT INTO userTbl VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.curs.execute(sql, (db_input[player_id[sql]], db_input[nickname[sql]], int(db_input[grade[sql]]),
                                db_input[clan_name[sql]], int(db_input[rating_point[sql]]),
                                int(db_input[max_rating_point[sql]]), db_input[tier_name[sql]],
                                int(db_input[rating_win[sql]]), int(db_input[rating_lose[sql]]),
                                int(db_input[rating_stop[sql]]), int(db_input[normal_win[sql]]),
                                int(db_input[normal_lose[sql]]), int(db_input[normal_stop[sql]])))

    def test_create(self):
        sql = '''
                CREATE TABLE USERS 
                (
                      USER_ID     VARCHAR(50)    NOT NULL PRIMARY KEY,
                      USER_NM     VARCHAR(200)    NOT NULL COMMENT '사용자명',
                      TEL_NO     VARCHAR(50)   COMMENT '전화번호',
                      EMAIL     VARCHAR(100)   COMMENT '이메일',
                      COMPNY_NM     VARCHAR(200)  COMMENT '회사명',
                      DEPT_NM     VARCHAR(200)   COMMENT '부서명',
                      JDEG_NM     VARCHAR(200)    COMMENT '직급명',
                      WORKING_SITE_NM   VARCHAR(200)  COMMENT '근무지역명',
                      REG_TM     TIMESTAMP   COMMENT '등록일시',
                      CHG_TM     TIMESTAMP   COMMENT '변경일시'
                 )ENGINE=InnoDB DEFAULT CHARSET=utf8
              '''
        self.curs.execute(sql)
        self.conn.commit()

    def test_insert(self):
        sql = '''
                   INSERT INTO TESTS VALUES (%s, %s)
                   '''
        self.curs.execute(sql, ("19910114144400", 142))
        self.conn.commit()

    def disconnect_db(self):
        self.conn.close()


db = {
    "player_id": "9ff6b86fcb477249ea6ef8ab57ec4795",
    "nickname": "아얌",
    "grade": "51",
    "clan_name": "마음속하유안",
    "rating_point": "1302",
    "max_rating_point":"1302",
    "tier_name": "히어로",
    "rating_win": "5801",
    "rating_lose": "12",
    "rating_stop": "0",
    "normal_win": "22",
    "normal_lose": "1",
    "normal_stop": "0"
}

testSQL = MysqlController('localhost', 'root', 'vmfhwprxm2@', 'modeldb')
#testSQL.insertAttribute('testID','testAtt','testAttexp','탱커')
#testSQL.test_query()
testSQL.insert_user(db)
testSQL.disconnect_db()
