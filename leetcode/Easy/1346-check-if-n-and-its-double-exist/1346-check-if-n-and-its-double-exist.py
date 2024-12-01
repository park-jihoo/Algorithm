class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for idx, val in enumerate(arr):
            try:
                if arr.index(val*2) != idx:
                    return True
            except:
                continue
        return False