import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def BernoulliT(n,p):
    X=(np.random.rand(n)<=p).sum()
    #True or False wil be typecasted to 1 and 0
    return X



print(BernoulliT(100,0.2))
N=10000
n=1000
P=0.612
Binomial=np.zeros(N)
for i in range(N):
    Binomial[i]=BernoulliT(n,P)
plt.hist(Binomial,density=True,bins=40)
sns.kdeplot(Binomial,shade=True,color='red')

plt.show()
