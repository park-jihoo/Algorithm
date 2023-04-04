class Solution:
    def partitionString(self, s: str) -> int:
        answer = 1
        sub_map = {}
        for a in s:
            if sub_map.get(a) is None:
                sub_map[a] = 1
            else:
                answer +=1
                sub_map = {a: 1}
        return answer