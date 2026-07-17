def show_main_menu():
    print("1-новая игра")
    print("2-загрузить игру")
    print("3-настройки")
    print("4-выход")

def menu_choose():
    
    choice = (input("Выберите пункт меню: "))

    if choice.isdigit():
        choice = int(choice)
    else:
        print("Неверный пункт меню ввидите число")
        return menu_choose()
    
    if choice > 0 and choice <5:
        print(f"выбрали пункт меню: {choice}")
    else:
        print("Неверный пункт меню ввидите число от 1 до 4")
        return menu_choose()
    return choice
