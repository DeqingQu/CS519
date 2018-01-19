def longest(t):
    return _helper(t)[1]


def _helper(t):
    if t:
        left_l, left_m = _helper(t[0])
        right_l, right_m = _helper(t[2])
        return max(left_l, right_l) + 1, max(left_m, right_m, left_l + right_l)
    else:
        return 0, 0


if __name__ == "__main__":
    print(longest([[[], 1, []], 3, [[[[[], 4, []], 5, []], 6, []], 7, [[], 8, [[], 9, [[], 10, []]]]]]))
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
    print(longest([[[], 1, []], 2, [[], 3, []]]))
    print(longest([[], 1, []]))
    print(longest([]))