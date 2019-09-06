import socket

s =socket.socket()
ip = '127.0.0.1'
port = 1233
s.connect((ip,port))

s.send('<Handshake done>'.encode())

data =""
while (data != '!'):
    data = input("client> ")
    s.send(data.encode())
    get = s.recv(2000)
    print("server> ",get.decode())

print("Disconnected")
s.close()


