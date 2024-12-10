class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = Counter(s)
        cand = {}
        for key, val in cnt.items():
            if val >= 3:
                cand[key] = defaultdict(int)
        if not cand:
            return -1
        for ltr, size in groupby(s):
            if ltr not in cand:
                continue
            test = len(list(size))
            for substr in range(test, 0, -1):
                cand[ltr][substr] += test - substr + 1
        ans = 1
        for substr in cand:
            for size in cand[substr]:
                if cand[substr][size] >= 3:
                    ans = max(ans, size)
        return ans
