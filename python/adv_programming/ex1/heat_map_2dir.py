#!/bin/python
import pylab as pl
import numpy as np

# --- PARAMETRY ---
x0 = 156
c = 191
a = 39397
m = 63
x_list = []
pos = []
walk = 0

# --- FUNKCJA LEHMER ---
def Lehmer(x0, a, c, m):
    x = (x0 * a + c) % m
    return x

# --- RANDOM WALK ---
for i in range(10000):
    x0 = Lehmer(x0, a, c, m)
    x_list.append(x0)

    # decyzja: lewo / prawo
    if x0 < m / 2:
        walk -= 1
    else:
        walk += 1
    pos.append(walk)

# --- HEATMAPA (czestość odwiedzin) ---
# zliczamy, ile razy walker był na danej pozycji
min_pos = min(pos)
max_pos = max(pos)

# tworzymy histogram pozycji (1D heatmap)
counts, bins = np.histogram(pos, bins=range(min_pos, max_pos + 1))

# rysujemy jako heatmapę (kolor = częstotliwość)
pl.figure(figsize=(8, 4))
pl.imshow(counts[np.newaxis, :], cmap="plasma", aspect="auto",
           extent=[min_pos, max_pos, 0, 1])
pl.colorbar(label="Visits count")
pl.xlabel("Position")
pl.yticks([])  # ukrywamy oś Y, bo to 1D
pl.title("Heatmap of 1D Random Walk (Left/Right)")
pl.show()

