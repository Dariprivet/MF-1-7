def f(x):
    return -260+121*x-12*x**2+x**3

def integrate_trapezoidal(a, b, n):
    h = (b-a) / n  # Вычисляем шаг разбиения
    result = 0.5*(f(a)+f(b))  # Используем формулу трапеций для первого и последнего значения
    for i in range(1,n):  # Суммируем значения функции внутри интервала
        result += f(a+i*h)
    result *= h  # Умножаем сумму на шаг разбиения
    return result

a = 0  # Нижний предел интегрирования
b = 3  # Верхний предел интегрирования
n = 4  # Количество интервалов разбиения

integral = integrate_trapezoidal(a,b,n)
print("Значение интеграла:", integral)
