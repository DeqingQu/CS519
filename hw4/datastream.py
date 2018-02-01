import heapq

class MaxHeap(object):
    def __init__(self, x):
        self.heap = [-e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        return -heapq.heappop(self.heap)

    def max(self):
        return -self.heap[0]

    def replace(self, value):
        heapq.heapreplace(self.heap, -value)

def ksmallest(k, a):
    if k > len(a):
        k = len(a)
    h = MaxHeap([])
    for i, value in enumerate(a):
        if i < k:
            h.push(value)
        else:
            if value < h.max():
                h.replace(value)
    res = []
    for _ in range(k):
        res[:0] = [h.pop()]
    return res

if __name__ == '__main__':
    print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(ksmallest(3, range(1000000, 0, -1)))
