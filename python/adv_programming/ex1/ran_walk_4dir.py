#!/bin/python
import pylab as pl
x0=1670
c=31543
a=12807
m=31672
x_list=[]
x_cor=10 #pozycja na środku tablicy 20X20
y_cor=10 #pozycja y na środku tablicy 20X20
x_l=[]
y_l=[]

def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range (0,10000):
    x0=Lehmer(x0,a,c,m)
    x_list.append(x0)

    if x0 <= 0.25*m: #0-0.25left
        x_cor-=1
        if x_cor <0:
            x_cor=19
    elif x0 >  0.5*m:  #0.25m-0.5m up
        y_cor+=1  
    elif x0 > 0.75*m:  #0.5m-0.75m right
        x_cor+=1
        if x_cor>19:
            x_cor=0
    else: #0.75m-1m down
        y_cor-=1
        if y_cor>19:
            y_cor=0
    x_l.append(x_cor)
    y_l.append(y_cor)

#4 wykres 
pl.plot(x_l,y_l,"b.-")
pl.xlabel("steps taken")
pl.ylabel("left/right")
pl.title("Random walk")
pl.show()
