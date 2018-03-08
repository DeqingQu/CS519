from collections import defaultdict
from heapdict import heapdict
from time import time

#   Total Time: 0.968 s
def shortest(n, edges):
    graph = defaultdict(dict)
    for (u, v, w) in edges:
        graph[u][v] = w
        graph[v][u] = w

    hd = heapdict()
    hd[0] = 0
    visited = set()
    back = defaultdict(int)

    while True:
        v, w = hd.popitem()
        length = w
        visited.add(v)
        if v == n-1: break

        for u, cost in graph[v].items():
            if u not in visited:
                if u not in hd or (u in hd and hd[u] > w + cost):
                    hd[u] = w + cost
                    back[u] = v

    #  backtrack the shortest path
    path, d = [], n-1
    path.append(n-1)
    path[:0] = [back[d]]
    while back[d] != 0:
        d = back[d]
        path[:0] = [back[d]]

    return length, path

#   initialize the hd to float('inf') -- time consuming
#   Total Time: 1.606 s
def shortest1(n, edges):
    graph = defaultdict(dict)
    for (u, v, w) in edges:
        graph[u][v] = w
        graph[v][u] = w

    hd = heapdict()
    for i in range(n):
        hd[i] = float("inf")
    hd[0] = 0
    back = defaultdict(int)

    while True:
        v, w = hd.popitem()
        length = w
        if v == n-1: break

        for u, cost in graph[v].items():
            if u in hd and hd[u] > w + cost:
                hd[u] = w + cost
                back[u] = v

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

    tuples = generate_seq(5, 5, 1)
    print(tuples)
    print(shortest(5, tuples))

    def performance_test():
        tuples_1 = generate_seq(5000, 50000, 1)
        tuples_2 = generate_seq(5000, 50000, 4)
        t = time()
        shortest(5000, tuples_1[:50000])
        print("test case 1 : ", time() - t)
        t = time()
        shortest(5000, tuples_2[:50000])
        print("test case 2 : ", time() - t)

    performance_test()