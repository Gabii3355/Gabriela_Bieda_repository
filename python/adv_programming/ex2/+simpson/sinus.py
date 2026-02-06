#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
def f(x):
    f=math.sin(x)
    return f
def calka(a,b):
    p = (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    return p
wynik = calka(0,math.pi)
print("Wynik: ",wynik)
def error(w,wr):
    e=(w-wr)/wr*100
    return e
err = error(wynik,2)
print("Error: ", err, "%")

