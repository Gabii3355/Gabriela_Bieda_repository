
import mysql.connector  # importuje bibliotekę do połączenia z bazą danych MySQL

# nawiązuje połączenie z bazą danych 'gbieda' jako użytkownik 'pyuser' z hasłem '12345'
conn = mysql.connector.connect(host='localhost', user='pyuser', password='12345', database='gbieda')

cur = conn.cursor()  # tworzy kursor — obiekt służący do wykonywania zapytań SQL

cur.execute('show databases;')  # wykonuje zapytanie SQL: pokaż wszystkie bazy danych
cur.fetchall()  # pobiera i odrzuca wyniki (czyści bufor, żeby można było wykonać kolejne zapytanie)

cur.execute('use gbieda;')  # wybiera bazę danych 'gbieda' do dalszych operacji
cur.fetchall()  # znowu czyści wynik zapytania

cur.execute('show tables;')  # zapytanie SQL: pobierz listę wszystkich tabel w bazie
result = cur.fetchall()  # pobiera wynik zapytania — listę nazw tabel
tables = []  # inicjalizuje pustą listę na nazwy tabel

for i in result:  # iteruje po wyniku zapytania (każdy element to tuple z nazwą tabeli)
    tables.append(i[0])  # dodaje nazwę tabeli (pierwszy element krotki) do listy 'tables'

total = 0  # zmienna sumująca liczbę wszystkich rekordów w bazie

for tab in tables:  # dla każdej tabeli w liście tabel
    cur.execute(f'select * from {tab}')  # wykonuje zapytanie: wybierz wszystko z danej tabeli
    result = cur.fetchall()  # pobiera wszystkie wiersze z tej tabeli
    a = len(result)  # liczy ile wierszy zostało pobranych
    total += a  # dodaje liczbę wierszy z tej tabeli do ogólnej sumy
    print(tab, a)  # wypisuje nazwę tabeli i liczbę jej rekordów

print(total)  # wypisuje łączną liczbę rekordów we wszystkich tabelach

