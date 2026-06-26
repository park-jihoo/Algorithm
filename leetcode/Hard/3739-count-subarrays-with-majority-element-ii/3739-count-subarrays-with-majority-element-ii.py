class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        freq = [0] * (2 * n + 1)
        freq[n] = 1
        i = n
        res, pref = 0, 0
        for x in nums:
            if x == target:
                pref += freq[i]
                i += 1
            else:
                i -= 1
                pref -= freq[i]
            freq[i] += 1
            res += pref
        return res