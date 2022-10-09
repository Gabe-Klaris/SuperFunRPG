class Fighter():
    def __init__(self, hp_in, atk_in):
        self.atk = atk_in
        self.hp = hp_in
    def damage(self, dmg):
        self.hp -= dmg
    def attack(self):
        return self.atk
    def is_alive(self):
        return self.hp > 0
    def current_hp(self):
        return self.hp

def battle(f1, f2):
    while f1.is_alive() and f2.is_alive():
        f1_attack = f1.attack()
        f2.damage(f1_attack)
        print(f"Fighter 1 hits fighter 2 for {f1_attack} damage, leaving fighter 2 with {f2.current_hp()} health")
        f2_attack = f2.attack()
        f1.damage(f2_attack)
        print(f"Fighter 2 hits fighter 1 for {f2_attack} damage, leaving fighter 1 with {f1.current_hp()} health")
    
    if f1.is_alive():
        print("Fighter 2 is slain. Fighter 1 is victorious.")
        return f1
    elif f2.is_alive():
        print("Fighter 1 is slain. Fighter 2 is victorious.")
        return f2
    else:
        print("Both fighters slay each other simultaneously")
        return None

def test_battle():
    f1 = Fighter(10,2)
    f2 = Fighter(4,1)
    battle(f1, f2)
test_battle()