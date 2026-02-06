
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

for tab in tables:  # dla każdej tabeli w liście tabel
    cur.execute(f'show columns from {tab} where field like "%doi%"')  # pokaz mi kolumny z tabeli {tab} ktore maja doi 
    result = cur.fetchall()  # pobiera wszystkie wiersze z tej tabeli
if result:
    print(f'{tab} have column with doi')
    print(result)
