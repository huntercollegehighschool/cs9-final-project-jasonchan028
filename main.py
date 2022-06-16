"""
Name(s): Jason Chan, Sam Yaffe
Name of Project: Filtopia Adventure
"""

#we wrote this on another replit doc without realizing that that doc wouldn't be able to submit. our work was distributed equally.

#Write the main part of your program here. Use of the other pages is optional.
import random
name = input("State your character's name: ")
print("Welcome to Filtopia", name + "!" "\nIn this mystical world, your mission is to complete tasks and slay as hard as your mortal vessel can.")
def start():
  attribute = input("Choose your class! Type W for warrior or F for Filosf: ")
  if attribute == "W": 
    warrior()
  elif attribute == "F":
    filosf()
  else:
   print("Please pick a valid character class: ")
   start()
#warrior
def warrior():    
  print("Fight things. This is self explanatory. You are anti-Filosf \nYour mission is to fight Filosfs, the mystical beasts that terrorize Filtopia.")
  wealth = random.randint(0,2)
  if wealth == 0:
    money = 0
    print("You're kind of... really broke. Welp, that's just how society works. Cope harder.")
  elif wealth == 1:
    money = 100
    print("You have a decent amount of money, but you're not exactly stacked.")
  else:
    money = 100000000
    print("You're rich.")
    
  weapon = input("Welcome to the Armory. Use your allotted money to purchase a weapon. Type S for a Small Stick, B for a Bigger Stick, and G for a Bedazzled Golf Club: ")
  if weapon == "S":
    money = money
  elif weapon == "B" and money > 100:
    money -= 100
  elif weapon == "G" and money > 1000:
    money -= 1000
  else:
    weapon = input("Enter a valid option: ")
    
  warriorfight()

def warriorfight():
  warriorfight1 = input("You come across your first Filosf! It seems quite strong, with 100 health. \nWhat do you do? Type F to fight or R to run: ")
  
  if warriorfight1 == "F":
    fight()
  elif warriorfight1 == "R":
    escape()
  else:
    print("Please enter a valid input: ")

def fight():
  warriorfight2 = input("You hit the Filosf with your weapon and a tear streams down it's face as its grade drops to zero. \nYou hear the sound of an army of Filosfs rushing to your location. Type R to run or F to fight: ")
  if warriorfight2 == "F":
    trample()
  elif warriorfight2 == "R":
    escape()
  else:
    print("ENTER A VALID INPUTTTTTT")
    warriorfight2 = input("You hit the Filosf with your weapon and a tear streams down it's face as its grade drops to zero. \nYou hear the sound of an army of Filosfs rushing to your location. Type R to run or F to fight: ")
  
def escape():
  print("You coward! You run away, and make it out with a few scratches.")
  escape = input("You hear the sound of Filosfs chasing you down. Type H to hide in a hole or R to keep running: ")
  if escape == "H":
    hide()
  elif escape == "R":
    run()
  else:
    escape = input("Enter a valid input: ")
      
def trample():
  print("You were no match for the army of angry Filosofs. You got trampled. THE END.")
  move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
  if move3 == "S":
    start()
  elif move3 == "F":
   print("Goodbye! Filtopia will miss you.")
  else:
   print("That's not a valid option. The head of the Warriors is very dissappointed in you... goodbye.")
  
def hide():
  print("The group of Filosfs corner you and you walk backwards into a ditch. THE END.")
  move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
  if move3 == "S":
    start()
  elif move3 == "F":
   print("Goodbye! Filtopia will miss you.")
  else:
   print("That's not a valid option. The head of the Warriors is very dissappointed in you... goodbye.")
  
#warrior
def run():
  print("You kept on running, but the Filosfs run faster. It's time to face the Filosfs (duh duh duhhhhhh)")
  action = input("Type G to swing your weapon at it or E to enchant it with your power of song.")
  if action == "G":
    print("You swing your very powerful weapon at the beast but your hands are sweaty and it flys over your shoulder.\nOops. I don't think I have to tell you what happens next...")
  elif action == "E":
    print("You channel Billie Holiday and belt a jazz standard.\nThe Filosf is shook by your power of song and befriends you. \nIn an unconventional pairing you runaway with the Filosf and start New Filtopia. ")
  else:
    print("Enter a valid input please...")
    action = input("Type G to swing your weapon at it or E to enchant it with your power of song.")
  move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
  if move3 == "S":
    start()
  elif move3 == "F":
   print("Goodbye! Filtopia will miss you.")
  else:
   print("That's not a valid option. The head of the Warriors is very dissappointed in you... goodbye.")  
    
  
def filosf(): #filosf
  print("You are a Filosf. \nYour mission is to destroy the Warriors that terrorize Filtopia.")
  equip = input("Equip your Filosf. \nType H for stabbing horns, T for a prehensile tail, and O for dazzling overalls.")
  if equip == "H":
    horns()
  elif equip == "T":
    tail()
  elif equip == "O":
    overalls()
  else:
    equip = input("That's not a valid option. How else are you going to slay?")
#filosf horns
def horns():
  print("You have come across your first Warrior! It aims its stick at you, but seems to want to talk.")
  move1 = input("Type T to talk, S to slay it with your horns, or R to run away: ")
  if move1 == "T":
    print("ABSOLUTELY NOT! As a Filosf you MUST slay every day. #werk #werk #werk")
    move1 = input("Type T to talk, S to slay it with your horns, or R to run away: ")
  elif move1 == "S":
    print("You slay the Warrior. Its dark eyes gloss over, and it slumps to the ground as its grade drops to 0. Nice Slay!\U0001F60D")
    horns2()
  elif move1 == "R":
    print("You take off at lightning speed, your hooves stirring up dust. The Warrior stares in shock as you disappear into the horizon")
    horns2()
  else:
    move1 = input("That's not a valid option. The Warrior stares at you in confusion. Enter a valid move: ")

def tail():
  print("After swinging through the forest of Filtopia on your new tail, you come across a birdwatching Warrior.")
  move1 = input("Type T to talk, S to slay it with your tail, or R to run into the bushes and swing away: ")
  if move1 == "T":
    print("ABSOLUTELY NOT! As a Filosf you MUST slay every day. #werk #werk #werk")
    move1 = input("Type T to talk, S to slay it with your tail, or R to run into the bushes and swing away: ")
  elif move1 == "S":
    print("The Warrior lowers it's binoculars to see you swing your tail at it and knock it out of it's tree. Nice Slay! ")
  elif move1 == "R":
    tail2()
  else:
    move1 = input("Enter a valid option: ")
  tail2()
 
def overalls(): #we have to do overalls 2
  print("While checking out your new fit in a shaded lake, you see a Warrior appear behind you. It seems curious but has one hand on its stick. ")
  move1 = input("Type T to talk, S to slay it with your overalls, or R to jump into the lake and swim away: ")
  if move1 == "T":
    print("ABSOLUTELY NOT! As a Filosf you MUST slay every day. #werk #werk #werk")
    move1 = input("Type T to talk, S to slay it with your overalls, or R to jump into the lake and swim away: ")
  elif move1 == "S":
    print("It stares at you in shock as you run over at lightning speed and tear into it. The light reflects off your dazzling overalls and blinds it. Nice Slay!")
    overalls2()
  elif move1 == "R":
    ("You take off at lightning speed, your overalls getting soaked in the lake. The Warrior stares in shock as you disappear under the surface.")
    overalls2()
  else:
    move1 = input("That's not a valid option. The Warrior stares at you in confusion. Enter a valid move: ")

 #overalls2
def overalls2():
  print("You survived your first Warrior encounter! But your overalls got messed up in the lake.\nTime to go into town! ")
  move2 = input("Ves una tienda de ropa. ¿Compras un traje rojo (R), verde (V) o amarillo(A)?")
  if move2 == "R":
    print("Muy bien! Estás muy 'drippy'. Adios Filosf...")
  elif move2 == "V":
    print("Pareces un rana. Estoy riendo. Adios rana...")
  elif move2 == "A":
    print("Bienvenidos plátano! No eres un filosf más. Estoy riendo.")
  move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
  if move3 == "S":
    start()
  elif move3 == "F":
    print("Goodbye! Filtopia will miss you.")
  else:
    print("That's not a valid option. The head of the Filosfs is very dissappointed in you... goodbye.")  
#tail2
def tail2():
  print("You have made it away safely.\n While walking you stumble upon an ancient Warrior library.")
  move2 = input("Type L to turn on the lights or D to search in the dark: ")
  if move2 == "L":
    print("A large army of warriors turns towards the source of the light, staring you in the eyes. They all charge at you. YOu get trapped in the library and perish. THE END.")
    move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
    if move3 == "S":
      start()
    elif move3 == "F":
      print("Goodbye! Filtopia will miss you.")
    else:
      print("That's not a valid option. The head of the Filosfs is very dissappointed in you... goodbye.")
  elif move2 == "D":
    print("You use your prehensile tail to feel around the deserted tables. \nOh no! You knocked over a table. When you go to pick it up you discover that it is an old manuscript.\nYou have found the Lost Book of Prejudice, a prized political document from the early days of Filtopia.\nYou return to your Filosf Village and are crowned ruler.")
    move4 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
    if move4 == "S":
      start()
    elif move4 == "F":
      print("Goodbye! Filtopia will miss you.")
    else:
      print("That's not a valid option... goodbye.")
  else:
    print("Please enter a valid choice")
    move2 = input("Type L to turn on the lights or D to search in the dark: ")

def horns2():
  print("One way or another, you have made it past your first Warrior encounter. Congrats! \nBut oh no- you see another monster coming from the bushes.")
  move2 = input("Type B to burrow into a hole, S to slay it with your horns, or K to kidnap it.")
  if move2 == "B":
    print("You're kind of a coward but I guess that's okay. \n You burrow into a hole using your horns to dig, but when you settle in there a Warrior sets up camp above you. \nIts tent covers your hole and you suffocate. THE END.")
  elif move2 == "S":
    print("Your horns stab the evil Warrior and it falls to the ground in defeat. Nice Slay!")
  elif move2 == "K":
    print("Okay that's kind of unconventional but it's fine. You take the warrior home and your Filosf village ends up keeping it as a pet. \nNever thought that would happen!")
  else:
    print("Come on you know you have to enter a valid input by now")
    move2 = input("Type B to burrow into a hole, S to slay it with your horns, or K to kidnap it.")
  move3 = input("Congratulations on finishing Filtopia. Type S to return to start or F to finish.")
  if move3 == "S":
    start()
  elif move3 == "F":
    print("Goodbye! Filtopia will miss you.")
  else:
    print("That's not a valid option. The head of the Filosfs is very dissappointed in you... goodbye.")


start()