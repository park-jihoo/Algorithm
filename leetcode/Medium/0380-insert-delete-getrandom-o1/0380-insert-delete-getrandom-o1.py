class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            last = self.nums[-1]
            idx = self.map[val]
            self.map[last] = idx
            self.nums[idx] = last
            self.nums[-1] = val
            self.nums.pop()
            self.map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
