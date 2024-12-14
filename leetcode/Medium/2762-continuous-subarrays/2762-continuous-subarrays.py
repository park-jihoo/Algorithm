class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # max(subarray) - min(subarray) < 2 여야함
        minpq, maxpq = [], []
        i, j, ans, cnt = 0, 0, 0, Counter()
        while j < len(nums):
            heapq.heappush(minpq, nums[j])
            heapq.heappush(maxpq, -nums[j])
            cnt[nums[j]] += 1
            while maxpq[0] + minpq[0] < -2:
                cnt[nums[i]] -= 1
                while not cnt[minpq[0]]:
                    heapq.heappop(minpq)
                while not cnt[-maxpq[0]]:
                    heapq.heappop(maxpq)
                i += 1
            ans += (j-i+1)
            j += 1
        return ans