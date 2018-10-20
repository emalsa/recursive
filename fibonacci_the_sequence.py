# Only your computer is the limit ;)

def fibonacci_sequence(n):
    # print(n)
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


for index in range(1, 100):
    print(str(index) + ". Fibonacci: " + str(fibonacci_sequence(index)))
