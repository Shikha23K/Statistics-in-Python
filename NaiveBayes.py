import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

carCsv=pd.read_csv('cars93.csv')
X=carCsv.mpg

Y=carCsv.origin
print(Y.unique())
#Y have 398 data of three unique value
Y[Y=='usa']= '0'
Y[Y=='japan']= '1'
Y[Y=='europe']= '2'
L=Y.unique()

#Separating Testing & Training dataset

dSet=np.random.permutation(np.arange(Y.size))
#Y have 398 data of three unique value
#permutation is shuffling 0 to 398 no. as sizes in an array
nTrain=280
nTest=dSet.size-nTrain
XTrain=X[dSet[:nTrain]]
YTrain=Y[dSet[:nTrain]]
XTest=X[dSet[nTrain:]]
YTest=Y[dSet[nTrain:]]

##
# P(Y)

Py=np.zeros(3)
Py[0]=(YTrain=='0').sum()/YTrain.size 
#probability just frequency or occurance of the data
Py[1]=(YTrain=='1').sum()/YTrain.size 
Py[2]=(YTrain=='2').sum()/YTrain.size 
print(Py)
fx_y=[[0,0],[0,0],[0,0]]
X_0=XTrain[YTrain=='0']
X_1=XTrain[YTrain=='1']
X_2=XTrain[YTrain=='2']
#estimating parameters mu and sigma for F(x)
#Mu = expectation or mean,therefore
mu_0=X_0.mean()
mu_1=X_1.mean()
mu_2=X_2.mean()
#std() standard deviation or variance
sgma_0=X_0.std()
sgma_1=X_1.std()
sgma_2=X_2.std()

#computing F(x)
fx_y[0][0]=mu_0
fx_y[0][1]=sgma_0
fx_y[1][0]=mu_1
fx_y[1][1]=sgma_1
fx_y[2][0]=mu_2
fx_y[2][1]=sgma_2
x=np.linspace(0,60,1000)
for i in range(3):
    mue=fx_y[i][0]
    sgma=fx_y[i][1]
    fx=np.exp((-(x-mue)**2)/(2*(sgma**2)))/((2*np.pi)*sgma**2)**0.5
    plt.plot(x,fx,label=str(i))

plt.legend()
plt.show() 
XTest=np.asarray(XTest)
xt=XTest[107]

#p(y=0|x=xt)
#predict the class

Py_0_X=(Py[0])*(np.exp((-(xt-mu_0)**2)/(2*(sgma_0**2)))/((2*np.pi)*sgma_0**2)**0.5)
Py_1_X=(Py[0])*(np.exp((-(xt-mu_1)**2)/(2*(sgma_1**2)))/((2*np.pi)*sgma_1**2)**0.5)
Py_2_X=(Py[0])*(np.exp((-(xt-mu_2)**2)/(2*(sgma_2**2)))/((2*np.pi)*sgma_2**2)**0.5)

print(Py_0_X,Py_1_X,Py_2_X)

YTest=np.asarray(YTest)
print(YTest[107])
