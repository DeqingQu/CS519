def num_no(n):
    s = {0: 1, 1: 2}
    def f(x):
        if x not in s:
            s[x] = f(x-2) + f(x-1)
        return s[x]
    return f(n)

def num_yes(n):
    s = 1
    for _ in range(n):
        s *= 2
    return s - num_no(n)


print(num_no(3))
print(num_yes(3))

print(num_no(2))
print(num_yes(2))

print(num_no(1))
print(num_yes(1))