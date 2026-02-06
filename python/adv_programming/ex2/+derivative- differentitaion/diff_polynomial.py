import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji f(x)
def f(x):
    return 11 * x**3 - 3 * x**2 - 7 * x + 13

# Analityczna pochodna f'(x)
def df_exact(x):
    return 33 * x**2 - 6 * x - 7

# Siatka punktów z krokiem 0.2
x = np.arange(0, 2.01, 0.2)
y = f(x)
y_derivative_exact = df_exact(x)

# Pochodna numeryczna metodą różnic centralnych
dy_dx = np.zeros_like(x)
dy_dx[1:-1] = (y[2:] - y[:-2]) / (x[2:] - x[:-2])
dy_dx[0] = (y[1] - y[0]) / (x[1] - x[0])       # różnica w przód
dy_dx[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])  # różnica w tył

# Wspólny wykres
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)', color='blue')
plt.plot(x, y_derivative_exact, label="f'(x) analityczna", color='green', linestyle='--')
plt.plot(x, dy_dx, label="f'(x) numeryczna", color='red', linestyle=':')

plt.title('f(x), pochodna analityczna i numeryczna [0, 2]')
plt.xlabel('x')
plt.ylabel('value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

