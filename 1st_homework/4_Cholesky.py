import numpy as np
import time

def solution(A, f, n):
    x = [0] * n
    for i in range(n):
        x[i] = f[i]
        for j in range(i):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return np.array(x)
 
def conversions(A, n):                    # A = S * S^t
    S = np.ones((n, n)) * 0.0
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                Sum = 0
                for k in range(i):
                    Sum = Sum + S[i][k] ** 2
                S[i][i] = (A[i][i] - Sum) ** 0.5
            else:
                Sum = 0
                for k in range(j):
                    Sum = Sum + S[i][k] * S[j][k]
                S[i][j] = (A[i][j] - Sum) / S[j][j]
    return S

def positive(A, n):          
    for i in range(n):
        Sum = 0
        for j in range(n):
            Sum = Sum + abs(A[i][j])
        A[i][i] = Sum + 1
    return A

n = int(input())
time_start = time.time()
A = np.random.rand(n, n)
f = np.random.rand(n)
A = positive(A, n)

S = conversions(A, n)
print(S, end = '\n\n')
M = np.linalg.cholesky(A)
print(M, end = '\n\n')
 
y = solution(S, f, n)
S.transpose()
x = solution(S, y, n)
print(x)
time_stop = time.time()
print("Time")
print(time_stop - time_start)

