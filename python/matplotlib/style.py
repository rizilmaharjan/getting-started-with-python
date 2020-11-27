from matplotlib import pyplot as plt
from matplotlib import style



x1 = [5,3,4]
y1 = [10,3,5]

x2 = [3,8,9]
y2 = [10,2,9]

plt.plot(x1,y1,"g",label = "line one",linewidth = 3)

plt.plot(x2,y2,"c",label = "line two",linewidth = 3)

plt.title("information")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

plt.grid(True,color = "k")
plt.show()