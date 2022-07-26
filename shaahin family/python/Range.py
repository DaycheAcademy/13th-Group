def rng(min_, max_, step):
    while x:
        if min_ < max_ - step:
            yield round(min_, 2)
            min_ += step
        else:
            yield round(min_, 2)
            break


if __name__ == "__main__":
    for i in rng(2.3, 3.78, 0.01):
        print(i)
