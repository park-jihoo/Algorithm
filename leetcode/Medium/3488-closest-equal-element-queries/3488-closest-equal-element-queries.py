class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        m = len(nums)
        for idx, val in enumerate(nums):
            d[val].append(idx)
        ans = []
        for q in queries:
            lst = d[nums[q]]
            n = len(lst)
            if n == 1:
                ans.append(-1)
            else:
                idx = bisect_left(lst, q)
                ans.append(
                    min(
                        (lst[idx] - lst[(idx - 1) % n]) % m,
                        (lst[(idx + 1) % n] - lst[idx]) % m,
                    )
                )
        return ans
