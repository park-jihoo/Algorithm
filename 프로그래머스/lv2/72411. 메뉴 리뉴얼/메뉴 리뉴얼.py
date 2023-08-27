from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for k in course:
        c = []
        for menu in orders:
            for i in combinations(menu, k):
                c.append("".join(sorted(i)))
        sc = Counter(c).most_common()
        answer += [x for x, cnt in sc if cnt > 1 and cnt == sc[0][1]]
    return sorted(answer)
