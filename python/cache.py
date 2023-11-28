
def cache(f):

    d={}
    def ret_f(x):

        if x in d:
            print('cached ',x)
            return d[x]
        else:
            d[x]=f(x)
            return d[x]

    return ret_f
