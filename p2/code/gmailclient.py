
from socket import *
from ssl import *
import base64, getpass

clientSocket = socket(AF_INET, SOCK_STREAM)
mailserver = getaddrinfo('smtp.gmail.com',465, AF_INET, SOCK_STREAM, IPPROTO_TCP)[0][4]
clientSocket = wrap_socket(clientSocket)
clientSocket.connect(mailserver)


username = input("Username: ")
password = getpass.getpass("Password: ")
print ("Connected: " , clientSocket.recv(1024).decode())
clientSocket.send('EHLO Benjamins-MacBook-Pro-5.local\r\n'.encode("ascii"))
clientSocket.recv(1024).decode()
clientSocket.send('AUTH PLAIN '.encode("ascii") +
                   base64.b64encode(('\0%s\0%s' % (username,password)).encode("ascii"))
                   + '\r\n'.encode("ascii"))
print ("Login: " + clientSocket.recv(1024).decode())


clientSocket.send(("mail FROM: <%s>\r\n" % (username)).encode("ascii"))
print ("Mail From Response: " + clientSocket.recv(1024).decode())
recipient = input("Email Address of Recipient: ")
clientSocket.send(("RCPT TO: <%s>\r\n" % (recipient)).encode("ascii"))
print ("Recipient Response: ", clientSocket.recv(1024).decode())
subject = input("Subject: ")
msg = input("\nMessage:\n\t")
clientSocket.send("DATA\r\n".encode("ascii"))
print ("\nTransmitting Message", clientSocket.recv(1024).decode())
clientSocket.send(("Subject: %s\r\n\r\n %s \r\n.\r\n" % (subject, msg)).encode("ascii"))
print ("Message Sent: ", clientSocket.recv(1024).decode())
clientSocket.send("QUIT\r\n".encode())
print ("Quit: ", clientSocket.recv(1024).decode())
