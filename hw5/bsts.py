def bsts(n):
    bsts_n = {0: 1, 1: 1}

    def f(x):
        if x not in bsts_n:
            s = 0
            for i in range(1, x+1):
                s += f(i-1)*f(x-i)
            bsts_n[x] = s
        return bsts_n[x]

    return f(n)

print(bsts(1))
print(bsts(2))
print(bsts(3))
print(bsts(4))
print(bsts(5))
print(bsts(6))

