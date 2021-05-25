import numpy as np
import matplotlib.pyplot as plt
import time

def running(a, b, c, f, n):
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

def find_index(array, value):
    left = 0
    right = len(array) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if array[mid] >= value:
            right = mid
        else:
            left = mid
    return left

def evaluate(x, A, B, C, D, z):
    index = find_index(x, z)
    tmp = z - x[index]
    return A[index] * (tmp ** 3) + B[index] * (tmp ** 2) + C[index] * tmp + D[index]

def generate_spline(x, y):
    n = len(x) - 1 
    h = (x[n] - x[0]) / n
    a = np.array([0] + [1] * (n - 1) + [0])
    b = np.array([1] + [4] * (n - 1) + [1])
    c = np.array([0] + [1] * (n - 1) + [0])
    f = np.zeros(n + 1)
    for i in range(1, n):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / (h ** 2)
    s = running(a, b, c, f, n + 1)
    A = np.array([0.0] * (n + 1))
    B = np.array([0.0] * (n + 1))
    C = np.array([0.0] * (n + 1))
    D = np.array([0.0] * (n + 1))
    for i in range(n):
        D[i] = y[i]
        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        if i != n - 1:
            C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        else:
            C[i] = (y[i + 1] - y[i]) / h - (2 * B[i]) * h / 3
    return A, B, C, D


time_start = time.time()
inputX = open('train.dat', 'r')
inputY = open('train.ans', 'r')
inputZ = open('test.dat', 'r')
outputY = open('test.ans', 'w')

n = int(inputX.readline())
inputY.readline()
m = int(inputZ.readline())

x = np.array([float(i) for i in inputX.readline().split()])
y = np.array([float(i) for i in inputY.readline().split()])
z = np.array([float(i) for i in inputZ.readline().split()])

A, B, C, D = generate_spline(x, y)

outputY.write(str(m) + '\n')
for i in range(m):
    y_new = evaluate(x, A, B, C, D, z[i]);
    outputY.write(str(y_new) + ' ')
inputX.close()
inputY.close()
inputZ.close()
outputY.close()

time_stop = time.time()
print("Time")
print(time_stop - time_start)

outputY = open('test.ans', 'r')
outputY.readline()
y_new = [float(i) for i in outputY.readline().split()]
outputY.close()

plt.plot(x, y, label = "Данные", marker = "*")
plt.plot(z, y_new, label = "Решение", marker = "o")
plt.legend(loc = "upper left")
plt.show()
