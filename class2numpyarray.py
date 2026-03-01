import numpy as np
a = np.arange (1,10)
b = a[2:6:1]
print (a)
print(b)
c = a[:5:]
print (c)
d = a[:9:2]
print(d)
e = a[::-1]
print(e)
f = np.arange(1,50).reshape (7,7)
print(f)
print(f[4:7,4:7])
print(f+1)


a1 = np.arange (1,11)
a2 = np.arange(11,22)
print(a1+a2)