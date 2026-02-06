#!/usr/bin/python3
fp=open('ethanol.xyz', 'r')
x=[]
y=[]
z=[]
a=0
lines=fp.readline() #read first line
fp.readline()
while a < (int(lines)): #change number from first line to integer
    a+=1
    l=fp.readline()
    columns=l.split() #split lines for columns
    x.append(float(columns[1])) #in [0] we have names such as C,H,O...
    y.append(float(columns[2]))
    z.append(float(columns[3]))
print(sum(x)/len(x))
print(sum(y)/len(y))
print(sum(z)/len(z))
