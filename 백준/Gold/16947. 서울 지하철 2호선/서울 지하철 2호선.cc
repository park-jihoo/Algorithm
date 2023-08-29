#include <cstring>
#include <iostream>
#include <queue>
#include <vector>
#define MAX 3001

using namespace std;

int n;
bool cycle[MAX];
vector<int> graph[MAX];
bool visited[MAX];
int pre[MAX];
bool hasCycle;
int dist[MAX];

void dfs(int start) {
  visited[start] = true;
  for (int next : graph[start]) {
    if (hasCycle)
      return;
    if (visited[next]) {
      if (pre[start] != next) {
        hasCycle = true;
        cycle[start] = true;
        while (start != next) {
          cycle[pre[start]] = true;
          start = pre[start];
        }
        return;
      }
    } else {
      pre[next] = start;
      dfs(next);
    }
  }
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int start, end;
    cin >> start >> end;
    graph[start].push_back(end);
    graph[end].push_back(start);
  }

  // find cycle with dfs
  dfs(1);

  // find distance with bfs
  memset(visited, false, sizeof(visited));
  queue<pair<int, int>> q;
  for (int i = 1; i <= n; i++) {
    if (cycle[i]) {
      q.push(make_pair(i, 0));
      visited[i] = true;
    }
  }
  while (!q.empty()) {
    int cur = q.front().first;
    int curDist = q.front().second;
    q.pop();
    dist[cur] = curDist;
    for (int next : graph[cur]) {
      if (!visited[next]) {
        visited[next] = true;
        q.push(make_pair(next, curDist + 1));
      }
    }
  }

  for (int i = 1; i <= n; i++) {
    cout << dist[i] << " ";
  }
}