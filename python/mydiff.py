

def diff(f,delta):

    def diff_f(x):

        return f(x+delta)-f(x)

    return diff_f


