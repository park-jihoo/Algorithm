class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt, mod = Counter(s), 10**9+7
        arr = deque([cnt[chr(ord('a')+c)] for c in range(26)])
        for i in range(t):
            z = arr.pop()
            arr[0] =(arr[0] + z) % mod
            arr.appendleft(z)
        return sum(arr) % mod