import numpy as np
array_1 = np.array([(23, 56,89),(67,99,56)])
array_2 = np.array([(89,25,69),(890,123,5689)])
vert = np.vstack((array_1, array_2))
horz = np.hstack((array_1, array_2))
print(vert)
print(horz)