class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(x[0]*x[1] for x in Counter(s).most_common())