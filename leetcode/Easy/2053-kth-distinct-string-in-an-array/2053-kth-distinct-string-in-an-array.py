class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        m = 0
        for word in arr:
            if cnt[word] == 1:
                m += 1
                if m == k:
                    return word
        return ""
