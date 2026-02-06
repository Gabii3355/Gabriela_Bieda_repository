#!/usr/bin/python3
fp=open("ethanol.xyz",'r')
a=0 
lines=fp.readline()

while a< (int(lines)):
        a+=1
        l=fp.readline()
        print(l)
