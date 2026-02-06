x=input("Podaj swoje imię:")
print("Podane przez ciebie imię to", x)
y=(input("Czy to naprawdę Twoje imię? Tak/Nie:"))

if y== "Tak":
    print("Bardzo się cieszę, że podałeś prawdziwe imię")
elif y=="Nie":
    print("Przykro mi, że zostałam oszukana")
else:
    print("Hej, nie odpowiadasz mi na moje pytanie!")