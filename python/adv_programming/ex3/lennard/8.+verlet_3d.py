# lennard-jones potential, distance between two points using coordinates
# then also calculating forces
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

xi, xj = 1, 2
yi, yj = 4, 5
zi, zj = 7, 8
i_mass = 1
j_mass = 1

dt = 0.001  # krok czasowy

Xi_p = []
t_p = []
Xj_p = []
Yi_p = []
Yj_p = []
Zi_p = []
Zj_p = []

def lennard(r, epsilon, sigma):
    U = 4 * epsilon * ((sigma/r)**12 - (sigma/r)**6)
    return U

def distance_3d(xi, yi, zi, xj, yj, zj):
    r = math.sqrt((xi-xj)**2 + (yi-yj)**2 + (zi-zj)**2)
    return r

def force(r):
    F = -(48*r**(-13) - 24*r**(-7))
    return F

# przechowywanie poprzednich pozycji
xi_prev, yi_prev, zi_prev = xi, yi, zi
xj_prev, yj_prev, zj_prev = xj, yj, zj

# dla każdego kroku trzeba policzyć przyspieszenie, siłę i wektor
for step in range(10000):

    # wektor odległości
    rx = xj - xi
    ry = yj - yi
    rz = zj - zi
    print("r vector from:", rx, ry, rz)

    r = math.sqrt(rx**2 + ry**2 + rz**2)
    F = force(r)
    print(r, F)

    # rozkład siły na osie
    Fix = F * rx / r
    Fiy = F * ry / r
    Fiz = F * rz / r

    # przyspieszenia
    axi = Fix / i_mass
    ayi = Fiy / i_mass
    azi = Fiz / i_mass

    axj = -Fix / j_mass
    ayj = -Fiy / j_mass
    azj = -Fiz / j_mass

    # Verlet integration
    xi_new = 2*xi - xi_prev + axi * dt**2
    yi_new = 2*yi - yi_prev + ayi * dt**2
    zi_new = 2*zi - zi_prev + azi * dt**2

    xj_new = 2*xj - xj_prev + axj * dt**2
    yj_new = 2*yj - yj_prev + ayj * dt**2
    zj_new = 2*zj - zj_prev + azj * dt**2

    # update positions
    xi_prev, yi_prev, zi_prev = xi, yi, zi
    xj_prev, yj_prev, zj_prev = xj, yj, zj

    xi, xj = xi_new, xj_new
    yi, yj = yi_new, yj_new
    zi, zj = zi_new, zj_new

    print(step, xi, xj, yi, yj, zi, zj)

    Xi_p.append(xi)
    Xj_p.append(xj)
    Yi_p.append(yi)
    Yj_p.append(yj)
    Zi_p.append(zi)
    Zj_p.append(zj)
    t_p.append(step)

print(t_p)

# --- 3D PLOT ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(Xi_p, Yi_p, Zi_p)
ax.plot(Xj_p, Yj_p, Zj_p)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
