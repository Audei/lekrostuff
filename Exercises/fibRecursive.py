def fib(x):
    if x <= 2:
        return 1
    #yes recursive is inefficient... but oh well
    else:
        return fib(x-1) + fib(x-2)
