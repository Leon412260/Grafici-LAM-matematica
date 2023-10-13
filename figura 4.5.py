import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as mpl

r=2000

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

P=[]
X=[]
e_gamma=[0.56146,0.56146]
x=[1,r+1]

p=1
for i in range(2,r+1):
    if deterministic_prime_test(i)==1:
        p*=1-1/i
        P.append(np.log(i)*p)
        X.append(i)


plt.plot(x, e_gamma,"--", label=r"$e^{-\gamma}$")
plt.plot(X, P, label=r"$\ln(x)\prod_{p\leq x}1-\frac{1}{p}$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="lower right")
plt.ylim(0.4,0.57)
plt.show()