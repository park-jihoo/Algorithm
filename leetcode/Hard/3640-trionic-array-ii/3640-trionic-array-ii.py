class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        
        ln = len(nums)

        @cache
        def recursive(ind,trend):
            if ind == ln : return 0 if trend == 3 else -float('inf')

            res = -float('inf')
            if trend == 0:
                if ind < ln-1 and nums[ind] < nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,1))
                res = max(res,recursive(ind+1,trend))
            
            elif trend == 1:
                if ind < ln-1 and nums[ind] < nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,trend))
                
                elif ind < ln-1 and nums[ind] > nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,trend+1))
                
            elif trend == 2:
                if ind < ln-1 and nums[ind] > nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,trend))
                if ind < ln-1 and nums[ind] < nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,trend+1))
            
            elif trend == 3:
                if ind < ln-1 and nums[ind] < nums[ind+1]:
                    res = max(res,nums[ind] + recursive(ind+1,trend))
                res = max(res,nums[ind])

            return res
        
        return recursive(0,0)
