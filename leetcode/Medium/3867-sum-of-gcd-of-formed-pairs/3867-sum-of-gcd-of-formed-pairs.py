class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pref = list(accumulate(nums, max))
        prefix_gcd = sorted([math.gcd(n, p) for n, p in zip(nums, pref)])
        n = len(nums)
        return sum(
            math.gcd(prefix_gcd[i], prefix_gcd[n - 1 - i]) for i in range(n // 2)
        )
