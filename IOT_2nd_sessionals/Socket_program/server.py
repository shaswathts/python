import socket 
host = socket.gethostname() 
port = 23456 
s = socket.socket() 
s.bind((host, port)) 
s.listen(5) 
conn, addr = s.accept() 
print('Got connection from ',addr[0], '(', addr[1], ')') 
print('I AM GIVING IoT LAB SESSIONALS') 
print('I AM THE INVIGILATOR')

while True:  
   data = conn.recv(1024)    
   if not data: break    
   conn.sendall(data) 
conn.close()