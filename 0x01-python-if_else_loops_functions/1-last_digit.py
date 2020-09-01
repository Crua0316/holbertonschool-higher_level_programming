#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ln = number % -10
else:
    ln = number % 10
if ln > 5:
    print("Las digit of {} is {} and is greter than 5".format(number, ln))
elif ln == 0:
    print("Las digit of {} is {} and is 0".format(number, ln))
else:
    print("Las digit of {} is {} and less than 6 and not 0".format(number, ln))
