num = int(input("Enter a number: "))
factorial = 1
number = []

def trailing_zero(factorial):
    factorial_string = str(factorial)
    zero_count = 0
    str_reversed = factorial_string[::-1]
    for i in str_reversed:
        if (str_reversed[int(i)] == "0"):
            zero_count = zero_count+1
        else:
            break


    print(zero_count)


if (num < 0):
    print("Factorial does not exist for negative number")
elif (num == 0):
    print("Factorial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("Factorial of ",num, "is ",factorial)
    trailing_zero(factorial)