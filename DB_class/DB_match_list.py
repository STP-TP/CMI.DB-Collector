import pickle
import DB_class.user_param.param_path as path_define
import datetime
import json


def convertStr2Datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")


class MatchList:
    __match_list = []
    __db_init = False
    __path: str
    __match = {
        "date": type(datetime),
        "gameTypeId": "",
        "matchId": "",
        "players": [],  # player id 0-4 are win players, 5-9 are lose players
    }
    __result = {
        "win": [],
        "lose": []
    }
    __game_type = {
        "rating": path_define.match_rating_path,
        "normal": path_define.match_normal_path
    }

    def __init__(self, game_type):
        if MatchList.__db_init is False:
            MatchList.loadDB()
            MatchList.__db_init = True
            MatchList.__path = MatchList.__game_type.get(game_type)

    def parsingCode(self, body: dict, match_id: str):
        json_code = json.loads(body)
        self.__match["date"] = convertStr2Datetime(str(json_code.get("date")))
        self.__match["matchId"] = match_id
        for team in json_code["teams"]:
            self.__result[(team.get("result"))] = team["players"]
        self.__match["players"] = self.__result.get("win") + self.__result.get("lose")

    def checkAddOrUpdate(self, db_input):
        # DB와 id 존재 유무 체크
        row = next((index for (index, match) in enumerate(MatchList.__match_list)
                    if match["matchId"] == db_input["matchId"]), None)
        if row is None:
            self.addDB(db_input)
            return "Add"
        else:
            return "None"

    @staticmethod
    def addDB(db_input):
        MatchList.__match_list.append(db_input)

    @staticmethod
    def updateDB(row, db_input):
        MatchList.__match_list[row] = db_input

    @classmethod
    def saveDB(cls):
        with open(cls.__path, 'wb') as file_out:
            pickle.dump(MatchList.__match_list, file_out)

    @classmethod
    def loadDB(cls):
        try:
            with open(cls.__path, 'rb') as file_in:
                MatchList.__match_list = pickle.load(file_in)
        except FileNotFoundError:
            pass

    @classmethod
    def getDB(cls):
        return cls.__match_list
