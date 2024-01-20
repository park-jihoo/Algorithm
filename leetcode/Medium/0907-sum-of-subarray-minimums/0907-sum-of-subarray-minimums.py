class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        s = deque([0])
        dp = [0] * len(arr)
        mod = 10**9+7
        for i in range(len(arr)):
            while arr[s[-1]] > arr[i]:
                s.pop()
            j = s[-1]
            dp[i] = dp[j] + (i-j)*arr[i]
            s.append(i)
        return sum(dp) % mod