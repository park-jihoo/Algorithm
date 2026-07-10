from typing import List
import bisect
from math import inf

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        values = sorted((v, i) for i, v in enumerate(nums))
        pos = [0] * n
        for i, (_, idx) in enumerate(values):
            pos[idx] = i

        nxt = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1][0] - values[l][0] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = n.bit_length()

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for a, b in queries:
            l = pos[a]
            r = pos[b]
            if l > r:
                l, r = r, l
            if l == r:
                ans.append(0)
                continue
            if nxt[l] == l:
                ans.append(-1)
                continue
            cur = l
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                nxt_pos = up[k][cur]
                if nxt_pos < r:
                    cur = nxt_pos
                    jumps += 1 << k

            if nxt[cur] >= r:
                ans.append(jumps + 1)
            else:
                ans.append(-1)

        return ans