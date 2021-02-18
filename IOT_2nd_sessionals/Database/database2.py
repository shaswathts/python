import sqlite3

conn = sqlite3.connect('Shash.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 1, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 2, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 3, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 4, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 5, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 6, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 7, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 8, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 9, 'same', 'same', 'same', 'same', 'same'))
cur.execute('INSERT INTO Shaswath (one , two , three , four , five , six , seven , eight , nine , ten ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
    ('same','same','same','same', 10, 'same', 'same', 'same', 'same', 'same'))


conn.commit()

print('Shaswath:')
cur.execute('SELECT one,two,three,four,five,six,seven,eight,nine,ten FROM Shaswath')
for row in cur:
     print(row)

cur.execute('DELETE FROM Shaswath WHERE five > 10')
conn.commit()

cur.close()
