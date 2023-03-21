class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int cnt = 0;
        for(int i=0;i<nums.size();i++){
            if(to_string(nums[i]).size() % 2){}
            else{
                cnt++;
            }
        }
        return cnt;
    }
};