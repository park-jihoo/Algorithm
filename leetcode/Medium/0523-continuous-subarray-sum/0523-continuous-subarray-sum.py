class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # length at least 2
        # sum of elements of subarray % k = 0
        prefix = 0
        mod_seen = {0: -1}
        for i in range(len(nums)):
            prefix += nums[i]
            prefix %= k
            if prefix in mod_seen:
                if i - mod_seen[prefix] > 1:
                    return True
            else:
                mod_seen[prefix] = i
        return False
