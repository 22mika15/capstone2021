
#Imports
import os
import time
import random
os.system("clear")

#WHEN USER CHOOSES THE WEAPON/ARMOUR, REMOVE FROM LIST
#ADD THE OLD WEAPON/ARMOUR BACK


#0.0 for testing, 0.1 for gameplay
DELAY = 0.0
    

   
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
        self.player_luck = player_luck

class Enemy(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.enemy_luck = enemy_luck

class Boss(Enemy):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Enemy.__init__(self, lives, money, weapon, armour, music_notes, enemy_luck)
        Character.__init__(self, lives, money, weapon, armour)
    #if player_music_notes > 5 boss_lives = 5
    #if player_music_notes > 7 boss_lives = 3
    #if player_music_notes > 10 boss_lives = 1
    

class Armour():
    def __init__(self, name, strength, coda, cost ):
        self.name = name
        self.strength = strength
        self.coda = coda
        self.cost = cost

class Weapon():
    def __init__(self, name, strength, music_bonus, coda, cost ):
        self.name = name
        self.strength = strength
        self.music_bonus = music_bonus
        self.coda = coda
        self.cost = cost


sword = Weapon("Sword", 2, 3, 15, 82)
spear = Weapon("Spear", 4, 0, 11, 76)
axe = Weapon("Axe", 1, 4, 20, 80)
mace = Weapon("Mace", 1, 8, 10, 63)

light = Armour("light", 2, 15, 78)
medium = Armour("Medium", 3, 5, 75)
heavy = Armour("Heavy", 2, 15, 59)
dark = Armour("Dark", 1, 22, 78)

#put in dictionary so I can print out what each weapon has as bonuses?
weapons = [sword, spear, axe, mace]
armours = [light, medium, heavy, dark]
        
#Create Instances
player = Player(3, 221, "from list", "from list", 3, 3)#random.randint(3,20)
enemy = Enemy(2, 400, "from list", "from list", 3, 2)#random.randint(1,15)

#have one enemy object, change armour, weapon (and therefore lives) in mainloop?
boss = Boss("from player music notes", 1560, "from list", "from list", 22, 1)




#Functions
#working
def typing(text):
  words = text
  for char in words:
    time.sleep(DELAY)
    print(char, end='', flush=True)

#working
def fight():
    while enemy.lives > 0 and player.lives > 0: 
        print(f"Enemy lives: {enemy.lives}")
        print(f"Player lives: {player.lives}")
        attack_dodge = input("\nAttack or Dodge >> ").lower()
        if attack_dodge == "a" or attack_dodge == "attack":
            if player.player_luck > enemy.enemy_luck:
                enemy.lives -= 1

                if enemy.lives == 0:
                    os.system("clear")
                    win()
                    
            elif player.player_luck < enemy.enemy_luck:
                player.lives -= 1
                
                if player.lives == 0:
                    os.system("clear")
                    lose()
                    return 0

        elif attack_dodge == "d" or attack_dodge == "dodge":
            if player.player_luck > enemy.enemy_luck:
                typing("\nyou dodge the monster's attack")
                
            elif player.player_luck < enemy.enemy_luck:
                typing("\nyou try to dodge, but the monster's attack lands")
                player.music_notes -= 2
                player.lives -=1
                
                if player.lives == 0:
                    os.system("clear")
                    lose()
                    return 0

#working
def lose():
    typing("\nYou did not defeat your enemy")
    typing("\nYou continue on to the next village, hungry and tired. The world grows colder and darker, and there is grey in the skies.")
                    
#working (not nice-looking output, but working)   
def win():
    typing("\nYou defeated the villain")
    typing("\nYou return to the village, trophy in hand. You approach your employer.")
    typing(f"\nYour employer thanks you, and hands you {enemy.money} coda, and points you towards a merchant.")
    player.money += enemy.money
    typing("\nYou approach the merchant, who is selling armour and weapons.")
    buy_armour = input("\nDo you want to purchase armour? Yes / No >> ").lower()
    if buy_armour == "yes" or buy_armour == "y":
        for armour in armours:
            print(f"{armours.index(armour)+1}: {armour.name}")
        armour_index = input(f"Which do you want to purchase? Enter the number (1-{len(armours)}) >> ")
        armour_index = int(armour_index)
        armour = armours[armour_index]
        player.lives += armour.strength
        enemy.money += armour.coda
        player.money -= armour.cost
        typing(f"Weapon strength: {armour.strength}")
        typing(f"Money Bonus {armour.coda}")
        typing(f"Your Coda: {player.money}")

    buy_weapon = input("\nDo you want to purchase a weapon? Yes / No >> ").lower()
    if buy_weapon == "yes" or buy_weapon == "y":
        for weapon in weapons:
            print(f"{weapons.index(weapon)+1}: {weapon.name}")
        weapon_index = input(f"Which do you want to purchase? Enter the number (1-{len(weapons)}) >> ")
        weapon_index = int(weapon_index)
        weapon = weapons[weapon_index]
        enemy.lives -= weapon.strength
        enemy.music_notes -= weapon.music_bonus
        enemy.money += weapon.coda
        player.money -= weapon.cost
        typing(f"Weapon strength: {weapon.strength}")
        typing(f"Music Bonus: {weapon.music_bonus}")
        typing(f"Money Bonus {weapon.coda}")
        typing(f"Your Coda: {player.money}")
            
            
    elif buy_weapon == "no" or buy_weapon == "n":
        typing("'No problem'")

#almost there        
def riddle():
    #There are as many constellations in the sky as there are keys in a piano. What number am I?
    #A: 88
    #Which musical instrument will never tell the truth?
    #A: A lyre

    typing("'To learn more music you must answer me this...'")
    typing("""I have a scroll but without any quill.)
    I have ribs and a neck but no legs.
    I have a saddle but there's no horse.
    I have a bridge but with no sign of water.""")
    guesses = 5
    while guesses > 0:
        answer =5 input("What am I? >> ").lower()
        if answer == "a violin" or answer == "violin":
            typing("'Well done, young warrior.'")
            typing("The witch disappears in a flash of liquid, smokey gold.")
            player.music_notes += guesses
            typing(f"You notice that you have {guesses} new music notes")
        else:
            typing("'Not quite, Child.")
            guesses -= 1
            


riddle()
#narrative

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
        fight()
    
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
        
        riddle()
    
    os.system("clear")
    typing("The air smells of rotting fish, and the sounds of scavanging birds and angry voices dirty the air.")
    typing("What should be a peaceful fishing village is overcome with pollution.")
    typing("As you explore the market, a man dressed in seawares approaches you suddenly.")
    typing("'I've a pro'osition for ye, Scherzo. Ye kill mo'sters, do ye not?'")
    typing("'Got some Gillers down in me well. Help me out?'")  
    
    #enemy = Enemy(2, 400, "from list", "from list", 3, 1)
      
    accept_contract = input("\nDo you want to take the contract? Yes / No >> ").lower()
    if accept_contract == "yes" or accept_contract == "y":
        typing("'Aye, thank ye Scherzo. I'll lead ye to the place.'")
        os.system("clear")
        typing("You jump into the well, and you can hear the deep sounds of Gillers below the icy waters")
        typing("Swiftly, you climb onto a small ledge, ready for the attack")
        fight()
            

