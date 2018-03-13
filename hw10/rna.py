from collections import defaultdict

def pairNule(a, b):
    if a == 'U' and (b == 'A' or b == 'G'):
        return True
    if a == 'G' and (b == 'C' or b == 'U'):
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'A' and b == 'U':
        return True
    return False

def best(sequence):

    opt = defaultdict(int)
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        elif len(sequence) == 0:
            opt[sequence] = (0, '')
        else:
            l = len(sequence)
            sub_sequence = sequence[1:l-1]
            n, s = best(sub_sequence)
            res = ['.'] + list(s) + ['.']
            stack = []
            for i in range(1, l):
                if res[i] == '(':
                    stack.append('(')
                elif res[i] == ')':
                    stack.pop()
                elif len(stack) == 0:
                    if pairNule(sequence[0], sequence[i]):
                        res[0] = '('
                        res[i] = ')'
                        n += 1
                        break
            if res[l-1] == '.':
                stack = []
                for i in range(l-2, -1, -1):
                    if res[i] == ')':
                        stack.append(')')
                    elif res[i] == '(':
                        stack.pop()
                    elif len(stack) == 0:
                        if pairNule(sequence[l-1], sequence[i]):
                            res[l-1] = ')'
                            res[i] = '('
                            n += 1
                            break
            opt[sequence] = (n, "".join(res))

    return opt[sequence]


def total(sequence):
    return len(sequence)

def kbest(sequence, k):
    return sequence, k

if __name__ == '__main__':

    print(best("CGAGGUGGCACUGACCAAACACCACCGAAAC"))
    print(best("ACAGU"))
    print(best("ACAGU"))
    print(best("GCACG"))
    print(best("UUCAGGA"))
    print(best("GUUAGAGUCU"))

    print(total("ACAGU"))

    print(kbest("ACAGU", 3))