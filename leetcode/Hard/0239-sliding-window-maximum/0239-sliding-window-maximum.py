class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i in range(len(nums)):
            self.clean_deque(q, nums, i, k)
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans

    def clean_deque(self, q, nums, i, k):
        if q and q[0] == i - k:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
