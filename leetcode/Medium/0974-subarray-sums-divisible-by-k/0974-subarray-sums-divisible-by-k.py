class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        mod_seen = defaultdict(int)
        mod_seen[0] = 1
        ans = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix %= k
            if prefix in mod_seen:
                if mod_seen[prefix] > 0:
                    ans += mod_seen[prefix]
            mod_seen[prefix] += 1
        return ans
