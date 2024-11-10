class Solution:
    def update(self, bits, x, change):
        for i in range(32):
            if (x >> i) & 1:
                bits[i] += change

    def convert(self, bits):
        result = 0
        for i in range(32):
            if bits[i]:
                result |= 1 << i
        return result

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 32
        ans = len(nums) + 1
        start = 0

        for end in range(len(nums)):
            self.update(bits, nums[end], 1)
            while start <= end and self.convert(bits) >= k:
                ans = min(ans, end - start + 1)
                self.update(bits, nums[start], -1)
                start += 1
        if ans == len(nums) + 1:
            return -1
        return ans
