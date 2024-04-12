class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, Counter(height[2:])
        for idx in range(1, len(height) - 1):
            mid = height[idx]
            rightmax = max(right.keys())
            left = max(left, height[idx - 1])
            right[height[idx + 1]] -= 1
            if right[height[idx + 1]] == 0:
                del right[height[idx + 1]]
            ans += max(min(left, rightmax) - mid, 0)
        return ans
