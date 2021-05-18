
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from replit import clear
import art
import random


def ran_value():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  ran1 = random.choice(cards)
  return ran1



def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards)==2:
      return 0

    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)  
        
    return sum(cards)




def compare(user,computer):
  if user == computer:
    return "It's a Draw \n"  

  elif computer == 0:
    return "You lose, Opponent has blackjack. \n"

  elif user == 0:
    return "You win. You got blackjack. \n"  

  elif computer > 21:
    return "Opponent went over. You win. \n"

  elif user > 21:
    return "You went over. You lose. \n"

  elif user > computer:
    return "You win. \n"    
  
  else:
    return "You Lose. \n"



def blackjack():
  print(art.logo)

  ur_card = []
  com_card = []

  for _ in range(2):
    ur_card.append(ran_value())
    com_card.append(ran_value())

  is_game_over = False

  while not is_game_over:

    cur_score = calculate_score(ur_card)
    comscore = calculate_score(com_card)


    print(f"\nYour cards : {ur_card}        Your current score : {cur_score}")
    print(f"Computer's first card : {com_card[0]}")

    if cur_score == 0 or comscore == 0 or cur_score > 21:
      is_game_over = True

    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        ur_card.append(ran_value())
      else:
        is_game_over = True

  while comscore != 0 and comscore < 17:
    com_card.append(ran_value())  
    comscore = calculate_score(com_card)
      

  print(f"\nYour final hand : {ur_card}     Your final score : {cur_score}")
  print(f"Computer's final hand : {com_card}       Computer's final score : {comscore} \n")

  print(compare(cur_score, comscore) )   
         

while input("Do you wanna play a game of blackjack: Type 'y' or 'n' : ") == "y":
  clear()
  blackjack()

  












