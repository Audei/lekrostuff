from itertools import combinations

sides = [2,3,4,5,8,10,12,13]
acu, obt, rig, non = 0, 0, 0, 0

for a, b, c in combinations(sides, 3):

    if a + b <= c:
        non += 1
    elif a ** 2 + b ** 2 > c ** 2:
        acu += 1
    elif a ** 2 + b ** 2 == c ** 2:
        rig += 1
    else:
        obt += 1

print("%s acute, %s obtuse, %s right, %s non" % (acu, obt, rig, non))
