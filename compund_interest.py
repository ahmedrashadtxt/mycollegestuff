
P = float(input("Enter principle amount: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter no. of time period elapsed: "))


def compound_interest(P, r, t):
 
    # Calculates compound interest
    Amount = P * (pow((1 + r / 100), t))
    CI = Amount - P 
    print("Compound interest is", CI)

compound_interest(P,r,t)