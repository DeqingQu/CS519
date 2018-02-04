import random
import heapq
import timeit

def test1():
    a = list(range(1000000))
    random.shuffle(a)
    heapq.heapify(a)

def test2():
    a = list(range(1000000))
    random.shuffle(a)
    heap = []
    for x in a:
        heapq.heappush(heap, x)

def test1_1():
    a = list(range(1000000))
    heapq.heapify(a)

def test2_1():
    a = list(range(1000000))
    heap = []
    for x in a:
        heapq.heappush(heap, x)

def test1_2():
    a = list(range(1000000))
    a.reverse()
    heapq.heapify(a)

def test2_2():
    a = list(range(1000000))
    a.reverse()
    heap = []
    for x in a:
        heapq.heappush(heap, x)

if __name__ == '__main__':
    print(timeit.timeit('test1()', setup="from __main__ import test1"))
    print(timeit.timeit('test2()', setup="from __main__ import test2"))
