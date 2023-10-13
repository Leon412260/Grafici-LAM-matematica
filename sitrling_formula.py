import matplotlib.pyplot as plt
import numpy as np

def logfactorial(n):
    if n==0:
        return 0
    else:
        logfact = 0
        for i in range(n):
            logfact=logfact+np.log(i+1)
        return logfact


X = np.linspace(0, 100, 10000)
y_1 = X*np.log(X)-X+1
x = [i for i in range(101)]
y_2 = []
for i in range(101):
    y_2.append(logfactorial(i))



#plt.grid(which="minor", color="gray", alpha=0.15)
#plt.grid(which="major",color="gray", alpha=0.45)
plt.scatter(x,y_2, label="ln(n!)", color="orange")
plt.plot(X,y_1, label="xln(x)-x+1")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")
plt.show()