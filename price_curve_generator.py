import random
import numpy as np
from datetime import datetime



## PYTHON LOOP

def random_price(num):
    return [round(random.uniform(0,100),3) for i in range(num)]
start_time_1= datetime.now()
price_curve = random_price(100)
print('price_curve:',random_price(100))
end_time_1 = datetime.now()
print("Loop time:", end_time_1 - start_time_1)

## NUMPY

def random_price(num):
    return np.round(np.random.uniform(0,100,num),3)
start_time_2 = datetime.now()
price_curve = random_price(100)
print('price_curve:',random_price(100))
end_time_2 = datetime.now()
print("NumPy time:", end_time_2 - start_time_2)

##Numpy is faster than the Python loop

