from api_controller import *


trigger_menu = {
    0: ["Go to back menu", ""],
    1: ["Start rating based",  1],
    2: ["Start normal based", 2]
    # 3: ["Start nickname based", 3]
}
continue_menu = {
    0: ["Go to back menu", ""],
    1: ["Start past database", 4],
    2: ["Start newest database", 5]
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
        while True:
            user_input = int(input("Enter menu number: "))
            if isinstance(user_input, int):
                if user_input in menu:
                    break
            print("Wrong number")

        if user_input == 0:
            break
        if isinstance(menu[user_input][1], dict):
            select_menu(menu[user_input][1])
        else:
            func_num = menu[user_input][1]
            if func_num is 1:
                api_ctrl.trigger_rating_based(0, 10, 1)
            elif func_num is 2:
                api_ctrl.trigger_normal_based(0, 5, 1)
            elif func_num is 3:
                # trigger nickname
                pass
            elif func_num is 4:
                # collect pass database
                pass
            elif func_num is 5:
                # collect newest database
                pass
        break


select_menu(main_menu)
