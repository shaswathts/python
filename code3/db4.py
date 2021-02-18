import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DELETE FROM Tracks WHERE title = "wath"')
conn.commit()
conn.close()