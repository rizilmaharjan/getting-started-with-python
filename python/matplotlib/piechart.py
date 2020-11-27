from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
slice_1 = [11,10,7,5,4,6]
activities_1 = ["facebook","Youtube","twitter","Instagram","Gallery","Other"]
cols_1 = ["cyan","green","pink","yellow","red","blue"]
slice_2 = [11,10,7,5,4,6]
activities_2 = ["facebook","Youtube","twitter","Instagram","Gallery","Other"]
cols_2 = ["cyan","green","pink","yellow","red","blue"]

plt.subplot(3,2,1)
plt.pie(slice_1,labels=activities_1,shadow=True,autopct="%1.1f%%",colors=cols_1)

plt.subplot(3,2,2)
plt.pie(slice_2,labels=activities_2,shadow=True,autopct="%1.1f%%",colors=cols_2)

plt.subplot(3,1,3)
plt.pie(slice_2,labels=activities_2,shadow=True,autopct="%1.1f%%",colors=cols_2)

plt.show()
