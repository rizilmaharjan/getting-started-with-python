from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

#'price of birthday cards 
x= [13,14,15,25,32,33,28,45,42,22,33,45,50,55,60,52,61,613,70,71,73,78,100,101,130,131,122]


#range 
y=np.arange(0,141,10)

plt.hist(x,y,histtype = "bar",color = "red",label = "histogram", linewidth = 10,rwidth = 0.8)
plt.title("price of birthdaycards")
plt.xlabel("range of price")
plt.ylabel("frequency")
plt.legend()
plt.show()