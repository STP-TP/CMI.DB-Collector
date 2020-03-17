import abc
import pickle
import DB_class.user_param.param_path as path_define
import DB_class.user_param.param_db as db_naming


class DbManager(metaclass=abc.ABCMeta):
    __db_init = False
    _db_list: list
    _path: str
    _db: dict

    def __init__(self, option=db_naming.rating):
        self.init_path(option)
        if self.__db_init is False:
            self.load_db()
            self.__db_init = True

    @abc.abstractmethod
    def overlap_check(self, db_input):  # if overlap db return row num, or None
        pass

    @abc.abstractmethod
    def init_path(self, option):  # db table setting
        pass

    def update_new_db_list(self, db_list: list):
        for db in db_list:
            self.update_new_db(db)

    def update_new_db(self, db_input):
        # DB와 id 존재 유무 체크
        res = self.overlap_check(db_input)

        if res is None:
            self.add_db(db_input)
        else:
            self.update_db(res, db_input)
        return res

    def add_db(self, db_input):
        self._db_list.append(db_input)

    def update_db(self, row, db_input):
        self._db_list[row] = db_input

    def save_db(self):
        with open(self._path, 'wb') as file_out:
            pickle.dump(self._db_list, file_out)

    def load_db(self):
        try:
            with open(self._path, 'rb') as file_in:
                self._db_list = pickle.load(file_in)
        except FileNotFoundError:
            self._db_list = []

    def get_db(self):
        return self._db_list
