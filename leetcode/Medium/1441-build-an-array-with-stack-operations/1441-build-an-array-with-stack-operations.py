class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n = min(max(target), n)
        answer = []
        for i in range(n):
            if i+1 in target:
                answer.append("Push")
            else:
                answer.extend(["Push", "Pop"])
        return answer