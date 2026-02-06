#!/usr/bin/python
import pylab as pl
from matplotlib.animation import FuncAnimation

#generator
x0, c, a, m = 1670, 31543, 12807, 31672
def Lehmer(x0, a, c, m): return (x0*a + c) % m

#ścieżka 20x20
N_STEPS = 2000
x_cor, y_cor = 10, 10
x_path, y_path = [], []

for _ in range(N_STEPS):
    x0 = Lehmer(x0, a, c, m)
    if x0 <= 0.25*m:       x_cor -= 1        # left
    elif x0 <= 0.50*m:     y_cor += 1        # up
    elif x0 <= 0.75*m:     x_cor += 1        # right
    else:                  y_cor -= 1        # down
    # wrap-around
    if x_cor < 0: x_cor = 19
    if x_cor > 19: x_cor = 0
    if y_cor < 0: y_cor = 19
    if y_cor > 19: y_cor = 0
    x_path.append(x_cor); y_path.append(y_cor)

#rysunek
fig, ax = pl.subplots()
ax.set_xlim(-0.5, 19.5); ax.set_ylim(-0.5, 19.5)
ax.set_aspect("equal"); ax.grid(True, alpha=0.3)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_title("Random walk 2D (LCG) — animacja")

(line,)  = ax.plot([], [], "b-", lw=1, alpha=0.8)
(point,) = ax.plot([], [], "ro", ms=6)

def init():
    line.set_data([], []); point.set_data([], [])
    return line, point

def update(frame):
    
    line.set_data(x_path[:frame], y_path[:frame])
    point.set_data(x_path[frame-1], y_path[frame-1])
    return line, point

ani = FuncAnimation(fig, update, frames=range(1, len(x_path)+1),
                    init_func=init, interval=30, blit=False, repeat=False)

pl.show()

