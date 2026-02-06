#!/bin/python
import numpy as np
import pylab as pl
#x0=100
#c=21
#a=19
#m=33
##B
#x0=156
#a=39397
#c=191
#m=63
##C
#x0=37
#a=65
#c=71
#m=997
##D
#x0=180
#c=223
#a=12863
#m=749274
##E
x0=150
a=16807
c=2
m=2147483500
x_list=[]
x_cor=10 #pozycja na środku tablicy 20X20
y_cor=10 #pozycja y na środku tablicy 20X20
x_l=[]
y_l=[]
heatmap=np.zeros((20,20))
def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range (0,400000):
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
    heatmap[y_cor,x_cor]+=1
'''
#4 wykres 
pl.plot(x_l,y_l,"b.-")
pl.xlabel("steps taken")
pl.ylabel("left/right")
pl.title("Random walk 8 directions")
pl.show()
'''
pl.figure(figsize=(6,6))
pl.imshow(heatmap,cmap='hot',origin='lower')
pl.colorbar(label='Number of visits')
pl.title("Heatmap")
pl.xlabel("X pos")
pl.ylabel("Y pos")
pl.show()
