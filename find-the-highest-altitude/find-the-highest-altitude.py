class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer, now = 0, 0
        for g in gain:
            now += g
            answer = max(now, answer)
        return answer