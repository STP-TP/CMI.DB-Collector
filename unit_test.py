import api_comm
import unittest

class CheckAPI(unittest.TestCase):
    comm = api_comm.CommToApiServer()

    def test_nicknameBlank(self):
        print(self.comm.lookup_nickname(""))

    def test_nickname_eng(self):
        print(self.comm.lookup_nickname("blur"))

    def test_nickname_kor(self):
        print(self.comm.lookup_nickname("뀨앆"))

    def test_playerInform(self):
        print(self.comm.lookup_playerInform("926bf0fcca3a1e1483b4ce8cd2d290ef"))

    def test_playerInformBlank(self):
        print(self.comm.lookup_playerInform(""))

    def test_playerInformUnknownId(self):
        print(self.comm.lookup_playerInform("1"))

    def test_playerInformNumeric(self):
        print(self.comm.lookup_playerInform(1))

    def test_playerMatch(self):
        print(self.comm.lookup_playerMatch("926bf0fcca3a1e1483b4ce8cd2d290ef"))

    def test_playerMatchBlank(self):
        print(self.comm.lookup_playerMatch(""))

    def test_playerMatchUnknownId(self):
        print(self.comm.lookup_playerMatch("1"))

    def test_playerMatchNumeric(self):
        print(self.comm.lookup_playerMatch(1))

    def test_playerMatch_next(self):
        print(self.comm.lookup_playerMatch_next("926bf0fcca3a1e1483b4ce8cd2d290ef"))

    def test_playerMatch_next_Blank(self):
        print(self.comm.lookup_playerMatch_next(""))

    def test_playerMatch_next_UnknownId(self):
        print(self.comm.lookup_playerMatch_next("1"))

    def test_playerMatch_next_Numeric(self):
        print(self.comm.lookup_playerMatch_next(1))

    def test_MatchInform(self):
        print(self.comm.lookup_matchInform("d0a6ea889eefffdfd084979eaacc323a9858ef26804532931533a4daa46bcb32"))

    def test_matchInformBlank(self):
        print(self.comm.lookup_matchInform(""))

    def test_matchInformNumeric(self):
        print(self.comm.lookup_matchInform(1))

    def test_matchInformUnknown(self):
        print(self.comm.lookup_matchInform("1"))

    def test_PlayerRatingRanking(self):
        print(self.comm.lookup_playerRatingRanking("926bf0fcca3a1e1483b4ce8cd2d290ef"))

    def test_totalRatingRanking(self):
        print(self.comm.lookup_totalRatingRanking(0, 100))

    """
    def lookup_playerCharacterRanking(self, player_id, character_id, ranking_type="exp"):
    def lookup_totalCharacterRanking(self, character_id, ranking_type="exp", offset=0, limit=10):
    def search_itemName(self, item_name, word_type="full", limit=10):
    def search_item(self, item_name, word_type="match", limit=10, q_lst=None):
    def lookup_itemInform(self, item_id):
    def lookup_itemMultiInform(self, item_id_lst=None):
    def get_characterInform(self):
    def lookup_position_attribute(self, attribute_id):
    """