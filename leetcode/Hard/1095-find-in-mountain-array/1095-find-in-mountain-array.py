# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find max value
        length = mountain_arr.length()

        left, right = 1, length - 2
        while left != right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        max_idx = left

        # increasing part
        left, right = 0, max_idx
        while left != right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        
        if mountain_arr.get(left) == target:
            return left
        
        # decreasing part
        left, right = max_idx+1, length - 1
        while left != right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid

        if mountain_arr.get(left) == target:
            return left

        return -1
