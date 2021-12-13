
def sum_list(input_list):
    sum = 0
    for i in range(len(input_list)+1):
        sum = sum + i

    return sum

my_list = [1,2,3,4,5]

print(sum_list(my_list))

#sum between 1-n, n is the parameter. Use recursion

def find_sum(n):
    if n == 1:
        return 1
    else:

        return n + find_sum(n-1)

print(find_sum(5))