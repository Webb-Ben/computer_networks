# SimplePingClient.py
# Ben Webb
# Professor Li
# CS331
# 11/12/2019

import socket
import statistics as st
import sys
import time
from math import inf


def main(argv):
    # Define default settings
    SERVER_ADDR = 'localhost'
    SERVER_PORT = 12345
    TTL = 55
    VERBOSE = False
    MAX_PACKETS = inf

    # Process flags
    if len(argv) > 1:
        for i in range(len(argv)):
            if argv[i] == '-T':
                TTL = int(argv[i+1])
            elif argv[i] == '-A':
                VERBOSE = True
            elif argv[i] == '-P':
                SERVER_PORT = int(argv[i+1])
            elif argv[i] == '-C':
                MAX_PACKETS = int(argv[i+1])

    # Create UDP socket and send first datagram to find server IP address
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.sendto(''.encode(), (SERVER_ADDR, SERVER_PORT))
    clientSocket.settimeout(TTL / 1000)
    try:
        _, address = clientSocket.recvfrom(8000)
        print('PING %s (%s): 56 data bytes' % (SERVER_ADDR, address[0]))
    except socket.timeout:
        var = None

    # Initialize variables for the loop
    RTT = []
    PACKETS_SENT = 0
    PACKETS_RECV = 0
    PACKETS_LOST = 0
    startTime = time.time()

    # Loop until exit criteria are met (max packets or KeyboardInterrupt)
    try:
        while PACKETS_SENT < MAX_PACKETS:

            # Send packet and record time when sent
            clientSocket.sendto(''.encode(), ('', SERVER_PORT))
            sendTime = time.time()

            # Receive datagram from server and print to terminal
            try:
                message, address = clientSocket.recvfrom(8000)
                RTT.append((time.time() - sendTime)*1000)
                print('64 bytes from %s: icmp_seq=%i ttl=%i time=%.3f ms' %
                      (address[0], PACKETS_SENT, TTL, RTT[PACKETS_SENT-PACKETS_LOST]))
                PACKETS_RECV += 1

            # If packet is lost (timeout exception occurs), print loss message
            except socket.timeout:
                if VERBOSE: print('56 bytes lost: icmp_seq=%i ttl=%i' % (PACKETS_SENT, TTL))
                PACKETS_LOST += 1

            # Sleep and continue loop
            time.sleep(1-time.time()+sendTime - 0.00765)
            PACKETS_SENT += 1

    except KeyboardInterrupt:
        var = None

    # Print statistics summary at the end of the program.
    print('--- %s ping statistics --' % SERVER_ADDR)
    print('%i packets transmitted, %i packets received, %.2f%% packet loss, time %.0f ms' %
          (PACKETS_SENT, PACKETS_RECV, (PACKETS_LOST / PACKETS_SENT) * 100, (time.time()-startTime)*1000))
    print('round-trip min/avg/max/stddev = %.3f/%.3f/%.3f/%.3f ms' % (min(RTT), st.mean(RTT), max(RTT), st.stdev(RTT)))


if __name__ == "__main__":
    main(sys.argv)
