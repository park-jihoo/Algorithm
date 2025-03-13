class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        freq = [0] * (n + 1)
        tmp, ans = 0, 0
        for i in range(n):
            while tmp < nums[i] - freq[i]:
                if ans >= m:
                    return -1
                l, r, v = queries[ans]
                if r < i:
                    ans += 1
                    continue
                freq[max(l, i)] += v
                freq[r + 1] -= v
                ans += 1
            tmp += freq[i]
        return ans
