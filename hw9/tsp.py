from collections import defaultdict
import copy
from time import time

def tsp(n, edges):

    graph = defaultdict(dict)
    for (u, v, w) in edges:
        graph[u][v] = w
        graph[v][u] = w
        if u == 0:
            graph[-1][v] = w
            graph[v][-1] = w
        if v == 0:
            graph[u][-1] = w
            graph[-1][u] = w

    def tsp_helper(visited, i):
        if visited == {0} and i == 0:
            return 0
        min_cost = float("inf")
        for v in visited:
            if v != i and v in graph[i]:
                new_visited = copy.deepcopy(visited)
                new_visited.remove(i)
                temp = tsp_helper(new_visited, v)
                if temp is not None and min_cost > temp + graph[v][i]:
                    min_cost = temp + graph[v][i]
        if min_cost == float("inf"):
            return None
        else:
            return min_cost

    v_set = set()
    for i in range(n):
        v_set.add(i)
    v_set.add(-1)

    return tsp_helper(v_set, -1)

if __name__ == '__main__':
    print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)]))
    print(tsp(4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6), (3, 0, 1)]))
    # print(tsp(11, [(0,1,29),(0,2,20),(0,3,21),(0,4,16),(0,5,31),(0,6,100),(0,7,12),(0,8,4),(0,9,31),(0,10,18),
    #             (1,2,15),(1,3,29),(1,4,28),(1,5,40),(1,6,72),(1,7,21),(1,8,29),(1,9,41),(1,10,12),
    #             (2,3,15),(2,4,14),(2,5,25),(2,6,81),(2,7,9),(2,8,23),(2,9,27),(2,10,13),
    #             (3,4,4),(3,5,12),(3,6,92),(3,7,12),(3,8,25),(3,9,13),(3,10,25),
    #             (4,5,16),(4,6,94),(4,7,9),(4,8,20),(4,9,16),(4,10,22),
    #             (5,6,95),(5,7,24),(5,8,36),(5,9,3),(5,10,37),
    #             (6,7,90),(6,8,101),(6,9,99),(6,10,84),
    #             (7,8,15),(7,9,25),(7,10,13),
    #             (8,9,35),(8,10,18),
    #             (9,10,38)]))
