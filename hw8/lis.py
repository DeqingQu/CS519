import math

# O(n^2 solution)
def lis(s):
    l, arr = len(s), []
    arr.append((0, s[0]))
    for i in range(1, l):
        max_lis = -1
        max_index = -1
        for j in range(i):
            if s[j] < s[i] and arr[j][0] > max_lis:
                max_lis = arr[j][0]
                max_index = j
        if max_index == -1: arr.append((0, s[i]))
        else: arr.append((max_lis + 1,  arr[max_index][1] + s[i]))
    return arr[l-1][1]

def lis_num(s):
    l, arr = len(s), []
    arr.append((0, [s[0]]))
    for i in range(1, l):
        max_lis = -1
        max_index = -1
        for j in range(i):
            if s[j] < s[i] and arr[j][0] > max_lis:
                max_lis = arr[j][0]
                max_index = j
        if max_index == -1: arr.append((0, s[i]))
        else: arr.append((max_lis + 1,  arr[max_index][1] + [s[i]]))
    return arr[l-1][1]

def binary_search(a, x):
    if a == []:
        return 0
    i = len(a) // 2
    if a[i] == x:
        return i
    elif a[i] > x:
        return binary_search(a[:i], x)
    return binary_search(a[i+1:], x) + i + 1

# O(nlogn solution)
def lis_num_2(s):
    a = []
    idx = []
    for i, n in enumerate(s):
        if a == [] or n > a[len(a)-1]:
            a.append(n)
            idx.append(i)
        else:
            bi = binary_search(a, n)
            a[bi] = n
            idx[bi] = i

    i = len(s)-1
    j = len(a)-1
    res = []
    while (i >= 0):
        if (s[i] >= a[j] and j == len(a)-1) or (s[i] >= a[j] and s[i] <= a[j+1]):
            res[:0] = [s[i]]
            j -= 1
        i -= 1

    return res

def performance_test():

    from time import time
    t = time()
    lis_num([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    print("n^2 Time : ", time() - t)
    t = time()
    lis_num_2([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    print("nlogn Time : ", time() - t)

if __name__ == '__main__':
    print(lis("aebbcg"))
    print(lis("zyx"))
    print(lis_num([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    print(lis_num_2([2, 6, 3, 4, 1, 2, 9, 5, 8]))
    print(lis_num_2([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    performance_test()