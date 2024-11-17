class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == k else -1
        q = deque([])
        pref = list(accumulate(nums, initial=0))
        ans = n + 1

        for idx, val in enumerate(pref):
            while q and val <= pref[q[-1]]:
                q.pop()
            while q and val - pref[q[0]] >= k:
                ans = min(ans, idx - q.popleft())
            q.append(idx)

        return ans if ans != n + 1 else -1
            