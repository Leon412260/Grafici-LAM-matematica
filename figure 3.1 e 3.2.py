import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

r=150
ln = []
H_n = [0]
X = []

for i in range(r):
    ln.append(np.log(i+1))
    H_n.append(H_n[i]+1/(i+1))
    X.append(i+1)
    if i%10000==0:
        print(i)
H_n.pop(0)

gamma = str(round(H_n[-1]-ln[-1], 7))
ox,oy=[],[]

fig,ax = plt.subplots()
"""
mpl.style.use("fast")
mpl.rcParams["path.simplify"]=True
mpl.rcParams["path.simplify_threshold"]=0
plt.ticklabel_format(useMathText=True)
ax.plot(ox, oy, label="γ="+gamma, color="white")
ax.plot(X, ln, markevery=1, label="ln(x)")
ax.plot(X, H_n, markevery=1, label=r"$H_n$
"""
plt.subplot(211)
plt.scatter(X[1:30], H_n[1:30], label=r"$H_n$", s=25)
plt.legend(fontsize=15,frameon=False)
plt.subplot(212)
plt.scatter(X, H_n, label=r"$H_n$", s=0.5)
plt.legend(fontsize=15,frameon=False)

ax.legend(fontsize=15,frameon=False,ncol=3,loc="lower right")
plt.show()