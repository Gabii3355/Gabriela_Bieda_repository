#!/usr/bin/env python3
import math
def f(x):
    f=math.exp(x)
    return f
def calka(a,b):
    p = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return p
wynik = calka(0,5)
print("Wynik: ",wynik)
def error(w,wr):
    e=(wr-w)/wr*100
    return e
err = error(wynik,147.413)
print("Error: ", err, "%")


