A = [x for x in range(1, 12)] #элемент слева - то, что кладем в массив.Справа - цикл перебора значений от 1 до 12
#me = [] 
#for x in range(1, 16):
#    me.append(x)
b = []
for XI in range(len(A)):
    if XI % 2 == 0:
        b.append(A[XI]) # типа 2 соответствует индекс 1, поэтому ее мы добавляем в список 
    else:
        b.append(0)
print(A, b, sum(b))  
    print("Массив:", spisok)
    print("Произведение всех чисел:", product2)
    print("Сумма всех чисел:", sum(spisok))
