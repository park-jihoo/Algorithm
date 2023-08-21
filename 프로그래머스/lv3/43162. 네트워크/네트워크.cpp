#include <string>
#include <vector>
using namespace std;
bool visited[200]={0, };
void dfs(int x, vector<vector<int>>computers){
    for(int i=0;i<computers.size();i++){
        if(computers[i][x] && !visited[i]){
            visited[i]=true;
            dfs(i, computers);
        }
    }
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for(int i=0;i<n;i++){
        if(!visited[i]){
            visited[i]=true;
            dfs(i, computers);
            answer++;
        }
    }
    return answer;
}