from collections import OrderedDict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dictArr = {i:abs(x - arr[i]) for i in range(len(arr))}
        result = sorted((sorted(dictArr.keys(), key = dictArr.get))[:k])
        return [arr[i] for i in result]