class Solution:
    def getSum(self, n, index, x):
        l = min(index, x-1)
        r = min(n-index, x)
        lSum = ((x-1)+(x-l))*l/2
        rSum = (x+(x-r+1))*r/2
        return lSum+rSum

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        #Binary Search Greedy
        maxSum -=n
        l = 0
        r = maxSum

        while l < r:
            med = (l + r) // 2
            if self.getSum(n, index, med) >= maxSum:
                r = med
            else:
                l = med + 1
        return l if self.getSum(n, index, l) > maxSum else l+1