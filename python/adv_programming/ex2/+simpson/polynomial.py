#!/usr/bin/env python3
import math
def f(x):
    f=11*x**3-3*x**2-7*x+13
    return f
def calka(a,b):
    p = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return p
wynik = calka(0,2)
print("Wynik: ",wynik)
def error(w,wr):
    e=(w-wr)/wr*100
    return e
err = error(wynik,48)
print("Error: ", err, "%")


