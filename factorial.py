# factorial value, n = result
def fac(n):
    # if 0 == 0,
    if n == 0:
        return 1
    # if 1 == 1, because for multiply
    if n == 1:
        return 1

    # recursive code
    else:
        return fac(n - 1) * n


n = int(input("input number: "))
print(fac(n))
