def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5, 6, 500, 2, 4))

def suma2(*args):
    return sum(args)

print('-----------------------')
print(suma2(5, 6, 500, 2, 4))