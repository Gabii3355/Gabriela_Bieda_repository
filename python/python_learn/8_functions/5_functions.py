#!/usr/bin/python3
'''
#def
def hello1():
	print('Hello')
hello1()

who='Gabi'
def hello2(who):
	print('Hello',who,'I like you') 
hello2(who)

def sum(a,b):
	return(a+b)

#if
variable =int(input('Give a number: '))
if variable > 0:
	print('Your variable is positive')
elif variable == 0:
	print('Your variable is zero')
else:
	print('Your variable is negative')

#while
x=0 
while x<=10:
	print('you fail the exam')
	x+=1
else:
	print('you pass the exam')
'''

#break, continue, pass
myname = 'Gabriela'
for letter in  myname:
	if letter == 'a':
		continue
	print(letter)

myname = 'Bieda'
for letter in myname:
	if letter == 'i':
		break 
	print(letter)
