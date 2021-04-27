
#Imports
import os
import time
import random
import threading
os.system("clear")

#I had some cool story I wanted to add, but didn't have quite enough time to figure out
#Will try in the future

#some of the sound is overlapping when it shouldn't


#0.0 for testing, 0.1 for gameplay
DELAY = 0.0
    

   
#Define Classes
class Character():
    def __init__(self, lives, money, weapon, armour):
        self.lives = lives
        self.money = money
        self.weapon = weapon
        self.armour = armour
        
        def set_lives(self, new_lives):
            self.lives = new_lives
        
        def get_lives(self):
            return self.lives
            
        def set_money(self, new_money):
            self.money = new_money
        
        def get_money(self):
            return self.money

        def set_weapon(self, new_weapon):
            self.weapon = new_weapon
        
        def get_weapon(self):
            return self.weapon
        
        def set_armour(self, new_armour):
            self.armour = new_armour
        
        def get_armour(self):
            return self.armour
            

class Player(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, player_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.player_luck = player_luck
        
        def set_notes(self, new_notes):
            self.music_notes = new_notes
        
        def get_notes(self):
            return self.music_notes
        
        def set_luck(self, new_luck):
            self.player_luck = new_luck
        
        def get_luck(self):
            return self.player_luck

class Enemy(Character):
    def __init__(self, lives, money, weapon, armour, music_notes, enemy_luck):
        Character.__init__(self, lives, money, weapon, armour)
        self.music_notes = music_notes
        self.enemy_luck = enemy_luck
        
        def set_notes(self, new_notes):
            self.music_notes = new_notes
        
        def get_notes(self):
            return self.music_notes
        
        def set_luck(self, new_luck):
            self.enemy_luck = new_luck
        
        def get_luck(self):
            return self.enemy_luck
    

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

weapons = [sword, spear, axe, mace]
armours = [light, medium, heavy, dark]
        
#Create Instances
player = Player(3, 221, "from list", "from list", 3, 0)
enemy = Enemy(2, 400, "from list", "from list", 3, 0)
boss = Enemy(0, 1560, "from list", "from list", 22, 0)



#Functions

def loop_audio(filename, t):
    threading.Timer(t, lambda: loop_audio(filename, t)).start()
    os.system(f"afplay {filename}&")
        
#working
def typing(text):
  words = text
  for char in words:
    time.sleep(DELAY)
    print(char, end='', flush=True)

#working
def fight():
    os.system("killall afplay")
    while enemy.lives > 0 and player.lives > 0:
        loop_audio("battle_music.mp3", 24.0) 
        print(f"\nEnemy lives: {enemy.lives}")
        print(f"Player lives: {player.lives}")
        
        #set character luck
        player.player_luck = random.randint(1,10)
        enemy.enemy_luck = random.randint(1,10)
        
        attack_dodge = input("\nAttack or Dodge >> ").lower()
        if attack_dodge == "a" or attack_dodge == "attack":
            if player.player_luck > enemy.enemy_luck:
                enemy.lives -= 1

                if enemy.lives == 0:
                    os.system("afplay win.wav&")
                    os.system("clear")
                    win()
                    
            elif player.player_luck < enemy.enemy_luck:
                player.lives -= 1
                
                if player.lives == 0:
                    os.system("clear")
                    os.system("afplay death.wav&")
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
                    os.system("afplay death.wav&")
                    lose()
                    return 0

#working
def lose():
    
    typing("\nYou did not defeat your enemy")
    typing("\nYou continue on to the next village, hungry and tired. The world grows colder and darker, and there is grey in the skies.")
                    
#working
def win():
    os.system("killall afplay")
    loop_audio("music.mp3", 19.0) 
    
    typing("\nYou defeated the villain")
    typing("\nYou return to the village, trophy in hand. You approach your employer.")
    typing(f"\nYour employer thanks you, and hands you {enemy.money} coda, and points you towards a merchant.")
    player.money += enemy.money
    typing("\nYou approach the merchant, who is selling armour and weapons.")
    buy_armour = input("\nDo you want to purchase armour? Yes / No >> ").lower()
    if buy_armour in ["yes", "y", "yep", "please", "yeah", "heck yeah"]:
        os.system("clear")
        for armour in armours:
            print(f"\n{armours.index(armour)+1}) {armour.name}")
            print(f"Strength: {armour.strength}")
            print(f"Money Bonus: {armour.coda}")
            print(f"Cost: {armour.cost}")
        armour_index = input(f"\nWhich do you want to purchase? Enter the number (1-{len(armours)}) >> ")
        os.system("afplay select.wav&")
        armour_index = int(armour_index) -1
        armour = armours[armour_index]
        #i want to remove armour from list once it is chosen. 
        player.lives += armour.strength
        enemy.money += armour.coda
        player.money -= armour.cost
        os.system("clear")
        typing(f"\nPlayer Lives: {player.lives}")
        typing(f"\nMoney Bonus: {armour.coda}")
        typing(f"\nYour Coda: {player.money}")

    buy_weapon = input("\nDo you want to purchase a weapon? Yes / No >> ").lower()
    if buy_weapon in ["yes", "y", "yep", "please", "yeah", "heck yeah"]:
        os.system("clear")
        for weapon in weapons:
            print(f"\n{weapons.index(weapon)+1}) {weapon.name}")
            print(f"Strength: {weapon.strength}")
            print(f"Music Bonus: {weapon.music_bonus}")
            print(f"Coda Bonus: {weapon.coda}")
            print(f"Cost: {weapon.cost}")
        weapon_index = input(f"\nWhich do you want to purchase? Enter the number (1-{len(weapons)}) >> ")
        os.system("afplay select.wav&")
        weapon_index = int(weapon_index) -1
        weapon = weapons[weapon_index]
        enemy.lives -= weapon.strength
        enemy.music_notes += weapon.music_bonus
        enemy.money += weapon.coda
        player.money -= weapon.cost
        os.system("clear")
        typing(f"\nEnemy Lives: {enemy.lives}")
        typing(f"\nMusic Bonus: {enemy.music_notes}")
        typing(f"\nCoda Bonus: {weapon.coda}")
        typing(f"\nYour Coda: {player.money}")
            
            
    elif buy_weapon == "no" or buy_weapon == "n":
        typing("'No problem'")

#working
def riddle():
    os.system("clear")
    guesses = 5
    decide_riddle = [1, 2, 3]
    random_decide = random.randint(1,len(decide_riddle))
    
    if random_decide == 1:
        decide_riddle.remove(1)
        typing(f"\n{guesses} tries you have, and more music will reveal itself to you")
        typing("\nI have a scross but without any quill...")
        typing("\nI have ribs and a neck but no legs...")
        typing("\nI have a saddle but there's no horse...")
        typing("\nI have a bridge but with no sign of water.")
        
        while guesses > 0:
            answer = input("\nWhat am I?  >> ").lower()
            if answer == "a violin" or answer == "violin":
                typing("\n'Well done, young warrior.'")
                typing("The witch disappears in a flash of liquid, smokey gold.")
                player.music_notes += guesses
                typing(f"You notice that you have {guesses} new music notes")
                guesses = 0
                break
            else:
                typing("'Not quite, Child.")
                guesses -= 1
                
    elif random_decide == 2:
        decide_riddle.remove(2)
        typing(f"\n{guesses} tries you have, and more music will reveal itself to you")
        typing("\nI am a musical instrument...")
        typing("\nAnd will never tell the truth...")
        
        while guesses > 0:
            answer = input("What am I?  >> ").lower()
            if answer == "a lyre" or answer == "lyre":
                typing("\n'Well done, young warrior.'")
                typing("\nThe witch disappears in a flash of liquid, smokey gold.")
                player.music_notes += guesses
                typing(f"\nYou notice that you have {guesses} new music notes")
                guesses = 0
                break
            else:
                typing("\n'Not quite, Child.")
                guesses -= 1
            
                
    elif random_decide == 3:
        decide_riddle.remove(3)
        typing(f"\n{guesses} tries you have, and more music will reveal itself to you")
        typing("\nThere as many constellations in the sky...")
        typing("\nas there are keys on a piano...")

        while guesses > 0:
            answer = input("What number am I?  >> ")
            answer = int(answer)
            if answer == 88:
                typing("\n'Well done, young warrior.'")
                typing("\nThe witch disappears in a flash of liquid, smokey gold.")
                player.music_notes += guesses
                typing(f"\nYou notice that you have {guesses} new music notes")
                guesses = 0
                break
            else:
                typing("\n'Not quite, Child.")
                guesses -= 1
                
    typing("\n'Farewell, and good luck'")
    os.system("clear")

#working
def accept_contract():
    accept_contract = input("\nDo you want to accept? Yes / No >> ").lower()
    if accept_contract in ["yes", "y", "yep", "yeah", "please"]:
        typing("\nYou take the notice from the board, and prepare for the fight...")
        time.sleep(3)
        os.system("clear")
        fight()
        
    else:
        typing("\nYou decided to leave the contract for someone else, and continue on.")
        time.sleep(3)
        os.system("clear")
        riddle()

#working
def boss_fight():
    os.system("killall afplay")
    if player.music_notes >= 5:
        boss.lives += 6
    elif player.music_notes >= 7:
        boss.lives += 4
    elif player.music_notes >= 9:
        boss.lives += 3
    
    while boss.lives > 0 and player.lives >0:
        os.system("afplay boss_music.wav&")
        #loop_audio("boss_music.wav")
        print(f"\nSliencer lives: {boss.lives}")
        print(f"Player lives: {player.lives}")
        print(f"Music Notes: {player.music_notes}")
        
        player.player_luck = random.randint(1,8)
        boss.enemy_luck = random.randint(4,10)
        
        attack_dodge = input("\nAttack or Dodge >> ").lower()
        if attack_dodge in ["attack", "a"]:
            if player.player_luck > boss.enemy_luck:
                boss.lives -= 1

                if enemy.lives == 0:
                    os.system("afplay win.wav&")
                    player.money += boss.money
                    player.music_notes += boss.music_notes
                    print(player.money)
                    print(player.music_notes)
                    time.sleep(3)
                    os.system("clear")
                    
                    typing("\nYou defeated Silencer, the great evil haunting the lands...")
                    typing("\nYou feel the warmth seep back into the skies, and the rustling of awakening leaves...")
                    typing("\nThank you, Warrior, the world is back in tune...")
                    time.sleep(4)
                    
                    
            elif player.player_luck < boss.enemy_luck:
                player.lives -= 1
                
                if player.music_notes > 0:
                    use_music_note = input("\n Use a music note to heal? >> ").lower()
                    if use_music_note in ["yes", "heal", "y", "h", "use", "please", "yup", "yeah", "heck yeah"]:
                        player.lives += 1
                        player.music_notes -=1
                
                if player.lives == 0:
                    os.system("clear")
                    os.system("afplay death.wav&")
                    typing("\nYou did not succeed...")
                    typing("\nThe evil begins to seep irreversibly into the world, there is no more you can do...")
                    typing("\nYou failed, warrior. you failed us all...")

        elif attack_dodge in ["dodge", "d"]:
            if player.player_luck > enemy.enemy_luck:
                typing("\nyou dodge the Silencer's attack")
                
            elif player.player_luck < enemy.enemy_luck:
                typing("\nyou try to dodge, but the Silencer's attack lands")
                player.music_notes -= 2
                player.lives -=1
                
                if player.lives == 0:
                    os.system("clear")
                    os.system("afplay death.wav&")
                    typing("\nYou did not succeed...")
                    typing("\nThe evil begins to seep irreversibly into the world, there is no more you can do...")
                    typing("\nYou failed, warrior. you failed us all...")
                    return 0
        
    
#FUNCTION TESTING

#Mainloop
while True:
    #Show Splash Screen
    loop_audio("splash_screen.flac", 48.0)
    
    print("""\n
████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█─█─█▄─▄▄─█▄─▄▄▀█░▄▄░▄█─▄▄─█
█▄▄▄▄─█─███▀█─▄─██─▄█▀██─▄─▄██▀▄█▀█─██─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀ """)

    typing("\nCollect music notes to save the world from monsters.\n")
    begin_game = input("Begin game? >> ").lower()
    if begin_game in ["yes", "y", "begin", "start", "s", "b", "let's go", "begin", "go", "yeah", "heck yeah"]:
        time.sleep(2)
        os.system("killall afplay")
        os.system("clear")
    else:
        break
        
    #Begin Game
    loop_audio("music.mp3", 19.0)
    
    
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
    os.system("clear")
    time.sleep(0.5)
    
    accept_contract()


    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    
    typing("The air smells of rotting fish, and the sounds of scavanging birds and angry voices dirty the air.")
    typing("What should be a peaceful fishing village is overcome with pollution.")
    typing("As you explore the market, a man dressed in seawares approaches you suddenly.")
    typing("'I've a pro'osition for ye, Scherzo. Ye kill mo'sters, do ye not?'")
    typing("'Got some Gillers down in me well. Help me out?'") 
    
    time.sleep(0.5)
    
    accept_contract()

    time.sleep(0.5)
    os.system("clear")
    time.sleep(0.5)
    
    typing("\n It is almost too late, the sun has begun to loose any light...")
    typing("There are no birds singing, no wind whistling...")
    typing("Nothing...")
    typing("\n It is time to take on the Silencer...")
    
    time.sleep(0.5)
    
    boss_fight()
    
    os.system("killall afplay")    

