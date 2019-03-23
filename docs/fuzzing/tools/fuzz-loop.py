#!/usr/bin/python

# Author: Tyler Bennett
# taken from various sources online and offsec
# I just wanted to make it less patch-work

from __future__ import print_function

import socket
import argparse

def fuzz(args):
    buffer=["A"]
    counter=100
    while len(buffer) <= 30:
    	buffer.append("A"*counter)
    	counter = counter + args.step

    for string in buffer:
        try:
            print("Fuzzing application with %s bytes" % len(string))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _ = s.connect((args.address,args.port))
            s.recv(1024)
            s.send(string + '\r\n')
        except:
            print("Could not connect")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--port',required=True,type=int,help='port to fuzz')
    parser.add_argument('-ip','--address',required=True,help='IP Address to attack.  Default is 127.0.0.1',default='127.0.0.1')
    parser.add_argument('-s','--step',required=True,type=int,help='Number of bytes to increment. Default is 200',default=200)
    args = parser.parse_args()
    fuzz(args)

if __name__=="__main__":
    main()
