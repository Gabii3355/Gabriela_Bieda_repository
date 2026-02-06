#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#liczy przyblizenie calki e^x [0,5] regułą punktu środkowego (midpoint) 
def calka(n):
    sum_area=0
    a=5/n
    for i in range(n):
        x=a*i+a*0.5
        b=math.exp(x)
        p=a*b
        sum_area+=p
    return sum_area
wynik=calka(11) #przyblizenie dla 11 przedzialów
print("Wynik: ",wynik)
def error(w,wr):
    e=(wr-w)/wr*100
    return e
err = error(wynik,147.413)
print("Error: ", err, "%")
#plot
x=[]
y=[]
for i in range(1,10):
    x.append(i)
    y.append(calka(i))
plt.plot(x,y)
plt.show()


