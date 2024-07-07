class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remain, drank, empty = numBottles, numBottles, 0
        while remain >= numExchange:
            remain, empty = divmod(remain, numExchange)
            drank += remain
            remain += empty
        return drank
