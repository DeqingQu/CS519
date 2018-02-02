import random


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y or (self.x + self.y == other.x + other.y and self.y < other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x + self.y > other.x + other.y or (self.x + self.y == other.x + other.y and self.y > other.y)

def qselect(k, a):
    if k < 1 or k > len(a) or a == []:
        return []
    else:
        r_index = random.randint(0, len(a)-1)
        a[0], a[r_index] = a[r_index], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_left = len(left)
        if k-1 < l_left:
            return qselect(k, left)
        elif k-1 == l_left:
            return pivot
        else:
            right = [x for x in a[1:] if x > pivot or x == pivot]
            return qselect(k-l_left-1, right)

def nbesta(a, b, n):
    product = []
    for va in a:
        for vb in b:
            product.append(Pair(va, vb))
    product.sort()
    return [(w.x, w.y) for w in product[:n]]

def nbestb(a, b, n):
    product = []
    for va in a:
        for vb in b:
            product.append(Pair(va, vb))
    p = qselect(n, product)
    res = [(w.x, w.y) for w in product if w < p]
    i = 0
    lp = len(product)
    while len(res) < n and i < lp:
        w = product[i]
        if w == p:
            res.append((w.x, w.y))
        i += 1
    return res

def nbestc(a, b, n):
    return ()

if __name__ == '__main__':
    a = [4, 1, 5, 3]
    b = [2, 6, 3, 4]
    print(nbesta(a, b, 4))
    print(nbestb(a, b, 4))
    print(nbestc(a, b, 4))