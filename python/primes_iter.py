#!/usr/bin/env python3

import math


def is_prime(k):
        
    # Testujeme, ci je k prvocislo
    if k<2:
        return False
    for d in range(2,int(math.sqrt(k))+1):
        if k%d == 0:
            return False
    return True
    

def primes(start_at=2):

    ret = []
    k=start_at
    while True:
        if is_prime(k):
            yield k
        k+=1 # k=k+1
    

