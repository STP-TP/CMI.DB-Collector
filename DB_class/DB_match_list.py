import pickle
import DB_class.user_param.param_path as path_define
import datetime
import json


def convertStr2Datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")


class MatchList:
    match_list = []
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
        self.__path = MatchList.__game_type.get(game_type)

    def parsingCode(self, body):
        json_code = json.loads(body)
        self.__match["date"] = convertStr2Datetime(str(json_code.get("date")))
        # self.__match["matchId"] = json_code["matchId"]
        for team in json_code["teams"]:
            self.__result[(team.get("result"))] = team["players"]
        self.__match["players"] = self.__result.get("win") + self.__result.get("lose")
        pass

    def checkAddOrUpdate(self, match):
        # DB와 id 존재 유무 체크
        row = next((index for (index, match) in enumerate(MatchList.match_list)
                    if match["matchId"] == match["matchId"]), None)
        if row is None:
            self.addDB(match)
            return "Add"
        else:
            return "None"

    def addDB(self, match):
        MatchList.match_list.append(match)

    def updateDB(self, row, match):
        MatchList.match_list[row] = match

    def saveDB(self):
        with open(self.__path, 'wb') as file_out:
            pickle.dump(MatchList.match_list, file_out)

    def loadDB(self):
        with open(self.__path, 'rb') as file_in:
            MatchList.map_list = pickle.load(file_in)
