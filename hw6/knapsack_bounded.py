
#   Top-Down Method
def best(W, items):

    back = {}
    for i in range(0, len(items)):
        back[i] = {}

    bounded = {}
    for i in range(0, len(items)+1):
        bounded[i] = {}
        bounded[i][0] = 0
    for i in range(0, W+1):
        bounded[0][i] = 0

    def best_helper(x, i):
        if x not in bounded[i+1]:
            max_v = 0
            w = items[i][0]
            counter = min(items[i][2], x//w)
            for j in range(0, counter+1):
                v = best_helper(x - j*w, i-1)
                if v + items[i][1]*j > max_v:
                    max_v = v + items[i][1]*j
                    back[i][x] = j
            bounded[i+1][x] = max_v
        return bounded[i+1][x]

    def solution(x, i):
        if i < 0:
            return []
        if x not in back[i]:
            back[i][x] = 0
        return solution(x - back[i][x] * items[i][0], i-1) + [back[i][x]]

    return best_helper(W, len(items)-1), solution(W, len(items)-1)

#   Bottom-Up Method
def best2(weight, item):
    opt = [[0 for _ in range(weight+1)] for _ in range(len(item)+1)]  # initialize results matrix

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
print(best(3, [(2, 4, 2), (3, 5, 3)]))
print(best(3, [(1, 5, 2), (1, 5, 3)]))
print(best(3, [(1, 5, 1), (1, 5, 3)]))
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))
#   Bottom-up test
print("Bottom-up test")
print(best2(3, [(2, 4, 2), (3, 5, 3)]))
print(best2(3, [(1, 5, 2), (1, 5, 3)]))
print(best2(3, [(1, 5, 1), (1, 5, 3)]))
print(best2(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
print(best2(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))

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
a = best(Weight, lst)
print("Top-Down Time : ", time() -t)
t= time()
a = best2(Weight, lst)
print("Bottom-Up Time : ", time() -t)
