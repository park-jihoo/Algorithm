class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        left = 0
        minx, maxx = -1, -1
        for idx, num in enumerate(nums):
            if num < minK or num > maxK:
                left = idx + 1
                continue
            if num == minK:
                minx = idx
            if num == maxK:
                maxx = idx
            answer += max(0, min(minx, maxx) - left + 1)
        return answer
