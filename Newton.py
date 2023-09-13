import math
from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate
def divided_differences(x_values, y_values, k):
    result = 0
    for j in range(k + 1):
        nul = 1
        for i in range(k + 1):
            if i != j:
                nul *= x_values[j] - x_values[i]
        result += y_values[j]/nul
    return result


def create_Newton_polynomial(x_values, y_values):
    div_diff = []
    for i in range(1, len(x_values)):
        div_diff.append(divided_differences(x_values, y_values, i))
    def newton_polinomial(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            nul = 1
            for j in range(k):
                nul *= (x-x_values[j])
            result += div_diff[k - 1] * nul
        return result
    return newton_polinomial

x_values = [0, math.pi/6, math.pi/4, math.pi/2]
y_values = [math.cos(0) + 0, math.cos(math.pi/6) + math.pi/6, math.cos(math.pi/4) + math.pi/4, math.cos(math.pi/2) + math.pi/2]

new_pol = create_Newton_polynomial(x_values, y_values)

for x in x_values:
    print("x = {:.4f}\t y = {:.4f}".format(x, new_pol(x)))

tck = interpolate.splrep(x_values, y_values)
x = np.linspace(0, math.pi, 100)
y = interpolate.splev(x, tck)
plt.plot(x, y)
plt.show()