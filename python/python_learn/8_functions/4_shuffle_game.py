#!/usr/bin/python3
from random import shuffle
#initial list
cups=[' ','0',' ']

#shuffle list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#user guess
def player_guess():
    guess=''
    while guess not in [0,1,2]:
        guess=int(input('Pick a number 0,1,2: ')) 
    return guess

#check the user guess
def check_guess(mylist, guess):
    if mylist[guess] == '0':
        print('You guest it!')
        print(f'The ball was in {mylist}')
    else:
        print('Maybe next time')
        print(f'The ball was in {mylist}')

check_guess(shuffle_list(cups), player_guess())
