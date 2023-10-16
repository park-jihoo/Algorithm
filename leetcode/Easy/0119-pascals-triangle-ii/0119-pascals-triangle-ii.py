class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            temp = self.getRow(rowIndex - 1)
            ans = [1] + [temp[x] + temp[x + 1] for x in range(rowIndex - 1)] + [1]
            return ans
