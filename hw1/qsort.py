def sort(array):
    if not array:
        return []
    pivot = array[0]
    left = [x for x in array if x < pivot]
    right = [x for x in array[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]


def sorted(t):
    if t:
        return sorted(t[0]) + [t[1]] + sorted(t[2])
    else:
        return []


def _search(t, x):
    if t[1] == x:
        return t
    elif t[1] > x:
        if t[0]:
            return _search(t[0], x)
        else:
            return t[0]
    elif t[1] < x:
        if t[2]:
            return _search(t[2], x)
        else:
            return t[2]


def search(t, x):
    if _search(t, x):
        return True
    else:
        return False


def insert(t, x):

    n = _search(t, x)
    if n == []:
        n.extend([[], x, []])


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