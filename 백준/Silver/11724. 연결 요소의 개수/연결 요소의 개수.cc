#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<bool> visited;

void dfs(int x) {
  visited[x] = true;
  for (int next : graph[x]) {
    if (!visited[next])
      dfs(next);
  }
}

int main() {
  int v, e;
  int s = 0;
  cin >> v >> e;
  graph.assign(v + 1, vector<int>(0, 0));
  visited.assign(v + 1, false);
  for (int i = 0; i < e; i++) {
    int start, end;
    cin >> start >> end;
    graph[start].emplace_back(end);
    graph[end].emplace_back(start);
  }

  for (int i = 1; i <= v; i++) {
    if (!visited[i]) {
      dfs(i);
      s++;
    }
  }

  cout << s << endl;
  return 0;
}