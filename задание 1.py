import random

def generate_matrix(rows, cols, min_val=-100, max_val=100):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def add_matrices(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("Матрицы должны иметь одинаковую размерность для сложения!")

    rows = len(matrix_1)
    cols = len(matrix_1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]

    return result

def print_matrix(matrix, name="Матрица"):
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()  

ROWS = int(input("Введите количество строк: "))
COLS = int(input("Введите количество столбцов: "))

matrix_1 = generate_matrix(ROWS, COLS)
matrix_2 = generate_matrix(ROWS, COLS)

print_matrix(matrix_1, "Матрица 1 (сгенерированная)")
print_matrix(matrix_2, "Матрица 2 (сгенерированная)")

matrix_3 = add_matrices(matrix_1, matrix_2)

print_matrix(matrix_3, "Матрица 3 (результат сложения Matrix_1 и Matrix_2)")
