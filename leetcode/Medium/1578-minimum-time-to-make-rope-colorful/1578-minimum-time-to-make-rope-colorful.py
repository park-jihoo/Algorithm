class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, prev = 0, 0
        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                ans += min(neededTime[prev], neededTime[i])
                if neededTime[prev] < neededTime[i]:
                    prev = i
        return ans