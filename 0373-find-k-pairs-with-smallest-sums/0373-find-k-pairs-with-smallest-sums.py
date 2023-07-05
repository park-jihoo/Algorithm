class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        out = []
        cnt = 0
        for i in range(min(len(nums1), k)):
            heapq.heappush(out, (nums1[i] + nums2[0], [nums1[i], nums2[0]], 0))

        answer = []
        while k > 0 and out:
            s, p, i = heapq.heappop(out)
            answer.append(p)
            if i + 1 < len(nums2):
                heapq.heappush(out, (p[0]+nums2[i+1], [p[0], nums2[i+1]], i+1))
            k -= 1
        return answer

            