


from classes.Weapon import Weapon

class Hero:
    def __init__(self, name, health, damage, crit_chance, miss_chance):
        self.name = name
        self.health = health
        self.damage = damage
        self.crit_chance = crit_chance
        self.miss_chance = miss_chance

        self.exp = 0
        self.level = 0
        self.weapon = None
        self.gold = 0
    
    def is_alive(self):
        return self.health > 0



    def stats(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Урон: {self.damage}")
        print(f"Крит: {self.crit_chance}")
        print(f"Шанс промаха: {self.miss_chance}")
        print(f"Кол-во золота: {self.gold}")


    def get_damage(self):
        """Урон героя + бонус от оружия, если оно есть."""
        damage = self.damage
        if self.weapon:
            damage = damage + self.weapon.damage
        return damage

    def to_dict(self):
        """Объект → словарь. Вложенный класс пакуем его же to_dict."""
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage,
            "crit_chance": self.crit_chance,
            "miss_chance": self.miss_chance,
            "exp": self.exp,
            "level": self.level,
            # если оружия нет — кладём None, иначе упадёт на None.to_dict()
            "weapon": self.weapon.to_dict() if self.weapon else None,
            "gold": self.gold
        }

    @classmethod
    def from_dict(cls, data):
        """Словарь → новый объект."""
        hero = cls(
            data["name"],
            data["health"],
            data["damage"],
            data["crit_chance"],
            data["miss_chance"],
        )
        hero.gold = data["gold"]
        hero.exp = data["exp"]
        hero.level = data["level"]
        # вложенный класс восстанавливаем его же from_dict
        if data["weapon"]:
            hero.weapon = Weapon.from_dict(data["weapon"])
        return hero


