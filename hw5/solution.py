# O(n) time & space
def max_wis(a):
    back = {} # not really needed
    n = len(a)

    def top_down(i, best={-1:0, -2:0}):
        if i in best:
            return best[i]
        best[i] = max(top_down(i-1), top_down(i-2)+a[i])
        back[i] = best[i] == best[i-1]
        return best[i]

    return top_down(n-1), solution(n-1, a, back)

def solution(i, a, back):
    if i < 0:
        return []
    if back[i]:
        return solution(i - 1, a, back)
    else:
        return solution(i-2, a, back) + [a[i]]

print(max_wis([7,8,5]))
print(max_wis([7,13,5]))
print(max_wis([-7,-5]))
print(max_wis([0,-5]))