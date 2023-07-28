class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:] # difference between first and second player
        
        for x in range(1, n):
            for l in range(n - x):
                r = l + x 
                dp[l] = max(nums[l] - dp[l + 1], nums[r] - dp[l])  # 현재 플레이어가 얻을 수 있는 최대 점수

        return dp[0] >= 0 