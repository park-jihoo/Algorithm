#include <string>
#include <vector>
#include <queue>
using namespace std;
bool visited[20001];
int dist[20001];
int d[20001][20001];
int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    int max = 0;
    for(int i=0;i<edge.size();i++){
        d[edge[i][0]][edge[i][1]]=1;
        d[edge[i][1]][edge[i][0]]=1;
    }
    queue<int>q;
    q.push(1);
    visited[1]=true;
    dist[1]=0;
    while(!q.empty()){
        int temp=q.front();
        q.pop();
        for(int i=2;i<=n;i++){
            if(d[temp][i]==1 && !visited[i]){
                dist[i]=dist[temp]+1;
                q.push(i);
                visited[i]=true;
                if(max<dist[i])
                    max=dist[i];
            }
        }
    }
    for(int i=1;i<=n;i++){
        if(dist[i]==max)
            answer++;
    }
    return answer;
}