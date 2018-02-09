

def max_wis2(a):
    mis = {-1:(0, []), 0:(0, [])}
    def f(l):
        if l not in mis:
            (x, x_s) = f(l-1)
            (y, y_s) = f(l-2)
            if x > y + a[l-1]:
                mis[l] = (x, x_s)
            else:
                n = list(y_s)
                n.append(a[l-1])
                mis[l] = (y + a[l-1], n)
        return mis[l]
    return f(len(a))

def max_wis(a):
    x = (0, [])
    y = (0, [])
    for i in range(0, len(a)):
        tmp = x
        if x[0] < y[0] + a[i]:
            n = list(y[1])
            n.append(a[i])
            x = (y[0] + a[i], n)
        y = tmp
    return x

print(max_wis([7, 8, 5, 4, 6, 1, 1, 6]))
print(max_wis([7, 8, 5]))
print(max_wis([-1, 8, 10]))
print(max_wis([]))
print(max_wis([-5, -1, -4]))

print(max_wis2([7, 8, 5]))
print(max_wis2([-1, 8, 10]))
print(max_wis2([]))
print(max_wis2([-5, -1, -4]))