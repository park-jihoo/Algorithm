class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = {}
        dp = [0 for _ in range(len(arr))]
        answer = 0
        for i in range(len(arr)):
            prev = arr[i] - difference
            if prev in table:
                dp[i] = dp[table[prev]] + 1
            else:
                dp[i] = 1
            table[arr[i]] = i
            answer = max(answer, dp[i])
        return answer
