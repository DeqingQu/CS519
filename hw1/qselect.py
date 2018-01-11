from random import *


def qselect(k, a):
    if k < 1 or k > len(a) or a == []:
        return []
    else:
        r_index = randint(0, len(a)-1)
        a[0], a[r_index] = a[r_index], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        l_left = len(left)
        if k-1 < l_left:
            return qselect(k, left)
        elif k-1 == l_left:
            return pivot
        else:
            return qselect(k-l_left-1, right)


def main():
    print(qselect(4, [3, 10, 4, 7, 19]))
    print(qselect(4, [11, 2, 8, 3]))


main()
