bool search(int* nums, int numsSize, int target){
    int start = 0;
  int end = numsSize - 1;

  while (start <= end) {
    int mid = start + (end - start) / 2;

    if (nums[mid] == target) {
      return true;
    }

    if(nums[start] == nums[end]){
        start++;
    }if (nums[start] <= nums[mid]) {
      if (target >= nums[start] && target < nums[mid]) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    } else {
      if (target > nums[mid] && target <= nums[end]) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
  }

  return false;
}