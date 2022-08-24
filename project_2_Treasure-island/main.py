print('''
                    |                    |                    |
____________________|____________________|____________________|________________
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,   ,adPPYba,
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  a8P_____88
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          8PP"""""""
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          "8b,   ,aa
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88           `"Ybbd8"'
                                                                                                                                         
                  88           88                                 88  
                  ""           88                                 88  
                               88                                 88  
                  88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
                  88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
                  88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
                  88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
                  88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
                  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

startDestination = input("You prepared yourself to go looking for treasure.\nYou are at a cross road. Where do you want to go?\nType 'left' or 'right' ").lower()

if startDestination == "left" :
  wayToIsland = input("Now, You have reached the beach.\nThere is an island in the ocean.\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
  if wayToIsland == "wait" :
    whichDoor = input("Finally after a long sailing, You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if whichDoor == "yellow" :
      print("You win!")
    elif whichDoor == "red" :
      print("Burned by fire.\nGame Over.")
    elif whichDoor == "blue":
      print("Eaten by beasts.\nGame Over.")
    else :
      print ("Game Over.")
  else:
    print("Attacked by trout.\nGame Over.")
else :
  print("Fall into a hole.\nGame Over.")   
