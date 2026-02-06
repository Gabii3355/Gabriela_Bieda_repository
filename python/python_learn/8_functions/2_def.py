#!/usr/bin/python3
# return all even numbers from the list 
list=[1,3,8,7,10]
def check_even_list(num_list):
    even_numbers=[]
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print('You have even numbers in your list',check_even_list(list))       
