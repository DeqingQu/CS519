

def max_wis(a):
    mis = {-1:0, 0:0}
    def f(l):
        if l == -1 or l == 0:
            return 0
        if l not in mis:
            x = f(l-1)
            y = f(l-2)
            mis[l] = max(x, y+a[l-1])
        return mis[l]
    return f(len(a))

def max_wis2(a):
    x, y = 0, 0
    for i in range(0, len(a)):
        x, y = max(x, y + a[i]), x
    return x

print(max_wis([7, 8, 5]))
print(max_wis([-1, 8, 10]))
print(max_wis([]))
print(max_wis([-5, -1, -4]))

print(max_wis2([7, 8, 5]))
print(max_wis2([-1, 8, 10]))
print(max_wis2([]))
print(max_wis2([-5, -1, -4]))