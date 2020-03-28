from api_controller import *


trigger_menu = {
    0: ["Go to back menu", ""],
    1: ["Start rating based stacking",  11],
    2: ["Start normal based stacking", 12],
    3: ["Start nickname based", 13],
    4: ["Start assist database stacking", 14]
}
continue_menu = {
    0: ["Go to back menu", ""],
    1: ["Start past database stacking", 21],
    2: ["Start newest database stacking", 22]
}
main_menu = {
    0: ["Exit", ""],
    1: ["Trigger function", trigger_menu],
    2: ["Continue function", continue_menu],
}
api_ctrl = CollectDbFlow()


def select_menu(menu: dict):
    if menu is None:
        return None
    while True:
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
            elif func_num is 21:
                # collect pass database
                pass
            elif func_num is 22:
                # collect newest database
                pass
            print(api_ctrl.get_api_com_error_list(True))


select_menu(main_menu)
