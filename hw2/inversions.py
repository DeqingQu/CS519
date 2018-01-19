def num_inversions(a):
    return _num_inversions_help(a)[1]


def _num_inversions_help(a):
    if len(a) == 1 or a == []:
        return a, 0
    first, first_inversions = _num_inversions_help(a[:len(a)//2])
    second, second_inversions = _num_inversions_help(a[len(a)//2:])
    inversions = 0
    result = []
    first_index = 0
    second_index = 0
    lfirst = len(first)
    lsecond = len(second)
    while first_index < lfirst or second_index < lsecond:
        if first_index == lfirst:
            result.append(second[second_index])
            second_index += 1
        elif second_index == lsecond:
            result.append(first[first_index])
            first_index += 1
        else:
            if second[second_index] < first[first_index]:
                inversions += lfirst - first_index
                result.append(second[second_index])
                second_index += 1
            else:
                result.append(first[first_index])
                first_index += 1
    return result, inversions + first_inversions + second_inversions


if __name__ == "__main__":
    print(num_inversions([4, 1, 3, 2]))
    print(num_inversions([2, 4, 1, 3]))