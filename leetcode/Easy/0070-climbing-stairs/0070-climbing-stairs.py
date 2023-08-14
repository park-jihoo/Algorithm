class Solution(object):
    def climbStairs(self, n):
        arr = [0, 1, 2]
        for i in range(n + 1):
            if i > 2:
                arr.append(arr[i - 1] + arr[i - 2])
        return arr[n]
