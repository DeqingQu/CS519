import bisect


def find(a, n, k):
    if k <= 0:
        return []
    if k >= len(a):
        return a

    j = bisect.bisect(a, n)

    if j == 0:
        return a[:k]
    if j == len(a):
        return a[len(a) - k:]

    i = j-1
    diff_i = abs(a[i] - n)
    diff_j = abs(a[j] - n)
    if diff_i > diff_j:
        i = j
        j += 1

    counter = 1
    while counter < k:
        if i <= 0:
            j += 1
            counter += 1
            continue
        if j >= len(a):
            i -= 1
            counter += 1
            continue
        diff_i = abs(a[i] - n)
        diff_j = abs(a[j] - n)
        if diff_i < diff_j:
            i -= 1
            counter += 1
        else:
            j += 1
            counter += 1

    return a[i:j]


def main():

    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1, 2, 3, 4, 4, 6, 6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))


main()