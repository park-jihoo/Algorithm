class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        cnt = Counter(workerTimes).most_common()
        lo , hi = 0, cnt[-1][0] * mountainHeight * (mountainHeight+1) //2 + 1
        while lo < hi:
            mi = (lo+hi)//2 * 8
            if sum((floor(sqrt(1+mi/w))-1)//2*c for w, c in cnt) >= mountainHeight:
                hi = mi//8
            else:
                lo = mi//8+1
        return lo