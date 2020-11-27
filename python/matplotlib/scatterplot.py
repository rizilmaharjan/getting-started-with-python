from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = np.arange(1,5)
y = np.arange(6,10)

plt.scatter(x,y, color="r", label = "skitscat")
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatterplot")
plt.legend()
plt.show()