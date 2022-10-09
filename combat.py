monster_test = {
    "name": "Goofy Goblin",
    "hp": 10,
    "atk": 2
}
player_test = {
    "name": "Big Hero Man",
    "hp": 100,
    "atk": 1
}


class Fighter():
    def __init__(self, stats):
        self.name = stats.get("name")
        self.atk = stats.get("atk")
        self.hp = stats.get("hp")
    def damage(self, dmg):
        self.hp -= dmg
    def attack(self):
        return self.atk
    def is_alive(self):
        return self.hp > 0
    def get_hp(self):
        return self.hp
    def get_name(self):
        return self.name

def battle(f1: Fighter, f2: Fighter):
    f1_name = f1.get_name()
    f2_name = f2.get_name()
    round = 1
    
    while f1.is_alive() and f2.is_alive():
        
        print(f"\n ===== Round {round} ===== ")

        f1_attack = f1.attack()
        f2.damage(f1_attack)
        print(f"{f1_name} hits {f2_name} for {f1_attack} damage, leaving {f2_name} with {f2.get_hp()} health")
        f2_attack = f2.attack()
        f1.damage(f2_attack)
        print(f"{f2_name} hits {f1_name} for {f2_attack} damage, leaving {f1_name} with {f1.get_hp()} health")
        
        round += 1
    
    if f1.is_alive():
        print(f"{f2_name} is slain. {f1_name} is victorious.")
        return f1
    elif f2.is_alive():
        print(f"{f1_name} is slain. {f2_name} is victorious.")
        return f2
    else:
        print("Both fighters slay each other simultaneously")
        return None

def test_battle():
    monster = Fighter(monster_test)
    player = Fighter(player_test)
    battle(player, monster)
test_battle()