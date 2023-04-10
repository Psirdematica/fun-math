import copy as cp


def gauss(A, b):
    ag_A = cp.deepcopy(A)
    row_num = len(A)
    col_num = row_num+1

    # merging matrix b with A to form Augmented matrix
    [ag_A[i].append(b[i][0]) for i in range(row_num)]

    print(f"The Given Matrix is:\n {A} \n and the solution matrix is:\n {b} ")
    print(f" The initial Augmented matrix is \n {ag_A}")

    itr = 0
    divisor = A[0][0]
    ag_A[0] = [val/divisor for val in ag_A[0]]
    print('\n')
    [print(row) for row in ag_A]

    R2, R3 = ag_A[1][0], ag_A[2][0]

    for i in range(row_num):
        for j in range(col_num):
            if i == 1:
                ag_A[i][j] = ag_A[i][j] - R2*ag_A[i-i][j]
            elif i == 2:
                ag_A[i][j] = ag_A[i][j] - R3*ag_A[i-i][j]

    print('\n')
    [print(row) for row in ag_A]

    itr = 1
    divisor = ag_A[itr][itr]
    ag_A[itr] = [val/divisor for val in ag_A[itr]]
    print('\n')
    [print(row) for row in ag_A]

    R3 = ag_A[2][1]
    for i in range(row_num):
        for j in range(col_num):
            if i == 2 and j > 0:
                ag_A[i][j] = ag_A[i][j] - R3*ag_A[i-1][j]

    print('\n')
    [print(row) for row in ag_A]

    i = 0
    while i < row_num:
        b[i][0] = ag_A[i].pop()
        i += 1

    print("\nThe row echelon form of the augmented matrix is:")
    [print(row) for row in ag_A]
    print('\n')
    [print(row) for row in b]

    x3 = b[2][0]/ag_A[-1][-1]
    x2 = b[1][0] - (ag_A[-2][-1]*x3)
    x1 = b[0][0] - (ag_A[-3][-1]*x2) - (ag_A[-3][-2] * x3)

    # soln = [round(x1, 4), round(x2, 4), round(x3, 4)]
    return x1, x2, x3


A = [[20, 15, 10],
     [-3, -2.249, 7],
     [5, 1, 3]]

b = [[45],
     [1.751],
     [9]]


B = [[25, 5, 1],
     [64, -8, 1],
     [144, 12, 1]]

c = [[106.8],
     [177.2],
     [279.2]]
print(gauss(B, c))
