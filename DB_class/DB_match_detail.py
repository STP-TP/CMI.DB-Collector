from DB_class.DB_manager import *
from DB_class.user_param.param_db import *


class MatchDetailList(DbManager):
    db = match_detail_db
    primary_key1 = match_id[sql]
    primary_key2 = player_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if ((item[self.primary_key1] == db_input[self.primary_key1])
                        and (item[self.primary_key2] == db_input[self.primary_key2]))), None)
        return row

    def init_path(self, option):
        self._path = path_define.match_detail_path
