class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in dic and i - dic[num] <= k:
                return True
            dic[num] = i
        return False
