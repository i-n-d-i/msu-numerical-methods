import numpy as np
import matplotlib.pyplot as plt

def solve(A, f, n, eps):
    x_new = [0] * n
    x_old = np.random.rand(n)
    while diff(x_old, x_new, n) > eps:
        x_old = x_new
        x_new = Seidel(A, f, x_old, n)
    return x_new
        
def Seidel(A, f, x_old, n):
    x_new = [0] * n
    for i in range(n):
        Sum = 0
        for j in range(i - 1):
            Sum = Sum + A[i][j] * x_new[j]
        for j in range(i + 1, n):
            Sum = Sum + A[i][j] * x_old[j]
        x_new[i] = (f[i] - Sum) / A[i][i]
    return x_new

def diff(x1, x2, n):
    Sum = 0
    for i in range(n):
        Sum = Sum + (x1[i] - x2[i]) ** 2
    Sum = Sum ** 0.5
    return Sum
        

n = int(input())
A = np.random.rand(n, n)
for i in range(n):
    Sum = 0
    for j in range(n):
        Sum = Sum + abs(A[i][j])
    A[i][i] = Sum + 1
print(A, end = '\n\n')
f = np.random.rand(n)
print(f, end = '\n\n')
u = np.arange(0, n)

x = solve(A, f, n, 0.000001)
print("Решение:")
print(x, end = '\n\n')

y = np.linalg.solve(A, f)
print("Проверка решения:")
print(y)

plt.plot(u, x, label = "My answer")
plt.plot(u, y, label = "True answer")
plt.legend(loc = 'upper left')
plt.show()
