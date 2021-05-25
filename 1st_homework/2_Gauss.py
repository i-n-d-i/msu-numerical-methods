import numpy as np
import matplotlib.pyplot as plt
import time

def conversions(A, f, n):      #приводим матрицу А к верхнетреугольному виду
    for k in range(n):
        A[k] = A[k] / A[k][k]
        f[k] = f[k] / A[k][k] 
        
        for i in range(k + 1, n):
            A[i] = A[i] - A[k] * A[i][k]
            f[i] = f[i] - f[k] * A[i][k]
            A[i][k] = 0
    return A, f

def solution(A, f, n):
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = f[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
    return np.array(x)


n = int(input())
time_start = time.time()
A = np.random.rand(n, n)
print("***Матрица А***")
print(A, end = '\n\n')
f = np.random.rand(n)
print("***Вектор f***")
print(f, end = '\n\n')
A, f = conversions(A, f, n)
u = np.arange(0, n)
x = solution(A, f, n)
y = np.linalg.solve(A, f)
print("***Вектор x***")
print(x)
print("***Проверка решения***")
print(y)
time_stop = time.time()
print("Time")
print(time_stop - time_start)

plt.plot(u, x, label = "My answer")
plt.plot(u, y, label = "True answer")
plt.legend(loc = "upper right")
plt.show()
