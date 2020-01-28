class GameRecord:
    def __init__(self, type_id, win, lose, stop):
        self.__game_type_id = type_id
        self.__win_count = win
        self.__lose_count = lose
        self.__stop_count = stop


class UserList:
    __num_user = 0
    __nickname = None
    __grade = None
    __clan_name = None
    __rating_point = None
    __max_rating_point = None
    __tier_name = None
    __record_rating = None
    __record_normal = None

    __user_list = {
        "playerId": "",
        "nickname": "",
        "grade": 0,
        "clanName": "",
        "ratingPoint": 0,
        "maxRatingPoint": 0,
        "tierName": "",
        "records": []
    }

    def __init__(self, player_id):
        self.__player_id = player_id
        UserList.__num_user += 1

    def setPlayerLookupResult(self, nickname, grade):
        self.setNickname(nickname)
        self.setGrade(grade)

    def setPlayerInformLookupResult(self, informList, recordList):
        """
        nickname, grade, clanName, ratingPoint, maxRatingPoint, tierName
        recordRating(gameTypeId, win, lose, stop), recordNormal(gameTypeId, win, lose, stop)
        """
        self.setNickname(informList[0])
        self.setGrade(informList[1])
        self.setClanName(informList[2])
        self.setRatingPoint(informList[3], informList[4])
        self.setTierName(informList[5])
        self.setRecordRating(recordList[0][0], recordList[0][1], recordList[0][2], recordList[0][3])
        self.setRecordNormal(recordList[1][0], recordList[1][1], recordList[1][2], recordList[1][3])

    def setNickname(self, nickname):
        self.__nickname = nickname

    def setGrade(self, grade):
        self.__grade = grade

    def setClanName(self, clan_name):
        self.__clan_name = clan_name

    def setRatingPoint(self, rating_point, max_rating_point):
        self.__rating_point = rating_point
        self.__max_rating_point = max_rating_point

    def setTierName(self, tier_name):
        self.__tier_name = tier_name

    def setRecordRating(self, type_id, win, lose, stop):
        self.__record_rating = GameRecord(type_id, win, lose, stop)

    def setRecordNormal(self, type_id, win, lose, stop):
        self.__record_normal = GameRecord(type_id, win, lose, stop)
