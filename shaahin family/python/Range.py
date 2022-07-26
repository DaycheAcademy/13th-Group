def rng(min_, max_, step):
    while True:
        if min_ < max_ - step:
            yield round(min_, 2)
            min_ += step
        else:
            yield round(min_, 2)
            break


def rng_char(start, stop, step):

    for i in range(ord(start), ord(stop) + 1, step):
        yield chr(i)


if __name__ == "__main__":
    print("new range(rng):")

    for i in rng(2.3, 3.78, 0.01):
        print(i)
    print("*" * 30)
    print("new range(rng_char):")

    for m in rng_char('a', 'm', 2):
        print(m)
