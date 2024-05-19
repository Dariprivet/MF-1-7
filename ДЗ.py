import numpy as np

G = int(input('Введи номер столбца: '))
S = int(input('Введи номер строки: '))
N = 3
p = 2 * (S + G)
m = -p + S
A = [[p, m, 2*S], [m, 2*p+S, m], [2*S, m, p]]
A = np.array(A) / 6
print('Исходный массив A')
for i in range(N):
    for j in range(N):
        print('%6.3f' % A[i][j], end='')
    print('')
L, X = np.linalg.eig(A)
print('\nСобственные значения A:')
print(L)
print('\nСобственные векторы A:')
for i in range(N):
    for j in range(N):
        print('%6.3f' % A[i][j], end=' ')
    print('')
