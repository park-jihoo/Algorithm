class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(max([sum(gain[:x]) for x in range(len(gain))]), sum(gain))

class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        answer, now = 0, 0
        for g in gain:
            now += g
            answer = max(now, answer)
        return answer