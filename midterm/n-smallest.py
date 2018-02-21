



def print3DMatrix(m):
    print("[")
    for m2 in m:
        for a in m2:
            print(a)
        print("---")
    print("]")
    print("------")

if __name__ == '__main__':
    testcase1 = [[[1, 2], [3, 4]], [[2, 3], [4, 5]]]
    testcase2 = [[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[2, 3, 4], [3, 4, 5], [4, 5, 6]], [[3,4,5], [4,5,6], [5,6,7]]]
    print3DMatrix(testcase1)
    print3DMatrix(testcase2)