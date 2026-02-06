import numpy as np
import matplotlib.pyplot as plt

# Funkcja wykładnicza
def f(x):
    return np.exp(x)

# Analityczna pochodna
def df_exact(x):
    return np.exp(x)

# Siatka punktów z krokiem 
x = np.arange(0,50.01,0.1)
y = f(x)
y_derivative_exact = df_exact(x)

# Pochodna numeryczna metodą różnic centralnych
dy_dx = np.zeros_like(x, dtype=float)
dy_dx[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])
dy_dx[0] = (y[1] - y[0]) / (x[1] - x[0])       # różnica w przód
dy_dx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # różnica w tył

# Wspólny wykres
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = exp(x)', color='blue')
plt.plot(x, y_derivative_exact, label="f'(x) analityczna", color='green', linestyle='--',)
plt.plot(x, dy_dx, label="f'(x) numeryczna", color='red', linestyle=':')
plt.scatter(x, y, color='black', label='punkty siatki')

plt.title('exp(x), pochodna analityczna i numeryczna (krok 50)')
plt.xlabel('x')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

