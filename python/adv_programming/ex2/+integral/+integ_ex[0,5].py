#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#numeryczne calkowanie e^x
def calka(n):
    #n=10
    sum_area=0
    a=5/n
    for i in range(n):
        x=a*i
        b=math.exp(x)
        p=a*b
        sum_area+=p
    return sum_area
wynik=calka(250)
print("Wynik całki: ",wynik)
error=(147.413-wynik)/147.413*100
print("Error: ",error)
#plot
x=[]
y=[]
for i in range(1,10):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()


