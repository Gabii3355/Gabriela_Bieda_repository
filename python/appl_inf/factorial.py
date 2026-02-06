#!/usr/bin/python3
print("Give a numer to make a factorial: ")
a=int(input())
def factorial(n):
	prod=1
	for x in range(1,n+1):
		prod=prod*x
	return prod
print(factorial(a))

def factorial2(n):
	prod=1
	x=1
	while x <= n:
		prod=prod*x
		x=x+1
	return prod
print(factorial2(a))

def factorial3(a):
	if a==1:
		return 1
	else:
		return factorial3(a-1)*a
print(factorial3(a))
