class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        maxlen = 1
        for num in sorted(set(nums)):
            while q and num-q[0] >= n:
                q.popleft()
            q.append(num)
            maxlen = max(maxlen, len(q))
        return n - maxlen