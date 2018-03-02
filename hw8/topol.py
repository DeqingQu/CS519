def order(n, edges):
    topol_order = []
    in_degree = [0]*n
    for i in range(len(edges)):
        in_degree[edges[i][1]] += 1
    #  initialize a queue for in_degree == 0
    queue = []
    op = 0
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    #   loop while queue is not empty
    count = 0
    while op != len(queue):
        source = queue[op]
        topol_order.append(source)
        op += 1

        for (u, v) in edges:
            if u == source:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        count += 1

    if count != n:
        return None
    return topol_order

if __name__ == '__main__':
    print(order(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))
    print(order(8, [(0, 2), (1, 2), (2, 3), (2, 4), (4, 3), (3, 5), (4, 5), (5, 6), (5, 7)]))
    print(order(4, [(0, 1), (1, 2), (2, 1), (2, 3)]))