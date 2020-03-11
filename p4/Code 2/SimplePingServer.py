# SimplePingServer.py
# Ying Li
# 08/29/2019

import socket
import random

def main():
    """ create a simple ping server """
    
    # create a UDP socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # assign IP address and port number to socket
    serverSocket.bind(('', 12345))
    
    while True:
        # receive the client packet from port 8000, the packet includes a 
        # message and the address of the ping client  
        message, address = serverSocket.recvfrom(8000)

        # add a delay to the response time
        for i in range(1000000):
            continue
            
        # generate random number between 1 and 10
        rand = random.randint(1, 11)
        # if rand is less than 3, we consider the packet is lost and do not 
        # respond to the ping client
        if rand < 3:
            continue
            
        # otherwise, the server responds
        serverSocket.sendto(message, address)
        
if __name__ == "__main__":
    main()