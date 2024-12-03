class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer, curr = "", 0
        for i, c in enumerate(s):
            if curr < len(spaces) and i == spaces[curr]:
                curr += 1
                answer += " "
            answer += c
        return answer