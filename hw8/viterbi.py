from collections import defaultdict

def order(n, edges):
    topol_order = []
    in_degree = [0]*n
    graph = defaultdict(list)

    for (u, v) in edges:
        in_degree[v] += 1
        graph[u].append(v)

    #  initialize a queue for in_degree == 0
    queue = []
    op = 0
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    #   loop while queue is not empty

    while op != len(queue):
        u = queue[op]
        topol_order.append(u)
        op += 1

        adjacents = graph[u]
        for v in adjacents:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(topol_order) != n:
        return None
    return topol_order

def longest(n, edges):

    in_degree = [0]*n
    dilg = [0]*n
    back = [0]*n

    graph = defaultdict(list)

    for (u, v) in edges:
        in_degree[v] += 1
        graph[v].append(u)

    topol_order = order(n, edges)

    max_dilg, max_v = 0, 0
    for i in topol_order:
        if in_degree[i] != 0:
            adjacents = graph[i]
            for v in adjacents:
                if dilg[i] < dilg[v] + 1:
                    dilg[i] = dilg[v] + 1
                    back[i] = v
            if dilg[i] > max_dilg:
                max_dilg = dilg[i]
                max_v = i

    path, v = [], max_v
    path.append(v)
    while in_degree[v] != 0:
        v = back[v]
        path[:0] = [v]

    return max_dilg, path

def performance_test():

    from time import time
    t = time()
    longest(20000, [(4402, 18651), (2067, 8358), (3863, 16234), (14728, 15474), (6879, 12439), (3075, 15986), (928, 12773), (14180, 19904), (69, 14594), (7496, 8727), (3349, 19370), (1002, 10401), (731, 833), (301, 17741), (7097, 12491), (951, 13831), (7264, 17289), (14348, 16246), (7637, 18116), (7565, 11327), (7169, 15060), (704, 9495), (13637, 18233), (3276, 6091), (3961, 9712), (10901, 16410), (13831, 16636), (6220, 9940), (9311, 19253), (16363, 16557), (12889, 19300), (1131, 15736), (7954, 13247), (5669, 13576), (12029, 17983), (2833, 12278), (14383, 16660), (3536, 5364), (12886, 17070), (12141, 16046), (969, 15378), (1424, 10109), (18945, 19437), (5582, 12897), (5524, 16457), (403, 7436), (6537, 17682), (7607, 17967), (13253, 16835), (11266, 18933), (11576, 15044), (8823, 17956), (187, 19953), (12572, 16793), (4235, 16996), (6733, 18394), (1839, 13962), (11951, 15764), (18166, 18677), (6548, 16538), (13546, 15890), (11691, 13579), (51, 11340), (17644, 17698), (10850, 15012), (916, 19656), (5806, 7523), (18047, 19151), (3001, 5923), (8365, 18056), (1063, 2308), (546, 2727), (477, 14843), (8177, 9214), (3587, 8802), (6049, 11286), (2277, 9512), (5230, 5487), (8362, 17281), (5509, 8942), (9649, 14899), (10551, 16269), (3741, 15524), (774, 10223), (11250, 12666), (6161, 13792), (3563, 8467), (8305, 16715), (6851, 19845), (682, 14144), (585, 7385), (4799, 13019), (1157, 5250), (14603, 16590), (13980, 17848), (7228, 16927), (7313, 14773), (1005, 17167), (12940, 18869), (10526, 13968)])
    print("Viterbi Algorithm : ", time() - t)

if __name__ == '__main__':
    print(longest(8, [(2, 0), (2, 1), (3, 2), (4, 2), (4, 3), (5, 3), (5, 4), (6, 5), (7, 5)]))
    print(longest(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))
    print(longest(20000, [(4402, 18651), (2067, 8358), (3863, 16234), (14728, 15474), (6879, 12439), (3075, 15986), (928, 12773), (14180, 19904), (69, 14594), (7496, 8727), (3349, 19370), (1002, 10401), (731, 833), (301, 17741), (7097, 12491), (951, 13831), (7264, 17289), (14348, 16246), (7637, 18116), (7565, 11327), (7169, 15060), (704, 9495), (13637, 18233), (3276, 6091), (3961, 9712), (10901, 16410), (13831, 16636), (6220, 9940), (9311, 19253), (16363, 16557), (12889, 19300), (1131, 15736), (7954, 13247), (5669, 13576), (12029, 17983), (2833, 12278), (14383, 16660), (3536, 5364), (12886, 17070), (12141, 16046), (969, 15378), (1424, 10109), (18945, 19437), (5582, 12897), (5524, 16457), (403, 7436), (6537, 17682), (7607, 17967), (13253, 16835), (11266, 18933), (11576, 15044), (8823, 17956), (187, 19953), (12572, 16793), (4235, 16996), (6733, 18394), (1839, 13962), (11951, 15764), (18166, 18677), (6548, 16538), (13546, 15890), (11691, 13579), (51, 11340), (17644, 17698), (10850, 15012), (916, 19656), (5806, 7523), (18047, 19151), (3001, 5923), (8365, 18056), (1063, 2308), (546, 2727), (477, 14843), (8177, 9214), (3587, 8802), (6049, 11286), (2277, 9512), (5230, 5487), (8362, 17281), (5509, 8942), (9649, 14899), (10551, 16269), (3741, 15524), (774, 10223), (11250, 12666), (6161, 13792), (3563, 8467), (8305, 16715), (6851, 19845), (682, 14144), (585, 7385), (4799, 13019), (1157, 5250), (14603, 16590), (13980, 17848), (7228, 16927), (7313, 14773), (1005, 17167), (12940, 18869), (10526, 13968)]))
    performance_test()
    # def generate_seq(k, length):
    #     import random;
    #     random.seed(1);
    #     return [tuple(sorted(random.sample(range(k), 2))) for _ in range(length)]
    #
    #
    # tuples = generate_seq(20000, 31000)
    # print(len(tuples), tuples)
    #
    # print(longest(len(tuples), tuples))

# Best Result
# Preparing Testcases...
# Testing Case  1 (open)...	0.003 s, Correct
# Testing Case  2 (open)...	0.004 s, Correct
# Testing Case  3 (open)...	0.004 s, Correct
# Testing Case  4 (open)...	0.005 s, Correct
# Testing Case  5 (open)...	0.005 s, Correct
# Testing Case  6 (hidden)...	0.006 s, Correct
# Testing Case  7 (hidden)...	0.010 s, Correct
# Testing Case  8 (hidden)...	0.015 s, Correct
# Testing Case  9 (hidden)...	0.020 s, Correct
# Testing Case 10 (hidden)...	0.059 s, Correct
# Total Time: 0.131 s
# Congratulations, you're correct on all test cases!
# You passed 10 out of 10 cases. Your autojudge score is 1.0.