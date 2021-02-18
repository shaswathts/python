import socket
host = socket.gethostname() 
port = 23456
s = socket.socket() 
s.connect((host, port))
s.sendall(b'I WANT TO WRITE IoT LAB SESSIONALS')
s.sendall(b'I AM STARTING THE TEST') 
data = s.recv(1024) 
s.close()
print(repr(data))