class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitSum = [0] * n
        for i, v in enumerate(nums):
            s = 0
            while v > 0:
                s += v % 10
                v //= 10
            digitSum[i] = s

        indices = list(range(n))
        indices.sort(key=lambda i: (digitSum[i], nums[i]))

        targetPos = [0] * n
        for pos, idx in enumerate(indices):
            targetPos[idx] = pos

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = targetPos[j]

        return n - cycles