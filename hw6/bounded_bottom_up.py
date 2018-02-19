def best(weight, item):
    opt = [[0 for _ in range(len(item)+1)] for _ in range(weight+1)]  # initialize results matrix

    back = [[0 for _ in range(len(item))] for _ in range(weight+1)]

#     wt, val, cp = zip(*item)
    for i, (wt, val, cp) in enumerate(item):
        i += 1
        for cap in range(1,weight+1):
            for j in range(min(cp, cap//wt)+1):
#                 opt[cap][i] = opt[cap][i-1]
                if cap >= j*wt and opt[cap][i] < opt[cap-j*wt][i-1] + j * val:
                    opt[cap][i] = opt[cap-j*wt][i-1] + j * val
                    back[cap][i-1] = j

    def solution(w, i):
        if i < 0:
            return []
        new_w = w - item[i][0] * back[w][i]
        return solution(new_w, i-1) + [back[w][i]]

    return opt[weight][len(item)], solution(weight, len(item)-1)



if __name__ == '__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))