class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(2**n):
            sub = []
            for j in range(n):
                if (i >> j) % 2 == 1:
                    sub.append(nums[j])
            ans.append(sub)
        return ans
