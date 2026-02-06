#!/bin/python
import pylab as pl
x0=180
c=223
a=12863
m=749274
x_list=[]
pos=[]
walk=0

def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range(0,40000):
    x0=Lehmer(x0,a,c,m)
    x_list.append(x0)

    if x0 < m//2:
        walk-=1
    else:
        walk+=1    
    pos.append(walk)
print(x_list)
print(pos)

#4 wykres 
X_index_num = list(range(len(pos)))
pl.plot(X_index_num,pos,"b-")
pl.xlabel("steps taken")
pl.ylabel("left/right")
pl.title("Random walk")
pl.show()
