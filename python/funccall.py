#!/usr/bin/env python3

def f(x,y):

    print('x=',x)
    print('y=',y)
    # UnboundLocalError
    print('z=',z)
    z=6.28

z=3.14

f(10,'slon')
print('z=',z)

