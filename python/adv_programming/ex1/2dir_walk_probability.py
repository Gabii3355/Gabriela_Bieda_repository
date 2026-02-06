#!/bin/python
import pylab as pl
x0=1670
c=31543
a=12807
m=31672
x_list=[]
pos=[]
walk=0
left_c=0
right_c=0

def Lehmer(x0,a,c,m):
    x=(x0*a+c)%m
    return x

for i in range(0,10000):
    x0=Lehmer(x0,a,c,m)
    x_list.append(x0)

    if x0 < m//2:
        walk-=1
        left_c+=1
    else:
        walk+=1  
        right_c+=1
    pos.append(walk)

print(x_list)
print(pos)

#probability
total_steps= right_c + left_c
p_right=right_c/total_steps
p_left=left_c/total_steps

#preference
if p_right > p_left:
    preference="Motion prefers to right"
elif p_left> p_right:
    preference='Motion prefers left'
else:
    preference='There are no preference'

#Wynik
print(f"Total steps: {total_steps}")
print(f"Steps right: {right_c} ({p_right:.4f} probability)")
print(f"Steps left:  {left_c} ({p_left:.4f} probability)")
print(preference)

#wykres 
X_index_num = list(range(len(pos)))
pl.plot(X_index_num,pos,"b-")
pl.xlabel("steps taken")
pl.ylabel("left/right")
pl.title("Random walk")
pl.show()
