import numpy as np
import matplotlib.pyplot as plt
w = np.array([[-3.2],[1],[1]])
X = np.array([[1,1],[0,1],[0,1]])
Y = np.array([[1],[-1]])
xx = np.linspace(-5,5,100)
def fun(w):
 w[2] = w[2]+0.1
 yy = (-w[0]/w[2]) -((w[1]/w[2])*xx)
 plt.plot(xx,yy)
 plt.xlim(0,3)
 plt.ylim(0,3)



update = 1
plt.scatter(X[1,:],X[2,:])
while(1):
 flag = 0
 if(update == 1):
 for i in range(2):
 x = X[:,i].reshape(w.shape)
 if(np.dot(w.T,x)>0):
 pre = 1
 if(pre != Y[i]):
 w = w + (x*Y[i])
 flag = 1
 fun(w)

 else:
 pre = -1
 if(pre != Y[i]):
 w = w + (x*Y[i])
 flag = 1
 fun(w)

 if(flag != 1):
 update = 0
 else:
 break
