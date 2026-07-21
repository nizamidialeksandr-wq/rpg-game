"""
Простой пример: сохранение и загрузка объекта класса.
Запуск: python3 save_class_example.py
"""

import json
from pathlib import Path

FILE = Path("example_hero.json")
FILE_GAME = Path("example_game.json")


from classes.Hero import Hero


class Game:


    def __init__(self, name):
        self.hero = None
        self.name = name

    def new_game(self):
        
        self.hero = Hero("Ассасин",90,45,Weapon("мушкет",20))
        print(f"Вы выбрали персонажа: {self.hero.name}")
        


    def save_game(self):
        with open(FILE_GAME, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        print(f"Сохранено в {FILE_GAME}")       
    
    
    @classmethod
    def load_game(self):
        if not FILE_GAME.exists():
            print("Файла ещё нет")
            return None

        with open(FILE_GAME, encoding="utf-8") as f:
            data = json.load(f)
        print(f"Прочитано из {FILE_GAME}")
        return Game.from_dict(data)

    def to_dict(self):
        """Объект → словарь (чтобы можно было записать в JSON)."""
        return {
            "hero" : self.hero.to_dict(),
            "name" : self.name
        }

    @classmethod
    def from_dict(cls, data):
        """Словарь → новый объект класса."""
        game = cls(data["name"])
        game.hero = Hero.from_dict(data["hero"])
        return game 





class Weapon:
    def __init__(self, name,damage):
        self.name = name
        self.damage = damage


    def to_dict(self):
        """Объект → словарь (чтобы можно было записать в JSON)."""
        return {
            "damage" : self.damage,
            "name" : self.name
        }


    @classmethod
    def from_dict(cls, data):
        """Словарь → новый объект класса."""
        return cls(data["name"],data["damage"])




class Hero:
    def __init__(self, name, health, damage, weapon):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon

    def __str__(self):
        return f"{self.name}: HP={self.health}, урон={self.damage}"

    def to_dict(self):
        """Объект → словарь (чтобы можно было записать в JSON)."""
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
            "weapon": self.weapon.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        """Словарь → новый объект класса."""
        Weapon.from_dict(data["weapon"])
        return cls(data["name"], data["health"], data["damage"], Weapon.from_dict(data["weapon"]))


def save(hero):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(hero.to_dict(), f, ensure_ascii=False, indent=2)
    print(f"Сохранено в {FILE}")


def load():
    if not FILE.exists():
        print("Файла ещё нет")
        return None

    with open(FILE, encoding="utf-8") as f:
        data = json.load(f)
    print(f"Прочитано из {FILE}")
    return Hero.from_dict(data)


# # --- демо ---
# hero = Hero("Маг", 80, 45,Weapon("мушкет",20))
# print("1) Объект в памяти:")
# print(hero)

# print("\n2) Пишем на диск:")
# save(hero)

# print("\n3) Читаем с диска в новый объект:")
# loaded = load()
# print(loaded)
# print("Это снова класс Hero?", type(loaded))





# # --- демо сохранение класса героя в файл ---
# hero = Hero("Маг", 80, 45)
# print("1) Объект в памяти:")
# print(hero)

# print("\n2) Пишем на диск:")
# save(hero)

# print("\n3) Читаем с диска в новый объект:")
# loaded = load()
# print(loaded)




# --- демо сохранение класса игры в файл ---
game = Game("Rpg_game")
game.new_game()
game.save_game()

game2 = Game.load_game()
print(game2.name)
print(game2.hero.name)
print(game2.hero.weapon.name)