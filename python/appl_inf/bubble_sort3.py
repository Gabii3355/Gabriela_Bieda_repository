#!/usr/bin/python3
from random import random
list=[]
for x in range(1,10):
	list.append(random())
print(list)
mem=list[0]
for y in list:
	if y<mem:
		print("y jest mniejsze od mem",y,mem)
	mem=y
print(mem)
list.sort()
print(list)
