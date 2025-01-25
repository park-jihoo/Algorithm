class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        numsort = sorted(nums)
        sets = []
        tempset = [numsort[0]]
        graph = {numsort[0] : 0}
        for i in range(1, len(nums)):
            if numsort[i] - tempset[-1] > limit:
                sets.append(tempset)
                tempset = [numsort[i]]
            else:
                tempset.append(numsort[i])
            graph[numsort[i]] = len(sets)
        sets.append(tempset)
        cur_idx = [0]*len(sets)
        ans = []
        for num in nums:
            idx = graph[num]
            ans.append(sets[idx][cur_idx[idx]])
            cur_idx[idx] += 1

        return ans