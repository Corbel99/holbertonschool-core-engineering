#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i != 'e' and i != 'q':
        print("{}".format(i), end='\n' if i == 'z' else '')
