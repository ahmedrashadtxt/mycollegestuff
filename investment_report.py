investment_amount = float(input("Enter the investment amount: "))
number_of_years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the rate as a %: "))
starting_balance = investment_amount
interest = starting_balance * (interest_rate / 100)

total_interest = 0
print("Year","%20s" % "Starting balance","%20s" % "Interest","%20s" % "Ending balance")

for i in range(number_of_years):
    ending_balance = starting_balance+interest
    print("%5s" % str(i+1),"%20.2f" % starting_balance,"%20.2f" % interest, "%20.2f" % ending_balance)
    starting_balance = starting_balance + interest
    total_interest =  total_interest + interest
    interest = starting_balance * (interest_rate / 100) 

print("Ending balance: $","%.2f" % ending_balance)
print("Total interest earned: $","%.2f" % total_interest)