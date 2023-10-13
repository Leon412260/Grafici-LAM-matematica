import xmlrpc.client

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math, random

r=100000
p=r/100

def deterministic_prime_test(n):
    if n <=4:
        if n==1 or n==0 or n==4:
            return 0
        else:
            return 1
    else:
        if n%2==0:
            return 0
        for i in range(3,int(math.ceil(np.sqrt(n))+1),2):
            if n%i==0:
                return 0
    return 1

Pi=[0]
x=[0]

for i in range(r+1):
    print(i/p)
    if deterministic_prime_test(i)==1:
        Pi.append(i)
        x.append(x[-1]+1)
    else:
        x.append(x[-1])
        Pi.append(Pi[-1])
x.pop(0)

plt.subplot(2,2,1)
plt.stairs(x[0:10],Pi[0:11], label=r"$\pi(x)$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")
plt.subplot(2,2,2)
plt.stairs(x[0:100],Pi[0:101], label=r"$\pi(x)$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")
plt.subplot(2,2,3)
plt.stairs(x[0:1000],Pi[0:1001], label=r"$\pi(x)$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")
plt.subplot(2,2,4)
plt.stairs(x[0:100000],Pi[0:100001], label=r"$\pi(x)$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")

plt.show()