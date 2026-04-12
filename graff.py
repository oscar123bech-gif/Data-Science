import matplotlib.pyplot as plt
import numpy as np
# x = [1, 2, 4, 8, 16]
# y = [2, 4, 8, 16, 32]
# plt.plot(x,y)
# plt.show()
# plt.plot(x,y,"r--")
# plt.show()
# plt.plot(x,y, label = "y = 2x" )
# plt.axis([1,43,2,83])
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("Plot")
# plt.legend()
# plt.show()
# plt.plot([2,4,8,16],[4,8,16,32],"g-", label = "y=2x")
# plt.plot([2,4,8,16],[16,8,4,2], "b-", label = "backwards")
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("backwards")
# plt.legend()
# plt.show()


# a = np.arange (1,10,0.2)
# print(a)

# y1 = a * a
# y2 = a * a * a
# plt.plot(a,y1, "r-" , a,y2, "r--",)
# plt.xlabel("x axis")
# plt.ylabel("y axis")
# plt.title("cubed and squared")
# plt.legend()
# plt.show()

# plt.bar([5,10,20,40],[10,20,40,80],color = "green")
# plt.bar([10,15,25,45],[20,40,80,160],color = "red")
# plt.show()

# plt.bar(["roblox", "minecraft", "fifa"],[10,100,50])
# plt.show()

# ages = [22,23,74,26,84,23,49,6,37,98,65,7,2,56,32,61,82,63,54,47,25,74,27,51,85]
# range = [10,20,30,40,50,60,70,80,90,100]


# plt.hist(ages,range,rwidth= 0.5)
# plt.show()

# x = [1,6,8,23,85,284,932,172]
# y = [2,12,16,46,170,568,1864,344]
# plt.scatter(x,y,color = "green", s = 10)
# plt.title("scatter") 
# plt.show()
# colors = ["green","red","blue","yellow","purple","orange"]
# time = [8,2,5,2,4,3]
# activity = ["sleep","eat","play","family","dog","read/netflix"]
# plt.pie(time,labels = activity,colors = colors,shadow=True)
# plt.show()
daynumber = [1,2,3,4,5]
coding = [0,0,1,0,1]
games = [21,21,20,21,20]
dog = [3,3,3,3,3]
plt.xlabel("day")
plt.ylabel("time")

plt.title("stackplot")

plt.stackplot(daynumber,coding,games,dog,labels=["coding","games","dog"])
plt.legend()
plt.show()

b = np.arange(0,5,0.1)
c = np.arange(0,25,0.5)
plt.figure()
plt.subplot(2,2,1)

plt.plot(b,c**2)
plt.subplot(2,2,2)
plt.plot(b**2,c)
plt.subplot(2,2,3)
plt.plot(b*2,c*2)
plt.subplot(2,2,4)
plt.plot(b,c)


plt.show()