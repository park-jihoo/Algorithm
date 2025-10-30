class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans, n = 0, len(target)
        for i in range(n - 1):
            if target[i] > target[i + 1]:
                ans += target[i] - target[i + 1]
        return ans + target[n - 1]
