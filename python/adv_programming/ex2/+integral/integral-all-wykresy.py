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

# ---------- WYKRESY ----------
import numpy as np
import matplotlib.pyplot as plt
import math

# pomocnik: policz błędy dla n=1..n_max
def error_vs_n(f, x_end, real_result, n_max=80):
    ns = np.arange(1, n_max + 1)
    errs_abs = []
    approxs = []
    for n in ns:
        approx, _, err = trapezoid(f, x_end, n, real_result)
        approxs.append(approx)
        errs_abs.append(abs(err))     # błąd bezwzględny w %
    return ns, np.array(errs_abs), np.array(approxs)

def plot_error_curves():
    real_poly = 48.0
    real_exp  = math.exp(5) - 1.0
    real_sin  = 2.0

    ns, e_poly, _ = error_vs_n(poly,      2.0,      real_poly)
    ns, e_exp,  _ = error_vs_n(math.exp,  5.0,      real_exp)
    ns, e_sin,  _ = error_vs_n(math.sin,  math.pi,  real_sin)

    # 1) wielomian
    plt.figure()
    plt.plot(ns, e_poly)
    plt.title("Trapezoid — błąd bezwzględny vs n (poly na [0,2])")
    plt.xlabel("n (liczba trapezów)")
    plt.ylabel("Błąd bezwzględny (%)")
    plt.grid(True)

    # 2) e^x
    plt.figure()
    plt.plot(ns, e_exp)
    plt.title("Trapezoid — błąd bezwzględny vs n (e^x na [0,5])")
    plt.xlabel("n (liczba trapezów)")
    plt.ylabel("Błąd bezwzględny (%)")
    plt.grid(True)

    # 3) sin(x)
    plt.figure()
    plt.plot(ns, e_sin)
    plt.title("Trapezoid — błąd bezwzględny vs n (sin(x) na [0,π])")
    plt.xlabel("n (liczba trapezów)")
    plt.ylabel("Błąd bezwzględny (%)")
    plt.grid(True)

def plot_trapezoids_for_sin(n=10):
    # podgląd trapezów dla sin(x) na [0, π]
    a, b = 0.0, math.pi
    h = (b - a) / n
    xs = np.linspace(a, b, 400)
    ys = np.sin(xs)

    plt.figure()
    plt.plot(xs, ys, label="sin(x)")
    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h
        y0 = math.sin(x0)
        y1 = math.sin(x1)
        # krawędzie trapezu:
        plt.plot([x0, x1], [y0, y1])  # górna
        plt.plot([x0, x0], [0, y0])   # lewa
        plt.plot([x1, x1], [0, y1])   # prawa
    plt.title(f"Trapezy dla sin(x) na [0,π] (n={n})")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

# --- UŻYCIE: po wyznaczeniu n1, n2, n3 ---
# (jeśli masz już: n1 = find_n(...), n2 = ..., n3 = ...)

plot_error_curves()
plot_trapezoids_for_sin(n3)  # np. użyj n3 albo podaj liczbę ręcznie, np. 10
plt.show()

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
