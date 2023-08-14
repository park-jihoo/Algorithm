class Solution {
public:
  int peakIndexInMountainArray(vector<int> &arr) {
    // binary search
    int start = 0;
    int end = arr.size() - 1;
    int mid = (start + end) / 2;

    while (mid > 0 and mid < arr.size() - 1) {
      if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
        return mid;
      else if (arr[mid] < arr[mid - 1])
        end = mid;
      else
        start = mid;
      mid = (start + end) / 2;
    }
    return 0;
  }
};