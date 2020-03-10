from DB_class.DB_manager import *


class GamePositions(DbManager):
    db = {
        "name": "",
        "explain": ""
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["name"] == db_input["name"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.position_path


class GameMaps(DbManager):
    db = {
        "mapId": "",
        "name": "",
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["mapId"] == db_input["mapId"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.map_path


class GameItems(DbManager):
    db = {
        "itemId": "",
        "itemName": "",
        "slotCode": "",
        "slotName": "",
        "rarityCode": "",
        "rarityName": "",
        "equipSlotCode": "",
        "equipSlotName": ""
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["itemId"] == db_input["itemId"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.item_path


class GameAttribute(DbManager):
    db = {
        "attributeId": "",
        "attributeName": "",
        "explain": "",
    }

    def overlap_check(self, db_input):
        row = next((index for (index, item) in enumerate(self._db_list)
                    if item["attributeId"] == db_input["attributeId"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.attribute_path


class GameCharacters(DbManager):
    db = {
        "characterId": "",
        "characterName": "",
    }

    def overlap_check(self, db_input):
        row = next((index for (index, char) in enumerate(self._db_list)
                    if char["characterId"] == db_input["characterId"]), None)
        return row

    def init_path(self, option):
        self._path = path_define.character_path
