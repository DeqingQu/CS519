import bisect


def find(a, n, k):
    return a[k:k+1]


def main():
    print(find([1, 2, 3, 4, 4, 6, 6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))


main()