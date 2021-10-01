import numpy as np
import sys
import time
def list_type():
    temp = range(2000)
    res = np.arange(2000)
    print(sys.getsizeof(10)*len(temp))
    print(res.size*res.itemsize)
list_type()

