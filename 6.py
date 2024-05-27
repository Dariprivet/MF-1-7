m = 10
A = [-3, 2, 5, -1, 0, 4, 7, -5, 2, 1]

print("Исходный массив A:", A)

positive_numbers = [num for num in A if num > 0]
if len(positive_numbers) > 0:
    min_positive = min(positive_numbers)
    min_positive_index = A.index(min_positive)
else:
    min_positive = None
    min_positive_index = None

print("Минимальный положительный элемент:", min_positive)
print("Индекс минимального положительного элемента:", min_positive_index)
print("Количество положительных элементов:", len(positive_numbers))
