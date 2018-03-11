from collections import defaultdict

def best(sequence):
    return sequence


def total(sequence):
    return len(sequence)

def kbest(sequence, k):
    return sequence, k

if __name__ == '__main__':

    print(best("ACAGU"))
    print(best("UUCAGGA"))

    print(total("ACAGU"))

    print(kbest("ACAGU", 3))