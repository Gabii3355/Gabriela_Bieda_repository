#!/usr/bin/python3
from random import randint
from sys import argv
a_score=0
b_score=0
for round in range(1):
    print(f'Current round: {round}')
    #a=int(input("Player A give a number: "))
    a=int(argv[1])
    b=randint(1,10)
    if a>b:
        if b+1==a:
            a_score+=2
            print("Player A has 2 point")
        else:
            b_score+=1
            print("PLayer B has 1 point")
    elif b>a:
        if a+1==b:
            b_score+=2
            print("Player B has 2 point")
        else: 
            a_score+=1
            print("Player A has 1 point")
    else:
        print("You have the same numbers: 0 points for you")
    print(f'Round number {round} END ------\nComputer gave: {b} \nPlayer A: {a_score},Player B: {b_score}')
