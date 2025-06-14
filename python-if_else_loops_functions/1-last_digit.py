#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number} is {number%10} and"
if n % 10 > 5:
    print(str + " is greater than 5")
elif n%10 == 0:
    print(str + " and is 0")
else:
    print(str + " is less than 6 and not 0")
