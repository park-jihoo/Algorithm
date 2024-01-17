class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = set()
        for idx, cnt in Counter(arr).items():
            if cnt in occur:
                return False
            occur.add(cnt)
        return True