from socket import *
HOST=''
PORT=9000
BUFSIZE=1024
ADDRESS=(HOST,PORT)
server=socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
print('Server Listening{}:{}'.format(ADDRESS[0],ADDRESS[1]))
server.listen(5)
try:
    while True:
        clientSocket,clientAddress=server.accept()
        print('1 Client connected:{}'.format(clientAddress))
        try:
            while True:
                data=clientSocket.recv(BUFSIZE)
                if data:
                    print('Receive data:{}'.format(data.decode('utf-8')))
                    print('*'*10)
                    clientSocket.send(data)
                else:
                    break
        finally:
            print('Client disconnected')
            clientSocket.close()
finally:
    print('Server closed')
    server.close()