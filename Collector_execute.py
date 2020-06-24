from api_controller import *
from auto_login import *
import threading

trigger_menu = {
    0: ["Go to back menu", ""],
    1: ["Start rating based stacking",  11],
    2: ["Start normal based stacking", 12],
    3: ["Start nickname based", 13],
    4: ["Start assist database stacking", 14]
}
continue_menu = {
    0: ["Go to back menu", ""],
    1: ["Past database stacking", 21],
    2: ["Newest database stacking", 22],
    3: ["Auto database stacking", 23]
}
main_menu = {
    0: ["Exit", ""],
    1: ["Trigger function", trigger_menu],
    2: ["Continue function", continue_menu],
}


def continuous_recent_collector():
    time_delta = datetime.timedelta(minutes=10)
    for tier in tier_list:
        api_ctrl.continuous_collecting(tier, "recent", time_delta)


def continuous_past_collector():
    time_delta = datetime.timedelta(minutes=10)
    for tier in tier_list:
        api_ctrl.continuous_collecting(tier, "past", time_delta)


def select_menu(menu: dict):
    if menu is None:
        return None
    while True:
        print("")
        for idx, script in menu.items():
            print(idx, ".", script[0])
        user_input: int
        while True:
            try:
                user_input = int(input("Enter menu number: "))
                if isinstance(user_input, int):
                    if user_input in menu:
                        break
                print("Wrong number")
            except ValueError:
                pass

        if user_input == 0:
            break
        if isinstance(menu[user_input][1], dict):
            select_menu(menu[user_input][1])
        else:
            api_ctrl.set_collect_mode(True)
            func_num = menu[user_input][1]
            if func_num is 11:
                api_ctrl.trigger_rating_based(0, 10, 1)
            elif func_num is 12:
                api_ctrl.trigger_normal_based(0, 5, 20)
            elif func_num is 13:
                # trigger nickname
                pass
            elif func_num is 14:
                # assist database
                api_ctrl.collect_character_db(True)
                api_ctrl.collect_items(True)
                api_ctrl.collect_attributes(True)
                pass
            elif func_num is 21:    # collect past database
                continuous_past_collector()
            elif func_num is 22:    # collect newest database
                continuous_recent_collector()
            elif func_num is 23:
                pass
            print(api_ctrl.get_api_com_error_list(True))
            api_ctrl.set_collect_mode(False)



private_info = AutoLogin()
private_info.call_log_in_menu()
api_ctrl = CollectDbFlow(private_info.db_access_list[0]["server_ip"],
                         private_info.db_access_list[0]["server_id"],
                         private_info.db_access_list[0]["server_pw"],
                         private_info.db_access_list[0]["server_db"],
                         private_info.api_key_list)
api_ctrl.set_collect_mode(True)
select_menu(main_menu)
