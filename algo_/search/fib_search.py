def fib_search(data, value):
    # search for max fib
    fib = 1
    while True:
        if fib + fib > data[-1]:
            break
        fib += fib
    return fib


if __name__ == '__main__':
    data = range(1, 100, 3)

    k = fib_search(data, 43)
    print k

    k = fib_search(data, 44)
    print k
