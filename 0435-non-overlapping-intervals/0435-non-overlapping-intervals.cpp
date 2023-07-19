class Solution {
public:

    static bool comp(vector<int>&a, vector<int>&b){
        return a[1]<b[1];
    }

    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), comp);
        int answer = 0;
        int k = -6 * pow(10, 4);

        for(auto x : intervals){
            if (x[0] >= k)
                k = x[1];
            else
                answer+=1;
        }
        return answer;
    }
};