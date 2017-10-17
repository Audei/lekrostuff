#prime tests if a number is prime or not
def prime(x):
    #d is divisor to test if the number is prime
    d = 2

    while d < x:
        #m is what's left from mod
        m = x % d
        if m == 0:
            print("x" + " is not a prime")
            return 0
        else:
            d += 1

    if d == x:
        print("x" + " is a prime")
        return 0
