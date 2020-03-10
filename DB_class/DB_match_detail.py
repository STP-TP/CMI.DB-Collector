from DB_class.DB_manager import *


class MatchDetailList(DbManager):
    db = {
        "matchId": str,
        "playerId": str,
        "result": str,
        "partyUserCount": int,
        "characterId": str,
        "level": int,
        "killCount": int,
        "deathCount": int,
        "assistCount": int,
        "attackPoint": int,
        "damagePoint": int,
        "battlePoint": int,
        "sightPoint": int,
        "playTime": int,
        "position": str,
        "attribute": list,
        "items": list
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if ((item["playerId"] == db_input["playerId"]) and (item["matchId"] == db_input["matchId"]))), None)
        return row

    def init_path(self, option):
        self._path = path_define.user_path
