def lis(s):
    l = len(s)
    if l == 1: return s
    pre = lis(s[0:l-1])
    if pre[len(pre)-1] < s[l-1]:
        return pre + s[l-1]
    else:
        return pre

if __name__ == '__main__':
    print(lis("aebbcg"))
    print(lis("zyx"))