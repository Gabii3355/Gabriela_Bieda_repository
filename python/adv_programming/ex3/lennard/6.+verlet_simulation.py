#lennard-jones potential, distance between two points using coordinates
#then also calculating forces
import numpy as np
import matplotlib.pyplot as plt
import math
xi,xj = 1,2
yi,yj = 4,5
epsilon= 1 #dołek w potencjale
sigma= 1 #rozmiar atomu
dt = 0.001 #krok czasowy
Xi_p = []
t_p = []
Xj_p = []
Yi_p = []
Yj_p = []
def lennard(r, epsilon, sigma):
	U= 4* epsilon* ((sigma/r)**12-(sigma/r)**6)
	return U
def distance_2d(xi,yi,xj,yj):
	r = math.sqrt((xi-xj)**2+(yi-yj)**2)
	return r
def force(r):
	F= -(48*r**(-13)-24*r**(-7))
	return F
#r = distance_2d(xi,yi,xj,yj)
#print(r)
#przechowywanie poprzednich pozycji
xi_prev, yi_prev = xi, yi
xj_prev, yj_prev = xj, yj
#dla kazdego kroku trzeba policzyc siłe i wektor, wiec petla
for step in range(10000):
	
	#wektor odległości
	rx=xj-xi
	ry=yj-yi
	print("r vector from:", rx, ry)
	r = math.sqrt(rx**2+ry**2)
	F = force(r) #force
	print(r, F)

	#rozkład siły na osie, czyli Fix /Fiy=rx/ry 
	#Fix^2+Fiy^2=F^2
	Fiy=F*ry/r
	Fix=F*rx/r
	#acceleration=force ax=Fx ay=Fy
	axi = Fix
	ayi = Fiy
	axj = -Fix
	ayj = -Fiy
	#first position in timestep r(t-dt)=r(t)
	
	#next position in timestep
	#r(t+dt)=2r(t)-r(t-dt)+dt**2*acc(t)
	#Verlet integration
	xi_new =2*xi-xi_prev+axi*dt**2
	yi_new =2*yi-yi_prev+ayi*dt**2
	xj_new =2*xj-xj_prev+axj*dt**2
	yj_new =2*yj-yj_prev+ayj*dt**2
	#new position
	xi_prev=xi
	yi_prev=yi
	xj_prev = xj
	yj_prev = yj
	xi, xj = xi_new, xj_new 
	yi, yj = yi_new,yj_new
	print(step, xi, xj, yi, yj)
	Xi_p.append(xi)
	Xj_p.append(xj)
	Yi_p.append(yi)
	Yj_p.append(yj)
	t_p.append(step)
print(t_p)
plt.plot(Xi_p, Yi_p)
plt.plot(Xj_p,Yj_p)
plt.show()
