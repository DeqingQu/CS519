

def max_wis(a):
    mis = {-1:0, 0:0}
    def f(l):
        if l == -1 or l == 0:
            return 0
        if l not in mis:
            x = f(l-1)
            y = f(l-2)
            mis[l] = max(x, y+a[l-1])
            print("f%:%", l, mis[l])
        return mis[l]
    return f(len(a))


print(max_wis([7,8,5]))