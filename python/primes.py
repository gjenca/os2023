#!/usr/bin/env python3
'''Modul pre generovanie prvočísel
'''
import math

def primes(n,start_at=2):
    '''Vráti zoznam všetkých prvočísel z 
intervalu [start_at,n)'''

    ret = []
    for k in range(start_at,n):
        # Testujeme, ci je k prvocislo
        for d in range(2,int(math.sqrt(k))+1):
            if k%d == 0:
                break
        else:
            ret.append(k)
    return ret


