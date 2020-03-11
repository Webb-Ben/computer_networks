import socket
s, data = socket.socket(socket.AF_INET, socket.SOCK_STREAM), ''
s.connect(('localhost', 25))
while True:
    print(s.recv(1024).decode())
    if data.lower() == 'data':
        data = input('> ')
        s.send((data + '\r\n.\r\n').encode())
        continue
    elif data.lower() == 'quit': exit()
    data = input('> ')
    s.send((data + '\r\n').encode())
