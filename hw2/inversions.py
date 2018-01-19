def num_inversions(a):


def _num_inversions_help(a)
    if len(a) == 1 or a == []:
        return a, 0
    first, first_inversions = a[:len(a)//2]
    second, second_inversions = a[len(a)//2:]



def main():
    print(num_inversions([4, 1, 3, 2]))
    print(num_inversions([2, 4, 1, 3]))


main()