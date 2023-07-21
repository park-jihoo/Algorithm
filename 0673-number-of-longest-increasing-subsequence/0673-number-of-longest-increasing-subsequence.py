class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Array DP
        n = len(nums)
        length = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # if longest subsequence change
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        cnt[i] = 0
                    # get one more lolngest subsequence
                    if length[j] + 1 == length[i]:
                        cnt[i] += cnt[j]
        maxlen = max(length)
        return sum(c for l, c in zip(length, cnt) if l == maxlen)