

from classes.Hero import Hero


class Game:
    HEROES = [
        Hero("Воин",150,20,10,10),
        Hero("Маг",80,45,5,5),
        Hero("Эльф",100,20,25,15),
        Hero("Ассасин",90,45,35,40)
    ]

    def __init__(self):
        self.hero = None
        self.enemies = []
        self.army = None
        self.shop = None
        self.is_running = True

    def new_game(self):
        player_id = self.choose_player()
        self.hero = Game.HEROES[player_id]
        print(f"Вы выбрали персонажа: {self.hero.name}")


    def choose_player(self):
        print("выберите персонажа")
        for i, hero in enumerate(Game.HEROES):
            print(f"{i} —  {hero.name}")

        while True:
            choice = input("Выбери персонажа: ")
            if not choice.isdigit():
                print("Выбери верное действие! Повторите выбор")
                continue

            choice = int(choice)

            if 0 <= choice < len(Game.HEROES):
                return choice
            else:
                print("Выбери верное действие! Повторите выбор")


    def main_menu(self):
        pass

    def battle(self):
        pass

    def save_game(self):
        pass

    def load_game(self):
        pass

