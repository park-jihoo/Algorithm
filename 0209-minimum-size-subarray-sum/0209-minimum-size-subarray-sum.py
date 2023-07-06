class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total, start, end = 0, 0, 0
        minlen = len(nums) + 1
        while start < len(nums):
            if total < target and end < len(nums):
                total += nums[end]
                end +=1
            elif total >= target:
                minlen = min(minlen, end-start)
                total -= nums[start]
                start+=1
            else:
                break
        return 0 if minlen > len(nums) else minlen
