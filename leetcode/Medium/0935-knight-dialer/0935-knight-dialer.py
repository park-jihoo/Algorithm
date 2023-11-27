class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        mod = 10 ** 9 + 7
        dp = [0] * 10
        prev_dp = [1] * 10
        
        for remain in range(1, n):
            dp = [0] * 10
            for s in range(10):
                ans = 0
                for i in jumps[s]:
                    ans = (ans + prev_dp[i]) % mod
                
                dp[s] = ans
                
            prev_dp = dp

        ans = 0
        for s in range(10):
            ans = (ans + prev_dp[s]) % mod
        return ans
        