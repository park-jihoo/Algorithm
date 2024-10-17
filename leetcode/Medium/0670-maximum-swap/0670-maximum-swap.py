class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(map(int, str(num)))
        for i in range(len(nums) - 1):
            if nums[i] >= max(nums[i+1:]):
                continue
            else:
                j=len(nums)-1-nums[::-1].index(max(nums[i+1:]))
                nums[i],nums[j]=nums[j],nums[i]
                break
        return int(''.join(map(str,nums)))