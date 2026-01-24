class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        val = nums[:]
        prev = [-1] + list(range(n - 1))
        next = list(range(1, n)) + [-1]
        alive = [True] * n

        bad = 0
        for i in range(n - 1):
            if val[i] > val[i + 1]:
                bad += 1
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (val[i] + val[i + 1], i))

        ops = 0

        while bad > 0:
            s, i = heapq.heappop(heap)

            j = next[i]
            if j == -1 or not alive[i] or not alive[j]:
                continue
            if val[i] + val[j] != s:
                continue

            pi = prev[i]
            nj = next[j]

            if pi != -1 and val[pi] > val[i]:
                bad -= 1
            if val[i] > val[j]:
                bad -= 1
            if nj != -1 and val[j] > val[nj]:
                bad -= 1

            val[i] += val[j]
            alive[j] = False

            next[i] = nj
            if nj != -1:
                prev[nj] = i

            if pi != -1 and val[pi] > val[i]:
                bad += 1
            if nj != -1 and val[i] > val[nj]:
                bad += 1

            if pi != -1:
                heapq.heappush(heap, (val[pi] + val[i], pi))
            if nj != -1:
                heapq.heappush(heap, (val[i] + val[nj], i))

            ops += 1

        return ops
