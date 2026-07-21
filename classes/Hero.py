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
    

    def stats(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Урон: {self.damage}")
        print(f"Крит: {self.crit_chance}")
        print(f"Шанс промаха: {self.miss_chance}")