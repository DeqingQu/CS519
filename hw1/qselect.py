import random

def qsort(array):
    if array == []:
        return []
    else:
        index = random.randint(0, len(array)-1)
        pivot = array[index]
        left = [x for x in array if x < pivot]
        right = [x for x in array[0:index] + array[index+1:len(array)] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)


def qselect(index, array):
    sorted_array = qsort(array)
    return sorted_array[index-1]


def main():
    print(qselect(2, [3, 10, 4, 7, 19]))
    print(qselect(4, [11, 2, 8, 3]))


main()
