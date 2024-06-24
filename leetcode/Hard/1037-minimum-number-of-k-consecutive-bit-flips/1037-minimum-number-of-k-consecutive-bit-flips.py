class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        cur, ans, n = 0, 0, len(nums)
        for i in range(n):
            if i >= k and nums[i - k] > 1:
                nums[i - k] -= 2
                cur -= 1
            if cur & 1 ^ nums[i] == 0:
                if i + k > n:
                    return -1
                nums[i] += 2
                cur += 1
                ans += 1
        return ans
