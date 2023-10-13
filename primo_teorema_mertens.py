import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

r = 10**6
X = []
Y = [0]
ln = []

def check_prime(n):
    d=int(math.ceil(np.sqrt(n)))+1
    if n==1 or n==0:
        return 0
    if n%2==0 and n!=2:
        return 0
    for i in range(int(math.ceil(np.sqrt(n)))-2):
        d-=1
        if n%d==0:
            return 0
    return 1

for i in range(r):
    if check_prime(i+1)==1:
        X.append(i+1)
        ln.append(np.log(i+1))
        Y.append(Y[-1]+np.log(i+1)/(i+1))
    if i%10000==0:
        print(i)
Y.pop(0)
R = str(round(Y[-1]-ln[-1], 6))

ox,oy=[],[]
"""
ax=plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)
"""
mpl.style.use("fast")
plt.ticklabel_format(useMathText=True)
mpl.rcParams["path.simplify"]=False
mpl.rcParams["path.simplify_threshold"]=0
plt.plot(ox, oy, label=r"$R(10^6)=$"+R, color="white")
plt.plot(X, ln, markevery=1, label="ln(x)")
plt.plot(X, Y, markevery=1, label=r"$\sum_{p\leq x}\ln(p)/p$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="lower right")
plt.show()