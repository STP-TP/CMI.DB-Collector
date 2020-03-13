import pymysql


class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()

    def insertAttribute(self, attribute_ID, attribute_name, attribute_explain, position_name):
        sql = 'INSERT INTO attributeTbl VALUES (%s, %s, %s, %s)'
        self.curs.execute(sql,(attribute_ID, attribute_name, attribute_explain, position_name))
        self.conn.commit()

    def insertCharacter(self, character_ID, character_name):
        sql = 'INSERT INTO characterTbl VALUES (%s, %s)'
        self.curs.execute(sql, (character_ID, character_name))
        self.conn.commit()

    def insertMatch(self, date, match_ID, map_ID, map_name, gametype_ID):
        sql = 'INSERT INTO matchTbl VALUES (%s, %s, %s, %s, %s)'
        self.curs.execute(sql, (date, match_ID, map_ID, map_name, gametype_ID))
        self.conn.commit()

    def insertMatchDetail(self, match_ID, player_ID, result, random, party_user_count, character_ID, level,
                          kill_count, death_count, assist_count, attack_point, damage_point, battle_point, sight_point,
                          play_time, position_Name, attribute_ID_lv1, attribute_ID_lv2, attribute_ID_lv3):
        sql = 'INSERT INTO match_detailTbl VALUES ()'

    def insertPosition(self):
        sql = 'INSERT INTO positionTbl VALUES ()'

    def insertUser(self):
        sql = 'INSERT INTO userTbl VALUES ()'

    def testCreate(self):
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

    def disconnect_db(self):
        self.conn.close()


testSQL = MysqlController('localhost', 'root', 'vmfhwprxm2@', 'modeldb')
#testSQL.insertAttribute('testID','testAtt','testAttexp','탱커')
testSQL.disconnect_db()
