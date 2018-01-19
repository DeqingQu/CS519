

def mergesort(a):
    if len(a) == 1 or a == []:
        return a
    first = mergesort(a[:len(a)//2])
    second = mergesort(a[len(a)//2:])

    if first == []: return second
    if second == []: return first

    first_index = 0
    second_index = 0
    result = []

    while first_index != len(first) or second_index != len(second):
        if first_index == len(first):
            result.append(second[second_index])
            second_index += 1
        elif second_index == len(second):
            result.append(first[first_index])
            first_index += 1
        else:
            if first[first_index] < second[second_index]:
                result.append(first[first_index])
                first_index += 1
            else:
                result.append(second[second_index])
                second_index += 1

    return result


def main():
    print(mergesort([4, 2, 5, 1, 6, 3]))


main()