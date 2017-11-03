def lin_int(x): #where x is a list
    i = 0
    #i = increment for list
    while i < len(x) - 1:
        x.insert(i+1, x[i] / 2 + x[i + 1] / 2)
        i += 2
    return x
