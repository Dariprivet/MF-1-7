def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix
def find_min_in_column(matrix):
    min_value = float(' inf')
    min_index = -1
    for i in range(len(matrix)):
        sum_=0
        for j in range(len(matrix[i])):
            #print(matrix[i][j])
            sum_+=abs(matrix[i][j])
        #print(sum_ ,'- сумма')
        if sum_< min_value:
            min_value = sum_
            min_index = i
    return min_value, min_index
def sum_of_abs_elements(row):
    return sum(abs(x) for x in row)
file_path = 'Kirill.txt'
matrix = read_matrix_from_file(file_path)
min_value, min_index = find_min_in_column(matrix)
print (f"Элементы с наименьшей суммой: {matrix[min_index]}")=' ')
    print('')
