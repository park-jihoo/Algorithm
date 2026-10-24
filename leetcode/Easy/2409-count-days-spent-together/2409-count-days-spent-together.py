class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = list(
            accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], initial=0)
        )
        aAm, aAd = map(int, arriveAlice.split("-"))
        lAm, lAd = map(int, leaveAlice.split("-"))
        aBm, aBd = map(int, arriveBob.split("-"))
        lBm, lBd = map(int, leaveBob.split("-"))
        aA, lA, aB, lB = (
            days[aAm - 1] + aAd,
            days[lAm - 1] + lAd,
            days[aBm - 1] + aBd,
            days[lBm - 1] + lBd,
        )
        return max(min(lA, lB) - max(aA, aB) + 1, 0)
