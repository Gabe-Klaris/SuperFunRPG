import random
import os

class Attack():
    def __init__(self, name = "an attack", base = 1, time = 1, ignores_dfn = False):
        self.name = name
        self.base = base
        self.time = time
        self.ignores_dfn = ignores_dfn
    def get_name(self):
        return self.name
    def get_time(self):
        return self.time
    def execute(self, str):
        return {"name": self.name, "quantity": self.base*str, "ignores_dfn": self.ignores_dfn}


class Fighter():
    def __init__(self, stats, attacks = None):
        self.name = stats.get("name")
        self.str = stats.get("str")
        self.hp = stats.get("hp")
        self.dfn = stats.get("dfn")
        self.spd = stats.get("spd")
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
        self.time -= this_attack.get_time()
        return attack_out


    def is_alive(self):
        return self.hp > 0
    def get_hp(self):
        return self.hp
    def get_name(self):
        return self.name
    def reset_turn(self):
        self.time = self.spd
    def is_turn(self):
        return self.time > 0

class Player(Fighter):
    def attack(self):
        print(f"Select an attack ({self.time} time remaining)")
        for num, attack in enumerate(self.attacks):
            print(f"{num+1}: {attack.get_name()} ({attack.get_time()} time)")
        attack_num = int(input())
        this_attack = self.attacks[attack_num-1]
        attack_out = this_attack.execute(self.str)
        self.time -= this_attack.get_time()
        return attack_out

slash = Attack("slash", base = 5, time = 3)
stab = Attack("stab", base = 1, ignores_dfn = True, time = 1)
bash = Attack("bash", base = 10, time = 4)
slam = Attack("slam", base = 5, ignores_dfn = True, time = 2)
monster_test = {
    "name": "Goofy Goblin",
    "hp": 50,
    "str": 2,
    "dfn": 0,
    "attacks": [stab, slash],
    "spd": 10
}
player_test = {
    "name": "Big Hero Man",
    "hp": 100,
    "str": 1,
    "dfn": 50,
    "spd": 5
}

def display_battle(f1, f2):
    size = os.get_terminal_size()
    width = size[0]
    height = size[1]
    print("\n"*5)
    print(f"{f1.get_name()} versus {f2.get_name()}".center(width))
    print("\n" * (height//2-4), end="")
    print("".ljust(width//10)
        + str(f1.get_name()).ljust(width//10*4) 
        + str(f2.get_name()).rjust(width//10*4)
        )
    print("".ljust(width//10)
        + "HP: " f"{f1.get_hp():0.1f}".ljust(width//10*4) 
        + "HP: " f"{f2.get_hp():0.1f}".rjust(width//10*4)
        )
    print("\n"*(height//2-4), end="")
    print()

def battle(f1: Fighter, f2: Fighter):
    f1_name = f1.get_name()
    f2_name = f2.get_name()

    while True:
        f1.reset_turn()
        while f1.is_turn():
            display_battle(f1, f2)
            f1_attack = f1.attack()
            f2.damage(f1_attack)
            print(f"{f1_name} uses {f1_attack['name']} on {f2_name} for {f1_attack['quantity']} damage, leaving {f2_name} with {f2.get_hp():0.1f} health")
            input("[Enter to continue]")

            if not f2.is_alive():
                print(f"{f2_name} is slain. {f1_name} is victorious.")
                return f1

        f2.reset_turn()
        while f2.is_turn():
            display_battle(f1, f2)
            f2_attack = f2.attack()
            f1.damage(f2_attack)
            print(f"{f2_name} uses {f2_attack['name']} on {f1_name} for {f2_attack['quantity']} damage, leaving {f1_name} with {f1.get_hp():0.1f} health")
            input("[Enter to continue]")

            if not f1.is_alive():
                print(f"{f1_name} is slain. {f2_name} is victorious.")
                return f2



def test_battle():
    monster = Fighter(monster_test)
    player = Player(player_test, attacks = [bash, slam])
    battle(player, monster)
test_battle()