import numpy as np
import matplotlib.pyplot as plt
import math

# --- initial positions ---
xi, yi, zi = 1.0, 4.0, 7.0
xj, yj, zj = 2.0, 5.0, 8.0

# --- initial velocities ---
vxi, vyi, vzi = 0.0, 0.1, 0.0
vxj, vyj, vzj = -0.1, 0.0, 0.0

# --- masses ---
i_mass = 4.0
j_mass = 4.0

# --- timestep ---
dt = 0.001

# --- storage for plotting ---
Xi_p, Yi_p, Zi_p = [], [], []
Xj_p, Yj_p, Zj_p = [], [], []

# --- Lennard-Jones force magnitude ---
def force_LJ(r):
    return -(48*r**(-13) - 24*r**(-7))

# --- compute force components between particles ---
def compute_force(xi, yi, zi, xj, yj, zj):
    rx = xj - xi
    ry = yj - yi
    rz = zj - zi
    r = math.sqrt(rx*rx + ry*ry + rz*rz)
    F = force_LJ(r)
    Fx = F * rx / r
    Fy = F * ry / r
    Fz = F * rz / r
    return Fx, Fy, Fz

# --- initial force ---
Fix, Fiy, Fiz = compute_force(xi, yi, zi, xj, yj, zj)
Fxj, Fyj, Fzj = -Fix, -Fiy, -Fiz

# --- open XYZ trajectory file ---
traj = open("traj.xyz", "w")

# ============================
#      VELOCITY VERLET LOOP
# ============================

for step in range(10000):

    # --- update positions ---
    xi += vxi*dt + 0.5*(Fix/i_mass)*dt*dt
    yi += vyi*dt + 0.5*(Fiy/i_mass)*dt*dt
    zi += vzi*dt + 0.5*(Fiz/i_mass)*dt*dt

    xj += vxj*dt + 0.5*(Fxj/j_mass)*dt*dt
    yj += vyj*dt + 0.5*(Fyj/j_mass)*dt*dt
    zj += vzj*dt + 0.5*(Fzj/j_mass)*dt*dt

    # --- compute new forces ---
    Fix_new, Fiy_new, Fiz_new = compute_force(xi, yi, zi, xj, yj, zj)
    Fxj_new, Fyj_new, Fzj_new = -Fix_new, -Fiy_new, -Fiz_new

    # --- update velocities ---
    vxi += 0.5 * (Fix + Fix_new) / i_mass * dt
    vyi += 0.5 * (Fiy + Fiy_new) / i_mass * dt
    vzi += 0.5 * (Fiz + Fiz_new) / i_mass * dt

    vxj += 0.5 * (Fxj + Fxj_new) / j_mass * dt
    vyj += 0.5 * (Fyj + Fyj_new) / j_mass * dt
    vzj += 0.5 * (Fzj + Fzj_new) / j_mass * dt

    # --- replace old forces ---
    Fix, Fiy, Fiz = Fix_new, Fiy_new, Fiz_new
    Fxj, Fyj, Fzj = Fxj_new, Fyj_new, Fzj_new

    # --- save trajectory frame (XYZ format) ---
    traj.write("2\n")
    traj.write(f"step={step}\n")
    traj.write(f"Ar {xi} {yi} {zi}\n")
    traj.write(f"Ar {xj} {yj} {zj}\n")

    # --- store for plotting ---
    Xi_p.append(xi)
    Yi_p.append(yi)
    Zi_p.append(zi)

    Xj_p.append(xj)
    Yj_p.append(yj)
    Zj_p.append(zj)

traj.close()

# --- simple 3D plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(Xi_p, Yi_p, Zi_p)
ax.plot(Xj_p, Yj_p, Zj_p)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
