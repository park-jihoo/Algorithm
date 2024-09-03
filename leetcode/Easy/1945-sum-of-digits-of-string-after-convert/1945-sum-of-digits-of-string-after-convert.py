class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_num = "".join([str(ord(d)-ord('a')+1) for d in s])
        ans = s_num
        for i in range(k):
            ans = str(sum([int(x) for x in list(ans)]))
        return int(ans)