#To retrive data or order the table 
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

#cur.execute('SELECT * FROM Tracks ORDER BY plays')

print('Tracks:')
cur.execute('SELECT * FROM Tracks ORDER BY title')
for row in cur:
    print(row)

conn.commit()
conn.close()
