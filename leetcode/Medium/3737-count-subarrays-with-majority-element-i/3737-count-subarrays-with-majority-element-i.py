class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + (1 if nums[i] == target else -1)

        ans = 0

        for l in range(n):
            for r in range(l, n):
                if pref[r + 1] - pref[l] > 0:
                    ans += 1

        return ans
