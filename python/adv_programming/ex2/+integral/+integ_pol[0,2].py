#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#numeryczne calkowanie dla wielomianu f(x)=11x^3-3x^2-7x+13 w przedziale [0,2] lewą sumą Riemanna
def calka(n):
    #n=10
    sum_area=0
    a=2/n #szerokośc przedziału
    for i in range(n):
        x=i*a
        b=11*x**3-3*x**2-7*x+13
        p=a*b
        sum_area+=p
    return sum_area
wynik=calka(129)
error=(48-wynik)/48*100
print("Wynik całki: ",wynik)
print("Error: ",error)
x=[]
y=[]
for i in range(1,130):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()

