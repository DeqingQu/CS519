
def best(W, items):

    back = {}
    for i in range(0, len(items)):
        back[i] = {}
        for j in range(0, W+1):
            back[i][j] = 0

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
        new_x = x - back[i][x] * items[i][0]
        return solution(new_x, i-1) + [back[i][x]]

    return best_helper(W, len(items)-1), solution(W, len(items)-1)



if __name__ == '__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))