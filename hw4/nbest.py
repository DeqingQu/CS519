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

def qsort(a):
    if a == []:
        return []
    pindex = random.randint(0, len(a)-1)
    a[0], a[pindex] = a[pindex], a[0]
    pivot = a[0]
    left = [w for w in a if w < pivot]
    middle = [w for w in a if w == pivot]
    right = [w for w in a if w > pivot]
    return qsort(left) + middle + qsort(right)

def qselect(a, k):
    return a

def nbesta(a, b, n):
    product = []
    for va in a:
        for vb in b:
            product.append(Pair(va, vb))
    sorted_product = qsort(product)
    return [(w.x, w.y) for w in sorted_product[:n]]

def nbestb(a, b, n):
    product = []
    for va in a:
        for vb in b:
            product.append((va, vb))
    return qselect(product, n)

def nbestc(a, b, n):
    return ()

if __name__ == '__main__':
    a = [4, 1, 5, 3]
    b = [2, 6, 3, 4]
    print(nbesta(a, b, 4))
    print(nbestb(a, b, 4))
    print(nbestc(a, b, 4))