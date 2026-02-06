#!/usr/bin/python3
list=[3,1,2]
print(f'The length of the list is {len(list)}')  #give the number of how many elements is in the  list
print(f'The second element of the list is {list[2]}') 
list.append(4) #append new item to the end of the list
print(f'After added 4 to list the list have {len(list)} arguments')
list.pop(2) #remove item from the list
print(f'After removing 2 the list is {list}')
list.sort()
print(f'List is sort {list}')
list.reverse()
print(f'Reverse list is {list}')
