#if coin is biased and given P(H)=0.7,P(T)=0.3 Bernulli Random Variable generated
import numpy as np
def BernulliRV(p=.5):
    X=int(np.random.rand()<=p)
    return X
countOnes=0
countZeros=0
P=0.67122
n=10000
for i in range(n):
    x=BernulliRV(P)
    if x==1:
        countOnes+=1
    else:
        countZeros+=1    
print("Success Fraction is: ",countOnes/n)
