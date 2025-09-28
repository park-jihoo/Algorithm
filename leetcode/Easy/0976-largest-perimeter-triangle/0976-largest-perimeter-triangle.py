class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sortnum = sorted(nums)
        for i in range(len(sortnum) - 3, -1, -1):
            if sortnum[i]+sortnum[i+1] > sortnum[i+2]:
                return sortnum[i] + sortnum [i+1] + sortnum [i+2]
        return 0