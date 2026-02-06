#!/usr/bin/python3
import numpy as np
A=np.zeros((3,3))
#print(A)
B=np.ones((1,4))
#print(B)
C=np.array([1,7,14,21,4,2,3])
#print(C)
D=np.append(C,7)
#print(D)
D=np.reshape(D,[2,4])
#print(D)
E=[1,2,3,4,5,6,7,8]
E=np.reshape(E,[4,2])
#print(E)
P=D@E
#print(P)
F=np.dot(D,E)
#print(F)
#G=np.cross(D,E)
#print(G)
H=[1,2,3,4]
I=H*2
#print(I)
J=np.array(H)
K=2*J
#print(K)
L=np.arange(1,10,0.1)
#print(L)
M=np.linspace(1,10,371)
#M=len(M)
#print(M)
BB=np.linspace(-np.pi,-np.pi,10)
#print(X)
BBB=np.sin(BB)
#print(Y)

import matplotlib.pyplot as plt
import numpy as np

# Tworzymy zakresy x i y (od -20 do 20, 1000 punktów każdy)
x = np.linspace(-20, 20, 1000)
y = np.linspace(-20, 20, 1000)

# Tworzymy siatkę 2D współrzędnych (każda para x, y)
X, Y = np.meshgrid(x, y)

# Obliczamy wartości Z na podstawie wzoru funkcji
Z = np.sin(np.sqrt((X**2) + (Y**2)))

# Tworzymy nową figurę 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Rysujemy powierzchnię 3D
surf = ax.plot_surface(X, Y, Z, cmap='winter', edgecolor='none')

# Dodajemy tytuł i podpisy osi
ax.set_title("3D Shine Surface")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Dodajemy pasek kolorów
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Wyświetlamy wykres
plt.show()
