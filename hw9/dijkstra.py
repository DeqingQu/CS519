from collections import defaultdict
from heapdict import heapdict

def shortest(n, edges):

    graph = defaultdict(list)
    for (u, v, w) in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    hd = heapdict()
    for i in range(n):
        hd[i] = float("inf")
    hd[0] = 0

    length = 0
    back = defaultdict(int)
    while len(hd) != 0:
        v, w = hd.popitem()
        length = w
        if v == n-1: break
        for (vv, ww) in graph[v]:
            if vv in hd and hd[vv] > w + ww:
                hd[vv] = w + ww
                back[vv] = v

    #  backtrack the shortest path
    path, d = [], n-1
    path.append(n-1)
    path[:0] = [back[d]]
    while back[d] != 0:
        d = back[d]
        path[:0] = [back[d]]

    return length, path


if __name__ == '__main__':
    print(shortest(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print(shortest(5, [(0, 1, 3), (0, 2, 1), (1, 3, 2), (2, 4, 1)]))
    print(shortest(4, [(0, 1, 24), (0, 2, 3), (0, 3, 20), (2, 3, 12)]))


    def generate_seq(k, length, seed):
        import random;
        random.seed(seed);
        return [tuple(sorted(random.sample(range(k), 2)) + [random.randint(5, 10)]) for _ in range(length)]

    def performance_test():
        tuples_1 = generate_seq(5000, 50000, 1)
        tuples_2 = generate_seq(5000, 50000, 4)
        from time import time
        t = time()
        shortest(5000, tuples_1[:50000])
        print("test case 1 : ", time() - t)
        t = time()
        shortest(5000, tuples_2[:50000])
        print("test case 2 : ", time() - t)

    performance_test()