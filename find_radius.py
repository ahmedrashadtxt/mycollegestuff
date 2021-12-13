#Find the radius of a circle from Area given
import math

def find_area(n):
    print("User input value is", n)
    r = math.sqrt(n/math.pi)
    print("Radius is", r)
    return r

user_input = int(input("Enter Area of circle: "))
find_area(user_input)
