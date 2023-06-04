# gradient descent method
import numpy as np
# objective function and the slopes
def f(x,y):
    return 0.5*(x**2-4*x*y+8*y**2)
def fx(x,y):
    return x-2*y
def fy(x,y):
    return -2*x+8*y
# initialization of variables 
x0,y0=1.0, 2.0
eps = 1e-6
t=0.1
# make lists 
xlist, ylist=[],[]
xlist.append(x0)
ylist.append(y0)
# gradient descent method 
xk,yk=x0,y0
iter=0
while True:
    tk=t
    delta_xk, delta_yk = -fx(xk,yk), -fy(xk,yk)
    
    xkp1=xk+tk*delta_xk
    ykp1=yk+tk*delta_yk
    
    xlist.append(xkp1)
    ylist.append(ykp1)
    if np.linalg.norm(np.array((xkp1-xk, ykp1-yk)))<eps:
        print("GD converges at iter =", iter)
        break
    
    iter = iter+1
    xk,yk = xkp1, ykp1
    