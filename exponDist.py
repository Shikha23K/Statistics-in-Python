import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,1000)
#lmda=np.linspace(0.1,5,10)
#if take fewer and lower values
lmda=np.linspace(.1,2,4)
# as the lower the lambda lasts long
# as higher the lambda decaying fast
for i in lmda:
    fx=i*np.exp(-i*x)
    plt.plot(x,fx,label=str(i))
plt.legend()
plt.show()
