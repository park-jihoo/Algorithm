class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for(int i=1;i<n/2+1;i++){
            if (n%i == 0){
                string sub = "";
                for(int j=0;j<n/i;j++)
                    sub += s.substr(0,i);
                
                if(sub == s)
                    return true;
            }
        }
        return false;
    }
};