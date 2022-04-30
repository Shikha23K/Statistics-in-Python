#Geometric RV Trials : No. of trials untill getting first required outcome. 
#Ex: keep tossing coin until geting the first Head
#Let if X=3(on third toss get head,after two Tail),let p=.7,q=.3
#then P(X=3)=q*q*p => 0.3*0.3*0.7

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
def BernoulliRV(p=.5):
    r=np.random.rand()
    X=int(r<=p)
    return X
def geometricTrial(p):
    X=1
    while True:
        if(BernoulliRV(p)==1):
            return X
        else:
            X+=1

n=10000
#the probability decrease the no of trials needed to be more and the frequency of first head also decreases
P=0.2
G=np.zeros(n)
for i in range(n):
    G[i]=geometricTrial(P)
#sns.displot(G)
plt.hist(G,density=True,color='cyan')
#sns.kdeplot(G,shade=True)
plt.show()
