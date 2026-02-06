#!/usr/bin/python3
'''
#only word starts with s
st='Print only the words that start with s in this sentence'
for word in st.split():
	if word[0] == 's':
	 	print(word)	

#even number from 0 to 10
for num in range(0,11,2):
	print(num)

#print even length of words
st='Print only the words that has an even number of letters'
for word in st.split():
	if len(word) % 2== 0:
		print(word) 
'''
#print only first letter
st='Print only the words that has an even number of letters'
for letter in st.split():
	print(letter[0])
