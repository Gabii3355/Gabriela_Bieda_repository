import numpy as np
import matplotlib.pyplot as plt
import math

# --- number of particles ---
N = 7

# --- box size for PBC ---
L = 10.0

# --- regular 3D grid (2×2×2 cube, take first 7 points) ---
coords = [
    (1,1,1),
    (1,1,4),
    (1,4,1),
    (4,1,1),
    (4,4,1),
    (4,1,4),
    (1,4,4)
]

x = np.array([c[0] for c in coords], float)
y = np.array([c[1] for c in coords], float)
z = np.array([c[2] for c in coords], float)

# --- initial velocities ---
vx = np.random.uniform(-0.1, 0.1, N)
vy = np.random.uniform(-0.1, 0.1, N)
vz = np.random.uniform(-0.1, 0.1, N)

# --- masses ---
m = np.ones(N)

# --- timestep ---
dt = 0.001

# --- storage for plotting ---
traj_x = [[] for _ in range(N)]
traj_y = [[] for _ in range(N)]
traj_z = [[] for _ in range(N)]

# --- Lennard-Jones force magnitude ---
def force_LJ(r):
    return -(48*r**(-13) - 24*r**(-7))

# --- minimum image convention ---
def min_image(dx):
    return dx - L * np.round(dx / L)

# --- compute force between two particles with PBC ---
def compute_force(i, j):
    rx = min_image(x[j] - x[i])
    ry = min_image(y[j] - y[i])
    rz = min_image(z[j] - z[i])

    r = math.sqrt(rx*rx + ry*ry + rz*rz)
    F = force_LJ(r)

    Fx = F * rx / r
    Fy = F * ry / r
    Fz = F * rz / r
    return Fx, Fy, Fz

# --- compute total forces on all particles ---
def compute_all_forces():
    Fx = np.zeros(N)
    Fy = np.zeros(N)
    Fz = np.zeros(N)

    for i in range(N):
        for j in range(i+1, N):
            fij = compute_force(i, j)
            Fx[i] += fij[0]
            Fy[i] += fij[1]
            Fz[i] += fij[2]

            Fx[j] -= fij[0]
            Fy[j] -= fij[1]
            Fz[j] -= fij[2]

    return Fx, Fy, Fz

# --- initial forces ---
Fx, Fy, Fz = compute_all_forces()

# --- open XYZ trajectory file ---
traj = open("traj_7atoms_pbc.xyz", "w")

# ============================
#      VELOCITY VERLET LOOP
# ============================

for step in range(10000):

    # --- update positions ---
    x += vx*dt + 0.5*(Fx/m)*dt*dt
    y += vy*dt + 0.5*(Fy/m)*dt*dt
    z += vz*dt + 0.5*(Fz/m)*dt*dt

    # --- apply PBC to positions ---
    x %= L
    y %= L
    z %= L

    # --- compute new forces ---
    Fx_new, Fy_new, Fz_new = compute_all_forces()

    # --- update velocities ---
    vx += 0.5 * (Fx + Fx_new) / m * dt
    vy += 0.5 * (Fy + Fy_new) / m * dt
    vz += 0.5 * (Fz + Fz_new) / m * dt

    # --- replace old forces ---
    Fx, Fy, Fz = Fx_new, Fy_new, Fz_new

    # --- save trajectory frame (XYZ format) ---
    traj.write(f"{N}\n")
    traj.write(f"step={step}\n")
    for i in range(N):
        traj.write(f"Ar {x[i]} {y[i]} {z[i]}\n")

    # --- store for plotting ---
    for i in range(N):
        traj_x[i].append(x[i])
        traj_y[i].append(y[i])
        traj_z[i].append(z[i])

traj.close()

# --- 3D plot ---
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(N):
    ax.plot(traj_x[i], traj_y[i], traj_z[i])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
