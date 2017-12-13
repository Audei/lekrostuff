from cmath import sqrt
def quad(quad):
    foo = quad.split("+")
    
    i = 0
    for y in foo:
        foo[i] = foo[i].strip()
        i += 1

    aTemp = foo[0].split("x^2")[0]
    bTemp = foo[1].split("x")[0]
    cTemp = foo[2]

    try:
        a = float(aTemp)
    except ValueError:
        a = 1
    try:
        b = float(bTemp)
    except ValueError:
        b = 1
    try:
        c = float(cTemp)
    except ValueError:
        c = 1

    x = [(-b + sqrt(b**2 - 4*a*c)) / 2*a,(-b - sqrt(b**2 - 4*a*c)) / 2*a]
    print(x)
    
#User Friendly
run = True
while run:
    bar = input("Input a quadratic equation in the form of ax^2 + bx + c. Ex: 3x^2 + -3x + 1. ")
    quad(bar)
