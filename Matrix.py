row = int(input("Please enter the rows"))
col = int(input("Please enter the col"))

matrix1 = []
for i in range(row):
    cols = []
    for j in range(col):
        val = int(input("Please enter the values"))
        cols.append(val)
    matrix1.append(cols)
# print(matrix1)

row = int(input("Please enter the rows"))
col = int(input("Please enter the col"))

matrix2 = []
for i in range(row):
    cols = []
    for j in range(col):
        val = int(input("Please enter the values"))
        cols.append(val)
    matrix2.append(cols)
# print(matrix2)

sumMatrix = []
for i in range(row):
    cols = []
    for j in range(col):
        val = matrix1[i][j] + matrix2[i][j]
        cols.append(val)
    sumMatrix.append(cols)
print(sumMatrix)


prdtMatrix = []
for i in range(row):
    cols = []
    for j in range(col):
        val = 0
        for k in range(row):
            val += matrix1[i][k] * matrix2[k][j]
        cols.append(val)
    prdtMatrix.append(cols)
print(prdtMatrix)
