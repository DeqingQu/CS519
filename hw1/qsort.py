
def sort(array):
    if array == []:
        return []
    pivot = array[0]
    left = [x for x in array if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]


def sorted(t):
    if t == []:
        return []
    return sorted(t[0]) + [t[1]] + sorted(t[2])


def _search(t, x):
    if t[1] == x:
        return t
    elif t[1] > x:
        if t[0] == []:
            return t[0]
        else:
            return _search(t[0], x)
    elif t[1] < x:
        if t[2] == []:
            return t[2]
        else:
            return _search(t[2], x)


def search(t, x):
    if _search(t, x) == []:
        return False
    else:
        return True


def insert(t, x):
    if t[1] == x:
        return
    elif t[1] > x:
        if t[0] == []:
            t[0] = [[], x, []]
        else:
            insert(t[0], x)
    elif t[1] < x:
        if t[2] == []:
            t[2] = [[], x, []]
        else:
            insert(t[2], x)


def main():
    tree = sort([4, 2, 6, 3, 5, 7, 1, 9])
    print(tree)

    print(sorted(tree))

    print(search(tree, 3))
    print(search(tree, 6.5))
    print(search(tree, 0))

    insert(tree, 6.5)
    insert(tree, 0)
    print(tree)


main()