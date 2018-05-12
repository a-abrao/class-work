def chop(t):
    del t[0]
    del t[-1]
    
    
def middle(t):
    newt = t[1:]
    del(newt[-1])
    return(newt)