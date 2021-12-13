#Write a function to return the minimum number of coins needed to sum up a given 
#amount of cash using only Rs. 5, Rs. 2 and Rs. 1 coins.
#If you input 9 to the function, it should print 
#1 - Rs. 5 coins , 2 - Rs. 2 coins , 0 - Rs. 1 coins


def check_coins(amount):
    five = amount // 5
    five_rem = amount % 5

    two = five_rem // 2
    two_rem = five_rem % 2

    one = two_rem // 1

    print(five, "- Rs. 5 coins,", two, "- Rs. 2 coins,", one, "- Rs. 1 coins")


amount = int(input("Enter amount: "))
check_coins(amount)