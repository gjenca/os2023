
def comb(pair):

    n=pair[0]
    k=pair[1]
    if n==k:
        return 1
    if k==0:
        return 1
    return comb((n-1,k-1))+comb((n-1,k))

