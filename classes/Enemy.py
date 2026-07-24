

import random



class Enemy:



    def __init__(self, name, health, damage_min, damage_max, crit_chance, miss_chance, exp):
        self.name = name
        self.health = health
        self.damage_min = damage_min
        self.damage_max = damage_max
        self.crit_chance = crit_chance
        self.miss_chance = miss_chance
        self.exp = exp


    def is_alive(self):
        return self.health > 0

    def get_damage(self):
        """У врага урон случайный в своём диапазоне."""
        return random.randint(self.damage_min, self.damage_max)

    def is_defeated(self):
        pass

    def enemy_stats(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Максимальный урон: {self.damage_min}")
        print(f"Минимальный урон: {self.damage_max}")
        print(f"Крит: {self.crit_chance}")
        print(f"Шанс промаха: {self.miss_chance}")





