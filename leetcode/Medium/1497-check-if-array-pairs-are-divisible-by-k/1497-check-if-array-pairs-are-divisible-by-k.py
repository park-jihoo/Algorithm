class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr_cnt = Counter([x % k for x in arr])
        if k % 2 == 0 and arr_cnt[k // 2] % 2 != 0:
            return False
        if arr_cnt[0] % 2 != 0:
            return False
        for i in range(1, (k + 1) // 2):
            if arr_cnt[i] != arr_cnt[k - i]:
                return False
        return True
