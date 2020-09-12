from socket import *
HOST='localhost'
HOSTPORT=9000
BUFSIZE=1024
ADDRESS=(HOST,HOSTPORT)
client=socket(AF_INET,SOCK_STREAM)
client.connect(ADDRESS)
while True:
    data=input()
    if not data:
        break
    client.send(data.encode('utf-8'))
    data=client.recv(BUFSIZE)
    print('Receice from {} : {}'.format(ADDRESS, data.decode('utf-8')))
    if not data:
        break

client.close()

