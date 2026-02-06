import mysql.connector
conn = mysql.connector.connect(host='localhost', user='pyuser', password='12345',database='gbieda')
cur=conn.cursor()

