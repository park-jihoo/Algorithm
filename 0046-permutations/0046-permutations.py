class Solution:
    def dfs(self, lst):
        if len(lst) == self.n:
            self.answer.append(lst[:])
            return
        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(lst + [self.nums[i]])
                self.visited[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.n = len(nums)
        self.nums = nums
        self.visited = [False] * self.n
        self.dfs([])
        return self.answer