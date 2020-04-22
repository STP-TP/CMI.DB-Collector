import os
import DB_class.user_param.param_path as path_define
import json


class AutoLogin:
    modify_db_menu = {
        0: ["Go to back menu", ""],
        1: ["Change DB ACCESS", 21],
        2: ["Add DB ACCESS", 22],
        3: ["Delete DB ACCESS", 23]
    }
    modify_key_menu = {
        0: ["Go to back menu", ""],
        1: ["Change API KEY", 31],
        2: ["Add API KEY", 32],
        3: ["Delete API KEY", 33]
    }
    log_in_menu = {
        0: ["Exit", ""],
        1: ["Use existing settings", 11],
        2: ["Modify DB ACCESS", 12],
        3: ["Modify API KEY", 13]
    }
    db_access_list = []
    db_access_dict = {
        "server_ip": "",
        "server_id": "",
        "server_pw": "",
        "server_db": ""
    }
    api_key_list = []
    api_key = ""
    is_db_access = False
    is_api_key = False

    def __init__(self):
        if os.path.isfile(path_define.db_access_path) is True:
            with open(path_define.db_access_path, mode='r', encoding='utf-8') as f:
                self.db_access_list = json.load(f)
            if self.db_access_list[0] is not None:
                self.is_db_access = True
        if os.path.isfile(path_define.api_key_path) is True:
            with open(path_define.api_key_path, mode='r', encoding='utf-8') as f:
                self.api_key_list = json.load(f)
            if self.api_key_list[0] is not None:
                self.is_api_key = True

    def call_log_in_menu(self):
        while True:
            print("")
            for idx, script in self.log_in_menu.items():
                print(idx, ".", script[0])
            print("")
            while True:
                try:
                    user_input = int(input("Select menu : "))
                    if isinstance(user_input, int):
                        if user_input in self.log_in_menu:
                            break
                    print("Select the menu number")
                except ValueError:
                    print("Select the menu number")
            if user_input == 0:
                break
            else:
                func_num = self.log_in_menu[user_input][1]
            if func_num == 11:
                if self.is_db_access and self.is_api_key is True:
                    return self.db_access_list[0], self.api_key_list[0]
                else:
                    if self.is_db_access is False:
                        print("You need enter new DB Access")
                    if self.is_api_key is False:
                        print("You need enter new API Key")
            elif func_num == 12:
                self.call_modify_db_menu()
            elif func_num == 13:
                self.call_modify_key_menu()

    def call_modify_db_menu(self):
        while True:
            print("")
            for idx, script in self.modify_db_menu.items():
                print(idx, ".", script[0])
            print("")
            while True:
                try:
                    user_input = int(input("Select menu : "))
                    if isinstance(user_input, int):
                        if user_input in self.modify_db_menu:
                            break
                    print("Select the menu number")
                except ValueError:
                    print("Select the menu number")
            if user_input == 0:
                break
            else:
                func_num = self.modify_db_menu[user_input][1]
            if func_num == 21:
                if self.is_db_access is False:
                    print("There's no DB access now")
                else:
                    print("")
                    print("0" + " . " + "Go to back menu")
                    for idx, item in enumerate(self.db_access_list):
                        if idx == 0:
                            print(idx + 1, ".", str(item) + " (Current DB access)")
                        else:
                            print(idx + 1, ".", str(item))
                    print("")
                    while True:
                        try:
                            user_input = int(input("Select number to use : "))
                            if isinstance(user_input, int):
                                if user_input in range(len(self.db_access_list) + 1):
                                    break
                                print("Select right number")
                        except ValueError:
                            print("Select right number")
                    if user_input == 0:
                        break
                    else:
                        temp_dict = self.db_access_list[user_input - 1]
                        del self.db_access_list[user_input - 1]
                        self.db_access_list.insert(0, temp_dict)
                        with open(path_define.db_access_path, mode='w', encoding='utf-8') as f:
                            json.dump(self.db_access_list, f, indent=2)
            elif func_num == 22:
                while True:
                    print("")
                    print("press 0 to go to back menu")
                    user_input = str(input("enter server ip : "))
                    if user_input == '0':
                        break
                    else:
                        self.db_access_dict["server_ip"] = user_input
                    user_input = str(input("enter server id : "))
                    if user_input == '0':
                        break
                    else:
                        self.db_access_dict["server_id"] = user_input
                    user_input = str(input("enter server pw : "))
                    if user_input == '0':
                        break
                    else:
                        self.db_access_dict["server_pw"] = user_input
                    user_input = str(input("enter server db name : "))
                    if user_input == '0':
                        break
                    else:
                        self.db_access_dict["server_db"] = user_input
                    self.db_access_list.append(self.db_access_dict)
                    with open(path_define.db_access_path, mode='w', encoding='utf-8') as f:
                        json.dump(self.db_access_list, f, indent=2)
                    if self.is_db_access is False:
                        self.is_db_access = True
                    break
            elif func_num == 23:
                if self.is_db_access is False:
                    print("There's no DB access now")
                else:
                    print("")
                    print("0" + " . " + "Go to back menu")
                    for idx, item in enumerate(self.db_access_list):
                        if idx == 0:
                            print(idx + 1, ".", str(item) + " (Current key)")
                        else:
                            print(idx + 1, ".", str(item))
                    print("")
                    while True:
                        try:
                            user_input = int(input("Select number to delete : "))
                            if isinstance(user_input, int):
                                if user_input in range(len(self.db_access_list) + 1):
                                    break
                                print("Select right number")
                        except ValueError:
                            print("Select right number")
                    if user_input == 0:
                        break
                    else:
                        del self.db_access_list[user_input - 1]
                        with open(path_define.db_access_path, mode='w', encoding='utf-8') as f:
                            json.dump(self.db_access_list, f, indent=2)
                        if self.db_access_list[0] is None:
                            self.is_db_access = False

    def call_modify_key_menu(self):
        while True:
            print("")
            for idx, script in self.modify_key_menu.items():
                print(idx, ".", script[0])
            print("")
            while True:
                try:
                    user_input = int(input("Select menu : "))
                    if isinstance(user_input, int):
                        if user_input in self.modify_key_menu:
                            break
                    print("Select the menu number")
                except ValueError:
                    print("Select the menu number")
            if user_input == 0:
                break
            else:
                func_num = self.modify_key_menu[user_input][1]
            if func_num == 31:
                if self.is_api_key is False:
                    print("There's no API key now")
                else:
                    print("")
                    print("0" + " . " + "Go to back menu")
                    for idx, item in enumerate(self.api_key_list):
                        if idx == 0:
                            print(idx + 1, ".", item + " (Current key)")
                        else:
                            print(idx + 1, ".", item)
                    print("")
                    while True:
                        try:
                            user_input = int(input("Select number to use : "))
                            if isinstance(user_input, int):
                                if user_input in range(len(self.api_key_list) + 1):
                                    break
                                print("Select right number")
                        except ValueError:
                            print("Select right number")
                    if user_input == 0:
                        break
                    else:
                        temp_str = self.api_key_list[user_input - 1]
                        del self.api_key_list[user_input - 1]
                        self.api_key_list.insert(0, temp_str)
                        with open(path_define.api_key_path, mode='w', encoding='utf-8') as f:
                            json.dump(self.api_key_list, f, indent=2)
            elif func_num == 32:
                while True:
                    print("")
                    print("press 0 to go to back menu")
                    user_input = str(input("enter api key : "))
                    if user_input == '0':
                        break
                    else:
                        self.api_key = user_input
                    self.api_key_list.append(self.api_key)
                    with open(path_define.api_key_path, mode='w', encoding='utf-8') as f:
                        json.dump(self.api_key_list, f, indent=2)
                    if self.is_api_key is False:
                        self.is_api_key = True
                    break
            elif func_num == 33:
                if self.is_api_key is False:
                    print("There's no API key now")
                else:
                    print("")
                    print("0" + " . " + "Go to back menu")
                    for idx, item in enumerate(self.api_key_list):
                        if idx == 0:
                            print(idx + 1, ".", item + " (Current key)")
                        else:
                            print(idx + 1, ".", item)
                    print("")
                    while True:
                        try:
                            user_input = int(input("Select number to delete : "))
                            if isinstance(user_input, int):
                                if user_input in range(len(self.api_key_list) + 1):
                                    break
                                print("Select right number")
                        except ValueError:
                            print("Select right number")
                    if user_input == 0:
                        break
                    else:
                        del self.api_key_list[user_input - 1]
                        with open(path_define.api_key_path, mode='w', encoding='utf-8') as f:
                            json.dump(self.api_key_list, f, indent=2)
                        if self.api_key_list[0] is None:
                            self.is_api_key = False
