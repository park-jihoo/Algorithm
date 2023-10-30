class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: (sum([int(y) for y in bin(x)[2:]]), x))
        return arr
