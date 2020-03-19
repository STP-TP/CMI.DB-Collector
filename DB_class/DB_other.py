from DB_class.DB_manager import *
from DB_class.user_param.param_db import *


class GamePositions(DbManager):
    db = position_db
    primary_key = position_name[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.position_path


class GameMaps(DbManager):
    db = map_db
    primary_key = map_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.map_path


class GameItems(DbManager):
    db = item_db
    primary_key = item_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.item_path


class GameAttribute(DbManager):
    db = attribute_db
    primary_key = attribute_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.attribute_path


class GameCharacters(DbManager):
    db = character_db
    primary_key = character_id[sql]

    def overlap_check(self, db_input):
        row = next((index for (index, char) in enumerate(self._db_list)
                    if char[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.character_path
