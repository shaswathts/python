import sqlite3

conn = sqlite3.connect('shash.sqlite')
cur = conn.cursor()

cur.execute('DELETE FROM Shaswath WHERE five = 2')
conn.commit()
conn.close()