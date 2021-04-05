#!/bin/python3

import socket
import argparse

parser = argparse.ArgumentParser(description='Simple script to resolve host name to ip address and vice versa')
parser.add_argument("-n" , "--name" , help='Enter your host name')
parser.add_argument("-a" , "--address" , help='Enter your ip address')
args = parser.parse_args()
name = args.name
address = args.address


if args.name :
    print(socket.gethostbyname(name))
elif args.address:
    print("Your host name is : " + socket.gethostbyaddr(address)[0] )

    print("Your IP was : " + socket.gethostbyaddr(address)[2][0] )


