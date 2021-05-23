#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random
# Allow the player to submit a guess for a number between 1 and 100.
print(logo)
print("\nWelcome to the Number Guessing Game! \n")
print("I'm thinking of a number between 1 and 100. \n")

com_num = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == "easy":
  num = 10

elif difficulty == "hard":
  num = 5

while num >= 0:
  print(f"You have {num} attempts remaining. \n")
  if num == 0:
    print("You've run out of guesses. You lose. \n")
    num = -1
  else:
    u_guess = int(input("Make a Guess : "))

    if u_guess > com_num:
      print("Too high.")
      num -= 1
    elif u_guess < com_num:
      print("Too Low.") 
      num -= 1
    elif u_guess == com_num:
      print(f"You got it!!. The answer was {com_num}.\n")
      num = -1  

  

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

