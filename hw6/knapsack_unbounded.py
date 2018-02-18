
def best(W, items):

    unbounded = {0: 0}
    def best_helper(W):
        if W not in unbounded:
            max = 0
            for item in items:
                if W - item[0] >= 0 and best_helper(W - item[0]) + item[1] > max:
                        max = best_helper(W - item[0]) + item[1]
            unbounded[W] = max
        return unbounded[W]

    return best_helper(W)


if __name__ == '__main__':
    print(best(3, [(2, 4), (3, 5)]))
    print(best(3, [(1, 5), (1, 5)]))
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))
    print(best(58, [(5, 9), (9, 18), (6, 12)]))
    print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))