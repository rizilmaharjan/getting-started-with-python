from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

days = np.arange(1,11)
sleeping = [3,2,1,1,1,2,2,3,1,1]
eating = [5,10,3,5,3,3,6,7,8,8]
xolne = [2,3,1,1,1,2,4,2,2,1]
exercise = [3,2,1,4,5,2,2,1,3,4]
gaming = [8,7,8,9,5,4,3,6,7,8]


plt.stackplot(days,sleeping,eating,xolne,exercise,gaming,colors=["g","r","w","k","m"])
plt.title("10 days routine")
plt.xlabel("days")
plt.ylabel("activity")
plt.show()