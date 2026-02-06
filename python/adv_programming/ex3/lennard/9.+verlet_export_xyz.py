#lennard-jones potential, distance between two points using coordinates
#then also calculating forces
import numpy as np
import matplotlib.pyplot as plt
import math
xi,xj = 1,2
yi,yj = 4,5
zi,zj = 7,8
i_mass = 1
j_mass = 1
#epsilon= 1 #dołek w potencjale
#sigma= 1 #rozmiar atomu
dt = 0.001 #krok czasowy
Xi_p = []
t_p = []
Xj_p = []
Yi_p = []
Yj_p = []
Zi_p = []
Zj_p = []
def lennard(r, epsilon, sigma):
	U= 4* epsilon* ((sigma/r)**12-(sigma/r)**6)
	return U
def distance_3d(xi,yi,zi,xj,yj,zj):
	r = math.sqrt((xi-xj)**2+(yi-yj)**2+(zi-zj)**2)
	return r
def force(r):
	F= -(48*r**(-13)-24*r**(-7))
	return F
#r = distance_2d(xi,yi,xj,yj,zi,zj)
#print(r)
#przechowywanie poprzednich pozycji
xi_prev, yi_prev, zi_prev = xi, yi, zi
xj_prev, yj_prev, zj_prev = xj, yj, zj
#dla kazdego kroku trzeba policzyc przyspieszenie, siłe i wektor, wiec petla
traj = open("traj.xyz","w")
for step in range(10000):
	
	#wektor odległości
	rx=xj-xi
	ry=yj-yi
	rz=zj-zi
	#print("r vector from:", rx, ry,rz)
	r = math.sqrt(rx**2+ry**2+ rz**2)
	F = force(r) #force
	#print(r, F)

	#rozkład siły na osie, czyli Fix /Fiy=rx/ry 
	#Fix^2+Fiy^2=F^2
	Fiy=F*ry/r
	Fix=F*rx/r
	Fiz=F*rz/r
	#acceleration=force ax=Fx ay=Fy
	axi = Fix/i_mass
	ayi = Fiy/i_mass
	azi = Fiz/i_mass
	axj = -Fix/j_mass
	ayj = -Fiy/j_mass
	azj = -Fiz/j_mass
	
	#first position in timestep r(t-dt)=r(t)
	
	#next position in timestep
	#r(t+dt)=2r(t)-r(t-dt)+dt**2*acc(t)
	#Verlet integration
	xi_new =2*xi-xi_prev+axi*dt**2
	yi_new =2*yi-yi_prev+ayi*dt**2
	zi_new =2*zi-zi_prev+azi*dt**2
	xj_new =2*xj-xj_prev+axj*dt**2
	yj_new =2*yj-yj_prev+ayj*dt**2
	zj_new =2*zj-zj_prev+azj*dt**2
	#new position
	xi_prev=xi
	yi_prev=yi
	zi_prev=zi
	xj_prev = xj
	yj_prev = yj
	zj_prev = zj
	xi, xj = xi_new, xj_new 
	yi, yj = yi_new,yj_new
	zi, zj = zi_new,zj_new
	t=step*dt
	#print(step,xi,xj,yi,yj,zi,zj)
	traj.write("2\n") 
	traj.write(f"t={step*dt}\n") 
	traj.write(f"Ar {xi} {yi} {zi}\n") 
	traj.write(f"Ar {xj} {yj} {zj}\n")

	Xi_p.append(xi)
	Xj_p.append(xj)
	Yi_p.append(yi)
	Yj_p.append(yj)	
	Zi_p.append(zi)
	Zi_p.append(zj)
	t_p.append(step)
traj.close()
#print(t_p)
#print(Xi_p)
#plt.plot(Xi_p, Yi_p,Zi_p)
#plt.plot(Xj_p,Yj_p,Zj_p)
#plt.show()
