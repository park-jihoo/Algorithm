class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search
        start, end = 0, len(arr)-1
        mid = (start + end) // 2

        while mid > 0 and mid < len(arr) - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid - 1]:
                end = mid
            else:
                start= mid
            mid = (start + end) // 2
        return 0
