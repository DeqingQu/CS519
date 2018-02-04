import random
import heapq
import copy
import timeit

def test1():
    a = list(range(10))
    random.shuffle(a)
    heapq.heapify(a)

def test2():
    a = list(range(10))
    random.shuffle(a)
    heap = []
    for x in a:
        heapq.heappush(heap, x)

if __name__ == '__main__':

    print(timeit.timeit('test1()', setup="from __main__ import test1"))
    print(timeit.timeit('test2()', setup="from __main__ import test2"))

# def test():
#     """Stupid test function"""
#     L = []
#     for i in range(100):
#         L.append(i)
#
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import random"))