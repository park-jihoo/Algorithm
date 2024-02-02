class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        minlen = len(str(low))
        maxlen = len(str(high))
        minans = ["".join(str(x+y) for x in range(minlen)) for y in range(1, 11-minlen)]
        maxans = ["".join(str(x+y) for x in range(maxlen)) for y in range(1, 11-maxlen)]
        ans = set()
        ans.update(int(x) for x in minans if int(x) >= low)
        for i in range(minlen+1, maxlen+1):
            lenans = ["".join(str(x+y) for x in range(i)) for y in range(1, 11-i)]
            ans.update(int(x) for x in lenans)
        ans -= set(int(x) for x in maxans if int(x) > high)
        return sorted(ans)