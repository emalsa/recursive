def fibonacci(n):
    if n >= 3:
        # print(n)
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return 1


print(fibonacci(7))
