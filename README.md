# CyphersMatchInformation
1. Neople 사이퍼즈 API를 이용하여 데이터베이스를 구축
2. 데이터베이스를 사용하여 간단한 통계분석부터 통계 알고리즘을 이용한 데이터 분석까지 다양한 아웃풋 도출

## Project Information
1. 설치 모듈
    * ```pip install -r requirements.txt```
    
2. 추가 필요 정보
    1. api key ( CMI.DB-Collector/DB_class/user_param/api_key.json)  
        > api_key list 형태로 여러개로 존재할 수 있습니다.    
            [Neople Open API](https://developers.neople.co.kr/contents/apiDocs/cyphers)
            에서 api key를 발급받을 수 있습니다.  
            ```python
           [apikey=CYPHERS_API_KEY1, apikey=CYPHERS_API_KEY2, ...]
           ```
    2. database access info ( CMI.DB-Collector/DB_class/user_param/db_access.json)
        > Database 연결을 위한 infomation을 저장합니다.  
            list 내의 dict형태로 작성합니다.  
            ```python
            [{
                "server_ip": ""     
                "server_id": ""
                "server_pw": ""
                "server_db": ""
            }]       
            ```
