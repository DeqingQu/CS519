

def find(a):
    if len(a) < 3:
        return []

    result = []
    a.sort()

    for p, pivot in enumerate(a):
        i = 0
        j = len(a) - 1
        if i == p: i += 1
        if j == p: j -= 1
        while i < j:
            val = a[i] + a[j]
            if val == pivot:
                result.append((pivot, a[i], a[j]))
                i += 1
                j -= 1
            elif val > pivot:
                j -= 1
            else:
                i += 1

    return result


def main():
    print(find([1, 4, 2, 3, 5]))
    print(find([-3, -2, -1]))

main()