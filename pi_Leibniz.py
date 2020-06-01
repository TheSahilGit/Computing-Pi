'''Approximating the value of Pi by Leibniz Method'''

### Sahil Islam ###
### 01/06/2020 ###


import math
import matplotlib.pyplot as plt


piValues = []
piActual = []
iteration = []
errorPercent = []
n = 1000
for j in range(500):
    pi = 1
    s = 0
    for i in range(n):
        den = (2 * i + 1)
        s += float(((-1) ** i) / den)
    piValues.append(4 * s)
    iteration.append(n)
    piActual.append(math.pi)
    n = n + 100

for k in range(len(piValues)):
    diff = piActual[k] - piValues[k]
    err = float(diff / piActual[k])
    errorPercent.append(100 * err)

plt.subplot(2, 2, 1)
plt.plot(iteration, piValues, label="Computed Values")
plt.plot(iteration, piActual, label='Actual Value')
plt.grid()
plt.legend()
plt.xlabel("Number of iteration")
plt.ylabel("Value of Pi")
plt.title("Original Value and Computed Value Comparison Plot")


plt.subplot(2, 2, 4)
plt.plot(iteration, errorPercent)
plt.grid()
plt.xlabel("Iteration")
plt.ylabel("Percentage Error")
plt.title(" Percentage Error Vs Iteration Plot")

plt.suptitle("Approximating the value of Pi by Leibniz Method")

plt.show()
