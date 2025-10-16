class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = {x: 0 for x in range(value)}
        for num in nums:
            cnt[num%value] += 1
        for i in range(len(nums)):
            if cnt[i%value] == 0:
                return i
            cnt[i%value] -= 1
        return len(nums)