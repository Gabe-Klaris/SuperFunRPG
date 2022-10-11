import random

class Attack():
    def __init__(self, name = "an attack", base = 1, ignores_dfn = False):
        self.name = name
        self.base = base
        self.ignores_dfn = ignores_dfn
    def execute(self, str):
        return {"name": self.name, "quantity": self.base*str, "ignores_dfn": self.ignores_dfn}


class Fighter():
    def __init__(self, stats, attacks = None):
        self.name = stats.get("name")
        self.str = stats.get("str")
        self.hp = stats.get("hp")
        self.dfn = stats.get("dfn")
        if attacks:
            self.attacks = attacks
        else:
            self.attacks = stats.get("attacks")

    def damage(self, damage):
        taken = damage.get("quantity")
        if not damage.get("ignores_dfn"):
            taken *= 1/(2**(self.dfn/100))
        self.hp -= taken

    def attack(self):
        this_attack = random.choice(self.attacks)
        attack_out = this_attack.execute(self.str)
        return attack_out

    def is_alive(self):
        return self.hp > 0
    def get_hp(self):
        return self.hp
    def get_name(self):
        return self.name


slash = Attack("slash", base = 5)
stab = Attack("stab", base = 2, ignores_dfn = True)
bash = Attack("bash", base = 10)
slam = Attack("slam", 5, True)
monster_test = {
    "name": "Goofy Goblin",
    "hp": 10,
    "str": 2,
    "dfn": 0,
    "attacks": [stab, slash]
}
player_test = {
    "name": "Big Hero Man",
    "hp": 100,
    "str": 1,
    "dfn": 50
}

def battle(f1: Fighter, f2: Fighter):
    f1_name = f1.get_name()
    f2_name = f2.get_name()
    round = 1

    while f1.is_alive() and f2.is_alive():
        
        print(f"\n ===== Round {round} ===== ")

        f1_attack = f1.attack()
        f2.damage(f1_attack)
        print(f"{f1_name} uses {f1_attack['name']} on {f2_name} for {f1_attack['quantity']} damage, leaving {f2_name} with {f2.get_hp():0.1f} health")
        f2_attack = f2.attack()
        f1.damage(f2_attack)
        print(f"{f2_name} uses {f2_attack['name']} on {f1_name} for {f2_attack['quantity']} damage, leaving {f1_name} with {f1.get_hp():0.1f} health")
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
    player = Fighter(player_test, attacks = [bash, slam])
    battle(player, monster)
test_battle()