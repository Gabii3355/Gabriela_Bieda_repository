#!/bin/python
import pylab as pl

#1 Lehmer w kodzie Python ze stałymi a,c,m
##all round of m
#x0=156
#a=39397
#c=191
#m=63
##idk
#x0=180
#c=223
#a=12863
#m=749274
##totally random numbers added to a c m x0
#x0=100
#a=19
#c=21
#m=33
##blizej 1000 powtórzeń
x0=37
a=65
m=997
c=71
##gpt idea
#x0=150
#a=16807
#c=2
#m=2147483500
##gpt idea 2
#x0= 150
#a=12807
#c=31672
#m=31543
x_list=[]
def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range (0,2000):
    X=Lehmer(x0,a,c,m)
    #prev_x0 = x0
    x0=X #po kazdym obliczeniu x staje sie ono x0 do kolejnych obliczen
    x_list.append(X)
    #print(f"Iteracja {i+1}: poprzednie x0 = {prev_x0}, nowe x = {X}")
print(x_list)

#2 period of generator -> co ile powtarza się dana liczba i jaka
len_list= len(x_list)
X_index_num=[]
for i in range (0,len_list):
    X_index_num.append(i)
print(f'Length of the list: {len_list}')

for i in range(1,len_list):
    if x_list[0] == x_list[i]:
        print(f"Liczba {x_list[0]} powtórzyła się po {i} krokach (indeksach).")
        break
else:
    print("Brak powtórzeń w liście.")

#3 znaleźć a i c ktore generuja max liczbe roznych wartosci (period)  zanim liczby sie zapetlą
'''
x0=156
a=39397
c=191
m=63
'''
#4 wykres 

pl.plot(X_index_num,x_list,"b.")
pl.xlabel("X index")
pl.ylabel("x list")
pl.title("Lehmer generator")
pl.show()
