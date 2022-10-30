

def my_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == '__main__':
    number = int(input("Enter an integer number: "))
    print("The factorial of {} is: {} "  .format(number, my_factorial(number)))
