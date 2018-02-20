def fib(n, fibs={1:1, 2:1}):
    if n not in fibs:
        fibs[n] = fib(n-2) + fib(n-1)
        print(n)
    return fibs[n]


if __name__ == '__main__':
    print("# fib(10) = ", fib(10))
    print("# fib(20) = ", fib(20))