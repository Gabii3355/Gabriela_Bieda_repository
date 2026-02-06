#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Parametry generatora Lehmera
a = 16807
c = 2
m = 2147483500

#Różne seedy
x0     = 150   # P1
x0_2   = 100   # P2
x0_dec = 777   # decyzja 90/10

#Plansza
W = H = 20

#Pozycje startowe
sx1, sy1 = 10, 10   # start P1
sx2, sy2 = 5,  5    # start P2
x_cor,  y_cor  = sx1, sy1
x_cor2, y_cor2 = sx2, sy2

#Trajektorie i RNG historia
x_list = []
x_l,  y_l  = [], []   # P1
x_l2, y_l2 = [], []   # P2

#heatmap
heatmap = np.zeros((H, W))

def Lehmer(x, a, c, m):
    return (x * a + c) % m

def step_move(x_rand, x, y):
    # 8 kierunków 
    if   x_rand <= 0.15 * m:      # LEFT
        x -= 1
    elif x_rand <= 0.25 * m:      # DOWN-LEFT
        x -= 1; y -= 1
    elif x_rand <= 0.40 * m:      # DOWN
        y -= 1
    elif x_rand <= 0.50 * m:      # DOWN-RIGHT
        x += 1; y -= 1
    elif x_rand <= 0.65 * m:      # RIGHT
        x += 1
    elif x_rand <= 0.75 * m:      # UP-RIGHT
        x += 1; y += 1
    elif x_rand <= 0.90 * m:      # UP
        y += 1
    else:                         # UP-LEFT
        x -= 1; y += 1
    # wrap-around
    return x % W, y % H

#Flaga piggy-back
together = False

#Symulacja
N = 40000
for _ in range(N):
    if not together:
        # P1
        x0 = Lehmer(x0, a, c, m); x_list.append(x0)
        nx1, ny1 = step_move(x0, x_cor, y_cor)
        # P2
        x0_2 = Lehmer(x0_2, a, c, m)
        nx2, ny2 = step_move(x0_2, x_cor2, y_cor2)

        x_cor,  y_cor  = nx1, ny1
        x_cor2, y_cor2 = nx2, ny2

        x_l.append(x_cor);   y_l.append(y_cor)
        x_l2.append(x_cor2); y_l2.append(y_cor2)

        heatmap[y_cor,  x_cor]  += 1
        heatmap[y_cor2, x_cor2] += 1

        if x_cor == x_cor2 and y_cor == y_cor2:
            together = True

    else:
        # 90% dalej razem, 10% rozłączenie
        x0_dec = Lehmer(x0_dec, a, c, m)
        continue_together = (x0_dec < 0.9 * m)

        if continue_together:
            # P1 follow P2: ruch wg RNG P2
            x0_2 = Lehmer(x0_2, a, c, m)
            nx, ny = step_move(x0_2, x_cor2, y_cor2)

            x_cor,  y_cor  = nx, ny
            x_cor2, y_cor2 = nx, ny

            x_l.append(x_cor);   y_l.append(y_cor)
            x_l2.append(x_cor2); y_l2.append(y_cor2)

            heatmap[y_cor, x_cor] += 2  # wspólny krok = 2

        else:
            # Rozłączenie – niezależne ruchy
            x0 = Lehmer(x0, a, c, m); x_list.append(x0)
            nx1, ny1 = step_move(x0, x_cor, y_cor)

            x0_2 = Lehmer(x0_2, a, c, m)
            nx2, ny2 = step_move(x0_2, x_cor2, y_cor2)

           
            if nx1 == nx2 and ny1 == ny2:
                x0_2 = Lehmer(x0_2, a, c, m)
                nx2, ny2 = step_move(x0_2, nx2, ny2)

            x_cor,  y_cor  = nx1, ny1
            x_cor2, y_cor2 = nx2, ny2

            x_l.append(x_cor);   y_l.append(y_cor)
            x_l2.append(x_cor2); y_l2.append(y_cor2)

            heatmap[y_cor,  x_cor]  += 1
            heatmap[y_cor2, x_cor2] += 1

            together = False


#  Pomocnicze: segmenty bez mostów
def segmented_no_wrap(xs, ys):
    """Zwraca wektory z NaN wstawionymi tam, gdzie był wrap (|Δ|>1)."""
    if len(xs) == 0:
        return np.array([]), np.array([])
    out_x = [xs[0]]
    out_y = [ys[0]]
    for i in range(1, len(xs)):
        dx = abs(xs[i] - xs[i-1])
        dy = abs(ys[i] - ys[i-1])
       
        if dx > 1 or dy > 1:
            out_x.append(np.nan)
            out_y.append(np.nan)
        out_x.append(xs[i])
        out_y.append(ys[i])
    return np.array(out_x), np.array(out_y)

#   ANIMACJA
fig, ax = plt.subplots(figsize=(6, 6))

# siatka 20x20
ax.set_xlim(-0.5, W-0.5)
ax.set_ylim(-0.5, H-0.5)
ax.set_xticks(np.arange(-0.5, W, 1))
ax.set_yticks(np.arange(-0.5, H, 1))
ax.grid(True, which='both', linewidth=0.5)
ax.set_xlabel("X position"); ax.set_ylabel("Y position")
ax.set_title("2D Random Walk — piggy-back (no wrap lines)")

# zaznaczone starty
start1 = ax.scatter([sx1], [sy1], s=140, facecolors='none', edgecolors='b', linewidths=2, label="Start P1")
start2 = ax.scatter([sx2], [sy2], s=140, facecolors='none', edgecolors='r', linewidths=2, label="Start P2")

# ścieżki i aktualne pozycje
line1, = ax.plot([], [], 'b-', lw=1, label="Path P1")
line2, = ax.plot([], [], 'r-', lw=1, label="Path P2")
curr1 = ax.scatter([], [], c='b', s=40)
curr2 = ax.scatter([], [], c='r', s=40)

ax.legend(loc='upper left')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    curr1.set_offsets(np.empty((0, 2)))
    curr2.set_offsets(np.empty((0, 2)))
    return line1, line2, curr1, curr2, start1, start2

def update(i):
    #trajektorie do klatki i z przerwami na wrap
    xs1, ys1 = segmented_no_wrap(x_l[:i+1],  y_l[:i+1])
    xs2, ys2 = segmented_no_wrap(x_l2[:i+1], y_l2[:i+1])
    line1.set_data(xs1, ys1)
    line2.set_data(xs2, ys2)
    curr1.set_offsets(np.array([[x_l[i],  y_l[i]]]))
    curr2.set_offsets(np.array([[x_l2[i], y_l2[i]]]))
    return line1, line2, curr1, curr2

ani = animation.FuncAnimation(
    fig, update, frames=len(x_l), init_func=init,
    interval=20, blit=False, repeat=False
)

plt.tight_layout()
plt.show()

#     HEATMAPA WSPÓLNA
plt.figure(figsize=(6,6))
plt.imshow(heatmap, cmap="hot", origin="lower")
plt.colorbar(label="Visits (solo=1, together=2)")
plt.title("Heatmap for 2 persons")
plt.xlabel("X position"); plt.ylabel("Y position")
plt.tight_layout()
plt.show()

