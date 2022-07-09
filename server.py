import socket
table={
         '192.168.2.1':'1E.4A.4A.11',
         '192.165.3.1':'1A.5B.6W.01',
         '139.165.2.1':'1B.4A.7D.32',
         }
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',999))
s.listen(4)
clientsocket,address=s.accept()
print("connection from",address,"has established")
ip= clientsocket.recv(1024)
ip=ip.decode("utf-8")
mac=table.get(ip,'no entry of address')
clientsocket.send(mac.encode())
