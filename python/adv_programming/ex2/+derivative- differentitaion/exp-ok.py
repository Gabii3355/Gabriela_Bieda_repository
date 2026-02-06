#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# siatka x na [0, 5]
n = 100
x = np.linspace(0, 5, n)

# funkcja f(x)=exp(x)
fx = np.exp(x)

# pochodna numeryczna f'(x) ~ d/dx exp(x)
fprime_num = np.gradient(fx, x)

# pochodna analityczna f'(x)=exp(x)
fprime_anal = np.exp(x)

plt.figure(figsize=(8, 6))
plt.plot(x, fx, label="f(x)=exp(x)")
plt.plot(x, fprime_num, linestyle="--", label="f'(x) numerical")
plt.plot(x, fprime_anal, linestyle=":", label="f'(x) analytical")

plt.title("exp(x) derivative")
plt.xlabel("x")
plt.ylabel("value")
plt.grid(True)
plt.legend()
plt.savefig('exp-ok.png', dpi=300, bbox_inches='tight')
plt.show()
