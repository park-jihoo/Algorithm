#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> dna;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        dna.push_back(s);
    }

    int h = 0;
    string answer = "";

    for(int i=0;i<m;i++){
        int a=0,c=0,g=0,t=0;
        for(int j=0;j<n;j++){
            if(dna[j][i]=='A') a++;
            else if(dna[j][i]=='C') c++;
            else if(dna[j][i]=='G') g++;
            else if(dna[j][i]=='T') t++;
        }
        int max = a;
        if (c > max) max = c;
        if (g > max) max = g;
        if (t > max) max = t;

        if(max==a) answer += 'A';
        else if(max==c) answer += 'C';
        else if(max==g) answer += 'G';
        else if(max==t) answer += 'T';
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(dna[i][j]!=answer[j]) h++;
        }
    }

    cout << answer << endl;
    cout << h << endl;
    return 0;
}