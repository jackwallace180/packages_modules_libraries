# from random import *        this imports all methods
from random import random, randrange   #only importing the methods you want
import math
import time

print(random())

print(randrange(5,50,5))

# libraries that come built into python, you need to import them
# they are maintained by python organisation , they are very stable and considered vanilla python
# https://docs.python.org/3/library/random.html   random function readme

num = 24.64

print(math.ceil(num))
time.sleep(60)
print(math.floor(num))
time.sleep(1)
print(math.pi)


