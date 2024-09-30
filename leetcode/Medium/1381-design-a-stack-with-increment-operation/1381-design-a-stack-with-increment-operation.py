class CustomStack:

    def __init__(self, maxSize: int):
        self.size = 0
        self.maxSize = maxSize
        self.stack = deque([])

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return
        else:
            self.size += 1
            self.stack.append(x)

    def pop(self) -> int:
        if self.size == 0:
            return -1
        else:
            self.size -= 1
            return self.stack.pop()
        
    def increment(self, k: int, val: int) -> None:
        temp = deque([])
        while self.stack:
            temp.append(self.stack.pop())
        cnt = 0
        while temp:
            ins = temp.pop()
            if cnt < k:
                ins += val
            cnt += 1
            self.stack.append(ins)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)