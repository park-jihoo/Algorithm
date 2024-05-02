class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        table = defaultdict(set)
        for num in nums:
            table[abs(num)].add(num)
            if len(table[abs(num)]) == 2:
                ans = max(ans, abs(num))
        return ans