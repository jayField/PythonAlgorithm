# fibonacci Sequence

# fibonacci recursive def, n : nth value
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


# n : nth value
n = int(input("Finding nth fibonacci value: "))

print(fib(n))