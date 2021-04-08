
#Imports
import os
import turtle
import time
import random
os.system("clear")

#Window Setup
#wn = turtle.Screen()
#wn.title("SCHERZO")
#wn.bgcolor("#227570")
#wn.setup(800, 600)
#wn.tracer(0)

#typing function
def typing(text):
  words = text
  for char in words:
    time.sleep(0.1)
    print(char, end='', flush=True)
    
##Create Pen
#pen = turtle.Turtle()
#pen.color("#00eb27")
#pen.speed(0)
#pen.penup()
#pen.goto(0, 250)
#pen.hideturtle()
#pen.write("Score: 200", move=False, align="center", font=("Courier New", 32, "normal"))


#Define Classes
#class Player():
#    def __init__(self, lives, money, music_notes, weapon, armour):
#        self.lives = 3
#        self.money = 12
#        self.music_notes = 0
#        self.weapon = weapon
#        self.armour = armour

#class Enemy():
#    def __init__(self, lives, weapon, armour):
#        self.lives = 2
#        self.weapon = weapon
#        self.armour = armour

#class Boss(Enemy):
#    def __init__(self, lives, weapon, armour):
#        Enemy.__init__(self, lives, weapon, armour)
            
#        self.lives = lives
    #if music_notes > 5 boss_lives = 5
    #if music_notes > 7 boss_lives = 3
    #if music_notes > 10 boss_lives = 1
 #       self.money = money
 #       self.music_notes = music_notes
 #       self.weapon = weapon
 #       self.armour = armour

#class Armour():
 #   def __init__(self, lives, music_notes):
 #       self.lives = lives
 #       self.music_notes = lives

#class Weapon():
 #   def __init__(self, lives, music_notes):
 #       self.lives = lives
  #      self.music_notes = music_notes
        


#Show Splash Screen
print("\nSCHERZO")
print("Collect music notes to save the world from monsters.\n")
time.sleep(3.5)
os.system("clear")

#Keyboard Bindings
#wn.listen()
#wn.onkeypress(select the option, "Enter")
#wn.onkeypress(move left, "Left")
#wn.onkeypress(move right, "Right")

player_money = 12
player_lives = 3
player_music_notes = 0

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
        #the battle stuff begins here
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
        

