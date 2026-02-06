#!/usr/bin/env python3
import math
def f(x):
    f=math.sin(x)
    return f
def calka(a,b):
    p = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return p
wynik=0
n=2
for i in range(n):
    x=math.pi/n
    wynik += calka(x*i,x*(i+1))
print("Wynik: ",wynik)
print("n =", n)
def error(w,wr):
    e=(w-wr)/wr*100
    return e
err = error(wynik,2)
print("Error: ", err, "%")


