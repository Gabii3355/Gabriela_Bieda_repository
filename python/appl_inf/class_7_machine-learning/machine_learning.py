#!/usr/bin/python3

# Importujemy potrzebne biblioteki
import random
import matplotlib.pyplot as plt

# Parametr uczenia (learning rate)
lr = 0.06

# Dane treningowe (X - wejście, Y - oczekiwane wyjście)
X = [1, 2, 3, 4]
Y = [1, 3, 5, 7]

# Wartości testowe (do późniejszej walidacji)
xt = [5, 6, 7, 8]
yt = [9, 11, 13, 15]

# Inicjalizacja wag modelu (losowe wartości startowe)
w = random.random()   # współczynnik kierunkowy (nachylenie)
b = random.random()   # bias (przesunięcie wykresu)

# Listy do zapamiętywania zmian wag i biasu
lw = []  # wartości w w każdej iteracji
lb = []  # wartości b
la = []  # numery iteracji

# Uczenie modelu przez 100 losowych próbek (Stochastic Gradient Descent)
for a in range(100):
    i = random.randint(0, len(X)-1)  # losowy indeks próbki treningowej
    result = w * X[i] + b            # przewidywana wartość modelu
    error = Y[i] - result            # błąd predykcji
    
    # Aktualizacja wag według gradientu błędu (regresja liniowa)
    w += error * X[i] * lr           # aktualizacja współczynnika kierunkowego
    b += error * lr                  # aktualizacja biasu

    # Zapisz aktualne wartości w, b i numer iteracji
    lw.append(w)
    lb.append(b)
    la.append(a)

# Sprawdzenie działania modelu na losowym przykładzie testowym
ii = random.randint(0, len(xt)-1)
result = w * xt[ii] + b              # przewidywanie na podstawie wytrenowanego modelu
error = yt[ii] - result              # błąd predykcji
print(error)                         # wypisz błąd

# Rysowanie zmian wag w czasie
plt.plot(la, lw, label='w')          # wykres wagi w
plt.plot(la, lb, label='b')          # wykres biasu b
plt.legend()
plt.show()
