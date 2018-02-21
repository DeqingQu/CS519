import heapq


def nsmallest(m):

    H = []
    n = len(m)
    for x in range(n):
        H.append((m[x][0][0], x, 0, 0))
    heapq.heapify(H)
    for _ in range(n-1):
        v, x, i, j = heapq.heappop(H)
        if i+1 < n:
            heapq.heappush(H, (m[x][i+1][j], x, i+1, j))
        if j+1 < n:
            heapq.heappush(H, (m[x][i][j+1], x, i, j+1))

    return heapq.heappop(H)[0]


def print3DMatrix(m):
    print("[")
    for m2 in m:
        for a in m2:
            print(a)
        print("---")
    print("]")
    print("------")

if __name__ == '__main__':
    testcase1 = [[[1,2], [3,4]], [[2,3], [4,5]]]
    testcase2 = [[[1,4,5], [4,5,6], [5,6,7]], [[1,3,4], [3,4,5], [4,5,6]], [[1,2,3], [2,3,4], [3,4,5]]]
    print3DMatrix(testcase1)
    print3DMatrix(testcase2)

    print(nsmallest(testcase1))
    print(nsmallest(testcase2))