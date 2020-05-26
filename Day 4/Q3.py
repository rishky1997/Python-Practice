def rfun(no):
    if no==0:
        return 0
    else:
        return (no+rfun(no-1))
    
rfun(10)
