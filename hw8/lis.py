def lis(s):
    l, arr = len(s), []
    arr.append((0, s[0]))
    for i in range(1, l):
        max_lis = -1
        max_index = -1
        for j in range(i):
            if s[j] < s[i] and arr[j][0] > max_lis:
                max_lis = arr[j][0]
                max_index = j
        if max_index == -1: arr.append((0, s[i]))
        else: arr.append((max_lis + 1,  arr[max_index][1] + s[i]))
    return arr[l-1][1]

if __name__ == '__main__':
    print(lis("aebbcg"))
    print(lis("zyx"))