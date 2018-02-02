import heapq
from math import ceil
from collections import defaultdict

def _kmergesorted(lst, k):

    res = []
    heap = []
    indexes = []
    counter = 0
    for i, array in enumerate(lst):
        counter += len(array)
        heap.append((array[0], i))
        indexes.append(0)
    heapq.heapify(heap)
    while len(res)+len(heap) < counter:
        (value, i) = heap[0]
        res.append(value)
        array = lst[i]
        if indexes[i]+1 < len(array):
            heapq.heapreplace(heap, (array[indexes[i]+1], i))
            indexes[i] += 1
        else:
            for i, index in enumerate(indexes):
                array = lst[i]
                if index+1 < len(array):
                    heapq.heapreplace(heap, (array[index+1], i))
                    indexes[i] += 1
                    break
    while len(res) < counter:
        res.append(heapq.heappop(heap)[0])
    return res


def kmergesort(a, k):
    l = len(a)
    if l < 2:
        return a

    j = ceil(len(a)/k)
    lst = [kmergesort(a[i:i+j], k) for i in range(0, len(a), j)]
    return _kmergesorted(lst, k)


if __name__ == '__main__':
    print(kmergesort([1,3,5,2,3,6,0,7], 3))