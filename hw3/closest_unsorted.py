from random import *


def qselect(k, a):
    if k < 1 or k > len(a) or a == []:
        return []
    else:
        r_index = randint(0, len(a)-1)
        a[0], a[r_index] = a[r_index], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_left = len(left)
        if k-1 < l_left:
            return qselect(k, left)
        elif k-1 == l_left:
            return pivot
        else:
            right = [x for x in a[1:] if x >= pivot]
            return qselect(k-l_left-1, right)


def find(a, x, k):
    if k <= 0:
        return []
    if k >= len(a):
        return a

    b = []
    for n in a:
        b.append(abs(n - x))

    t = qselect(k, b)

    result = []
    count = 0
    for n in a:
        if abs(n - x) < t and count < k:
            result.append(n)
            count += 1
    for n in a:
        if abs(n - x) == t and count < k:
            result.append(n)
            count += 1

    return result


if __name__=="__main__":
    print(find([4,1,3,2,7,4], 5.2, 2))
    print(find([4,1,3,2,7,4], 6.5, 3))
    print(find([5,3,4,1,6,3], 3.5, 2))
    print(find([5,5,5,4,5,8,8,9,], 4, 2))