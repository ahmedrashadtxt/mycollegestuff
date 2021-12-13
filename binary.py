def binary(number):
    arr = []
    while (number>0):
        num = number%2
        arr.append(num)
        number = number//2

    for i in range(len(arr)):
        print(arr[len(arr)-i-1],end="")


binary(34)

print("")

def convert_to_bin(num):
    if(num!=0):
        convert_to_bin(num//2)
        print(str(num%2),end="")

convert_to_bin(34)