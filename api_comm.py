import datetime
import time
import urllib.request as socket
import urllib.error as urlerr
from urllib.parse import quote


class CommToApiServer:
    _apiKey = "apikey=0rYk7DYbNFelyQguZRmwhWxF1QhZ0yJP"
    _apiURL = "https://api.neople.co.kr/cy/"
    _apiWordType = "wordType=full"
    _matchNextEnable = False
    _innerErrCode = 0
    __api_start_time = [];

    _itemList = {
        0: "characterId",
        1: "slotCode",
        2: "rarityCode",
        3: "seasonCoe"
    }
    _permissions = {
        200: "정상적인 응답",
        400: "요청에 대한 유효성 검증 실패 또는 필수 파라미터 에러",
        401: "인증 오류",
        404: "존재하지 않은 리소스 또는 페이지",
        500: "시스템 오류",
        503: "시스템 점검",
        1900: "매개변수 공백 입력",  # 매개변수 공백일시 urllib Error 발생함
        1901: "매개변수 타입 에러",  # 매개변수 타입 설정 오류발생
        1092: "초기값 없는 Next 명령 기입"
    }

    def __init__(self, api_key="0rYk7DYbNFelyQguZRmwhWxF1QhZ0yJP"):
        self.apiKey = "apikey=" + api_key

    def _get_apiBody(self, request_url):
        # 횟수 제한 확인
        if len(CommToApiServer.__api_start_time) is 0:
            CommToApiServer.__api_start_time.append(datetime.datetime.now())
        else:
            CommToApiServer.__api_start_time.append(datetime.datetime.now())
            api_cnt = len(CommToApiServer.__api_start_time)
            span_time = (CommToApiServer.__api_start_time[api_cnt - 1]
                         - CommToApiServer.__api_start_time[0])

            if (span_time.total_seconds() < 1) & (api_cnt >= 100):
                time.sleep(1 - span_time.total_seconds() + 0.3)
            if api_cnt >= 100:
                del CommToApiServer.__api_start_time[0]

        try:
            response = socket.urlopen(request_url)
            res_code = response.getcode()
            responseBody = response.read().decode('utf-8')
            return self._get_response_code(res_code, responseBody)
        except urlerr.URLError as err:
            errReturn = {"code": err.code,
                         "explain": err.reason,
                         "body": ""}
            return errReturn

    def _get_response_code(self, code, response_body=""):
        apiReturn = {"code": code,
                     "explain": self._permissions.get(code),
                     "body": response_body}
        self._innerErrCode = 0
        return apiReturn

    def __check_strBlank(self, str_param):
        if not str_param:
            self._innerErrCode = 1900
            return False
        return True

    def __check_strType(self, str_param):
        if not isinstance(str_param, str):  # str type check
            self._innerErrCode = 1901
            return False
        return True

    def __check_intType(self, int_param):
        if not isinstance(int_param, int):  # int type check
            self._innerErrCode = 1901
            return False
        return True

    def _check_name(self, name_param):
        return self.__check_strBlank(name_param)

    def _check_id(self, id_param):
        return self.__check_strBlank(id_param) & self.__check_strType(id_param)

    def _check_int_value(self, int_param):
        return self.__check_intType(int_param)

    def _check_type(self, type_param):
        return self.__check_strBlank(type_param) & self.__check_strType(type_param)

    def _check_enabled(self, bool_param):
        if bool_param is False:
            self._innerErrCode = 1902
            return False
        return True

    def lookup_nickname(self, nickname, limit=1):
        ret = self._check_name(nickname) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        nickname_url = quote(nickname)
        requestUrl = self._apiURL + "players?nickname=" + nickname_url + "&" + self._apiWordType + "&limit=" \
                     + str(limit) + "&" + self.apiKey
        return self._get_apiBody(requestUrl)

    def lookup_playerInfo(self, player_id):
        ret = self._check_id(player_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "players/" + player_id + "?" + self.apiKey
        return self._get_apiBody(requestUrl)

    def lookup_playerMatch(self, player_id, game_type="rating", limit=100, start_date=None, end_date=None):
        ret = self._check_id(player_id) & self._check_type(game_type) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "players/" + player_id + "/matches?gameTypeId=" + game_type
        if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
            startDate = start_date.strftime("%Y%m%dT%M%S")
            endDate = end_date.strftime("%Y%m%dT%M%S")
            requestUrl = requestUrl + "&startDate=" + startDate + "&endDate=" + endDate
        requestUrl = requestUrl + "&limit=" + str(limit) + "&" + self.apiKey
        print(requestUrl)
        return self._get_apiBody(requestUrl)

    def lookup_playerMatch_next(self, player_id):
        ret = self._check_id(player_id) & self._check_enabled(self._matchNextEnable)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "players/" + player_id + "/matches?next=<next>&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_matchInfo(self, match_id):
        ret = self._check_id(match_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "matches/" + match_id + "?" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_playerRatingRanking(self, player_id):
        ret = self._check_id(player_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "ranking/ratingpoint?playerId=" + player_id + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    # offset: start ranking number
    # limit: output number (max : 1000)
    def lookup_totalRatingRanking(self, offset=0, limit=10):
        ret = self._check_int_value(offset) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "ranking/ratingpoint?offset=" + str(offset) + "&limit=" + str(
            limit) + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_playerCharacterRanking(self, player_id, character_id, ranking_type="exp"):
        ret = self._check_id(player_id) & self._check_id(character_id) & self._check_type(ranking_type)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "ranking/characters/" + character_id + "/" + ranking_type + "?playerId=" \
                     + player_id + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_totalCharacterRanking(self, character_id, ranking_type="exp", offset=0, limit=10):
        ret = self._check_id(character_id) & self._check_type(ranking_type) & \
              self._check_int_value(offset) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "ranking/characters/" + character_id + "/" + ranking_type + "?offset=" \
                     + str(offset) + "&limit=" + str(limit) + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def search_itemName(self, item_name, word_type="full", limit=10):
        ret = self._check_name(item_name) & self._check_type(word_type) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        item_name = quote(item_name)
        requestUrl = self._apiURL + "battleitems?itemName=" + item_name + "&wordType=" + word_type \
                     + "&limit=" + str(limit) + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def search_item(self, item_name, word_type="match", limit=10, q_lst=None):
        ret = self._check_name(item_name) & self._check_type(word_type) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        opt_url = ""
        div_value = {
            1: ";",
            2: ",",
            3: ","
        }
        if q_lst is not None:
            number = 0
            opt_url = "&q="
            for opt_value in q_lst:
                opt_url = opt_url + div_value.get(number, "") + self._itemList[number] + ":" + opt_value
                number = number + 1

        item_name = quote(item_name)
        requestUrl = self._apiURL + "battleitems?itemName=" + item_name + "&wordType=" + word_type + "&limit=" \
                     + str(limit) + opt_url + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_itemInfo(self, item_id):
        ret = self._check_id(item_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "battleitems/" + item_id + "?" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_itemMultiInfo(self, item_id_lst=None):
        if item_id_lst is None:
            item_id_lst = []

        item_url = ""
        for item_id in item_id_lst:
            item_url = item_url + item_id
            if item_id is not item_id_lst(len(item_id_lst) - 1):
                item_url = item_url + ","
        requestUrl = self._apiURL + "multi/battleitems/?itemIds=" + item_url + "&" + self._apiKey
        return self._get_apiBody(requestUrl)

    def get_characterInfo(self):
        requestUrl = self._apiURL + "characters?" + self._apiKey
        return self._get_apiBody(requestUrl)

    def lookup_position_attribute(self, attribute_id):
        ret = self._check_id(attribute_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        requestUrl = self._apiURL + "position-attributes/" + attribute_id + "?" + self._apiKey
        return self._get_apiBody(requestUrl)
