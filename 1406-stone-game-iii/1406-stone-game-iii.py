class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def dp(i):
            if i == len(stoneValue):
                return 0
            res = float('-inf')
            summ = 0
            for j in range(i, i+3):
                if j == len(stoneValue):
                    break
                summ += stoneValue[j]
                res = max(res, summ - dp(j+1))
            return res
        
        score = dp(0)
        if score == 0:
            return 'Tie'
        elif score > 0:
            return 'Alice'
        return 'Bob'