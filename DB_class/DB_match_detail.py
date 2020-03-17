from DB_class.DB_manager import *
import DB_class.user_param.param_db as db_naming


class MatchDetailList(DbManager):
    db = db_naming.match_detail_db
    primary_key = db_naming.match_id

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if (item[self.primary_key] == db_input[self.primary_key])), None)
        return row

    def init_path(self, option):
        self._path = path_define.match_detail_path
