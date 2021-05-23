from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bid_info = {}
bidding = True

def highest_bid(bid_data):
  bids = 0
  winner = ""
  for name in bid_info:
    bid = bid_info[name]

    if bid > bids:
      bids = bid
      winner = name

  print(f"\n \n The winner is {winner} with a bid of {bids} \n")


while bidding == True:

  name = input("Enter your name : \n")
  bid_price = int(input("Enter your bid : \n"))

  bid_info[name] = bid_price

  users = input("Do we have other bidders? : Type 'yes' or 'no' \n")
  if users =="yes":
    clear()
  else:
    bidding = False  

    

if bidding == False:
  highest_bid(bid_info)  
