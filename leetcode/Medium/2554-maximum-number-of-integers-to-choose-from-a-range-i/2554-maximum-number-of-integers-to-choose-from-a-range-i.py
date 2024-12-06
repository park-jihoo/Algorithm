class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans, x = 0, 0
        banned = set(banned)
        for i in range(1, n + 1):
            if x + i > maxSum:
                break
            if i not in banned:
                ans += 1
                x += i
        return ans
