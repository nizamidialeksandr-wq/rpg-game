from functions import *
from classes.Game import Game

def main():
    show_main_menu()
    choice = menu_choose()

    if choice == 1:
        print("Начали новую игру")
        game = Game()
        game.new_game()

    elif choice == 2:
        game = Game.load_game()
        if game is None:
            return main()          # сохранёнки нет — обратно в меню
        game.continue_game()

    elif choice == 3:
        print("Настройки")

    elif choice == 4:
        print("Выход")

main()