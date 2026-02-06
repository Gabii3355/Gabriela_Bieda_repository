#!/usr/bin/python3
# return true if any number is even inside a list
list=[1,3,8,7,10]
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
    return num_list
print('In your list are even numbers',check_even_list(list))       
