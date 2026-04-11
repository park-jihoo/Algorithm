class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        elems = defaultdict(list)
        for idx, val in enumerate(nums):
            elems[val].append(idx)
        ans = float("inf")
        for key, val in elems.items():
            if len(val) >= 3:
                distance = 2 * min(val[i + 2] - val[i] for i in range(len(val) - 2))
                ans = min(ans, distance)
        return ans if ans != float("inf") else -1
