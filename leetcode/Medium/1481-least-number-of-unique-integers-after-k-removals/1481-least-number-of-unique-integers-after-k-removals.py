class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        s = sorted(arr,key = lambda x:(count[x],x))
        return len(set(s[k:]))