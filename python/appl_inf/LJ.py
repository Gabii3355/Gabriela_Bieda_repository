#!/usr/bin/python3
import  matplotlib.pyplot as plt
def LJ (x): 
        E=1
        sigm=1
        Elj=4*E*((sigm/r**(12))-(sigm/r**(6)))
        return Elj
LJ_x=[]
LJ_y=[]
for d in range (6,21):
        r=d/10
        print(LJ(r))
        LJ_x.append(r)
        LJ_y.append(LJ(r))

plt.plot(LJ_x, LJ_y )
plt.show()
