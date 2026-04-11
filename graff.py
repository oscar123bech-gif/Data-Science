import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 4, 8, 16]
y = [2, 4, 8, 16, 32]
plt.plot(x,y)
plt.show()
plt.plot(x,y,"r--")
plt.show()
plt.plot(x,y, label = "y = 2x" )
plt.axis([1,43,2,83])
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Plot")
plt.legend()
plt.show()
plt.plot([2,4,8,16],[4,8,16,32],"g-", label = "y=2x")
plt.plot([2,4,8,16],[16,8,4,2], "b-", label = "backwards")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("backwards")
plt.legend()
plt.show()


a = np.arange (1,10,0.2)
print(a)

y1 = a * a
y2 = a * a * a
plt.plot(a,y1, "r-" , a,y2, "r--",)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("cubed and squared")
plt.legend()
plt.show()

plt.bar([5,10,20,40],[10,20,40,80],color = "green")
plt.show()
