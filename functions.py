import random
def choice_attack(): 
    while True:
        
        print("1 — Удар")
        print("2 — Лечение (+30 хп)")
        choice = input("Выбери действие: ") 

        if choice != "1" and choice != "2":
            print("Выбери верное действие! Повторите выбор")
            continue    
        
        return choice




def show_main_menu():
    print("1-новая игра")
    print("2-загрузить игру")
    print("3-настройки")
    print("4-выход")

def menu_choose():
    choice = input("Выберите пункт меню: ")


    if choice.isdigit():
        choice = int(choice)
    else:
        print("Неверный пункт меню, введите число")
        return menu_choose() 


    if choice > 0 and choice < 5:
        print(f"выбрали пункт меню: {choice}")
    else:
        print("Неверный пункт меню, введите число от 1 до 4")
        return menu_choose()
    return choice

def chance(percent):
    chance_random = random.randint(0,100)  
    chance = 100 - percent
       
    return chance_random > chance

def player_turn(choice,hero,enemy):
    if choice == "1":

        is_miss = chance(enemy.miss_chance)

        if is_miss:
            print ("вы не попали по противнику") 
            return
        is_crit = chance(hero.crit_chance)
        if is_crit:
            krit_coef = random_crit()
        else:
            krit_coef = 1

        if krit_coef > 1:
            print ("случился критический удар")

        damage = (hero.damage) * krit_coef
        enemy.health -= damage
        print(f"{hero.name} нанёс {damage} урона по противнику!")

    elif choice == "2":
        heal = 30
        hero.health += heal
        print(f"Ты вылечился на {heal} хп. Теперь у тебя {hero.health} хп.")
    
def random_crit():
    return round(random.uniform(1.5, 2), 1)

def  enemy_turn(hero,enemy):
    print(f"\nХод {enemy.name}!")
    is_miss = chance(hero.miss_chance)
    
    if is_miss:
        print ("Противник не попал по вам") 
        return
        
    is_crit = chance(enemy.crit_chance)
    if is_crit:
        krit_coef = random_crit()
    else:
        krit_coef = 1

    if krit_coef > 1:
        print ("случился критический удар")

    damage = random.randint(enemy.damage_min, enemy.damage_max)
    
    print(f"{enemy.name} нанёс {damage * krit_coef} урона тебе!")
    hero.health -= damage * krit_coef 


