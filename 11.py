def f(x):
    return -260+121*x-12*x**2+x**3
def integrate_trapezoidal(a, b, n):
    h = (b-a) / n  
    result = 0.5*(f(a)+f(b))  
    for i in range(1,n): 
        result += f(a+i*h)
    result *= h  
    return result
a = 0  
b = 3  
n = 4  
integral = integrate_trapezoidal(a,b,n)
print("Значение интеграла:", integral)
