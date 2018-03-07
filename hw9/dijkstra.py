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

    length, res = 0, []
    while len(hd) != 0:
        v, w = hd.popitem()
        length = w
        res.append(v)
        for (vv, ww) in graph[v]:
            if vv in hd:
                if hd[vv] > w + ww:
                    hd[vv] = w + ww
    return length, res

if __name__ == '__main__':
    print(shortest(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))