class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minque, maxque = deque(), deque()
        start, end = 0, 0
        ans = 0
        while end < len(nums):
            while minque and nums[end] <= nums[minque[-1]]:
                minque.pop()
            while maxque and nums[end] >= nums[maxque[-1]]:
                maxque.pop()
            minque.append(end)
            maxque.append(end)

            while nums[maxque[0]] - nums[minque[0]] > limit:
                start += 1
                if start > minque[0]:
                    minque.popleft()
                if start > maxque[0]:
                    maxque.popleft()
            ans = max(ans, end - start + 1)
            end += 1
        return ans
