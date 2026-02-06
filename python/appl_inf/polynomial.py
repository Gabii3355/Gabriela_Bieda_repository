#!/usr/bin/python3
print("Give a numer to make a polynomial: ")
a=int(input())
def polynomial(x):
	y=x**3-3*x+13
	return y
print(polynomial(a))
