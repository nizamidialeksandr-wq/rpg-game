
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
        self.choose_player()
        self.hero = Game.HEROES[playerID]


    def main_menu(self):
        pass

    def battle(self):
        pass

    def save_game(self):
        pass

    def load_game(self):
        pass

def choose_player(HEROES):
    print("выберите персонажа")
    for i, hero in enumerate(HEROES):
        print(f"{i} —  {hero.name}") 

    choice = -1
    while True:   
        choice = input("Выбери действие: ")
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Выбери верное действие! Повторите выбор")
            continue

        if choice >= 0 and choice < len(HEROES):
            break
        else:
            print("Выбери верное действие! Повторите выбор")
            continue

    return choice


