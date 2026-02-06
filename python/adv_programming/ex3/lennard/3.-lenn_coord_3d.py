#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
def r(x1,y1,z1,x2,y2,z2):
    r=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
    return r
def U(r,E,b):
    u=4*E*((b/r)**12-(b/r)**6)
    return u 
#x1=np.linspace(1.7,5,100) 
#y1=np.linspace(1.7,5,100) 
#z1=np.linspace(1.7,5,100) 
#x2=np.linspace(0,0,100) 
#y2=np.linspace(0,0,100) 
#z2=np.linspace(0,0,100)
x1=0
y1=0
z1=0
x2=1
y2=1
z2=1
r=r(x1,y1,z1,x2,y2,z2)
E=0.99
b=3.405
u=U(r,E,b)
print('U=',u)
#plt.plot(r,u)
#plt.show()
def F(r,E,b):
    f=24*E*(2*b**12*r**(-13)-b**6*r**(-7))
    return f
f=F(r,E,b)
print('F=',f)
def v(x1,y1,z1,x2,y2,z2,F):
    xr=x2-x1
    yr=y2-y1
    zr=z2-z1
    Fiz=(F**2/(((xr**2+yr**2)/zr**2)+1))**0.5
    Fiz=np.sign(F)*(-1)*Fiz
    Fix=xr*Fiz/zr
    Fiy=yr*Fiz/zr
    Fjx=-Fix
    Fjy=-Fiy
    Fjz=-Fiz
    return Fix,Fiy,Fiz,Fjx,Fjy,Fjz
v=v(x1,y1,z1,x2,y2,z2,f)
print('Fix,Fiy,Fiz,Fjx,Fjy,Fjz:', v)
