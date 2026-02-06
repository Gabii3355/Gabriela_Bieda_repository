#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
#lewa suma Riemanna -> im większe n, tym lepsze przyblizenie
#numeryczne calkowanie sinx w przedziale [0,pi] metoda sum prostokatow lewych, a ppotem rysunek zbieznosci wyniku do wartosci dokladnej
def calka(n):
    #n=10
    sum_area=0
    a=math.pi/n #szerokość prostokąta
    for i in range(n):
        b=math.sin(a*i)
        p=a*b
        sum_area+=p
    return sum_area
wynik=calka(10)
print("Wynik całki: ",wynik)
x=[]
y=[]
for i in range(1,10):
    x.append(i) #liczba podziału
    y.append(calka(i)) #odpowiednie przyblizenie liczby podzialu
plt.plot(x,y) #rysuje jak wynik zblizenia rosnie i zbiega do 2 wraz ze zrostem n
plt.show()



