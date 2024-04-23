import numpy as np
import matplotlib.pyplot as plt

a0 = float(input("Введите a0: "))
a1 = float(input("Введите a1: "))
a2 = float(input("Введите a2: "))
a3 = float(input("Введите a3: "))
a4 = float(input("Введите a4: "))
y = lambda x:(2*x**4) + (8*x**3) + (3*x**2 - 10*x) + 2
print("y:", y)
x = np.linspace(-5, 5, 42)
print(' x y(x)')
for temp in x :
    print ( temp, y(temp))
xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')
fmax = max(y(x))
print('Ymax = ',fmax)
xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')
fmin = min(y(x))
print('Ymin = ',fmin)
fig = plt.subplots()
plt.plot(x, y(x))
