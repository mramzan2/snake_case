import random
import numpy as np
from datetime import datetime



## PYTHON LOOP

def random_number(num):
    return [round(random.uniform(0,100),3) for i in range(num)]
list_loop = random_number(100)
print('loop_number:',random_number(100))
start_time_1= datetime.now()
end_time_1 = datetime.now()
print("Loop time:", end_time_1 - start_time_1)

## NUMPY

def random_number(num):
    return np.round(np.random.uniform(0,100,num),3)
list_numpy = random_number(100)
print('numpy_number:',random_number(100))
start_time_2 = datetime.now()
end_time_2 = datetime.now()
print("NumPy time:", end_time_2 - start_time_2)

##Numpy is faster than the Python loop

