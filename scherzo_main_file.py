
#Imports
import os
import time
import random
os.system("clear")

DELAY = 0.1

#put in dictionary so I can print out what each weapon has as bonuses?
weapons = ["", "weapon1", "weapon2", "weapon3", "weapon4"]
armours = ["", "armour1", "armour2", "armour3", "armour4"]

#WHEN USER CHOOSES THE WEAPON/ARMOUR, REMOVE FROM LIST
#ADD THE OLD WEAPON/ARMOUR BACK


#(If i get these working I'm pretty sure I should have the bulk of the game code, and just have to code the boss, and the narrative)
#FIGHT FUNCTION
#holds code for attack/dodge, similar to track and field code
#WIN FUNCTION
#holds code for purchasing weapons and armour
#RIDDLE FUNCTION
#holds code for riddles, similar to guessing game

#narrative
#do you want to take the contract y/n
#if y, fight() >>> if enemy lives == 0, win() >>> narrative
#if n, riddle() >>> if guesses >= 5, music_notes += number >>> narrative


#0.0 for testing, 0.1 for gameplay
DELAY = 0.0

#Functions
def typing(text):
  words = text
  for char in words:
    time.sleep(DELAY)
    print(char, end='', flush=True)
    
#haven't finished all the sales code yet    
def player_win():
    typing("\nYou defeated the villain")
    typing("\nYou return to the village, trophy in hand. You approach the owner of the contract")
    typing(f"\nThe owner thanks you, and hands you {enemy.money} coda, and points you towards a merchant")
    player.money += enemy.money
    typing("\nYou approach the merchant, who is selling armour, weapons, and potions")
    buy_armour = input("\nDo you want to purchase armour? Yes / No >> ").lower()
    if buy_armour == "yes" or buy_armour == "y":
        for armour in armours:
            print(f"{armours.index(armour)}: {armour}")
        new_armour = input("Which do you want to purchase? Enter the number (1-4) >> ")
        if new_armour == "1":
            player.lives += 2
            enemy.money += 15
            player.money -= 78
            typing(f"Lives: {player.lives}")
            typing(f"Money: {player.money}")
        elif new_armour == "2":
            player.lives += 3
            enemy.money += 5
            player.money -= 73
            typing(f"Lives: {player.lives}")
            typing(f"Money: {player.money}")
        elif new_armour == "3":
            player.lives += 2
            enemy.money += 15
            player.money -= 59
            typing(f"Lives: {player.lives}")
            typing(f"Money: {player.money}")
        elif new_armour == "4":
            player.lives += 1
            enemy.money += 22
            player.money -= 78
            typing(f"Lives: {player.lives}")
            typing(f"Money: {player.money}")
        else:
            typing("'Ok, thanks'")
        
    elif buy_armour == "no" or buy_armour == "n":
        typing("'Ok, thanks'")
   
    buy_weapon = input("\nDo you want to purchase a weapon? Yes / No >> ").lower()
    if buy_weapon == "yes" or buy_weapon == "y":
        for weapon in weapons:
            print(f"{weapons.index(weapon)}: {weapon}")
        for armour in armours:
            print(f"{armours.index(armour)}: {armour}")
        new_weapon = input("Which do you want to purchase? Enter the number >> ")
        if new_weapon == "1":
            enemy.lives -= 2
            enemy.music_notes -=3
            enemy.money += 15
            player.money -= 82
            typing("Weapon strength +2")
            typing("Music Bonus +3")
            typing("Money Bonus +15")
            typing(f"Your Coda: {player.money}")
        elif new_weapon == "2":
            enemy.lives -=4
            enemy.music_notes = 0
            enemy.money += 11
            player.money -= 82
            typing("Weapon strength +4")
            typing("Money Bonus +15")
            typing(f"Your Coda: {player.money}")
        elif new_weapon == "3":
            enemy.lives -=1
            enemy.music_notes += 4
            enemy.money +=20
            player.money -= 82
            typing("Weapon strength +2")
            typing("Music Bonus +3")
            typing("Money Bonus +15")
            typing(f"Your Coda: {player.money}")
        elif new_weapon == "4":
            enemy.lives += 1
            enemy.music_notes += 8
            enemy.money += 10
            player.money -= 82
            typing("Weapon strength +2")
            typing("Music Bonus +3")
            typing("Money Bonus +15")
            typing(f"Your Coda: {player.money}")
        else:
            typing("'Ok, thanks'")
        new_weapon = input("Which do you want to purchase? Enter the number >> ")
    elif buy_weapon == "no" or buy_weapon == "n":
        typing("'No problem'")
   
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
        self.player_luck = 3 #random.randint(1,20)

class Enemy(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.enemy_luck = 2 #random.randint(1,20) #it asked for me to set a number in the instance, and I'm not sure if it overrides the random.randint

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
        
#Create Instances
player = Player(3, 221, "from list", "from list", 3, 1)
enemy = Enemy(1, 400, "from list", "from list", 3, 1)
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
    typing("\nThe reward is 400 coda, enough for repairs to all of your gear, but not a place to rest in safety.")
    
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
                    player_win()
                    continue
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
        if attack_dodge == "d" or attack_dodge == "dodge":
            if player.player_luck > enemy.enemy_luck:
                typing("\nyou dodge the monster's attack")
                    #repeat back to attack or dodge

            elif player.player_luck < enemy.enemy_luck:
                typing("\nyou try to dodge, but the monster's claw catches you")
                player.music_notes -= 2
                player.lives -=1
                if player.lives == 0:
                    typing("\nYou did not defeat the villain")
                    typing("\nYou continue on to the next village, hungry and tired. The world grows colder and darker, and there is grey in the skies.")
                    continue
                elif player.lives > 0:
                    #repeat back to attack or dodge
                    pass

    elif accept_contract == "no" or accept_contract == "n":
        time.sleep(0.5)
        typing("\nYou decided to leave the contract for someone else, and continue on.")
        
        os.system("clear")
        typing("\nContinuing past the town, you approach a river that should be teaming with life.")
        typing("\nYou think you are alone, but notice an old woman leaning over the dirty water, further down the bank.") 
        typing("\nWith deliberatly loud steps, so as not to startle her, you approach.")
        typing("\nThe old woman looks up at you. Her eyes are black and furious, far too ancient to belong to a mortal human.")
        typing("\n'Hello, young warrior-' the crashing sounds of thousands of lives and death trickle through her voice. 'I have a game for you.'")
        time.sleep(0.5)
        #guessing game starts here
    
    os.system("clear")
    typing("The air smells of rotting fish, and the sounds of scavanging birds and angry voices dirty the air.")
    typing("What should be a peaceful fishing village is overcome with pollution.")
    typing("As you explore the market, a man dressed in seawares approaches you suddenly.")
    typing("'I've a pro'osition for ye, Scherzo. Ye kill mo'sters, do ye not?'")
    typing("'Got some Gillers down in me well. Help me out?'")    
    accept_contract = input("\nDo you want to take the contract? Yes / No >> ").lower()
    if accept_contract == "yes" or accept_contract == "y":
        typing("'Aye, thank ye Scherzo. I'll lead ye to the place.'")
        os.system("clear")
        typing("You jump into the well, and you can hear the deep sounds of Gillers below the icy waters")
        typing("Swiftly, you climb onto a small ledge, ready for the attack")
        #fight()
            
    
        

