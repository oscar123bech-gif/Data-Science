import numpy as np
import random

list = [1,3,7,3,53]
print (type(list))
a = np.array(list)
print(type(a))
print(a)
print(a+1)
b = np.zeros(5)
print(b)
c = np.array([1,3,35,7,4],dtype="f")
print(c)
d = np.array([[2,5],[23,8]])
print(d)
print(d.ndim)
print(d.size)
e = np.arange(1,100)
print(e)
f = np.arange(1,100,2)
print(f)
g = np.random.permutation(np.arange(1,100))
print(g)
h = np.random.rand(2,3)
print(h)
j = np.arange(0,6).reshape(2,3)
print(j)








# for i in range(5):
#     print(list[i])





# list.append (3)
# print (list)
# print (list[3])
