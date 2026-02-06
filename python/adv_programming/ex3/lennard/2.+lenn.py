#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
def U(r,E,b):
    u=4*E*((b/r)**12-(b/r)**6)
    return u
def F(r):
    f=24*(2*r**(-13)-r**(-7))
    return f
E=1
b=1
r=np.linspace(0.95,3,100)
u=U(r,E,b)
f=F(r)
plt.plot(r,f)
plt.plot(r,u)
plt.show()
