from DB_class.DB_manager import *
from DB_class.user_param.param_db import *


class User(DbManager):
    db = user_db
    primary_key = player_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.user_path
