class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for x in nums:
            events.append((x - k, 1)) 
            events.append((x + k + 1, -1)) 
        events.sort()
        max_beauty, current_beauty = 0, 0
        for _, delta in events:
            current_beauty += delta
            max_beauty = max(max_beauty, current_beauty)
        return max_beauty