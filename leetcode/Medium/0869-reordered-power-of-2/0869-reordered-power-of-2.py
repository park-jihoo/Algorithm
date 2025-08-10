class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c = []
        for i in range(31):
            c.append(Counter(str(1 << i)))
        return Counter(str(n)) in c
