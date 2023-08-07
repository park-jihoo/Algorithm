class Solution {
public:
  int searchInsert(vector<vector<int>> &matrix, int target) {
    int start = 0;
    int end = matrix.size() - 1;
    while (start <= end) {
      int center = (start + end) / 2;
      if (matrix[center][0] > target)
        end = center - 1;
      else if (matrix[center][0] < target)
        start = center + 1;
      else
        return center;
    }
    return start;
  }
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    int m = matrix.size();
    int n = matrix[0].size();
    int row = searchInsert(matrix, target);
    int left = 0;
    int right = n;
    while (left < right) {
      int mid = (left + right) / 2;
      if (matrix[row][mid] == target)
        return true;
      else if (matrix[row][mid] > target)
        right = mid;
      else
        left = mid + 1;
    }
    return false;
  }
};