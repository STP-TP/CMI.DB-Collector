import pickle
import DB_class.user_param.param_path as path_define


class User:
    __user_list = []
    __db_init = False
    __num_user = 0
    __path = path_define.user_path
    __user_info = {
        "playerId": "",
        "nickname": "",
        "grade": 0,
        "clanName": "",
        "ratingPoint": 0,
        "maxRatingPoint": 0,
        "tierName": "",
        "ratingWin": "",
        "ratingLose": "",
        "ratingStop": "",
        "normalWin": "",
        "normalLose": "",
        "normalStop": ""
    }

    def __init__(self):
        if not User.__db_init:
            User.loadDB()
            User.__db_init = True

    def setPlayerInfoSearchResult(self, dict_input):
        self.__user_info["playerId"] = dict_input.get("playerId")
        self.__user_info["nickname"] = dict_input.get("nickname")
        self.__user_info["grade"] = dict_input.get("grade")
        self.__user_info["clanName"] = dict_input.get("clanName")
        self.__user_info["ratingPoint"] = dict_input.get("ratingPoint")
        self.__user_info["maxRatingPoint"] = dict_input.get("maxRatingPoint")
        self.__user_info["tierName"] = dict_input.get("tierName")
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
        self.__user_info["ratingWin"] = res[0].get("winCount")
        self.__user_info["ratingLose"] = res[0].get("loseCount")
        self.__user_info["ratingStop"] = res[0].get("stopCount")
        self.__user_info["normalWin"] = res[1].get("winCount")
        self.__user_info["normalLose"] = res[1].get("loseCount")
        self.__user_info["normalStop"] = res[1].get("stopCount")

    def checkAddOrUpdate(self, dict_input):
        row = next((index for (index, item) in enumerate(User.__user_list)
                    if item["playerId"] == dict_input["playerId"]), None)
        if not row:
            User.countNumUser()
            self.addDB(dict_input)
            return "Add"
        else:
            self.updateDB(row, dict_input)
            return "Update"

    @classmethod
    def countNumUser(cls):
        cls.__num_user += 1

    @staticmethod
    def addDB(user_info):
        if not user_info.get("playerId"):
            pass
        else:
            User.__user_list.append(user_info)

    @staticmethod
    def updateDB(row, user_info):
        User.__user_list[row] = user_info

    @classmethod
    def saveDB(cls):
        with open(cls.__path, 'wb') as file_out:
            pickle.dump(User.__user_list, file_out)
            pickle.dump(User.__num_user, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.__path, 'rb') as file_in:
                User.__user_list = pickle.load(file_in)
                User.__num_user = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__user_list

    @classmethod
    def getNumUser(cls):
        return cls.__num_user
