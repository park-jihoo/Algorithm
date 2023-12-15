class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        ends = set()
        for s, e in paths:
            starts.add(s)
            ends.add(e)
        return list(ends - starts)[0]
