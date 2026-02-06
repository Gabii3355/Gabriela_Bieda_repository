#!/usr/bin/python3
s='Hello new friends'
print(s.upper()) #upper case
print(s.lower()) #lower case
print(s.split()) #split a string by a space
print(s.split('e')) #split a string by 'e'
print('Hello {1} {0} {2}'.format('new', 'my', 'friends')) #put strong into {}
print('Hello {m} {n} {f}'.format(m='my',n='new',f='friends')) #put strong into {}
print(s.format())
