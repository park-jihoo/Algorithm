class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        up = 0
        la, lb = list(a), list(b)
        while la or lb:
            ba, bb = 0, 0
            if la:
                ba = int(la.pop())
            if lb:
                bb = int(lb.pop())
            if up & ba & bb:
                up = 1
                ans.append("1")
            elif ba&bb or up&ba or up&bb:
                up = 1
                ans.append("0")
            elif ba or bb or up:
                up = 0
                ans.append("1")
            else:
                ans.append("0")
        if up:
            ans.append("1")
        return "".join(ans[::-1])