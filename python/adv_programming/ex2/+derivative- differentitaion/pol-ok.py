#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# siatka x na [0, 2]
n = 100
x = np.linspace(0, 2, n)

# f(x) = 11x^3 - 3x^2 - 7x + 13
fx = 11*x**3 - 3*x**2 - 7*x + 13

# pochodna numeryczna
fprime_num = np.gradient(fx, x)

# pochodna analityczna: f'(x) = 33x^2 - 6x - 7
fprime_anal = 33*x**2 - 6*x - 7

plt.figure(figsize=(8, 6))
plt.plot(x, fx, label=r"$f(x)=11x^3-3x^2-7x+13$")
plt.plot(x, fprime_num, linestyle="--", label="f'(x) numerical")
plt.plot(x, fprime_anal, linestyle=":", label="f'(x) analytical")

plt.title("polynomial derivative")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.show()
