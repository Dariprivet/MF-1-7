x = [5,6,7,13,13,11,10,9,8,2,2,2,4]
y = [4,7,7,15,17,11.5,10,8,6.5,1,3,4] 
sum_x = sum_y = sum_xy = sum_x_squared = 0
for i in range(12):
    sum_x += x[i]
    sum_y += y[i]
    sum_xy += x[i] * y[i]
    sum_x_squared += x[i] ** 2
a = (12 * sum_xy - sum_x * sum_y) / (12 * sum_x_squared - sum_x ** 2)
b = (sum_y - a * sum_x) / 12
print(f"y = {a}x + {b}")
