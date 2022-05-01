import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-20,20,10000)
m=np.arange(1,20,2)
for mu in m:
    sgma=1
    fx=np.exp((-(x-mu)**2)/(2*(sgma**2)))/((2*np.pi)*sgma**2)**0.5
    plt.plot(x,fx)

mue=2
sigma=np.arange(1,10,2)
for sgma in sigma:
    fx=np.exp((-(x-mue)**2)/(2*(sgma**2)))/((2*np.pi)*sgma**2)**0.5
    plt.plot(x,fx,label=str(sgma))

plt.legend()
plt.show()
