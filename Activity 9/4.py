# Multiplication of two user defined matrices using function.
def matrix(rows, columns):
    l1 = []
    print("\n")
    for i in range(rows):
        l2 = []
        for j in range(columns):
            ele = int(input(f"Enter the {i}{j} element of Matrix: "))
            l2.append(ele)
        l1.append(l2)

    return l1

def multiplication(matrix1, matrix2, matrix3):
    for i in range(r):
        for j in range(c):
            sum = 0
            for k in range(c):
                sum += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] = sum
    return matrix3

def printMatrixForm(matrix):
    for items in matrix:
        print(items)


r = int(input("Enter the no of rows in the Matrix: "))
c = int(input("Enter the no of columns in the Matrix: "))

A = matrix(r,c)
print("\nMatrix A = ")
printMatrixForm(A)
B = matrix(r,c)
print("\nMatrix B = ")
printMatrixForm(B)
C = [[0,0,0],[0,0,0],[0,0,0]]
result = multiplication(A,B,C)
print("\nResultant Matrix C = ")
printMatrixForm(result)