class Solution {
public:
  int arraySign(vector<int> &nums) {
    bool flag = true;
    for (int num : nums) {
      if (num == 0)
        return 0;
      else if (num < 0)
        flag = !(flag);
    }
    if (flag)
      return 1;
    else
      return -1;
  }
};
