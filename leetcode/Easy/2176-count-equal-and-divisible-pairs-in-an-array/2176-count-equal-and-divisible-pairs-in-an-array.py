class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnts = defaultdict(list)
        for idx, num in enumerate(nums):
            cnts[num].append(idx)
        ans = 0
        for key in cnts.keys():
            ans += sum([1 for a, b in combinations(cnts[key], 2) if (a*b)%k == 0])
        return ans