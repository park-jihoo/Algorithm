class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        full = []
        ids = []
        heap = [(n[0], list_idx, 0) for list_idx, n in enumerate(nums)]
        heapq.heapify(heap)
        while heap:
            n, list_idx, i = heapq.heappop(heap)
            full.append(n)
            ids.append(list_idx)
            if i < len(nums[list_idx]) - 1:
                heapq.heappush(heap, (nums[list_idx][i + 1], list_idx, i + 1))

        ans = [float("-inf"), float("inf")]
        k, s, uniq = len(nums), [0] * len(nums), 0
        l = 0
        for r in range(len(full)):
            s[ids[r]] += 1
            if s[ids[r]] == 1:
                uniq += 1
            while uniq == k:
                if full[r] - full[l] < ans[1] - ans[0]:
                    ans = [full[l], full[r]]
                s[ids[l]] -= 1
                if s[ids[l]] == 0:
                    uniq -= 1
                l += 1
        return ans
