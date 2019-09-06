import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ""
port = 1233
s.bind((ip,port))

s.listen(5)

while(True):
    c,a = s.accept()
    get = c.recv(2000)
    print(get.decode())
    data = ""
    while(data != "!"):
        data = c.recv(2000).decode()
        print("client> ", data)
        get = input("server> ")
        c.send(get.encode())
    print("client disconnected")
    c.close()
s.close()
