from collections import defaultdict

def shortest(n, edges):

    graph = defaultdict(list)
    for (u, v, w) in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph

if __name__ == '__main__':
    print(shortest(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))