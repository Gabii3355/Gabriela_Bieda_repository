#!/usr/bin/python3

number=int(input('Give a number and I will count from it to 100: '))
while number > 0:
	print(number)
	number+=1 #increase by one
	if number > 100: break
