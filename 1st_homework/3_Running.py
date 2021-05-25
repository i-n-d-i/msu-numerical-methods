import numpy as np
import matplotlib.pyplot as plt
import time

def solution(a, b, c, f, n):
    alpha = np.array([0.0] * (n + 1))
    beta = np.array([0.0] * (n + 1))
    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i] / d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x = np.array([0.0] * n)
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x
   
n = int(input())
time_start = time.time()
A = np.ones((n,n)) * 0.0
a = np.random.rand(n)
b = np.random.rand(n)
c = np.random.rand(n)
f = np.random.rand(n)
a[0], c[n - 1] = 0, 0
print(a)
print(b)
print(c, end = '\n\n')
print(f, end = '\n\n')
for i in range(n):        #создаем трехдиагональную матрицу
    A[i][i] = b[i]
    if i > 0:
        A[i][i - 1] = a[i]
    if i < n - 1:
        A[i][i + 1] = c[i]
print(A, end = '\n\n')
u = np.arange(0, n)
x = solution(a, b, c, f, n)
y = np.linalg.solve(A, f)
print("Вектор x")
print(x)
print("Проверка решения")
print(y)

time_stop = time.time()
print("Time")
print(time_stop - time_start)

plt.plot(u, x, label = "My answer")
plt.plot(u, y, label = "True answer")
plt.legend(loc = "upper right")
plt.show()
