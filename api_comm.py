import datetime
import time
import urllib.request as socket
import urllib.error as urlerr
from urllib.parse import quote
from DB_class.user_param.param_private import *


class CommToApiServer:
    _apiKey = apiKey_jss
    _apiURL = "https://api.neople.co.kr/cy/"
    _apiWordType = "wordType=full"
    _innerErrCode = 0
    __api_start_time = []
    _api_error_list = []

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

    def __init__(self, param_api_key=apiKey_jss):
        __apiKey = param_api_key

    @staticmethod
    def _api_communication_count():
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

    def _get_api_body(self, request_url):
        # 횟수 제한 확인
        self._api_communication_count()
        err_return = {}
        for i in range(5):
            try:
                response = socket.urlopen(request_url)
                res_code = response.getcode()
                response_body = response.read().decode('utf-8')
                return self._get_response_code(res_code, response_body)
            except urlerr.HTTPError as err:
                err_return = {"code": err.code,
                              "explain": err.reason,
                              "body": ""}
                print("HTTP Error !!")
                print(err.reason)
                print("(", i+1, "/", 5, ")retry...")
                time.sleep(0.5)
            except urlerr.URLError as err:
                err_return = {"explain": err.reason,
                              "body": ""}
                print("URL Error !!")
                print(err.reason)
                print("(", i+1, "/", 5, ")retry...")
                time.sleep(0.5)
        err_log_dict = err_return.copy()
        err_log_dict["url"] = request_url
        self._api_error_list.append(err_log_dict)
        return err_return

    def get_api_error_list(self):
        return self._api_error_list.copy()

    def del_api_error_list(self):
        self._api_error_list = []

    def _get_response_code(self, code, response_body=""):
        api_return = {"code": code,
                      "explain": self._permissions.get(code),
                      "body": response_body}
        self._innerErrCode = 0
        return api_return

    def __check_str_blank(self, str_param):
        if not str_param:
            self._innerErrCode = 1900
            return False
        return True

    def __check_str_type(self, str_param):
        if not isinstance(str_param, str):  # str type check
            self._innerErrCode = 1901
            return False
        return True

    def __check_int_type(self, int_param):
        if not isinstance(int_param, int):  # int type check
            self._innerErrCode = 1901
            return False
        return True

    def _check_name(self, name_param):
        return self.__check_str_blank(name_param)

    def _check_id(self, id_param):
        return self.__check_str_blank(id_param) & self.__check_str_type(id_param)

    def _check_int_value(self, int_param):
        return self.__check_int_type(int_param)

    def _check_type(self, type_param):
        return self.__check_str_blank(type_param) & self.__check_str_type(type_param)

    def lookup_nickname(self, nickname, limit=1):
        ret = self._check_name(nickname) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        nickname_url = quote(nickname)
        request_url = self._apiURL + "players?nickname=" + nickname_url + "&" + self._apiWordType + "&limit=" \
                      + str(limit) + "&" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_player_info(self, player_id):
        ret = self._check_id(player_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "players/" + player_id + "?" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_player_match(self, player_id, game_type="rating", limit=100, start_date=None, end_date=None):
        ret = self._check_id(player_id) & self._check_type(game_type) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "players/" + player_id + "/matches?gameTypeId=" + game_type
        if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
            startDate = start_date.strftime("%Y%m%dT0000")
            endDate = end_date.strftime("%Y%m%dT0000")
            request_url = request_url + "&startDate=" + startDate + "&endDate=" + endDate
        request_url = request_url + "&limit=" + str(limit) + "&" + self._apiKey
        # print(request_url)
        return self._get_api_body(request_url)

    def lookup_player_match_next(self, player_id, next_code):
        ret = self._check_id(player_id) & self.__check_str_blank(next_code)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "players/" + player_id + "/matches?next=" + next_code + "&" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_match_info(self, match_id):
        ret = self._check_id(match_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "matches/" + match_id + "?" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_player_rating_ranking(self, player_id):
        ret = self._check_id(player_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "ranking/ratingpoint?playerId=" + player_id + "&" + self._apiKey
        return self._get_api_body(request_url)

    # offset: start ranking number
    # limit: output number (max : 1000)
    def lookup_total_rating_ranking(self, offset=0, limit=10):
        ret = self._check_int_value(offset) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "ranking/ratingpoint?offset=" + str(offset) + "&limit=" + str(
            limit) + "&" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_player_character_ranking(self, player_id, character_id, ranking_type="exp"):
        ret = self._check_id(player_id) & self._check_id(character_id) & self._check_type(ranking_type)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "ranking/characters/" + character_id + "/" + ranking_type + "?playerId=" \
                      + player_id + "&" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_total_character_ranking(self, character_id, ranking_type="exp", offset=0, limit=10):
        ret = self._check_id(character_id) & self._check_type(ranking_type) & \
              self._check_int_value(offset) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "ranking/characters/" + character_id + "/" + ranking_type + "?offset=" \
                      + str(offset) + "&limit=" + str(limit) + "&" + self._apiKey
        return self._get_api_body(request_url)

    def search_item_name(self, item_name, word_type="full", limit=10):
        ret = self._check_name(item_name) & self._check_type(word_type) & self._check_int_value(limit)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        item_name = quote(item_name)
        request_url = self._apiURL + "battleitems?itemName=" + item_name + "&wordType=" + word_type \
                      + "&limit=" + str(limit) + "&" + self._apiKey
        return self._get_api_body(request_url)

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
        request_url = self._apiURL + "battleitems?itemName=" + item_name + "&wordType=" + word_type + "&limit=" \
                      + str(limit) + opt_url + "&" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_item_info(self, item_id):
        ret = self._check_id(item_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "battleitems/" + item_id + "?" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_item_multi_info(self, item_id_lst=None):
        if item_id_lst is None:
            item_id_lst = []

        item_url = ""
        for idx, item_id in enumerate(item_id_lst):
            item_url = item_url + item_id
            if idx != len(item_id_lst)-1:
                item_url = item_url + ","
        request_url = self._apiURL + "multi/battleitems/?itemIds=" + item_url + "&" + self._apiKey
        return self._get_api_body(request_url)

    def get_character_info(self):
        request_url = self._apiURL + "characters?" + self._apiKey
        return self._get_api_body(request_url)

    def lookup_position_attribute(self, attribute_id):
        ret = self._check_id(attribute_id)
        if ret is not True:
            return self._get_response_code(self._innerErrCode)

        request_url = self._apiURL + "position-attributes/" + attribute_id + "?" + self._apiKey
        return self._get_api_body(request_url)
