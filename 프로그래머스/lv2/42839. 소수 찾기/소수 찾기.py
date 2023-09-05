from itertools import permutations


def solution(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(list(numbers), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5 + 1)):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
