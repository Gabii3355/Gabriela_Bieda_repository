#!/usr/bin/python3
fp=open("ethanol.xyz", 'r')
x=0
y=0
z=0
a=0
M=0
d={'C':12,'H':1,'O':16}
lines=fp.readline()
fp.readline() #pomija 2 linijke, ktora jest pusta w plikach xyz
while a < (int(lines)):
    a+=1
    l=fp.readline()
    column=l.split()
   # atom= column[0]
   # mass= d[atom]
   # M+= mass
    M+=d[column[0]]
#    x+=float(column[1])*mass
#    y+=float(column[2])*mass
#    z+=float(column[3])*mass
    z+=float(column[3])*d[column[0]]
    y+=float(column[2])*d[column[0]]
    x+=float(column[1])*d[column[0]]

print(x/M)
print(y/M)
print(z/M)

