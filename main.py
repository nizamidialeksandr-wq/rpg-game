from functions import *
from classes.Hero import Hero
from classes.Game import Game











def main():

    show_main_menu()
    menu_choose()
    choice = menu_choose()





    if choice == 1:
        print("Начали новую игру")
        game = Game() 
        game.new_game()
    elif choice == 2:
        print("Загрузили игру")
    elif choice == 3:
        print("Настройки")
    elif choice == 4:
        print("Выход")




main()






