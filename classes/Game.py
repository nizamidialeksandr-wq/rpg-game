
import json
from pathlib import Path

from classes.Hero import Hero
from classes.Enemy import Enemy
from functions import *

SAVE_FILE = Path("savegame.json")




class Game:
    HEROES = [
        Hero("Воин", 150, 20, 10, 10),
        Hero("Маг", 80, 45, 5, 5),
        Hero("Эльф", 100, 20, 25, 15),
        Hero("Ассасин", 90, 45, 35, 40)
    ]

    ENEMIES = [
        Enemy("Крыса-переросток", 60, 5, 12, 3, 15, 50),
        Enemy("Гоблин-неудачник", 80, 8, 18, 5, 20, 70),
        Enemy("Болотный слизень", 120, 10, 20, 5, 10, 100),
        Enemy("Лесной волк", 140, 15, 28, 12, 8, 130),
        Enemy("Орк-разведчик", 180, 18, 32, 15, 10, 180),
        Enemy("Теневой лучник", 150, 22, 40, 20, 25, 200),
        Enemy("Вампир-отступник", 200, 25, 45, 25, 10, 250),
        Enemy("Паладин падший", 280, 20, 38, 10, 5, 280),
        Enemy("Древний лич", 350, 30, 55, 15, 15, 350),
        Enemy("Дракон-разрушитель", 500, 35, 60, 20, 5, 500)
    ]    


    def __init__(self):
        self.hero = None
        self.army = None
        self.shop = None
        self.is_running = True
        self.level = 0

    def new_game(self):
        player_id = self.choose_player()
        template = Game.HEROES[player_id]
        self.hero = Hero(
            template.name,
            template.health,
            template.damage,
            template.crit_chance,
            template.miss_chance,
        )
        print(f"Вы выбрали персонажа: {self.hero.name}")

        self.level = 0
        self.hero.stats()
        self.run()

    def choose_player(self):
        print("выберите персонажа")
        for i, hero in enumerate(Game.HEROES):
            print(f"{i} —  {hero.name}")

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

    def run(self):
        """Бьёмся с противниками по очереди, пока есть кому и с кем."""
        while self.level < len(Game.ENEMIES):
            won = self.battle()

            if not won:
                print("\nИГРА ОКОНЧЕНА. Ты погиб.")
                return

            self.level = self.level + 1
            self.hero.stats()
            self.ask_save()         
            


        if self.level >= len(Game.ENEMIES):
            print("\nПОБЕДА! Все противники повержены.")




    def battle(self):
        """Один бой. Возвращает True, если герой победил."""
        template_enemy = Game.ENEMIES[self.level]
     
        enemy = Enemy(
            template_enemy.name,
            template_enemy.health,
            template_enemy.damage_min,
            template_enemy.damage_max,
            template_enemy.crit_chance,
            template_enemy.miss_chance,
            template_enemy.exp
        )


        print(f"\n=== БОЙ {self.level + 1}: {self.hero.name} против {enemy.name} ===")        
        while self.hero.is_alive() and enemy.is_alive():
            choice = choice_attack()
            player_turn(choice,self.hero,enemy)
            if not enemy.is_alive():
                break
            enemy_turn(self.hero,enemy)
            print(f"HP: {self.hero.name} {self.hero.health} | {enemy.name} {enemy.health}")

        if self.hero.is_alive():
            print(f"{enemy.name} повержен!")
            return True
        return False



    def ask_save(self):
        """Микроменю после победы."""
        while True:
            print("\n1 - сохранить прогресс")
            print("2 - не сохранять")
            choice = input("Выбор: ")

            if choice == "1":
                self.save_game()
                return
            elif choice == "2":
                return
            else:
                print("Неверный ввод, повторите")

    def to_dict(self):
        return {
            "hero": self.hero.to_dict(),
            "level": self.level,
        }

    @classmethod
    def from_dict(cls, data):
        game = cls()
        game.hero = Hero.from_dict(data["hero"])
        game.level = data["level"]
        return game

    def save_game(self):
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"Игра сохранена в {SAVE_FILE}")

    # ---------- загрузка ----------

    @classmethod
    def load_game(cls):
        """Читает файл и возвращает игру. Если файла нет — None."""
        if not SAVE_FILE.exists():
            print("Сохранений нет")
            return None

        with open(SAVE_FILE, encoding="utf-8") as f:
            data = json.load(f)

        return cls.from_dict(data)

    def continue_game(self):
        """После загрузки: показать статистику и сразу в бой."""
        print("Игра загружена. Текущее состояние:")
        self.hero.stats()
        print(f"Следующий противник: {Game.ENEMIES[self.level].name}")
        self.run()