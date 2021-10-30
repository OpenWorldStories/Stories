#!/usr/bin/env python3

"""A simple python script template.

"""

import os
import sys
import argparse
import signal
import time
import readchar

def addworld():
    print("What do you want to do?")
    print("1). - List worlds")
    print("2). - Select world")
    print("3). - Add world") 

    answer = input(">")
    print(answer)

    
def main(arguments):

    os.system('clear')
    i = 0
    while i < 1:
        print("What do you want to do?")
        print("1). - Select World")
        print("q). - quit")

        answer = input(">")
        print(answer)

        if answer == "1":
            addworld()
        elif answer == "q":
            i = 1
        else: 
            print("Invalid option")

def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = input(">")
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)
 
 
signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))