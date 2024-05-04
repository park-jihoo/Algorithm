class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        n = len(people)
        count = 1
        start, end = 0, n - 1
        interval_sum = 0
        interval_count = 0
        while start <= end:
            if interval_sum + people[start] > limit or interval_count == 2:
                interval_sum = 0
                interval_count = 0
                count += 1
            elif interval_sum + people[end] > limit:
                interval_sum += people[start]
                interval_count +=1
                start += 1
            else:
                interval_sum += people[end]
                interval_count +=1
                end -= 1
        return count