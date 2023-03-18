class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.now = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.now+1]
        self.history.append(url)
        self.now+=1

    def back(self, steps: int) -> str:
        if steps >= self.now:
            self.now = 0
        else:
            self.now = self.now - steps
        return self.history[self.now]

    def forward(self, steps: int) -> str:
        self.now = min(self.now + steps, len(self.history)-1)
        return self.history[self.now]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)