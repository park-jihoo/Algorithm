class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans, n = [], len(code)
        m = {"electronics" : 0, "grocery" : 1, "pharmacy" : 2, "restaurant" : 3}
        for i in range(n):
            if re.fullmatch(r'^[a-zA-Z0-9_]+', code[i]) is not None and isActive[i] and businessLine[i] in m:
                ans.append([m[businessLine[i]], code[i]])
        return [c[1] for c in sorted(ans, key=lambda x:(x[0], x[1]))]