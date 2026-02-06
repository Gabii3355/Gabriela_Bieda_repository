#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
def f(x):
    f=math.exp(x)
    return f
def der(x1,x2):
    y1=f(x1)
    y2=f(x2)
    der=(y2-y1)/(x2-x1)
    return der
n=35000
y=[]
x=[]
s=[]
c=[]
for i in range(n):
    x1=710/n*i
    x2=710/n*(i+1)
    d=der(x1,x2)
    ex=f(x1)
    exd=f(x1)
    s.append(ex)
    c.append(exd)
    x.append(x1)
    y.append(d)
plt.plot(x,y,label='approximated derivative')
plt.plot(x,s,label='exp(x)')
#plt.plot(x,c,label='exact derivative')
plt.legend()
plt.show()
