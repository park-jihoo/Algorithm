int searchInsert(int* nums, int numsSize, int target){
    int start = 0;
    int end = numsSize - 1;
    while (start <= end) {
      int center = (start + end) / 2;
      if (nums[center] > target)
        end = center - 1;
      else if (nums[center] < target)
        start = center + 1;
      else
        return center;
    }
    return start;
}