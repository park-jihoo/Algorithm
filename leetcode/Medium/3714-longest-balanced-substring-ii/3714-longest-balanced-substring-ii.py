class Solution:
    def longestBalanced(self, s: str) -> int:
        di, res, p = defaultdict(lambda: inf), 1 ,[[0,0,0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]['abc'.index(c)] += 1
        for i, (a,b,c) in enumerate(p):
            for key in [('abc', a-b, a-c), ('ab', a-b, c), ('ac', a-c, b), ('bc', b-c, a), ('a', b, c), ('b', a, c), ('c', a, b)]:
                res, di[key] = max(res, i - di[key]), min(di[key], i)
        return res