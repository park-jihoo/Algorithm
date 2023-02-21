class Solution {
    public int singleNonDuplicate(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end){
            int center = (start + end) / 2;
            if(center == 0 || center == nums.length - 1)
                return nums[center];
            if(nums[center] == nums[center + 1] && center % 2 == 0)
                start = center + 1;
            else if(nums[center] == nums[center - 1] && center % 2 == 0)
                end = center - 1;
            else if(nums[center] == nums[center + 1] && center % 2 == 1)
                end = center - 1;
            else if(nums[center] == nums[center - 1] && center % 2 == 1)
                start = center + 1;
            else
                return nums[center];
            }
        return nums[start];
    }
}