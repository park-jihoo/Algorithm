class Solution:
    def calcSum(self, nums, cost, target):
        r = 0
        for n, c in zip(nums, cost):
            r += abs(n - target) * c
        return r

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        s, e = min(nums), max(nums)
        while s < e:
            mid = (s + e) // 2
            left, right = self.calcSum(nums, cost, mid), self.calcSum(
                nums, cost, mid + 1
            )
            if left < right:
                e = mid
            else:
                s = mid + 1
        return self.calcSum(nums, cost, s)
