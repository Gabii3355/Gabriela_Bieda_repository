#!/usr/bin/python3
from sys import argv
a=int(argv[1])

if a>0:
    a=1
elif a<0:
    a=-1
else:
    a=0
print(f'Sign of you number is {a}')
