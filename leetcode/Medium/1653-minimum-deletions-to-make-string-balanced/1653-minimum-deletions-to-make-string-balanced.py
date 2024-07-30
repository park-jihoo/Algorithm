class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt, dp = 0, [0]
        for ch in s:
            if ch == 'b':
                cnt += 1
                dp.append(dp[-1])
            else:
                dp.append(min(cnt, dp[-1]+1))
        return dp[-1]