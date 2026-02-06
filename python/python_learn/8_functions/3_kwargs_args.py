#!/usr/bin/python3
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[0]} {kwargs["food"]}')
myfunc(10,20,30,fruit='orange', animal='dog', food='eggs')
