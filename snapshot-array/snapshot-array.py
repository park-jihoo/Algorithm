class SnapshotArray:

    def __init__(self, length: int):
        self.curr = 0
        self.arr = [[[0, 0]] for i in range(length+1)]

    def set(self, index: int, val: int) -> None:
        temp = self.arr[index][-1]
        if temp[0] == self.curr:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.curr, val])

    def snap(self) -> int:
        self.curr +=1
        return self.curr - 1

    def get(self, index: int, snap_id: int) -> int:
        temp = self.arr[index]
        low, high = 0, len(temp) - 1
        while low < high:
            mid = low + (high - low + 1)//2
            if temp[mid][0] <= snap_id:
                low = mid
            else:
                high = mid - 1
        return temp[low][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)