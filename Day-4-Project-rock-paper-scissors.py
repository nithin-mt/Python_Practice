rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

print("Welcome to Rock Paper Scissors! \n \n ")

mchoice = input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors \n")

mch = int(mchoice)
comchoice = random.randint(0,2)

rcp = [rock, paper, scissors]




if (mch == 0 and comchoice == 2) or (mch == 1 and comchoice == 0) or (mch == 2 and comchoice == 1):
  print("You Won!!")

elif (mch==0 and comchoice==1) or (mch==1 and comchoice==2) or (mch==2 and comchoice==0):
  print("Computer Won!!")

elif mch == comchoice:
  print("Its a draw!")

else:
  print("You typed an invalid number.")  


if (mch < 3 and mch >= 0) and (comchoice < 3 and comchoice >= 0):
  print(f"Your choice is \n {rcp[mch]}")
  print(f" Computer chooses \n {rcp[comchoice]}")

