import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5.1, 0.1)

y1 = x
y2 = x*x
y3 = x*x*x

plt.plot(x, y1, label="y = x", linestyle="-")
plt.plot(x, y2, label="y = x^2", linestyle="--")
plt.plot(x, y3, label="y = x^3", linestyle=":")

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.title("Polynomial Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()