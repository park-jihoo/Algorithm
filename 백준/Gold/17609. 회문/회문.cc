#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isPalindrome(const string &s, int start, int end) {
    while (start < end) {
        if (s[start] != s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

bool isPseudoPalindrome(const string &s) {
    int len = s.length();
    for (int i = 0; i < len / 2; i++) {
        if (s[i] != s[len - i - 1]) {
            return isPalindrome(s, i + 1, len - i - 1) || isPalindrome(s, i, len - i - 2);
        }
    }
    return true;
}
int main(){
    int n;
    cin>> n;
    vector<string> v;
    for(int i=0; i<n; i++){
        string s;
        cin>> s;
        v.push_back(s);
    }
    for(const string &s : v){
        if(isPalindrome(s, 0, s.length()-1)){
            cout << 0 << endl;
        }else if(isPseudoPalindrome(s)){
            cout << 1 << endl;
        }else{
            cout << 2 << endl;
        }
    }
}