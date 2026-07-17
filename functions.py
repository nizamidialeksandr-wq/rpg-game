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
    
def pocess_menu_choice(choice):
    if choice == 1:
        print("Начали новую игру")
    elif choice == 2:
        print("Загрузили игру")
    elif choice == 3:
        print("Настройки")
    elif choice == 4:
        print("Выход")
    else:
        print("Неверный пункт меню")
        return pocess_menu_choice(choice)

