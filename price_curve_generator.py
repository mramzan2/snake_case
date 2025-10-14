import sys
import random
import numpy as np
from datetime import datetime



## PYTHON LOOP using List Comprehension

def random_price_loop(num):
    return [round(random.uniform(0,100),3) for i in range(num)]

## NUMPY using List Comprehension

def random_price_numpy(num):
    return np.round(np.random.uniform(0,100,num),3)



def main():
    if len(sys.argv)<2:
        print("Usage: python price_curve_generator.py <num>")
        sys.exit(1)
    num = int(sys.argv[1])
    print(f"Generating {num} random prices....")

    start_time_1 = datetime.now()
    random_price_loop(num)
    end_time_1 = datetime.now()
    print(f"Loop time: {end_time_1 - start_time_1}")

    start_time_2 = datetime.now()
    random_price_numpy(num)
    end_time_2 = datetime.now()
    print(f"NumPy time: {end_time_2 - start_time_2}")

if __name__ == '__main__':
    main()

##Numpy is faster than the Python loop

