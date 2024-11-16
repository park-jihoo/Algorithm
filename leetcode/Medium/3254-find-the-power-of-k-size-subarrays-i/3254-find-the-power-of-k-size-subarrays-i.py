class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        inc = [0]
        for idx in range(1, len(nums)):
            if nums[idx] - 1 != nums[idx-1]:
                inc.append(idx)
        inc.append(len(nums))
        ans = [-1] * (len(nums) - k + 1)
        for idx in range(len(inc)-1):
            if inc[idx+1] - inc[idx] >= k:
                # strictly increasing하는 k개가 있으니까, answer의 inc[idx]번째 게 nums[inc[idx] + k] 번째가 됨
                for j in range(inc[idx], inc[idx+1]-k+1):
                    ans[j] = nums[j] + k - 1

        return ans