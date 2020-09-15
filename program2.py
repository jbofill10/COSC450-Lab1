import random
import pprint
def run_matrix_mul():
    pp = pprint.PrettyPrinter()
    cols = random.randint(2,8)
    rows = random.randint(2,8)
    matrix_a = [[0 for i in range(cols)] for j in range(rows)]
    matrix_b = [[0 for i in range(cols)] for j in range(rows)]
    matrix_c = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix_a[i][j] = random.randint(1,30)
            matrix_b[i][j] = random.randint(1,30)
    print("Matrix A:")
    pp.pprint(matrix_a)
    print()
    print('Matrix B:')
    pp.pprint( matrix_b)
    print()
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):

                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    print('Matrix after multiplying matrix A * matrix B:')
    pp.pprint(matrix_c)
    
if __name__ == "__main__":
    run_matrix_mul()