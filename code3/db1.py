import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Racecar')
cur.execute('CREATE TABLE Racecar (title TEXT, plays INTEGER)')

conn.close()
