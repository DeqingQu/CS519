import bisect

def find(a, n, k):

    p = bisect.bisect_left(a, n)

    left = p - 1
    right = p
    counter = 0
    result = []

    while counter < k:
        if left == -1:
            result.append(a[right])
            right += 1
            counter += 1
            continue
        elif right == len(a):
            result.insert(0, a[left])
            left -= 1
            counter += 1
            continue
        else:
            diff_l = abs(a[left] - n)
            diff_r = abs(a[right] - n)
            if diff_l <= diff_r:
                result.insert(0, a[left])
                left -= 1
                counter += 1
            else:
                result.append(a[right])
                right += 1
                counter += 1

    return result

if __name__ == "__main__":
    print(find([1,2,3,4,4,7], 1.2, 3))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1, 2, 3, 4, 4, 6, 6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
    print(find([1,2,3,4,4,6,6], 5, 3))