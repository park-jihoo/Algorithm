class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [list(map(int, x.split(":"))) for x in timePoints]
        mts = sorted([x[0] * 60 + x[1] for x in times])
        mts.append(mts[0] + 24 * 60)
        return min(mts[i+1]-mts[i] for i in range(len(timePoints)))
