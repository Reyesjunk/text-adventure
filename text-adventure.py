
import random
import math

#Game Classes
inventory = []

class Character():
    global inventory
    def __init__(self, name = "none", hp = 100, ap = 30, element="none", is_enemy=False):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.element = element
        self.is_enemy = is_enemy
        
    def take_dmg(self, dmg):
        self.hp = self.hp - dmg
        
    def heal(self, heal):
        self.hp = self.hp + heal
        
    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False
            
    def get_atk(self):
        atk = random.randint(0, self.ap)
        return atk
        
    def has_item(self, item):
        if item in inventory:
            return True
        else:
            return False
    def rnd_attack(self):
        atk = random.choice(["attack", "defend"])
        return atk
    def profile(self):
        print("NAME: {} | HP: {}  |  AP: {}  ".format(self.name, self.hp, self.ap))
        print("ELEMENT: {}".format(self.element))
        if not self.is_enemy: 
            print("INVENTORY: {}".format(inventory))
    def analyze(self):
        print(self.profile())

    def take(self, item):
        inventory.append(item)
        
class Item():
    def __init__(self, name = "none", type = "none", element="none", atk = 0, heal = 0):
        self.name = name
        self.type = type
        self.element = element
        self.atk = atk
        self.heal = heal
    def __str__(self):
        return self.name
    def __repr__(self):
       return self.name
            
class Combat():
    def check_attack(self, pc, npc):
        while not pc.is_dead() and not npc.is_dead():
            print("Player has {} hitpoints ".format(pc.hp))
            print("Enemy has {} hitpoints ".format(npc.hp))
            choice = self.check_answer("attack, defend, analyze, run\n", ["attack", "defend" , "analyze", "run"])
            print("You " + choice + "!!!")
            npc_atk = npc.rnd_attack()
            print(npc.name + " "+ npc_atk + "s!!!")
            if choice == "analyze":
                npc.analyze()
            elif choice == "attack":
                if npc_atk == "attack":
                    pc.take_dmg(npc.get_atk())
                    npc.take_dmg(pc.get_atk())
                    print("You take " + str(npc.get_atk()) + " damage")
                    print(npc.name + " takes " + str(pc.get_atk()) + " damage")
                else:
                    pc.take_dmg(npc.get_atk()//2)
                    npc.take_dmg(pc.get_atk()//3)
                    print("You take {} damage".format(npc.get_atk()//2))
                    print("{} takes {} damage".format(npc.name, pc.get_atk()//3))
            elif choice == "defend":
                if npc_atk == "attack":
                    npc.take_damage(pc.get_atk()//2)
                    pc.take_damage(npc.get_atk()//3)
                    print("You take {} damage".format(pc.get_atk()//2))
                    print("{} takes {} damage".format(npc.name, pc.get_atk()//3))
                else:
                    print("no damage")
            
    
    def check_answer(self, question, answers): 
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer


class Story():
    global inventory
    def __init__(self):
        self.cm = Combat()
        print("Welcome to Magic Mystery")
        self.new_game()
        
    def twoWordParser(self, input, verb, noun):
        word_list = input.split()
        if verb in word_list and noun in word_list:
            return True
        
    def check_answer(self, question, answers): 
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer
        
    def new_game(self):
        self.create_char()
        self.room()
        
    def dead(self):
        print ("You are incinerated instantly")
        answer = self.check_answer('Do you want to restart ga4me?', ["yes", "no"])
        if answer == "yes":
            self.new_game()
        else:
            print("Game Over")
    
    def create_char(self):
        name = input("Please enter your name: ")
        self.pc = Character(name)
        print ("Welcome to Magic Mystery %s" % (name))
        
    def menu(self, pc=" ", expected="", resolution=""):
        while True:
            print("")
            print("~~~~MENU~~~~~~~~~\n 1. Look \n 2. Use \n 3. Inventory \n 4. Status \n 5. Exit")
            choice = input().lower()
            print("")
            if choice == "1" or choice == "look":
                print("You examine your sorroundings.")
                print(self.description)
                print("")
        
            if choice == "2" or choice == "use":
                print(inventory)
                item = input("choose item to use\n")
                if item == expected:
                    print(resolution)
                    return True
                else:
                    if item in inventory:
                        print("This item can't be used right now.")
                    else:
                        print("The item you requested doesn't exist.")
                print("")
    
            if choice == "3" or choice == "inventory":
                print(inventory)
                print("")
            
            
            if choice == "4" or choice == "status":
                self.pc.profile()
                print("")
            
    
            if choice == "5" or choice == "exit":
                print("=========Exiting menu=========\n")
                print("")
                break
    
    
    def fight(self):
        monster = Character("Lizard", hp = 30, ap = 6)
        print("You are now engaged in combat with a " + monster.name)
        self.cm.check_attack(self.pc, monster)
        if self.pc.is_dead():
            print("The monster wins the fight")
            self.dead()
        else:
            print("The winner is you")
        
        
    def room(self):
        self.description = "You are in a square, thinly lit room\
        \nThere are no windows\
        \nThere is a box in the center of the room\
        \nTo the left is a pile of bones with what looks like a bowl mounted on top\
        \nTo the center is a box\
        \nTo the right you see a door that is slightly ajar."
        skeleton = Character('Skeleton', hp=20, ap=5)
        skeleton_key = Item('Skeleton Key', type = "quest")
        wooden_sword = Item("Wooden Sword", "weapon", "none", 15, 0)
        potion = Item("potion", "potion", "none", 0, 20)
        spoon = Item("Spoon", "quest",)
        print("You find yourself in a dark room.")
        print(self.description)
        while(True):
            answer = self.check_answer("What will you do?  \n 1. go to door  2. go to box  3. go to bones  4. MENU \n", ["1", "2", "3","4"])
            if answer == "1":
                print("You walk towards the door")
                print("It is a plain wooden door")
                print("It seems as though it will open with minimal effort")
                if not "rock" in inventory:
                    print("Near the door there is a rock\n")
                    answer = self.check_answer("What will you do?: 1. Take rock.  2. Open door  3. Go back\n", ["1", "2", "3"])
                    
                    if answer == "1":
                        self.pc.take("rock")
                        print("You place the rock in your inventory")
                    elif answer == "2":
                        print("As you attempt to open the door, a force compells you to stay.")
                        print("You feel as if something is left unfinished\n")
                    elif answer =="3":
                        print('You do nothing and go back where you came.\n')
                else:
                    answer = self.check_answer("What will you do?: 1. Open door 2. Go back\n", ["1", "2"])
                    if answer == "1":
                        if skeleton_key in inventory:
                            print("You open the door without much effort.")
                            self.hallway()
                            break
                        print("As you attempt to open the door, a force compells you to stay.")
                        print("You feel as if something is left unfinished\n")
                    else: 
                        print('You do nothing and go back where you came.')

            elif answer == "2":
                print("You walk towards the box")
                print("It is a metal box that appears to be old and rusted\n")
                print("")
                answer = self.check_answer("What do you do?: \n 1. open box \n 2. Do Nothing \n 3. MENU", ["1", "2", "3"])
                print("")
                if answer == "1":
                    print("You attempt to open the box but it appears to be rusted shut\n")
                elif answer == "2":
                    print("Nothing of value happend. You return where you started\n")
                elif answer == "3":
                    success = self.menu(self.pc, 'rock', 'You throw the rock at the box causing it to burst open. A Spoon and a Wooden Sword  fall out\n')
                    if success:
                        print("You put the Wooden Sword and the Spoon in your inventory\n")
                        self.pc.take(wooden_sword)
                        self.pc.take(spoon)
                        
                
            elif answer == "3":
                print("You walk towards the pile of bones")
                print("You notice the bowl on the pile of bones is filled with what appears to be pudding")
                print("Despite how sketchy it seems, you almost feel compelled to eat the pudding.\n")
                answer = self.check_answer("What do you do?:  \n 1. Eat the pudding. \n 2. examine the bones \n 3. Do nothing\n", ["1", "2", "3"])
                if answer == "1" and spoon in inventory:
                    print("You eat the pudding")
                    print("Suddently the bones begin to shake")
                    print("A blood curdling howl can be heard as the bones magically assemble themselves into a skeleton")
                    print("The skeleton speaks, 'What have you done!!'")
                    print("We are no where near the holidays!\n")
                    answer = self.check_answer("Respond: \n 1. What has got to do with anything  2. Yes we are\n", ["1", "2"])
                    if answer == "1":
                        print("That was Christmas pudding!!!")
                        print("The skeleton readies for combat")
                        self.cm.check_attack(self.pc, skeleton)
                        if self.pc.is_dead():
                            print("The monster wins the fight")
                            self.dead()
                        else:
                            print("You defeated the monster")
                            print("You receive the skeleton key")
                    else:
                        print("Is it really? Have I been out of it for so long?")
                        answer = self.check_answer("1. Yes, you've missed everything  2. I am lying you fool", [
                        "1", "2"])
                        if answer == "1":
                            print("The skeleton hunches over in disappointment and desintegrates")
                            print("You receive the skeleton key")
                            self.pc.take(skeleton_key)
                            for item in inventory:
                                print(item)
                        else:
                            print("The skeleton's anger is multiplied tenfold")
                            print("With one swing he crushes your skull with a club")
                    
                elif answer == "2":
                    print("You inspect the bones")
                    print("They appear to be real human bones.")
                    print("There placement does not seem natural.")
                    print("They almost seem like decorations,")
                else:
                    print("You have no spoon. Eating it is out of the question. You are not a savage!")
                    
            elif answer == "4":
                self.menu(self.pc)
    def hallway(self):
        self.description = "You find yourself in the middle of a large hallway\
        \nThere is a painting right in front of you\
        \nTo your right is a window\
        \n To your left is a old potted plant"
        print(self.description)
        while(True):
            answer = self.check_answer('What will you do:  1. Go to painting  2. Go to window  3. Go to plant  4. MENU\n', ["1", "2", "3", "4"])
            if answer == "1":
                print("You go to the painting")
                print("It is a striking image a woman with an intense stare")
                print("You almost feel as if she is right there looking at you!")
            elif answer =="2":
                print("You head over to the window.")
                print("You cannot make out anything beyond the glass")
            elif answer ==  "3":
                print("You head over to the plant.")
                print("It is a potted plant.")
                print("It appears as though someone has been watering it.")
            else:
                self.menu(self.pc)
            
new_game = Story()
