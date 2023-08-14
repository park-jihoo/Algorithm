from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.logs = []
        self.train = defaultdict(tuple)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.train[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.logs.append([self.train[id], (stationName, t)])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summ = 0.0
        cnt = 0
        for log in self.logs:
            if log[0][0] == startStation and log[1][0] == endStation:
                summ += log[1][1] - log[0][1]
                cnt += 1
        return summ / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
