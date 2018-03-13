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

#   First Version of Best (has duplication)
def best_dup(sequence, opt=defaultdict(int)):

    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        elif len(sequence) == 0:
            opt[sequence] = (0, '')
        else:
            max_pair, str_pair, l = 0, '', len(sequence)
            #   best(i+1, j-1) + 1
            if pairNule(sequence[0], sequence[l-1]) == True:
                pre_max, pre_res = best_dup(sequence[1:l-1])
                max_pair = 1 + pre_max
                str_pair = '(' + pre_res + ')'
            #   max (best(i,k) + best(k+1,j))
            for k in range(1, l-1):
                pre_max_1, pre_res_1 = best_dup(sequence[:k])
                pre_max_2, pre_res_2 = best_dup(sequence[k:])
                if pre_max_1 + pre_max_2 > max_pair:
                    max_pair = pre_max_1 + pre_max_2
                    str_pair = pre_res_1 + pre_res_2
            opt[sequence] = (max_pair, str_pair)
    return opt[sequence]

def best(sequence, opt=defaultdict(int)):
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        elif len(sequence) == 0:
            opt[sequence] = (0, '')
        else:
            max_pair, str_pair, l = 0, '', len(sequence)
            #   best(i+1, j)
            pre_max, pre_res = best(sequence[1:])
            max_pair = pre_max
            str_pair = '.' + pre_res
            #   max(1+best(1,k)+best(k+1, j))
            for k in range(1, l):
                if pairNule(sequence[0], sequence[k]):
                    pre_max_1, pre_res_1 = best(sequence[1:k])
                    pre_max_2, pre_res_2 = best(sequence[k+1:])
                    if 1 + pre_max_1 + pre_max_2 > max_pair:
                        max_pair = 1 + pre_max_1 + pre_max_2
                        str_pair = '(' + pre_res_1 + ')' + pre_res_2
            opt[sequence] = (max_pair, str_pair)
    return opt[sequence]


def total(sequence):
    return len(sequence)

def kbest(sequence, k):
    return sequence, k

if __name__ == '__main__':

    print(best_dup("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))
    print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))
    print(best_dup("ACAGU"))
    print(best("ACAGU"))
    print(best_dup("GCACG"))
    print(best("GCACG"))
    print(best_dup("UUCAGGA"))
    print(best("UUCAGGA"))
    print(best_dup("GUUAGAGUCU"))
    print(best("GUUAGAGUCU"))

    print(total("ACAGU"))

    print(kbest("ACAGU", 3))