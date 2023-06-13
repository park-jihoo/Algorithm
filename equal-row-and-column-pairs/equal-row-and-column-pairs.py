class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        for row in grid:
            for i in range(len(grid)):
                col = [x[i] for x in grid]
                if row == col:
                    answer +=1


        return answer