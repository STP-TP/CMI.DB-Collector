from DB_class.DB_manager import *
import DB_class.user_param.param_db as db_naming


class GamePositions(DbManager):
    db = db_naming.position_db
    primary_key = db_naming.name

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.position_path


class GameMaps(DbManager):
    db = db_naming.map_db
    primary_key = db_naming.map_id

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.map_path


class GameItems(DbManager):
    db = db_naming.item_db
    primary_key = db_naming.item_id

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.item_path


class GameAttribute(DbManager):
    db = db_naming.attribute_db
    primary_key = db_naming.attribute_id

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.attribute_path


class GameCharacters(DbManager):
    db = db_naming.character_db
    primary_key = db_naming.character_id

    def overlap_check(self, db_input):
        row = next((index for (index, char) in enumerate(self._db_list)
                    if char[self.primary_key] == db_input[self.primary_key]), None)
        return row

    def init_path(self, option):
        self._path = path_define.character_path
