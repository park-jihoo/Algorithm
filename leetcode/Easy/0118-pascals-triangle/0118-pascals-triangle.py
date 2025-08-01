class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ans = self.generate(numRows - 1)
        line = [1]
        for i in range(1, numRows - 1):
            line.append(ans[numRows - 2][i] + ans[numRows - 2][i - 1])
        line.append(1)
        ans.append(line)
        return ans
