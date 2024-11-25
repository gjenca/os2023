
def cache(f):

    d={}
    def ret_f(x):

        if x not in d:
            d[x]=f(x)
            print('cache not hit',x)
        else:
            print('cache hit')
        return d[x]

    return ret_f
