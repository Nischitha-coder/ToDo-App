import random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
num = random.randrange(lower, upper+1)
print(num)