import random
# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock, paper, scissors]
computer = random.randint(0,2)
user = int(input("Enter '0' for rock, '1' for paper, '2' for scissors:\n"))
if 0 <= user <= 2:
    print("You chose:\n" + game[user])

print ("Computer chose:\n" + game[computer])

if user >= 3 or user < 0:
    print("Wrong Input, You Lose!")
elif computer == 0 and user == 2:
    print("You Lose!")
elif user > computer:
    print("You Win!")
elif user == 0 and computer == 2:
    print("You Win!")
elif computer > user:
    print("You Lose!")
elif user == computer:
    print("Draw")
    