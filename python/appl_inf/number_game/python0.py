#!/usr/bin/python3
print("Give a number and I tell you a sign: ")
a=int(input())
def sign(x):
    if x>0:
        return(1)
    elif x<0:
        return(-1)
    else:
        return(0)
print(sign(a))

