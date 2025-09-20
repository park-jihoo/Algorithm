class Router:
    def __init__(self, memoryLimit: int):
        self.routes = deque()
        self.max_routes = memoryLimit
        self.routes_set = set()
        self.dest_timestamp = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.routes_set:
            return False
        if len(self.routes) == self.max_routes:
            self.forwardPacket()

        self.routes.append([source, destination, timestamp])
        self.routes_set.add((source, destination, timestamp))
        self.dest_timestamp[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.routes:
            source, destination, timestamp = self.routes.popleft()
            self.routes_set.remove((source, destination, timestamp))
            self.dest_timestamp[destination].popleft()
            return [source, destination, timestamp]
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time_range = self.dest_timestamp[destination]
        L = bisect_left(time_range, startTime)
        R = bisect_right(time_range, endTime)
        return R - L


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
