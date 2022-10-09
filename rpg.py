import combat

class thing():
    def __init__(self, name, damage, health, location, items, weapon):
        self.name = name
        self.damage = damage
        self.health = health
        self.location = location
        self.items = items
        self.weapon = weapon
class place():
    def __init__(self, name, enemies, item, pathleft, pathright):
        self.name = name
        self.enemies = enemies
        self.item = item
        self.pathleft = pathleft
        self.pathright = pathright

def locationchanger(string):
    if string == "computer":
        paths.clear()
        paths.append(computer.pathleft)
        paths.append(computer.pathright)
        items.clear()
        items.append(place.item)
        player.location = "computer"
    elif string == "white board":
        paths.clear()
        paths.append(computer.pathleft)
        paths.append(computer.pathright)
        items.clear()
        items.append(place.item)
        player.location = "white board"
    else:
        print("na")
def battle():
    print("hi")
    # No reason to actually run any combat from main yet
def menu():
    print("what would you like to do?:")
    check = 0
    while check == 0:
        print("""Move
Check inventory
Pick up
Location""")
        answer = input("").lower()
        if answer == "move":
            print("you can move to " + paths[0] + "or " + paths[1])
            check = 1
            move_to = input("").lower()
            locationchanger(move_to)
        elif answer == "check inventory":
            print("here is your inventory")
            print(Player.items)
        elif answer == "pick up":
            print("what would you like to pick up")
            print(items)
        elif answer == "location":
            print(Player.location)
        else:
            print("?????????")
    
playername = input("Hello player, what is your name? ")

start = place("Start place", "none" , "none" , "computer", "white board")

Player = thing(playername,10,100, start.name, "", "")
#computerlab = place("computer lab", "basic item" , "basic item", "hallway")
#hallway = place("hallway" , "yeah", "yeah", "wade")
#wadeL = place("First floor of wade", "k", "k", "Second floor")
whiteboard = place("Whiteboard", "", "", "", "")
computer = place("computer","", "", "", "")
##zipdesk = place("matt zippin's desk")
##poster = place("poster")
##hallwaystart("hallwaystart")
paths = ["computer", "white board"]
items = [""]






def main():
        print("Welcome to Cool RPG, " + Player.name + " this is the start of a great game")
        print("Currently you are in the " + Player.location)
        menu()
    





main()
        
    
    
