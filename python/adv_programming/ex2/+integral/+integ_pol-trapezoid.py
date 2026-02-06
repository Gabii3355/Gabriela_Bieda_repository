#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#calkuje numerycznie wielomian metoda trapezow i rysuje zbienzosc
def calka(n):
    sum_area=0
    a=2/n
    for i in range(n):
        x=a*i
        xn=a*(i+1)
        b=11*x**3-3*x**2-7*x+13
        bn=11*xn**3-3*xn**2-7*xn+13
        p=a*(b+bn)/2
        sum_area+=p
    return sum_area
wynik=calka(10)
print("Wynik: ",wynik)
error=(48-wynik)/48*100
print("Error: ",error)
#plot
x=[]
y=[]
for i in range(1,10):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()


