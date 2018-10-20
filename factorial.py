# Factorial
# e.g: fact(4) => 4*3*2*1


def fact(n):
    if n >= 1:
        print(n * fact(n - 1))
        return n * fact(n - 1)
    else:
        return 1


print(fact(4))
