#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
# przybliżenie całki sinx dx [0,pi] metodą trapezów i pokazuje zbieznośc wyniku
def calka(n):
    sum_area=0
    a=math.pi/n
    for i in range(n):
        x=a*i
        xn=a*(i+1)
        b=math.sin(x)
        bn=math.sin(xn)
        p=a*(b+bn)/2
        sum_area+=p
    return sum_area
wynik=calka(10)
print("Wynik: ",wynik)
error=(2-wynik)/2*100
print("Error: ",error)
#plot
x=[]
y=[]
for i in range(1,10):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()


