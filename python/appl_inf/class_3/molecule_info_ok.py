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
        d={'C':12,'O':16,'H':1}
        m.append({'elem': column[0], 'x': float(column[1]), 'y': float(column[2]), 'z': float(column[3]), 'mass':d[column[0]]})
    fp.close()
    return m

if __name__ == "__main__":
    filename = input("Give the name of the file: ")
    mol = read_molecule(filename)
    print("I split the file into given columns: ",mol)

###

def get_com(m):              #this def gives centre of mass
    x=0
    y=0
    z=0
    a=0
    M=0
    for atom in m:
        mass = atom['mass']
        x+=atom['x']*mass
        y+=atom['y']*mass
        z+=atom['z']*mass
        M+=mass
    x=x/M
    y=y/M
    z=z/M
    return[x,y,z]
print('Your average centre mass is: ',get_com(mol))

###
def get_cog(m):
    x=0
    y=0
    z=0
    a=0
    for atom in m:
        x+=atom['x']
        y+=atom['y']
        z+=atom['z']
        a+=1
    x=x/a
    y=y/a
    z=z/a
    return[x,y,z]
print("Your average namber of x,y,z is: ",get_cog(mol))










