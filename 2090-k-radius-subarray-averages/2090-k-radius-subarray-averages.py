class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for idx, val in enumerate(nums):
            if idx < k or idx + k >= len(nums):
                answer.append(-1)
            elif idx == k:
                answer.append(sum(nums[: 2 * k + 1]))
            else:
                answer.append(answer[idx - 1] + nums[idx + k] - nums[idx - k - 1])
        return [x if x < 0 else x // (2 * k + 1) for x in answer]
