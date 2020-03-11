'''
CS 331
Ben Webb
Project 1
'''

import sys

def main():
    # ip = input("Enter IP address: ")
    ip = "255.0.0.255"
    ip = ip.split('.')
    bip = int('{:08b}{:08b}{:08b}{:08b}'.format(*map(int,ip)),2)
    ip = [int(i) for i in ip]

    # prefix = int(input("Enter prefix length: "))
    prefix = 32
    # print (bin(2**32-1), bin(2**prefix-1))
    mask = 2**prefix-1
    print(mask & bip)
    i1, i2, i3, i4 = (mask & bip).to_bytes(4, 'little')
    print(i1, i2, i3, i4)
    print (bip, mask)


if __name__ == "__main__":
    main()