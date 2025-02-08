class NumberContainers:
    def __init__(self):
        self.map = {}
        self.revmap = defaultdict(list)
        self.valid = {}

    def change(self, index: int, number: int) -> None:
        if index in self.map:
            prev = self.map[index]
            if prev == number:
                return
            self.valid[(prev, index)] = False

        self.map[index] = number
        heapq.heappush(self.revmap[number], index)
        self.valid[(number, index)] = True

    def find(self, number: int) -> int:
        if number not in self.revmap:
            return -1
        while self.revmap[number]:
            index = self.revmap[number][0]
            if self.valid.get((number, index), False):
                return index
            heapq.heappop(self.revmap[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
