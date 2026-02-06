#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
def f(x):
    f=math.sin(x)
    return f
def der(x1,x2):
    y1=f(x1)
    y2=f(x2)
    der=(y2-y1)/(x2-x1)
    return der
n=100
y=[]
x=[]
s=[]
c=[]
for i in range(n):
    x1=math.pi/n*i
    x2=math.pi/n*(i+1)
    d=der(x1,x2)
    sin=math.sin(x1)
    cos=math.cos(x1)
    s.append(sin)
    c.append(cos)
    x.append(x1)
    y.append(d)
plt.plot(x,y,label='approximated derivative')
plt.plot(x,s,label='sin(x)')
plt.plot(x,c,label='cos(x)')
plt.legend()
plt.savefig('sinx-1.png', dpi=300, bbox_inches='tight')
plt.show()
