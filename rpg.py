from importlib.metadata import PathDistribution
#import combat
places = []
class players():
    def __init__(self, name, attack, speed, health, place, item):
        self.name = name
        self.attack = attack
        self.speed = speed
        self.health = health
        self.place = place
        self.item = item
class enemy():
    def __init__(self,name,attack,health,speed,item):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        self.item = item
class place():
    def __init__(self, name, enemy1, enemy2, enemy3, item, pathleft, pathright,pathup,pathdown):
        self.name = name
        self.enemy1 = enemy1
        self.enemy2 = enemy2
        self.enemy3 = enemy3
        self.item = item
        self.pathleft = pathleft
        self.pathright = pathright
        self.pathup = pathup
        self.pathdown = pathdown
        places.append(self)

def locationchanger(new_location):
    for i in paths:
        for j in places:
            if new_location == i.lower() and new_location == j.name.lower():   
                Player.place = j
                paths.clear()
                paths.append(j.pathleft)
                paths.append(j.pathright)
                paths.append(j.pathup)
                paths.append(j.pathdown)
                items.clear()
                items.append(j.item)
                return("You have moved to " + j.name)
    return("not a valid location")
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
            for i in paths:
                if i != "":
                    print("you can move to", i)
            check = 1
            move_to = input("").lower()
            print(locationchanger(move_to))
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

start = place("Tavern",'','','','','Back Alley','','','')
Back_Alley = place("Back Alley",'','','','','Street','Tavern','Alchemy Shop','')
Street = place("Street,'",'','','','','Street3','Street','Street4','Street2')
Alchemy_Shop = place("Alchemy Shop",'','','','','','','Back Room','Street')
Street2 = place('street')
Player = players(playername,10,1,10,start,'')
#computerlab = place("computer lab", "basic item" , "basic item", "hallway")
#hallway = place("hallway" , "yeah", "yeah", "wade")
#wadeL = place("First floor of wade", "k", "k", "Second floor")
##zipdesk = place("matt zippin's desk")
##poster = place("poster")
##hallwaystart("hallwaystart")
paths = [start.pathleft,start.pathright,start.pathup]
items = [start.item]





def main():
        print("Welcome to Cool RPG, " + Player.name + " this is the start of a great game")
        print("Currently you are in the",Player.place.name)
        menu()
    





main()
        
    
    
