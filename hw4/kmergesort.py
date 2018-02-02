import heapq
from math import ceil


def _kmergesorted(lst):
    heap = []
    res = []
    for i, array in enumerate(lst):
        heapq.heappush(heap, (array[0], 0, i))
    while heap:
        #   value is the minimum element
        #   i is the index of the min in the k-th array
        #   k is the index of the array in lst
        value, i, k = heapq.heappop(heap)
        res.append(value)
        if i+1 < len(lst[k]):
            heapq.heappush(heap, (lst[k][i+1], i+1, k))
    return res


def kmergesort(a, k):
    l = len(a)
    if l < 2:
        return a

    j = ceil(len(a)/k)
    lst = [kmergesort(a[i:i+j], k) for i in range(0, len(a), j)]
    return _kmergesorted(lst)


if __name__ == '__main__':
    print(kmergesort([1,3,5,2,3,6,0,7], 3))