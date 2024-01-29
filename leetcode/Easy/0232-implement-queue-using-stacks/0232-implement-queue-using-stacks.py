class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                temp = self.push_stack.pop()
                self.pop_stack.append(temp)
        return self.pop_stack.pop()

    def peek(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                temp = self.push_stack.pop()
                self.pop_stack.append(temp)  
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return False if self.push_stack or self.pop_stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()