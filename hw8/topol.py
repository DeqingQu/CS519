def order(n, graph):
    return graph

if __name__ == '__main__':
    print(order(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))
    print(order(8, [(0, 2), (1, 2), (2, 3), (2, 4), (4, 3), (3, 5), (4, 5), (5, 6), (5, 7)]))
    print(order(4, [(0, 1), (1, 2), (2, 1), (2, 3)]))