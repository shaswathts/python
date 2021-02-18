import sqlite3

conn = sqlite3.connect('shash.sqlite')
cur = conn.cursor()

cur.execute('UPDATE Shaswath SET one = "Shaswath" WHERE five = "1"')
cur.execute('UPDATE Shaswath SET one = "Shash" WHERE five = "2"')
cur.execute('UPDATE Shaswath SET one = "Shaswath TS" WHERE five = "3"')
conn.commit()

print('Number:')
cur.execute('SELECT one,two,three,four,five,six,seven,eight,nine,ten FROM Shaswath')
for row in cur:
     print(row)


conn.commit()

cur.close()


