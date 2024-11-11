import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

i=0
while True:
    data = mysock.recv(512)
    if i == 0 :
        pos=data.find(b"\r\n\r\n")
        data=data[pos+4:]
    if len(data) < 1:
        break
    print(data.decode(),end='')
    i=i+1

mysock.close()
