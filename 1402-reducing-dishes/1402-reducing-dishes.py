class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        start, end = 0, len(satisfaction) - 1
        while True:
            if start >= end:
                break
            mid = (start + end) // 2
            if satisfaction[mid] == 0:
                start = mid
                break
            elif satisfaction[mid] < 0:
                start = mid + 1
            else:
                end = mid - 1
        if len(satisfaction) == 1 and satisfaction[0] < 0:
            return 0
        elif start == 0:
            return sum([(idx + 1) * val for idx, val in enumerate(satisfaction)])
        elif start == len(satisfaction) - 1:
            return 0
        else:
            minus = satisfaction[start - 1 :: -1]
            plus = satisfaction[start:]
            answer = sum([(idx + 1) * val for idx, val in enumerate(plus)])
            sumplus = sum(plus)
            for num in minus:
                if num + sumplus > 0:
                    answer += num + sumplus
                    sumplus += num
                else:
                    return answer
        return answer
