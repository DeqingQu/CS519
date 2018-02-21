



def print3DMatrix(m):
    print("[")
    for m2 in m:
        for a in m2:
            print(a)
        print("---")
    print("]")


if __name__ == '__main__':
    m = [[[1, 2], [3, 4]], [[2, 3], [4, 5]]]
    print3DMatrix(m)