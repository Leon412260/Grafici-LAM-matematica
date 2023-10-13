import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

r=10**6
X = []
x = []
reciprocals = [0]
ln_ln = []
prod_p = [0]

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
        reciprocals.append(reciprocals[-1] + 1 / (i + 1))
        #prod_p.append(prod_p[-1]-np.log(1-1/(i+1)))
        X.append(i+1)
        ln_ln.append(np.log(np.log(i+1)))
    if i%10000==0:
        print(i)
reciprocals.pop(0)
prod_p.pop(0)

miessel_mertens = str(round(reciprocals[-1]-ln_ln[-1], 6))
#d=str(round(-reciprocals[-1]+prod_p[-1], 5))

ox,oy=[],[]
mpl.style.use("fast")
mpl.rcParams["path.simplify"]=False
mpl.rcParams["path.simplify_threshold"]=0
plt.ticklabel_format(useMathText=True)
plt.plot(ox, oy, label="M="+miessel_mertens, color="white")
plt.plot(X, ln_ln, markevery=1, label="ln(ln(x))")
#plt.plot(ox, oy, label="B="+d, color="white")
plt.plot(X, reciprocals, markevery=1, label=r"$\sum_{p \leq x}1/p$")
#plt.plot(X, prod_p, label=r"$\ln\prod_{p\leq x}\frac{1}{1-p^{-1}}$")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="lower right")
plt.show()