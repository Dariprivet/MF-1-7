import numpy as np
A = np.array([[1, 2, 3], [1, 2, 1], [3, 2, 0]]) #создание массива
B = np.array([[4, 1, 2], [0, 4, 3], [1, 1, 1]]) #создание массива
P = np.array([[0.1], [1.7], [-1.5]]) #создание массива
Q = np.array([[-1.6], [0.8], [-1.5]]) #создание массива
R = np.array([[-0.7], [1.3], [0.2]]) #создание массива
AP = np.dot(A,Q)
print ('AP =', AP)
BR = np.dot(B,R)
print ('BR =', BR)
s = np.dot(AP.flatten(),BR.flatten())
print ('s =', s)
