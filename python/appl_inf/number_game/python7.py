#!/usr/bin/python3
from random import randint
import matplotlib.pyplot as plt
a_score=0
b_score=0
round=0
win_num=[]
for round in range(100):
    a=randint(1,10)
    b=randint(1,10)
    if a>b:
        if b+1==a:
            a_score+=2
            win_num.append(a)
        else:
            b_score+=1
            win_num.append(b)
    elif b>a:
        if a+1==b:
            b_score+=2
            win_num.append(b)
        else: 
            a_score+=1
            win_num.append(a)
    else:
        print("You have the same numbers: 0 points for you")
    print(f'Round number {round} END ------\nComputer gave: {b} \nPlayer A: {a_score},Player B: {b_score}')
plt.hist(win_num)
plt.show()
