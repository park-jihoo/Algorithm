class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        desc = [0, *accumulate(a > b for a, b in pairwise(nums))]
        premax = list(accumulate(nums, max)) 
        sufmin = list(accumulate(reversed(nums), min))[::-1]
        cut = [True] + [premax[m - 1] <= sufmin[m] for m in range(1, n)]  

        def rotatable(l, r): 
            return desc[r] - desc[l] + (nums[r] > nums[l]) <= 1

        def sortable(k): 
            return all(cut[l] and rotatable(l, l + k - 1) for l in range(0, n, k))

        divisors = [k for k in range(1, n + 1) if n % k == 0]
        return sum(filter(sortable, divisors))