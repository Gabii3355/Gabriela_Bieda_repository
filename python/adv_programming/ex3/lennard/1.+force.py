#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
def F(r):
    f=24*(2*r**(-13)-r**(-7))
    return f
r=np.linspace(0.95,3,100)
f=F(r)
plt.plot(r,f)
plt.show()
