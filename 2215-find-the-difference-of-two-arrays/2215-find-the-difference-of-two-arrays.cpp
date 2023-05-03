#include <set>

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> num1(nums1.begin(), nums1.end());
        set<int> num2(nums2.begin(), nums2.end());
        set<int> dif1 = {};
        set<int> dif2 = {};
        set_difference(num1.begin(), num1.end(), num2.begin(), num2.end(), inserter(dif1, dif1.begin()));
        set_difference(num2.begin(), num2.end(), num1.begin(), num1.end(), inserter(dif2, dif2.begin()));
        vector<vector<int>> answer = {{}, {}};
        answer[0].assign(dif1.begin(), dif1.end());
        answer[1].assign(dif2.begin(), dif2.end());
        return answer;
    }
};