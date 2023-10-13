import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math, random

start=1
fin=100
dice=random.SystemRandom()

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

def single_test(n,a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
    if pow(a, exp, n) == 1:
        return True
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1
    return False
def probabilistic_prime_test(n, k=20):
    for i in range(k):
        a = dice.randrange(2,n-1)
        if not single_test(n,a):
            return False
    return True

def prime_list_maker(s,f):
    prime_list=[]
    for i in range(s,(f+1)):
        if deterministic_prime_test(i):
            prime_list.append(i)
        if i % 1000000 == 0:
            print(i / 1000000)
    return prime_list

primes=prime_list_maker(start,fin)

X = []
y_gammalog = []
y_log = []

Pi=[i for i in range(1,int(len(primes)+1))]
print(Pi[-1])

for i in range(0,int(fin+1),1):
    X.append(i)
    log =i / np.log(i)
    gammalog=1.1229*log
    y_gammalog.append(gammalog)
    y_log.append(log)
    if i%100000==0:
        print(i/100000)


mpl.style.use("fast")
mpl.rcParams["path.simplify"]=True
mpl.rcParams["path.simplify_threshold"]=0.9
plt.plot(primes, Pi, label="π(x)")
plt.plot(X, y_gammalog, label=r"$2e^{-\gamma}x/\ln(x)$")
plt.plot(X, y_log, label="x/ln(x)")
plt.legend(fontsize=15,frameon=False,ncol=3,loc="upper left")
plt.show()