#!/usr/bin/env python3

def uppercase(str):
    # Convert all lowercase letters in the string to uppercase.

    for c in str:
        if 97 <= ord(c) <= 122:
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
