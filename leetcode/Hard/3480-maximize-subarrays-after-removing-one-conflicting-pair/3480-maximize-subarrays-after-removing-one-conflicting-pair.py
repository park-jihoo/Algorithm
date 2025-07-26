class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        ans, left, bonus = 0, [0, 0], [0]*(n+1)
        for r in range(n):
            for l in right[r+1]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            ans += (r+1) - left[0]
            if left[0] > 0:
                bonus[left[0]] += (left[0] - left[1])
        return ans + max(bonus)