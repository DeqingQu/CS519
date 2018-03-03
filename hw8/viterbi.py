
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

def longest(n, edges):

    in_degree = [0]*n
    dilg = [0]*n
    back = [0]*n
    for (v, u) in edges:
        in_degree[u] += 1
    # topol_order = order(n, edges)
    for i in range(n):
        if in_degree[i] != 0:
            for (v, u) in edges:
                if u == i:
                    if dilg[i] < dilg[v] + 1:
                        dilg[i] = dilg[v] + 1
                        back[i] = v
    max_dilg, v = 0, 0
    for i, w in enumerate(dilg):
        if w > max_dilg:
            max_dilg = w
            v = i

    path = []
    path.append(v)
    while in_degree[v] != 0:
        v = back[v]
        path[:0] = [v]

    return max_dilg, path


if __name__ == '__main__':
    print(longest(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))