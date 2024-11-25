
#from cache import memoize
from functools import cache

@cache
def comb(n,k):

    if n==k:
        return 1
    if k==0:
        return 1
    return comb(n-1,k-1)+comb(n-1,k)


