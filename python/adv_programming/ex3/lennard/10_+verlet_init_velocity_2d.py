import numpy as np
import matplotlib.pyplot as plt
import math

# --- initial positions ---
xi, yi = 1.0, 4.0
xj, yj = 2.0, 5.0

# --- initial velocities ---
vxi, vyi = 0.0, 0.1
vxj, vyj = -0.1, 0.0

# --- masses ---
i_mass = 1.0
j_mass = 1.0

# --- timestep ---
dt = 0.001

# --- storage for plotting ---
Xi_p, Yi_p = [], []
Xj_p, Yj_p = [], []

# --- Lennard-Jones force magnitude ---
def force_LJ(r):
    return -(48*r**(-13) - 24*r**(-7))

# --- compute force components between particles ---
def compute_force(xi, yi, xj, yj):
    rx = xj - xi
    ry = yj - yi
    r = math.sqrt(rx*rx + ry*ry)
    F = force_LJ(r)
    Fx = F * rx / r
    Fy = F * ry / r
    return Fx, Fy

# --- initial force ---
Fix, Fiy = compute_force(xi, yi, xj, yj)
Fxj, Fyj = -Fix, -Fiy

# ============================
#      VELOCITY VERLET LOOP
# ============================

for step in range(10000):

    # --- update positions ---
    xi += vxi*dt + 0.5*(Fix/i_mass)*dt*dt
    yi += vyi*dt + 0.5*(Fiy/i_mass)*dt*dt

    xj += vxj*dt + 0.5*(Fxj/j_mass)*dt*dt
    yj += vyj*dt + 0.5*(Fyj/j_mass)*dt*dt

    # --- compute new forces ---
    Fix_new, Fiy_new = compute_force(xi, yi, xj, yj)
    Fxj_new, Fyj_new = -Fix_new, -Fiy_new

    # --- update velocities (full step) ---
    vxi += 0.5 * (Fix + Fix_new) / i_mass * dt
    vyi += 0.5 * (Fiy + Fiy_new) / i_mass * dt

    vxj += 0.5 * (Fxj + Fxj_new) / j_mass * dt
    vyj += 0.5 * (Fyj + Fyj_new) / j_mass * dt

    # --- replace old forces ---
    Fix, Fiy = Fix_new, Fiy_new
    Fxj, Fyj = Fxj_new, Fyj_new

    # --- store trajectory ---
    Xi_p.append(xi)
    Yi_p.append(yi)
    Xj_p.append(xj)
    Yj_p.append(yj)

# --- plot ---
plt.plot(Xi_p, Yi_p)
plt.plot(Xj_p, Yj_p)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Velocity Verlet 2D LJ Trajectories")
plt.show()
