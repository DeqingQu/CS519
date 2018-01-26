import bisect


def find(a, x, k):

    len_a = len(a)
    if k <= 0:
        return []
    if k >= len_a:
        return a

    p = bisect.bisect_left(a, x)

    if p == 0:
        return a[:k]
    if p == len_a:
        return a[len_a - k:]

    left = p-1
    right = p
    counter = 0
    while counter < k:
        if left == -1:
            right += k - counter
            break
        elif right == len_a:
            left -= k - counter
            break
        else:
            diff_l = abs(a[left] - x)
            diff_r = abs(a[right] - x)
            if diff_l <= diff_r:
                left -= 1
                counter += 1
            else:
                right += 1
                counter += 1

    return a[left+1:right]


if __name__ =="__main__":
    print(find([1,2,3,4,4,7], 1.2, 3))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1, 2, 3, 4, 4, 6, 6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([1,2,3,4,4,6,6], 5, 3))