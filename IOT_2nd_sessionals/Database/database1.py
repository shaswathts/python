import sqlite3

conn = sqlite3.connect('shash.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Shaswath')
cur.execute('CREATE TABLE Shaswath (one TEXT, two TEXT, three TEXT, four TEXT, five INTEGER, six TEXT, seven TEXT, eight TEXT, nine TEXT, ten TEXT)')

conn.close()
