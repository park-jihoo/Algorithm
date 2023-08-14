#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> vals;
        for(int i=0;i<nums.size();i++){
            
            if(vals.find(nums[i]) != vals.end()){
                return {vals.at(nums[i]), i};
            }else{
                vals.insert({target-nums[i], i});
            }
        }
        return {0, 0};
    }
};