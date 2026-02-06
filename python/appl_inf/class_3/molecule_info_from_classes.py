#!/usr/bin/python3

def read_molecule(filename): #this def read all file devided by columns
    fp = open(filename, 'r')
    lines = fp.readline()
    fp.readline()
    a = 0
    m = []
    while a < int(lines):
        a += 1
        l = fp.readline()
        column = l.split()
        m.append({'elem': column[0], 'x': float(column[1]), 'y': float(column[2]), 'z': float(column[3])})
    fp.close()
    return m
mol = read_molecule('ethanol.xyz')

###

def get_com(m):              #this def gives centre of mass
    x=0
    y=0
    z=0
    a=0
    M=0
    d={'C':12,'H':1,'O':16}
    for atom in m:
        x+=atom['x']*d[atom['elem']]
        y+=atom['y']*d[atom['elem']]
        z+=atom['z']*d[atom['elem']]
        M+=d[atom['elem']]
    x=x/M
    y=y/M
    z=z/M
    return[x,y,z]
print(get_com(mol))














