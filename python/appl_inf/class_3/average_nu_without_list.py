#!/usr/bin/python3
fp=open('ethanol.xyz', 'r')
x=0
y=0
z=0
a=0
lines=fp.readline() #read first line
fp.readline()
while a < (int(lines)): #change number from first line to integer
    a+=1
    l=fp.readline()
    columns=l.split() #split lines for columns
    x+=(float(columns[1]))
    y+=(float(columns[2]))
    z+=(float(columns[3]))
print(x/(int(lines)))
print(y/(int(lines)))
print(z/(int(lines)))
