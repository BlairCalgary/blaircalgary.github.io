# receive 3 arguments from command line
from sys import argv

# unpack arguments
script, a, b, c = argv

# define functions
def largest_of_two_max(a, b):
    x = max(a, b)
    return x

def largest_of_two_ifelse(a, b):
    if a > b:
        return a
    else:
        return b

def smallest_of_three_min(a, b, c):
    x = min(a, b, c)
    return x

def smallest_of_three_ifelse(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c

# query user
print(f"a = {a}, b = {b}, c = {c}")
print("Do you want to use these values or enter new ones?")
print("Type 'n' to use new. Press 'enter' to accept these.")
answer = input("> ")

# evaluation user input
if answer == "n":
    a = int(input("Enter new value for 'a':")) # receives user input and converts string to integer
    b = int(input("Enter new value for 'b':"))
    c = int(input("Enter new value for 'c':"))

# print results
print(f"The largest value between 'a' and 'b' is {largest_of_two_max(a, b)}, using the 'max' function.")
print(f"The largest value between 'a' and 'b' is {largest_of_two_ifelse(a, b)}, using the 'if/else' function.")
print(f"The smallest value of all three is {smallest_of_three_min(a, b, c)}, using the 'min' function.")
print(f"The smallest value of all three is {smallest_of_three_ifelse(a, b, c)}, using the 'if/else' function.")
