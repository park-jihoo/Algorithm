class AllOne:

    def __init__(self):
        self.dict = {}
        self.max = ""

    def inc(self, key: str) -> None:
        if key in self.dict:
            self.dict[key] += 1
            if self.dict[key] > self.dict[self.max]:
                self.max = key
        else:
            self.dict[key] = 1
            if self.max == "":
                self.max = key

    def dec(self, key: str) -> None:
        self.dict[key] -= 1
        if self.dict[key] == 0:
            del self.dict[key]
            if key == self.max:
                self.max = ""
        else:
            if key == self.max:
                self.max = max(zip(self.dict.values(), self.dict.keys()))[1]

    def getMaxKey(self) -> str:
        return self.max

    def getMinKey(self) -> str:
        if not self.dict:
            return ""
        return min(zip(self.dict.values(), self.dict.keys()))[1]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
