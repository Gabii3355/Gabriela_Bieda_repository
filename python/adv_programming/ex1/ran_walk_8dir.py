#!/bin/python
import pylab as pl
x0=100
c=31
a=1207
m=6003
x_list=[]
x_cor=10 #pozycja na środku tablicy 20X20
y_cor=10 #pozycja y na środku tablicy 20X20
x_l=[]
y_l=[]

def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range (0,2000):
    x0=Lehmer(x0,a,c,m)
    x_list.append(x0)

    if x0 <= 0.15*m:
        x_cor-=1
    elif x0 <= 0.25*m:
        x_cor-=1
        y_cor-=1
    elif x0 <= 0.4*m:
        y_cor-=1
    elif x0 <= 0.5*m:
        x_cor+=1
        y_cor-=1
    elif x0 <= 0.65*m:
        x_cor+=1
    elif x0 <= 0.75*m:
        x_cor+=1
        y_cor+=1
    elif x0 <= 0.9*m:
        y_cor+=1
    else:
        x_cor-=1
        y_cor+=1
    if x_cor == 20:
        x_cor = 0
    if y_cor == 20:
        y_cor = 0
    if x_cor == -1:
        x_cor = 19
    if y_cor == -1:
        y_cor = 19
    x_l.append(x_cor)
    y_l.append(y_cor)

#4 wykres 
pl.plot(x_l,y_l,"b.-")
pl.xlabel("steps taken")
pl.ylabel("left/right")
pl.title("Random walk")
pl.show()
