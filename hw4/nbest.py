import random

def qsort(a):
    if a == []:
        return []
    pindex = random.randint(0, len(a)-1)
    a[0], a[pindex] = a[pindex], a[0]
    (pivot_x, pivot_y) = a[0]
    left = [(w_x, w_y) for (w_x, w_y) in a if ((w_x + w_y) < (pivot_x + pivot_y) or ((w_x + w_y) == (pivot_x + pivot_y) and w_y < pivot_y))]
    middle = [(w_x, w_y) for (w_x, w_y) in a if (w_x == pivot_x and w_y == pivot_y)]
    right = [(w_x, w_y) for (w_x, w_y) in a if (w_x + w_y) > (pivot_x + pivot_y) or ((w_x + w_y) == (pivot_x + pivot_y) and w_x > pivot_x)]
    return qsort(left) + middle + qsort(right)

def nbesta(a, b, n):
    product = []
    for va in a:
        for vb in b:
            product.append((va, vb))
    sorted_product = qsort(product)
    return sorted_product[:n]

def nbestb(a, b, n):
    return ()

def nbestc(a, b, n):
    return ()

if __name__ == '__main__':
    a = [4, 1, 5, 3]
    b = [2, 6, 3, 4]
    print(nbesta(a, b, 4))
    print(nbestb(a, b, 4))
    print(nbestc(a, b, 4))