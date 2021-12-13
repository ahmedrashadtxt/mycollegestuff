string = input("Enter string: ").lower()

if (string==string[::-1]):
    print("Palindrome")
else:
    print("Nah")