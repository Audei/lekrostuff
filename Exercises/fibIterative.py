def yourmom(x):

    if x == 2:
        return 1

    xi = x
    yi = 2
    y = 1
    z = 1
    
    while yi < xi:
        y = z + y
        z = y - z
        yi += 1
        x = y
    return x
