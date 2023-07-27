class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[:-n]) # sum of extra battery

        live = batteries[-n:] # n largest batteries to choose for each computers

        for i in range(n-1):
            if extra // (i+1) < live[i+1]-live[i]:
                return live[i]+extra//(i+1)
            extra -= (i+1)*(live[i+1]-live[i])
        return live[-1]+extra//n