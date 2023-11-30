
def histogram_slov(s,min_length=0):

    slova=''.join(c for c in s if c.isalpha() or c.isspace()).split()
    ret={}
    for slovo in filter(lambda x: len(x)>=min_length,slova):
        if slovo in ret:
            # Uz sme slovo videli
            ret[slovo]=ret[slovo]+1
        else:
            # Este sme slovo nevideli
            ret[slovo]=1
    return ret

            

