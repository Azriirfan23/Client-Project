import socket
import sys
import json

s = socket.socket()

port = 8080

s.connect(('192.168.179.4', port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client!');

dataJ = json.loads(data)

print (type(dataJ))
print(dataJ)

while True:
   Input = input('Answer ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
        c, addr = s.accept()
        c.sendall(bytes(sendData,encoding="utf-8"))
        buffer = c.recv(1024)
        print(buffer)


s.close()

