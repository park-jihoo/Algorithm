class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pref, cur, ans, freq = [0], 0, 0, Counter()
        for n in nums:
            cur += n
            pref.append(cur)
        
        for idx in range(len(nums)):
            freq[nums[idx]] += 1
            if idx >= k:
                freq[nums[idx-k]] -= 1
                if freq[nums[idx-k]] == 0:
                    del freq[nums[idx-k]]
            if len(freq) == k:
                ans = max(ans, pref[idx+1]-pref[idx+1-k])
        return ans