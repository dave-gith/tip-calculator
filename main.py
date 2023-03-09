#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


# Welcome Message
print("Welcome to the tip calculator!")

# The whole bill to be paid excluding tip
total_bill = float(input("What is the total bill? $"))

# calculating the tip
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip = (tip_percentage / 100) * total_bill

# Splitting the bill
num_of_people = int(input("How many people to split the bill? "))
amount = (total_bill + tip) / num_of_people
final_amount = '{:.2f}'.format(amount)

# Final amount to be paid by each
print(f"Each person should pay: {final_amount}")
