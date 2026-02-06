import math
import matplotlib.pyplot as plt
import numpy as np
#numeryczne calkowanie i porownanie wyniku zblizonego z wynikiem "prawdziwym" (analitycznym). 
def integ(n): #proste sumy prostokatow (lewostronne) dla f(x)=sinx
	result = 0
	a = math.pi/n
	for i in range(n):
		result += math.sin(i * a) * a
	real_result = -math.cos(math.pi)+math.cos(0)
	error = (real_result- result)/real_result * 100 #error - bład wzgledny w % ( jest (-) gdy przyblizenie "przesacuje" lub "nieodszacuje")
	return result, error, real_result
def polynom(n): #proste sumy prostokątow (lewostronne) dla wielomianów
	result = 0
	a = 2/n
	for i in range(n):
		x= i * a
		b = 11*x**3 - 3*x**2-7*x + 13
		result += a*b
	real_result = 48
	error = (real_result- result)/real_result * 100
	return result, error, real_result
#test = polynom(129)
#print(test)
def e_fun(n): #f(x)=e^x na [0,5], lewostronne i punkt środkowy
	result = 0
	a = 5/n
	for i in range(n):
		x = i * a
		b = math.e**x
		result +=a*b
	real_result= 147.413
	error = (real_result- result)/real_result * 100
	return result, error, real_result
def new_meth(n):#metoda punktu środkowego (dokładniejsza niż lewostronna)
	result = 0
	a = 5/n
	x = 0
	for i in range(n):
		x = i * a + a/2
		b = math.e**x
		result +=a*b
	real_result= 147.413
	error = (real_result- result)/real_result * 100
	return result, error, real_result
def trapezoid(f, x, n, real_result): #metoda trapezów dla f(t)dt [0,x]
	result = 0
	h = x/n
	for i in range(n):
		a = i * h
		b = (i+1) * h
		y0 = f(a)
		y1 = f(b)
		result += ((y0+y1)*h)/2
	error = (real_result- result)/real_result * 100
	return result, real_result, error
def poly(x): #definicja wielomianu, która przekazuje funkcję do TRAPEZOID
    return 11 * x**3 - 3 * x**2 - 7 * x + 13
def find_n(f,x,real_result,threshold = 1.0): #dobiera minimalne n, aby bezwgledny błąd procentowy metody trapezów byc < "trehold"
	n = 1
	while True:
		res, r_res, error = trapezoid(f, x, n, real_result)
		if abs(error) < threshold:
			break
		n+=1
	return n
'''
n1 = find_n(poly, 2, 48)
n2 = find_n(math.exp, 5, 147.413)
n3 = find_n(math.sin, math.pi, 2)
print(n1,n2,n3)
print(trapezoid(poly, 2, n1, real_result= 48))
print(trapezoid(math.exp, 5, n2, real_result= 147.413))
print(trapezoid(math.sin, math.pi, n3, real_result= 2)) 
'''
def report(name, f, x, n, real):
    approx, exact, err = trapezoid(f, x, n, real)
    print(f"{name:10s} | n={n:3d} | approx={approx:.6f} | exact={exact:.6f} | error={err:+.3f}%")

n1 = find_n(poly, 2, 48)
n2 = find_n(math.exp, 5, math.exp(5) - 1)   # lepiej bez zaokrągleń
n3 = find_n(math.sin, math.pi, 2)

print("Minimal n for <1% error (trapezoid):")
print(f"  poly [0,2]: {n1}\n  e^x [0,5]: {n2}\n  sin [0,π]: {n3}\n")

report("poly [0,2]", poly,      2,       n1, 48)
report("e^x [0,5]",  math.exp,  5,       n2, math.exp(5) - 1)
report("sin [0,π]",  math.sin,  math.pi, n3, 2)

'''
test1 = new_meth(33)
print(test1)
test = e_fun(250)
print(test)
'''
'''
POLYNOM
n = 1
xaxis = []
yaxis = []
res, err, real = polynom(n)
while err > 1:
	xaxis.append(n)
	n += 1
	res, err, real = polynom(n)
	yaxis.append(err)
plt.plot(xaxis, yaxis)
plt.show()
'''
'''
SINUS
n = 1
xaxis = []
yaxis = []
res, err, real = integ(n)
while err > 1:
	xaxis.append(n)
	n += 1
	res, err, real = integ(n)
	yaxis.append(err)
plt.plot(xaxis, yaxis)
plt.show()
print(res)
print(err)
print(real)
print(n)
'''
