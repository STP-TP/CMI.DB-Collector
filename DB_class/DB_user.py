from DB_class.DB_manager import *


class User(DbManager):
    db = {
        "playerId": str,
        "nickname": str,
        "grade": int,
        "clanName": str,
        "ratingPoint": int,
        "maxRatingPoint": int,
        "tierName": str,
        "ratingWin": str,
        "ratingLose": str,
        "ratingStop": str,
        "normalWin": str,
        "normalLose": str,
        "normalStop": str
    }
    __db = {
        "playerId": str,
        "nickname": str,
        "grade": int,
        "clanName": str,
        "ratingPoint": int,
        "maxRatingPoint": int,
        "tierName": str,
        "ratingWin": str,
        "ratingLose": str,
        "ratingStop": str,
        "normalWin": str,
        "normalLose": str,
        "normalStop": str
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["playerId"] == db_input["playerId"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.user_path

    def setPlayerInfoSearchResult(self, dict_input):
        self.__db["playerId"] = dict_input.get("playerId")
        self.__db["nickname"] = dict_input.get("nickname")
        self.__db["grade"] = dict_input.get("grade")
        self.__db["clanName"] = dict_input.get("clanName")
        self.__db["ratingPoint"] = dict_input.get("ratingPoint")
        self.__db["maxRatingPoint"] = dict_input.get("maxRatingPoint")
        self.__db["tierName"] = dict_input.get("tierName")
        """
        dict_input.get("records") means
        [{"gameTypeId" : "rating", "winCount" : num, "loseCount" : num, "stopCount" : num},
         {"gameTypeId" : "normal", "winCount" : num, "loseCount" : num, "stopCount" : num}]
        so
        res[0] = {"gameTypeId" : "rating", "winCount" : num, "loseCount" : num, "stopCount" : num},
        res[1] = {"gameTypeId" : "normal", "winCount" : num, "loseCount" : num, "stopCount" : num}]
        """
        res = []
        res = dict_input.get("records")
        self.__db["ratingWin"] = res[0].get("winCount")
        self.__db["ratingLose"] = res[0].get("loseCount")
        self.__db["ratingStop"] = res[0].get("stopCount")
        self.__db["normalWin"] = res[1].get("winCount")
        self.__db["normalLose"] = res[1].get("loseCount")
        self.__db["normalStop"] = res[1].get("stopCount")
