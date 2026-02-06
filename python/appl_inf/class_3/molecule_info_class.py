#!/usr/bin/python3 

# Definicja klasy Molecule, która przechowuje atomy i oblicza centrum masy i geometrii
class Molecule:
    def __init__(self):
        self.atoms = []  # Inicjalizujemy pustą listę, gdzie będą przechowywane dane o atomach

    def read_molecule(self, filename):
        fp = open(filename, 'r')  # Otwieramy plik XYZ w trybie odczytu
        lines = fp.readline()     # Pierwsza linia to liczba atomów
        fp.readline()             # Druga linia to komentarz – pomijamy ją

        a = 0  # Licznik atomów
        d = {'C': 12, 'O': 16, 'H': 1}  # Słownik z masami atomowymi pierwiastków

        while a < int(lines):  # Czytamy tyle wierszy, ile podano w pierwszej linii
            a += 1
            l = fp.readline()         # Czytamy kolejną linię z danymi atomu
            column = l.split()        # Dzielimy linię na kolumny (np. C 0.0 0.0 0.0)

            # Tworzymy słownik dla danego atomu i dodajemy do listy
            self.atoms.append({
                'elem': column[0],             # Symbol pierwiastka
                'x': float(column[1]),         # Współrzędna X
                'y': float(column[2]),         # Współrzędna Y
                'z': float(column[3]),         # Współrzędna Z
                'mass': d[column[0]]           # Masa atomowa z tabeli d
            })

        fp.close()  # Zamykamy plik

    def get_com(self):  # Obliczanie środka masy (Center of Mass)
        x = y = z = M = 0  # Inicjalizacja sum i całkowitej masy

        for atom in self.atoms:  # Dla każdego atomu w cząsteczce
            mass = atom['mass']
            x += atom['x'] * mass  # Sumujemy x * masa
            y += atom['y'] * mass
            z += atom['z'] * mass
            M += mass              # Sumujemy całkowitą masę

        return [x/M, y/M, z/M]  # Zwracamy średnią ważoną – środek masy

    def get_cog(self):  # Obliczanie środka geometrii (Center of Geometry)
        x = y = z = a = 0  # Inicjalizacja sum i licznika atomów

        for atom in self.atoms:
            x += atom['x']
            y += atom['y']
            z += atom['z']
            a += 1  # Zliczamy liczbę atomów

        return [x/a, y/a, z/a]  # Zwracamy zwykłą średnią – środek geometrii

# Uruchamiany tylko, gdy plik jest wykonywany bezpośrednio (nie importowany)
if __name__ == "__main__":
    filename = input("Give the name of the file: ")  # Użytkownik podaje nazwę pliku XYZ
    mol = Molecule()  # Tworzymy nowy obiekt klasy Molecule
    mol.read_molecule(filename)  # Wczytujemy dane z pliku

    print("I split the file into given columns: ", mol.atoms)  # Wyświetlamy dane atomów
    print("Your average centre mass is: ", mol.get_com())      # Wyświetlamy środek masy
    print("Your average number of x,y,z is: ", mol.get_cog())  # Wyświetlamy środek geometrii













































