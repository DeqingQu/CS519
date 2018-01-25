import bisect


def find(a, n, k):
    if k <= 0:
        return []
    if k >= len(a):
        return a

    p = bisect.bisect_left(a, n)

    if p == 0:
        return a[:k]
    if p == len(a):
        return a[len(a) - k:]

    diff_1 = abs(a[p-1] - n)
    diff_2 = abs(a[p] - n)
    if diff_1 <= diff_2:
        p -= 1

    i = p - 1
    j = p + 1
    counter = 1
    result = [a[p]]
    while counter < k:
        if i <= 0:
            result.append(a[j])
            j += 1
            counter += 1
            continue
        if j >= len(a):
            result.insert(0, a[i])
            i -= 1
            counter += 1
            continue

        diff_i = abs(a[i] - n)
        diff_j = abs(a[j] - n)
        if diff_i <= diff_j:
            result.insert(0, a[i])
            i -= 1
            counter += 1
        else:
            result.append(a[j])
            j += 1
            counter += 1

    return result


if __name__ =="__main__":
    print(find([1,2,3,4,4,7], 1.2, 3))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1, 2, 3, 4, 4, 6, 6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([1,2,3,4,4,6,6], 5, 3))