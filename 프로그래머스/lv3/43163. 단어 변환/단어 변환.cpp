#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
bool visited[50];
string mybeg, mytar;
int answer=100;
bool com(string a, string b){
    int cnt=0;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i])cnt++;
        if(cnt==2)return false;
    }
    if(cnt==1)return true;
    return false;
}
void dfs(string begin, string target, vector<string>words, int cnt){
    if(begin==target){
        if(answer>cnt)
            answer=cnt;
        return;
    }
    for(int i=0;i<words.size();i++){
        if(!visited[i] && com(begin, words[i])){
            visited[i]=true;
            dfs(words[i],target, words, cnt+1);
            visited[i]=false;
        }
    }
}
int solution(string begin, string target, vector<string> words) {
    mybeg=begin;
    mytar=target;
    bool existence=false;
    for(int i=0;i<words.size();i++){
        if(target==words[i]) existence=true;
    }
    if(!existence) return 0;
    dfs(begin, target, words, 0);
    return answer;
}