class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = sorted(list(map(str, nums)), key=lambda a:a*100, reverse=True)
        return str(int("".join(numstr)))