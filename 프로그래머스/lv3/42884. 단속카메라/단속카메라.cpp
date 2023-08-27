#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    sort(routes.begin(), routes.end());
    int cPosition=routes[0][1];
    for(int i=1;i<routes.size();i++){
     if(routes[i][1]<cPosition)
         cPosition=routes[i][1];
        if(routes[i][0]>cPosition){
            answer++;
            cPosition=routes[i][1];
        }
    }
    return answer;
}