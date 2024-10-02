class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap = {}
        for idx, val in enumerate(sorted(list(set(arr)))):
            hashmap.setdefault(val, (idx + 1))
        return [hashmap[x] for x in arr]
