# Using the prefeared method as per assignment guidlines or using python to retrive data from the web

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

#mysock.close()

# using "TELNET" method to hack into the web and retrive the data
# step 1:- telnet data.pr4e.org 80
# step 2:- hit enter
# step 3:- type GET (URL) and hit enter twice
# step 4:- output
