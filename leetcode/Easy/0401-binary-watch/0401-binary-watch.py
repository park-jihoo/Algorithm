class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        bmap = defaultdict(list)
        for i in range(60):
            bl = i.bit_count()
            bmap[bl].append(i)
        ans = []
        for hr in range(turnedOn + 1):
            mn = turnedOn - hr
            for h in bmap[hr]:
                if 0 <= h < 12:
                    for m in bmap[mn]:
                        ans.append(f"{h}:{m:02}")
        return ans
