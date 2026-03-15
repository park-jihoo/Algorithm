class Fancy:
    def __init__(self):
        self.arr=[]
        self.add=0
        self.mul=1
        self.mod=10**9+7

    def append(self, val: int) -> None:
        inverse_mul = pow(self.mul, -1, self.mod)
        self.arr.append(((val - self.add) * inverse_mul) % self.mod)

    def addAll(self, inc: int) -> None:
        self.add=(self.add+inc)%self.mod

    def multAll(self, m: int) -> None:
        self.mul=(self.mul*m)%self.mod
        self.add=(self.add*m)%self.mod

    def getIndex(self, idx: int) -> int:
        return (self.arr[idx]*self.mul+self.add)%self.mod if len(self.arr)>idx else -1