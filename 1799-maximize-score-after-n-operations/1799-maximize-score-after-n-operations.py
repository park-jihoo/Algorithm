import math # for gcd

class Solution:
    def __init__(self):
        self.nums = []
        self.dp = []

    def dfs(self, i, mask):
        if i > len(self.nums)// 2:
            return 0
        if self.dp[i][mask] == 0:
            for j in range(len(self.nums)):
                for k in range(j+1, len(self.nums)):
                    new_mask = (1 << j) + (1 << k)
                    if mask & new_mask == 0:
                        self.dp[i][mask] = max(self.dp[i][mask], i* math.gcd(self.nums[j], self.nums[k]) +  self.dfs(i+1, mask+new_mask))
        return self.dp[i][mask]

    def maxScore(self, nums: List[int]) -> int:
        '''
        Array, Math, DP, Backtracking, Bit Manipulation, Number Theory, Bitmask
        '''
        answer = 0
        self.nums = nums
        # dp, bitmask
        self.dp = [[0]*(1 << len(nums)) for _ in range(len(nums)//2 + 1)]
        return self.dfs(1, 0)