#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


bill_amount = input("Enter the total bill amount : ")

percentage = input ("What percentage of the bill do you want to give as tip 10, 12 or 15 : ")

billamount = float(bill_amount)
percent = float(percentage) 

tip = billamount * (percent/100)
total_amount = billamount + tip

no_of_people = input ("How many people are splitting the bill : ")

num_people = float(no_of_people)

amount_per_person = total_amount/num_people
amount_pp =round(amount_per_person, 2)

print(f"Each person should pay : {amount_pp}")
