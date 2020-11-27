matrix1=[]
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
print("Enter elements of first matrix: ")

for i in range (n):
    row=[]

    for j in range(0,m):
        e = int(input())
        row.append(e)
    matrix1.append(row)


matrix2=[]

print("Enter elements of second matrix:")

for i in range (0,n):
    row=[]
    for j in range(0,m):
        e = int(input())
        row.append(e)
    matrix2.append(row)


import numpy as np
a = np.array(matrix1)
b = np.array(matrix2)
c = a + b
print("Sum of matrices: ",c)
c = a * b

print("Element wise product of matrices: ",c )

c = np.transpose(a)
print("Transpose of a: ", c)
c = np.dot(a, b)
print("multiplication of matrices: ", c)
