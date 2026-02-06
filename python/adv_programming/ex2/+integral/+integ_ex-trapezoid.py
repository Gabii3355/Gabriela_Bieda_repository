#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#liczy przyblizenie calki metoda trapezow i rysuje zbieznosc wyniku dowwartosci calkowitej 
def calka(n):
    #n=10
    pc=0
    a=5/n
    for i in range(n):
        x=a*i
        xn=a*(i+1)
        b=math.exp(x)
        bn=math.exp(xn)
        p=a*(b+bn)/2
        pc+=p
    return pc
wynik=calka(15)
print(wynik)
error=(147.413-wynik)/147.413*100
print(error)
#plot
x=[]
y=[]
for i in range(1,10):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()


