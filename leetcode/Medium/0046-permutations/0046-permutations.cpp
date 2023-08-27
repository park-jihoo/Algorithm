class Solution {
public:
    void dfs(vector<int>& nums, vector<bool>& visited, vector<int>& current, vector<vector<int>>& result) {
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = 0; i < nums.size(); ++i) {
            if (!visited[i]) {
                visited[i] = true;
                current.push_back(nums[i]);
                dfs(nums, visited, current, result);
                current.pop_back();
                visited[i] = false;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> answer;
        int n = nums.size();
        vector<bool> visited(n, false);
        vector<int> current;
        dfs(nums, visited, current, answer);

        return answer;
    }
};