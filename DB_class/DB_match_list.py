class MatchList:
    __game_date = None
    __game_type_id = None
    __map_id = None
    # player id 0-4 are win players, 5-9 are lose players
    __players_list = []

    def __init__(self, match_id):
        self.__match_id = match_id

    def setMatchInformLookupResult(self, date, type_id, map_id, player_list):
        self.setGameDate(date)
        self.setGameTypeId(type_id)
        self.setMapId(map_id)
        self.setPlayers(player_list)

    def setGameDate(self, game_date):
        self.__game_date = game_date

    def setGameTypeId(self, type_id):
        self.__game_type_id = type_id

    def setMapId(self, map_id):
        self.__map_id = map_id

    def setPlayers(self, player_list):
        self.__players_list = player_list
