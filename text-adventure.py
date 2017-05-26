
import random
import math

#Game Classes

class Character():
    def __init__(self, name = "none", hp = 100, ap = 30, element="none"):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.element = element
        self.items = ["sword", "health potion"]
        
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
        if item in self.items:
            return True
        else:
            return False
    def rnd_attack(self):
        atk = random.choice(["attack", "defend"])
        return atk
    def profile(self):
        print("NAME: {} | HP: {}  |  AP: {}  ".format(self.name, self.hp, self.ap))
        print("ELEMENT: {}".format(self.element))
        print("INVENTORY: {}".format(self.items))
    def analyze(self, npc):
        print(npc.analyze)
    def inventory(self):
        wooden_sword = Item("sword", "weapon", "none", 15, 0)
        potion = Item("potion", "potion", "none", 0, 20)
        items = [
                wooden_sword, potion
            ]
        
        
class Item():
    def __init__(self, name = "none", type = "none", element="none", atk = 0, heal = 0):
        self.name = name
        self.type = type
        self.element = element
        self.atk = atk
        self.heal = heal
            
class Combat():
    def check_attack(self, pc, npc):
        while not pc.is_dead() and not npc.is_dead():
            choice = self.check_answer("attack, defend, analyze, run", ["attack", "defend" , "analyze", "run"])
            print("You " + choice + "!!!")
            npc_atk = npc.rnd_attack()
            print(npc.name + " "+ npc_atk + "s!!!")
            if choice == "attack":
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
            else:
                if npc_atk == "attack":
                    npc.take_damage(pc.get_atk()//2)
                    pc.take_damage(npc.get_atk()//3)
                    print("You take {} damage".format(pc.get_atk()//2))
                    print("{} takes {} damage".format(npc.name, pc.get_atk()//3))
                else:
                    print("no damage")
                    
            print("Player has {} hitpoints ".format(pc.hp))
            print("Enemy has {} hitpoints ".format(npc.hp))
            
    
    def check_answer(self, question, answers): 
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer


class Story():
    def __init__(self):
        self.cm = Combat()
        print("Welcome to Magic Mystery")
        self.new_game()
        
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
        answer = self.check_answer('Do you want to restart game?', ["yes", "no"])
        if answer == "yes":
            self.new_game()
        else:
            print("Game Over")
    
    def create_char(self):
        name = input("Please enter your name: ")
        self.pc = Character(name)
        print ("Welcome to Magic Mystery %s" % (name))
        
    def menu(self, pc=" "):
        while True:
            print("========MENU=======\n 1. Look \n 2. Take \n 3. Use \n 4. Inventory \n 5. Status \n 6.Exit")
            choice = input().lower()
            if choice == "1" or choice == "look":
                print("You examine your sorroundings.")

    
            if choice == "2" or choice == "take":
                print("You pick up a {}.".format("item"))
        
        
            if choice == "3" or choice == "use":
                print("You use an item from your inventory")
                
    
            if choice == "4" or choice == "inventory":
                print("You are now looking at inventory")
            
            
            if choice == "5" or choice == "status":
                self.pc.profile()
            
    
            if choice == "6" or choice == "exit":
                print("=========Exiting menu=========\n6")
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
        skeleton = Character('Skeleton', hp=20, ap=5)
        is_skeletion_defeated = False
        goToNextRoom = False
        gotSpoon = False
        print("You find yourself in a dark room.")
        print("There does not appear to be an exit.")
        print("In the center of the room, there is a box.")
        print("to the right you see a door that is slightly ajar.")
        print("To the left is a pile of bones with what looks like a bowl mounted on top\n")
        while(not is_skeletion_defeated and not goToNextRoom):
            answer = self.check_answer("What will you do?  \n 1. got to door  2. got to box  3. go to bones  4. MENU \n", ["1", "2", "3","4"])
            if answer == "1":
                print("You walk towards the door")
                print("It is a plain wooden door")
                print("It seems as though it will open with minimal effort")
                if answer == "1":   
                    print("As you attempt to open the door, a force compells you to stay.")
                    print("You feel as if something is left unfinished\n")
            elif answer == "2":
                print("You walk towards the box")
                print("Inside the box there is a spoon")
                answer = self.check_answer("What do you do?: \n 1. Take spoon \n 2. Do Nothing", ["1", "2"])
                if answer == "1":
                    gotSpoon = True
                else:
                    print("Nothing of value happend. You return where you started")
                
            elif answer == "3":
                print("You walk towards the pile of bones")
                print("You notice the bowl on the pile of bones is filled with what appears to be pudding")
                answer = self.check_answer("What do you do?:  \n 1. Eat the pudding. \n 2. examine the bones \n 3. Do nothing", ["1", "2", "3"])
                if answer == "1" and gotSpoon:
                    print("You eat the pudding")
                    print("Suddently the bones begin to shake")
                    print("A blood curdling howl can be heard as the bones magically assemble themselves into a skeleton")
                    print("The skeleton speaks, 'What have you done!!'")
                    print("We are no where near the holidays!")
                    answer == self.check_answer("Respond: \n 1. What has got to do with anything  2. Yes we are", ["1", "2"])
                    if answer == "1":
                        print("That was Christmas pudding!!!")
                        print("The skeleton readies for combat")
                        self.cm.check_attack(self.pc, skeleton)
                        if self.pc.is_dead():
                            print("The monster wins the fight")
                            self.dead()
                        else:
                            print("You defeated the monster")
                            is_skeletion_defeated = True
                            print("You receive the skeleton key")
                    elif answer == "2":
                        print("Is it really? Have I been out of it for so long?")
                        answer = self.check_answer("1. Yes, you've missed everything  2. I am lying you fool", [
                        "1", "2"])
                        if answer == "1":
                            print("The skeleton hunches over in disappointment and desintegrates")
                            print("You receive the skeleton key")
                        if answer == "2":
                            print("The skeleton's anger is multiplied tenfold")
                            print("With one swing he crushes your skull with a club")
                    
                else:
                    print("You have no spoon. Eating it is out of the question. You are not a savage!")
                    
            elif answer == "4":
                self.menu(self.pc)
                
                
            
new_game = Story()
