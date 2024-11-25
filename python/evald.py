
import operator

oper={
    '+':operator.add,
    '*':operator.mul,
    '-':operator.sub,
    '/':operator.truediv,
    }

def evald(t,d):

    if type(t) in (float,int):
        return t
    if type(t) == str:
        return d[t]
    val1=evald(t[1],d)
    val2=evald(t[2],d)
    return oper[t[0]](val1,val2)
    

# const = lambda x: c
def const(c):

    def ret_f(x):
        return c

    return ret_f

def id(x):

    return x

def eval_f(t):

    if type(t) in (float,int):

        return const(t)
    
    if t=='x':

        return id

    f1=eval_f(t[1])
    f2=eval_f(t[2])

    def ret_f(x):
        
        return oper[t[0]](f1(x),f2(x))

    return ret_f
