import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

X = np.linspace(1, 10, 100)
Y = 1/X
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,0.5,1/3,0.25,0.2,0.167,0.143,0.125,0.111]
x_1 = [1,2,3,4,5,6,7,8,9,10]
y_1 = [0.5,1/3,0.25,0.2,0.167,0.143,0.125,0.111,0.1]

plt.plot(X,Y,label="1/x")
plt.fill_between(X,Y,0,color="blue",alpha=0.25)
plt.stairs(y,x, hatch="//", label=r"$H_n$")
plt.xlim(1,10)
plt.ylim(0,1.1)
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper right")


plt.plot(X,Y, label="1/x")
plt.fill_between(X,Y,0,color="blue",alpha=0.25)
plt.stairs(y_1,x_1, hatch="//", label=r"$H_{n+1}$")
plt.xlim(1,10)
plt.ylim(0,1.1)
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper right")

plt.show()


