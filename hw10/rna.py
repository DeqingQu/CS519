from collections import defaultdict

def best(sequence):

    opt = defaultdict(int)
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        else:
            l = len(sequence)
            sub_sequence = sequence[:l-1]
            n, res = best(sub_sequence)
            opt[sequence] = (n+1, res+'.')
    return opt[sequence]


def total(sequence):
    return len(sequence)

def kbest(sequence, k):
    return sequence, k

if __name__ == '__main__':

    print(best("ACAGU"))
    print(best("UUCAGGA"))

    print(total("ACAGU"))

    print(kbest("ACAGU", 3))