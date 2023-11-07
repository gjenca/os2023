#!/usr/bin/env python3

import math

def primes(n,start_at=2):

    ret = []
    for k in range(start_at,n):
        # Testujeme, ci je k prvocislo
        for d in range(2,int(math.sqrt(k))+1):
            if k%d == 0:
                break
        else:
            ret.append(k)
    return ret


