import datetime
import urllib.request as socket
import urllib.error as urlerr
from urllib.parse import quote


class CommToApiServer:
    apiKey = "apikey=0rYk7DYbNFelyQguZRmwhWxF1QhZ0yJP"
    apiURL = "https://api.neople.co.kr/cy/"
    apiWordType = "wordType=full"
    matchNextEnable = False

    permissions = {
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
                     "explain": self.permissions.get(code),
                     "body": response_body}
        return apiReturn

    def search_nickname(self, nickname, limit=1):
        if not nickname:
            return self._get_response_code(1900)
        if not isinstance(limit, int):
            return self._get_response_code(1901)

        nickname_url = quote(nickname)
        requestUrl = self.apiURL + "players?nickname=" + nickname_url + "&" + self.apiWordType + "&limit=" \
                     + str(limit) + "&" + self.apiKey
        return self._get_apiBody(requestUrl)

    def search_playerInform(self, player_id):
        if not player_id:
            return self._get_response_code(1900)
        if not isinstance(player_id, str):
            return self._get_response_code(1901)

        requestUrl = self.apiURL + "players/" + player_id + "?" + self.apiKey
        return self._get_apiBody(requestUrl)

    def search_playerMatch(self, player_id, game_type="rating", start_date=None, end_date="", limit=100):
        if not player_id:
            return self._get_response_code(1900)
        if not isinstance(player_id, str):
            return self._get_response_code(1901)

        requestUrl = self.apiURL + "players/" + player_id + "/matches?gameTypeId=" + game_type
        if isinstance(start_date, datetime.date) and isinstance(end_date, datetime.date):
            startDate = start_date.strftime("%Y%m%dT%M%S")
            endDate = end_date.strftime("%Y%m%dT%M%s")
            requestUrl = requestUrl + "&startDate=" + startDate + "&endDate=" + endDate
        requestUrl = requestUrl + "&limit=" + str(limit) + "&" + self.apiKey
        return self._get_apiBody(requestUrl)

    def search_playerMatch_next(self, player_id):
        if not player_id:
            return self._get_response_code(1900)
        if not isinstance(player_id, str):
            return self._get_response_code(1901)
        if not self.matchNextEnable:
            return self._get_response_code(1902)

        requestUrl = self.apiURL + "players/" + player_id + "/matches?next=<next>&" + self.apiKey
        return self._get_apiBody(requestUrl)

    def search_matchInform(self, match_id):
        if not match_id:
            return self._get_response_code(1900)
        if not isinstance(match_id, str):
            return self._get_response_code(1901)

        requestUrl = self.apiURL + "matches/" + match_id + "?" + self.apiKey
        return self._get_apiBody(requestUrl)
