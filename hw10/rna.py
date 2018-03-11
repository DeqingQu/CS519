from collections import defaultdict

def best(sequence):

    opt = defaultdict(int)
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        else:
            l = len(sequence)
            sub_sequence = sequence[:l-1]
            n, s = best(sub_sequence)
            res = list(s)
            stack = []
            increase = False
            for i in range(l-2, -1, -1):
                if res[i] == ')':
                    stack.append(')')
                elif res[i] == '(':
                    stack.pop()
                if res[i] == '.' and len(stack) == 0:
                    if sequence[l-1] == 'U' and (sequence[i] == 'A' or sequence[i] == 'G'):
                        res[i] = '('
                        increase = True
                        break
                    if sequence[l-1] == 'G' and (sequence[i] == 'C' or sequence[i] == 'U'):
                        res[i] = '('
                        increase = True
                        break
                    if sequence[l-1] == 'U' and sequence[i] == 'G':
                        res[i] = '('
                        increase = True
                        break
                    if sequence[l-1] == 'A' and sequence[i] == 'U':
                        res[i] = '('
                        increase = True
                        break
            if increase:
                res.append(')')
                opt[sequence] = (n + 1, "".join(res))
            else:
                res.append('.')
                opt[sequence] = (n, "".join(res))
    return opt[sequence]


def total(sequence):
    return len(sequence)

def kbest(sequence, k):
    return sequence, k

if __name__ == '__main__':

    print(best("ACAGU"))
    print(best("UUCAGGA"))
    print(best("GUUAGAGUCU"))

    print(total("ACAGU"))

    print(kbest("ACAGU", 3))