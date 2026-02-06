
def dodaj (x,y):
    return x+y
def odejmij (x,y):
        return x-y
def pomnóż (x,y):
    return x*y
def podziel (x,y):
    return x/y
def potęgowanie (x,y):
    return x**y

print("Wybierz operację liczbową:")
print("""1.Dodawanie
2.Odejmowanie
3.Mnożenie
4.Dzielenie
5.Potęgowanie""")

choice=input("Którą operację chcesz wykonać? Wybierz(1/2/3/4/5):")

num1=float(input("Podaj pierwszą wartość:"))
num2=float(input("Podaj drugą wartość:"))

if choice == '1':
    print(num1,"+", num2, "=", dodaj (num1,num2))
elif choice == '2':
    print(num1,"-", num2, "=", odejmij(num1,num2))
elif choice == '3':
    print(num1,"*", num2, "=", pomnóż (num1,num2))
elif choice == '4':
    print(num1,"/", num2, "=", podziel(num1,num2))
elif choice == '5':
    print(num1,"^", num2, "=", potęgowanie(num1,num2))
    
else:
    print("Niepoprawna wartość")

print("Czy chcesz dodać kolejną wartość do równania? (t/n):")
