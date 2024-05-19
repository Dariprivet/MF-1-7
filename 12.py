import math 
 # Заданные значения S и G 
S = 4
G = 7 
S = S/10 
G = G/10 
 # Коэффициенты полинома 
a0 = -S * (G**2 + S**2) 
a1 = (G + S)**2 
a2 = -(2*G - S) 
a3 = 1  # По условию задачи 
 # Функция полинома 
def f(x): 
    return a0 + a1*x + a2*x**2 + a3*x**3 
 # Производная функции полинома 
def df(x): 
    return a1 + 2*a2*x + 3*a3*x**2 
 # Метод Ньютона 
def newtons_method(f, df, x0, tolerance=0.001): 
    while True: 
        x1 = x0 - f(x0) / df(x0) 
        if abs(x1 - x0) < tolerance: 
            return x1 
        x0 = x1 
 # Начальное приближение 
x0 = 1.5  # Выбрано как середина интервала [0,3] 
 # Вызов метода Ньютона 
root = newtons_method(f, df, x0) 
 print(f"Корень полинома на интервале [0,3]: {root:.3f}")
