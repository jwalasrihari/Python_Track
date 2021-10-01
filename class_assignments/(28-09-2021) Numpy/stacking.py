#PROGRAM       : Concatenation on two numpy array vertically and horizantally
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 28-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None


import numpy as np
array_1 = np.array([(23, 56,89),(67,99,56)])
array_2 = np.array([(89,25,69),(890,123,5689)])
vert = np.vstack((array_1, array_2))
horz = np.hstack((array_1, array_2))
print(vert)
print(horz)
