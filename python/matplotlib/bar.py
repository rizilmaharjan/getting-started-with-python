from matplotlib import pyplot as plt
from matplotlib import style



x1 = [5,3,4]
y1 = [10,3,5]

x2 = [3,8,9]
y2 = [10,2,9]

plt.bar(x1,y1,color = "green",linewidth = 3)

plt.bar(x2,y2,linewidth = 3)

plt.title("information")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")
plt.legend()
plt.show()