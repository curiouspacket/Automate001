#!/usr/bin/env python

import sys
from argparse import ArgumentParser

def get_ip_info():
    do = False
    while do == False:
        ip ={}
        ip['address'] = input("What IP address do you want to set? ")
        ip['mask'] = input("What Subnet Mask do you want to set? ")
        yn = input("Would you like to add more(Y//N) ? ")
        if yn == 'N':
            do = True
    return(ip)

def main():
    print("Hellow World")
    ip = get_ip_info()
    print(('IP: {address} \n SM: {mask}').format(**ip))
if __name__ == '__main__':
    main()