class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        ans = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                prev = arr[j]
                curr = arr[i] + arr[j]
                curlen = 2
                while curr in nums:
                    prev, curr = curr, curr + prev
                    curlen += 1
                    ans = max(ans, curlen)

        return ans
