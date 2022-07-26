def fac_rec(i):
    if i <= 1:
        return i
    else:
        return i * fac_rec(i-1)


def fac_for(n):
    c = n
    for i in range(n - 1, 1, -1):
        c = c * i
        print(c)


def fact_yield(n):
    c = n
    for i in range(1, n):
        c *= i
        yield c


if __name__ == "__main__":
    print(fac_rec(5))
    print("*" * 30)
    print(fac_for(5))
    print("*" * 30)
    for h in fact_yield(5):
        print(h)
