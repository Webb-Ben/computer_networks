import socket

SMTPserver = socket.socket()
SMTPserver.bind(('localhost', 3000))
SMTPserver.listen(1)
process = ['220 localhost SMTP Postfix', '250 localhost, ', '250 Ok', '354 End data with <CR><LF>.<CR><LF>']
c, a = SMTPserver.accept()
i = 0
while True:
    c.sendall(process[i].encode())
    recv = c.recv(1024).decode()
    print (recv)
    if recv.split()[0].upper() == "HELO":
        i = 1
        process[i] += recv
    elif recv.split()[0].upper() == "MAIL FROM":
        i = 2