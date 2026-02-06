#!/usr/bin/python3 
import numpy as np  
import matplotlib.pyplot as plt  # Import biblioteki do rysowania wykresów jako "plt"

# Funkcja generująca zbiór Julii
def julia_set(h_range, w_range, max_iterations):
    # Tworzymy dwie siatki współrzędnych: y i x (kompleksowe wartości na płaszczyźnie)
    y, x = np.ogrid[1.4:-1.4:h_range*1j, -1.4:1.4:w_range*1j] #h_range-wygeneruj od gory do dolu w_range-od lewo do prawo
    
    # Tworzymy macierz liczb zespolonych (z = x + iy)
    z_array = x + y * 1j
    
    # Parametr zespolony 'a' używany do generowania zbioru Julii
    a = -0.744 + 0.148j

    # Tablica do przechowywania liczby iteracji, po których punkt "ucieka" (czyli przekracza promień)
    iterations_till_divergence = max_iterations + np.zeros(z_array.shape)

    # Iterujemy po każdym punkcie na płaszczyźnie (wysokość)
    for h in range(h_range):
        # Iterujemy po każdym punkcie na płaszczyźnie (szerokość)
        for w in range(w_range):
            # Pobieramy wartość zespoloną z siatki dla punktu [h][w]
            z = z_array[h][w]
            
            # Iterujemy równanie: z = z² + a, maksymalnie przez max_iterations razy
            for i in range(max_iterations):
                z = z ** 2 + a  # Główne równanie zbioru Julii
                
                # Sprawdzamy, czy moduł z przekroczył 2 (czyli z * z.conj() > 4)
                if z * np.conj(z) > 4:
                    # Zapisujemy numer iteracji, w której nastąpiło "ucieczka"
                    iterations_till_divergence[h][w] = i
                    break  # Kończymy iterację, bo punkt już uciekł

    # Zwracamy gotową tablicę z informacjami, kiedy punkt uciekał
    return iterations_till_divergence

# Wywołanie funkcji julia_set z dużą rozdzielczością: 2000x2000 punktów, max 70 iteracji
plt.imshow(julia_set(2000, 2000, 70), cmap='twilight_shifted')  # Rysujemy obraz z kolorem 'twilight_shifted'
plt.axis('off')     # Wyłączamy osie (żeby nie pokazywało skali wokół obrazka)
plt.show()          # Pokazujemy wykres na ekranie
plt.close()         # Zamyka wykres po pokazaniu (czyści pamięć)
