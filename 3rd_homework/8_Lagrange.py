import numpy as np
import matplotlib.pyplot as plt
import time

def Lagrange(x, y, z):
    y_new = 0.0
    n = len(x)
    for i in range(n):
        if z == x[i]:
            return y[i]
    for i in range(n):
        phi = 1.0
        for j in range(n):
            if i != j:
                phi = phi * (z - x[j]) / (x[i] - x[j])
        y_new = y_new + y[i] * phi     
    return y_new


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

outputY.write(str(m) + '\n')
for i in range(m):
    y_new = Lagrange(x, y, z[i])
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
