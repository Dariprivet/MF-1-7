def u_k(k, x):
   return (-1)**(k+1)*(x**(k + 1)/k*(k + 1))))

def calculate_S(x, n):
    S = 0
    for k in range(1, n+1):
        S += u_k(k, x)
    return S

x_values = [0.1, 0.3, 0.4, 0.7, 1.0]
n = 10

print("**********************")
for x in x_values:
    S = calculate_S(x, n)
    print(f"X={x} S={S:.2f}")
print("**********************")
