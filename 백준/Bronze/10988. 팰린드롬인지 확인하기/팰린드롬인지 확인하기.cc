#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin >> s;

    for(int i=0; i<s.length()/2; i++){
        if (s[i] == s[s.length()-1-i]) continue;
        else{
            cout << 0;
            return 0;
        }
    }
    cout << 1;
}