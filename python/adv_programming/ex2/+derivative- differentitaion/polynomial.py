#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
def f(x):
    f=11*x**3-3*x**2-7*x+13
    return f
def der(x1,x2):
    y1=f(x1)
    y2=f(x2)
    der=(y2-y1)/(x2-x1)
    return der
n=100
y=[]
x=[]
h=[]
g=[]
for i in range(n):
    x1=2/n*i
    x2=2/n*(i+1)
    d=der(x1,x2)
    p=f(x1)
    pd=33*x1**2-6*x1-7
    h.append(p)
    g.append(pd)
    x.append(x1)
    y.append(d)
plt.plot(x,y,label='approximated derivative')
plt.plot(x,h,label='f(x)')
plt.plot(x,g,label='exact derivative')
plt.legend()
plt.show()
