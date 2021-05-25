import numpy as np

def solution(A, L, U, n):
    for j in range(n):
        U[0][j] = A[0][j]
        L[j][0] = A[j][0] / U[0][0] 
        for i in range(1, n):
            for j in range(i, n):
                U[i][j] = A[i][j] 
                L[j][i] = A[j][i]
                for k in range(i):
                    U[i][j] -= L[i][k] * U[k][j]
                    L[j][i] -= L[j][k] * U[k][i]
                L[j][i] /= U[i][i]
    return L, U

n = int(input())
A = np.random.rand(n, n)
L = np.tril(np.random.rand(n, n))
U = np.triu(np.random.rand(n, n))
print("***Матрица А***")
print(A, end = '\n\n')
L, U = solution(A, L, U, n)
print("***Матрица L***")
print(L, end = '\n\n')
print("***Матрица U***")
print(U, end = '\n\n')

