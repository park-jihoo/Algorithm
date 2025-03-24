class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        unavailable = 0
        prev_end = 0

        for start, end in meetings:
            if start > prev_end:
                unavailable += end - start + 1
            else:
                unavailable += max(0, end - prev_end)
            prev_end = max(prev_end, end)

        return days - unavailable
