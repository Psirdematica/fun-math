# import numpy as np
A = [[20, 15, 10, 45], [-3, -2.249, 7, 1.751], [5, 1, 3, 9]]
# A = np.array([[20, 15, 10], [-3, -2.249, 7], [5, 1, 3]])

b = [[45], [1.751], [9]]

x = 3
y = 4
A1 = []
for val in A[0]:
    A1.append(val/20)
print(A1)
A[0] = A1
print(A)
R2 = abs(A[1][0])
R3 = abs(A[2][0])
print(R2, R3)
for i in range(x):
    for j in range(y):
        if i == 1:
            A[i][j] = A[i][j] + R2*A[i-i][j]
        elif i == 2:
            A[i][j] = A[i][j] - R3*A[i-i][j]
R4 = abs(A[1][1])
A1 = []
for val in A[1]:
    A1.append(val/R4)
print(A1)
A[1] = A1
print(A)

R3 = abs(A[2][1])
print(R2, R3)
for i in range(x):
    for j in range(y):
        if i == 2 and j > 0:
            A[i][j] = A[i][j] + R3*A[i-i+1][j]
print(A)


x = '\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in A])
print(x)


x3 = A[-1][-1]/A[-1][-2]
x2 = A[-2][-1] - (A[-2][-2]*x3)
x1 = A[-3][-1] - (A[-3][-2]*x2) - (A[-3][-3] * x3)
print(x1, x2, x3)
