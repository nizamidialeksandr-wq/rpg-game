"""
Простой пример: сохранение и загрузка объекта класса.
Запуск: python3 save_class_example.py
"""

import json
from pathlib import Path

FILE = Path("example_hero.json")


class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def __str__(self):
        return f"{self.name}: HP={self.health}, урон={self.damage}"

    def to_dict(self):
        """Объект → словарь (чтобы можно было записать в JSON)."""
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
        }

    @classmethod
    def from_dict(cls, data):
        """Словарь → новый объект класса."""
        return cls(data["name"], data["health"], data["damage"])


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


# --- демо ---
hero = Hero("Маг", 80, 45)
print("1) Объект в памяти:")
print(hero)

print("\n2) Пишем на диск:")
save(hero)

print("\n3) Читаем с диска в новый объект:")
loaded = load()
print(loaded)
print("Это снова класс Hero?", type(loaded))