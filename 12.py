def f(x):
 return-260+121*x-12*x**2+x**3
def bisection_method(a, b, epsilon):
    while (b - a) >= epsilon:
        c = (a + b)/2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b)/2
a = 0
b = 3
epsilon = 0.001
root = bisection_method(a, b, epsilon)
print("Корень полинома на отрезке [0,3] методом половинного деления:", root)
