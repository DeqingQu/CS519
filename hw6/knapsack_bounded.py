
#   Top-Down Method
def best0(W, items):

    back = {}
    for i in range(0, len(items)):
        back[i] = {}

    opt = {}
    for i in range(0, len(items)+1):
        opt[i] = {}

    def best_helper(i, x):
        if i+1 == 0 or x == 0:
            return 0
        if x not in opt[i+1]:
            max_v = 0
            w, v, c = items[i]
            counter = min(c, x//w)
            for j in range(0, counter+1):
                val = best_helper(i-1, x - j*w) + v*j
                if val > max_v:
                    max_v = val
                    back[i][x] = j
            opt[i+1][x] = max_v
        return opt[i+1][x]

    def solution(i, x):
        if i < 0:
            return []
        if x not in back[i]:
            back[i][x] = 0
        return solution(i-1, x - back[i][x] * items[i][0]) + [back[i][x]]

    return best_helper(len(items)-1, W), solution(len(items)-1, W)

#   Bottom-Up Method
def best(weight, item):
    opt = [[0 for _ in range(weight+1)] for _ in range(len(item)+1)]

    back = [[0 for _ in range(weight+1)] for _ in range(len(item))]

    for i, (w, v, c) in enumerate(item):
        i += 1
        for x in range(1, weight+1):
            for j in range(min(c, x//w)+1):
                if x >= j*w and opt[i][x] < opt[i-1][x-j*w] + j * v:
                    opt[i][x] = opt[i-1][x-j*w] + j * v
                    back[i-1][x] = j

    def solution(w, i):
        if i < 0:
            return []
        new_w = w - item[i][0] * back[i][w]
        return solution(new_w, i-1) + [back[i][w]]

    return opt[len(item)][weight], solution(weight, len(item)-1)

#   Top-down test
print("Top-down test")
print(best0(3, [(2, 4, 2), (3, 5, 3)]))
print(best0(3, [(1, 5, 2), (1, 5, 3)]))
print(best0(3, [(1, 5, 1), (1, 5, 3)]))
print(best0(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best0(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
#   Bottom-up test
print("Bottom-up test")
print(best(3, [(2, 4, 2), (3, 5, 3)]))
print(best(3, [(1, 5, 2), (1, 5, 3)]))
print(best(3, [(1, 5, 1), (1, 5, 3)]))
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))

def performance_test():
    import sys
    sys.setrecursionlimit(1000000)

    import random
    times = 200
    lst = []
    for _ in range(times):
        lst.append((random.randint(1, 10), random.randint(5, 20), random.randint(1, 10)))
    Weight = random.randint(times*10, times*11)

    print("weight = ", Weight)

    from time import time
    t= time()
    a = best0(Weight, lst)
    print("Top-Down Time : ", time() -t)
    t= time()
    a = best(Weight, lst)
    print("Bottom-Up Time : ", time() -t)

performance_test()