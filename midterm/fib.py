def fib(n, fibs={1:1, 2:1}):
    if n not in fibs:
        fibs[n] = fib(n-2) + fib(n-1)
        print(n)
    return fibs[n]

def fib2(n, fibs=None):
    if fibs is None:
        fibs = {1:1, 2:1}
    if n not in fibs:
        fibs[n] = fib2(n-2, fibs) + fib2(n-1, fibs)
        print(n)
    return fibs[n]

def fib3(n):
    a,b = 1,1
    for _ in range(3,n+1):
        a,b = b,a+b
    return b

if __name__ == '__main__':
    print("# fib(10) = ", fib(10))
    print("# fib(20) = ", fib(20))
    print("# fib2(10) = ", fib2(10))
    print("# fib2(20) = ", fib2(20))
    print("# fib3(20) = ", fib3(20))
