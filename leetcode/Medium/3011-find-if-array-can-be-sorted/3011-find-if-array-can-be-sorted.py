class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        setbits = [bin(x).count('1') for x in nums]
        segments = [[0]]
        for idx, (num, setbit) in enumerate(zip(nums, setbits)):
            if idx == 0:
                continue
            if setbits[segments[-1][0]] == setbits[idx]:
                segments[-1].append(idx)
            else:
                segments.append([idx])
        for idx in range(len(segments)-1):
            bfr = [nums[x] for x in segments[idx]]
            aft = [nums[x] for x in segments[idx+1]]
            if not max(bfr) < min(aft):
                return False
        return True