class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr).most_common()
        return c[0][0]
