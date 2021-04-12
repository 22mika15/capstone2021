
#Imports
import os
import time
import random
os.system("clear")

DELAY = 0.1

#Window Setup
#wn = turtle.Screen()
#wn.title("SCHERZO")
#wn.bgcolor("#227570")
#wn.setup(800, 600)
#wn.tracer(0)

##Create Pen
#pen = turtle.Turtle()
#pen.color("#00eb27")
#pen.speed(0)
#pen.penup()
#pen.goto(0, 250)
#pen.hideturtle()
#pen.write("Score: 200", move=False, align="center", font=("Courier New", 32, "normal"))


#0.0 for testing, 0.1 for gameplay
DELAY = 0.0

#Functions
def typing(text):
  words = text
  for char in words:
    time.sleep(DELAY)
    print(char, end='', flush=True)
    


#Define Classes
class Character():
    def __init__(self, lives, money, weapon, armour):
        self.lives = lives
        self.money = money
        self.weapon = weapon
        self.armour = armour

class Player(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, player_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.player_luck = random.randint(1,20)

class Enemy(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.enemy_luck = random.randint(1,20) #it asked for me to set a number in the instance, and I'm not sure if it overrides the random.randint

class Boss(Enemy):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Enemy.__init__(self, lives, money, weapon, armour, music_notes, enemy_luck)
        Character.__init__(self, lives, money, weapon, armour)
    #if player_music_notes > 5 boss_lives = 5
    #if player_music_notes > 7 boss_lives = 3
    #if player_music_notes > 10 boss_lives = 1
    

class Armour():
    def __init__(self, lives, music_notes):
        self.lives = lives
        self.music_notes = lives

class Weapon():
    def __init__(self, lives, music_notes):
        self.lives = lives
        self.music_notes = music_notes

weapons = []
armour = []

#MAKE A LIST OF WEAPONS AND A LIST OF ARMOUR
#WHEN USER CHOOSES THE WEAPON/ARMOUR, REMOVE FROM LIST
        
#Create Instances
player = Player(3, 221, "from list", "from list", 3, 1)
enemy = Enemy(3, 400, "from list", "from list", 3, 1)
#have one enemy object, change armour, weapon (and therefore lives) in mainloop?
boss = Boss("from player music notes", 1560, "from list", "from list", 22, 1)

#Show Splash Screen
print("\nSCHERZO")
print("Collect music notes to save the world from monsters.\n")
time.sleep(3.5)
os.system("clear")


#Mainloop
while True:
    typing("\nYou awaken in a dark, freezing forest, despite it being the height of summer")
    typing("\nYour armour is broken, and your weapons are damaged.")
    typing("\nYou will need to get them repaired, but your money pouches are very light.")
    typing("\n\nIn the distance, you can hear the sounds of a town waking up.")
    
    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    
    typing("\nYou approach the town, cautiously.")
    typing("\nThere is a notice on the town board - a monster, terrifying and dark as a winter blizzard.")
    typing("\nThe reward is 400 Coda, enough for repairs to all of your gear, but not a place to rest in safety.")
    
    time.sleep(0.5)
    
    accept_contract = input("\nDo you want to take the contract? Yes / No >> ").lower()
    if accept_contract == "yes" or accept_contract == "y":
        time.sleep(0.5)
        typing("\nYou accept the contract.")
        typing("\nYou enter a clearing, and approach the beast.")
        typing("\n[description of enemy, I'm working on it]")
                #the battle stuff begins here
        attack_dodge = input("\nAttack or Dodge >> ").lower()
        if attack_dodge == "a" or attack_dodge == "attack":
            if player.player_luck > enemy.enemy_luck:
                typing("\nsuccess")
                enemy.lives -= 1
                player.music_notes += enemy.music_notes
                if enemy.lives == 0:
                    typing("\nYou defeated the villain")
                    typing("\nYou return to the village, trophy in hand. You approach the owner of the contract")
                    typing(f"\nThe owner thanks you, and hands you {enemy.money} coda, and points you towards a merchant")
                    player.money += enemy.money
                    
                elif enemy.lives > 0:
                    pass
                    #repeat back to attack or dodge
                    
            elif player.player_luck < enemy.enemy_luck:
                typing("\nfail")
                player.lives -= 1
                if player.lives == 0:
                    typing("\nYou did not defeat the villain")
                    typing("\nYou continue on to the next village, hungry and tired. The world grows colder and darker, and there is grey in the skies.")
                    continue
                elif player.lives > 0:
                    pass
                    #repeat back to attack or dodge
        
    elif accept_contract == "no" or accept_contract == "n":
        time.sleep(0.5)
        typing("\nYou decided to leave the contract for someone else, and continue on.")
        s
        os.system("clear")
        typing("\nContinuing past the town, you approach a river that should be teaming with life.")
        typing("\nYou think you are alone, but notice an old woman leaning over the dirty water, further down the bank.") 
        typing("\nWith deliberatly loud steps, so as not to startle her, you approach.")
        typing("\nThe old woman looks up at you. Her eyes are black and furious, far too ancient to belong to a mortal human.")
        typing("\n'Hello, young warrior-' the crashing sounds of thousands of lives and death trickle through her voice. 'I have a game for you.'")
        time.sleep(0.5)
        #guessing game starts here
        

