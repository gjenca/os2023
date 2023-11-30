
def mydebug(f):
    
    def ret_f(x):
        
        print(f'Volane {f.__name__}({x})')
        return f(x)

    return ret_f
