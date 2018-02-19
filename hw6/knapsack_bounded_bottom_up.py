def best(weight, item):
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



if __name__ == '__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))