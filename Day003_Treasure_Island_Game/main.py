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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island\nYour mission is to find the treasure")
choise1 = input('You\'re at a cross road. weher do you want to go\nType "left" or "right"\n').lower()
if choise1 == "right":
    print("Game Over")
elif choise1 == "left":
    choise2 = input('You\'ve come to a lake, there is an island in the middle of the lake.\nType "wait" to wait for the boat or "swim" to swim accross\n').lower()
    if choise2 == "swim":
        print("Game Over")
    elif choise2 == "wait":
        color = input("You have arrived at Island unharmed. There is a house with 3 doors (red, blue, yellow)\nEnter your choise\n").lower()
        if color == "red" and color == "blue":
            print("Game Over")
        elif color == "yellow":
            print("You Win!")
        else :
            print("Wrong Choise")
    else:
        print('Wrong Choise')
else:
    print('Wrong Choise')
    