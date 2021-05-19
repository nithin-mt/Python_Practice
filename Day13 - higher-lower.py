from art import logo
from art import vs
from game_data import data
import random
import replit


def compare(a,b):
  if a >= b:
    return "a"
  elif a < b:
    return "b"


def option():
  opt = random.choice(data)
  return opt

game_over = False
score = 0



A = option()

while game_over == False:

  print(logo)
  
  B = option()

  a = A['follower_count']
  b = B['follower_count']



  print(f"\nCompare A : {A['name']}, {A['description']}, {A['country']}  followers : {A['follower_count']}\n")

  print(vs)

  print(f"\nAgainst B : {B['name']}, {B['description']}, {B['country']}  followers : {B['follower_count']}\n")

  ans = input("Who has more followers? : Type 'A' or 'B' :  ").lower()


  if compare(a,b) == ans:
    score += 1
    A = B
    replit.clear()
    print(f"You're right! Current Score : {score}")
  else:
    replit.clear()
    print(f"Sorry that's wrong. Final Score : {score}")
    game_over = True

