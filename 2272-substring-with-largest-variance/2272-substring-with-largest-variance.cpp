#include<bits/stdc++.h>

class Solution {
public:
    int kadane(char a, char b, string s) {
        int ans = 0;
        int countA = 0;
        int countB = 0;
        bool canExtendPrevB = false;

        for (char c : s) {
            if (c != a && c != b)
                continue;
            if (c == a)
                countA++;
            else
                countB++;
            if (countB > 0)
                ans = max(ans, countA - countB);
            else if (countB == 0 && canExtendPrevB)
                ans = max(ans, countA - 1);
            if (countB > countA) {
                countA = 0;
                countB = 0;
                canExtendPrevB = true;
            }
        }
        return ans;
    }

    int largestVariance(string s) {
        set<char> unique_chars(s.begin(), s.end());
        int max_variance = 0;
        for (char c1 : unique_chars) {
            for (char c2 : unique_chars) {
                if (c1 != c2)
                    max_variance = max(max_variance, kadane(c1, c2, s));
            }
        }
        return max_variance;
    }
};
