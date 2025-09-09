import random
import sys
import numpy as np

#I know only for loop to generate random numbers
def random_number(num):
    return [random.uniform(0,100) for i in range(num)]
print(random_number(100))
#another way of generating random number is through Numpy,but I don't know how to use it.

