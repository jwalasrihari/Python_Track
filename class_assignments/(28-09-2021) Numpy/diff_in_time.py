#PROGRAM       : Difference between time of execution from list and numpy array
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 28-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None

import numpy as np
import sys
import time
def list_type():
    temp = range(2000)
    res = np.arange(2000)
    print(sys.getsizeof(10)*len(temp))
    print(res.size*res.itemsize)
list_type()

