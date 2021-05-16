print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

lor = input("Where do you wanna go?   Left or Right  ")
lorr = lor.lower()

if lorr == "left":
  print("You came to a lake. There is an island in middle of the lake.")
  swim = input("What do you want to do : type 'swim' for swim across or type 'wait' for wait for boat  ")
  wait = swim.lower()

  if wait == "wait":
    print("You arrived at the island unharmed.")
    doors = input("There is a house with three doors, one red, one yellow and one blue. Which one do you choose? ")
    
    door = doors.lower()
    if door == "yellow":
      print (" You enter the room of treasure!! Congrats you won!")
    elif door == "red":
      print("You entered the room of Beasts!!! Game Over!")
    elif door == "blue":
      print("You entered the room of ice!! Game Over!!")  

  else:
    print("Game Over!!")
else:
  print("Game Over!!")