import socket
url=input('Enter URL: ')

try:
    host=url.split('/')
    host=host[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd='GET '+url+' HTTP/1.0\r\n\r\n'
    cmd =cmd.encode()
    mysock.send(cmd)

    count=0
    while True:
        data = mysock.recv(500)
        data=data.decode()
        count=count+len(data)
        if len(data) < 1 :
            break
        if count <= 3000 :
            print(data,end='')

    mysock.close()
    print('\r\n\r\nNumber of characters:', count)

except:
    print('Invalid URL')
    quit()
