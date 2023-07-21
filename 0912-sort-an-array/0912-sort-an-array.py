class Solution:
    # Merge Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums1, nums2 = nums[: len(nums) // 2], nums[len(nums) // 2 :]
        nums1, nums2 = self.sortArray(nums1), self.sortArray(nums2)
        i = 0
        j = 0
        answer = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                answer.append(nums1[i])
                i += 1
            else:
                answer.append(nums2[j])
                j += 1
        if i == len(nums1):
            answer += nums2[j:]
        else:
            answer += nums1[i:]
        return answer
