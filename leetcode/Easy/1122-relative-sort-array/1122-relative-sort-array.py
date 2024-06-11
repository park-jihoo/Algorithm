class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * cnt[num])
            del cnt[num]
        ans.extend(sorted(cnt.elements()))
        return ans