import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0.0001, 0.75, 1000)
y_1 = np.log(1/X +1)
y_2 = -np.log(X)+X
y_3 = -np.log(1-np.exp(-X))+X


#plt.grid(which="minor", color="gray", alpha=0.15)
#plt.grid(which="major",color="gray", alpha=0.45)
plt.plot(X,y_1, label="ln(1/x + 1)" )
plt.plot(X,y_2, label="-ln(x)+x" )
plt.plot(X,y_3, label=r"$-\ln(1-1/e^x)+x$" )
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper right")
plt.show()