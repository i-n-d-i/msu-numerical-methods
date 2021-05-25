import numpy as np
import matplotlib.pyplot as plt
import time

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

def segment_build(x, y):
    n = len(x)
    k = [0.0] * (n - 1) 
    b = [0.0] * (n - 1)
    for i in range(n - 1):
        tmp = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
        k[i] = tmp
        b[i] = y[i] - x[i] * tmp
    return k, b


time_start = time.time()
inputX = open('train.dat', 'r')
inputY = open('train.ans', 'r')
inputZ = open('test.dat', 'r')
outputY = open('test.ans', 'w')

n = int(inputX.readline())
inputY.readline()
m = int(inputZ.readline())

x = [float(i) for i in inputX.readline().split()]
y = [float(i) for i in inputY.readline().split()]
z = [float(i) for i in inputZ.readline().split()]
k, b = segment_build(x, y)

outputY.write(str(m) + '\n')
for i in range(m):
    index = find_index(x, z[i])
    y_new = k[index] * z[i] + b[index]
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

    
