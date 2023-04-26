class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        strnum = str(num)
        numlist = [int(x) for x in list(strnum)]
        return self.addDigits(sum(numlist))