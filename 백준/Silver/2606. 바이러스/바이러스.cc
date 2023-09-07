#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, m;
  cin >> n;
  cin >> m;

  vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));
  vector<bool> visited(n + 1, false);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    graph[a][b] = 1;
    graph[b][a] = 1;
  }

  int cnt = 0;
  vector<int> q;
  q.push_back(1);
  visited[1] = true;
  while (!q.empty()) {
    int cur = q.front();
    q.erase(q.begin());
    for (int i = 1; i <= n; i++) {
      if (graph[cur][i] == 1 && !visited[i]) {
        q.push_back(i);
        visited[i] = true;
        cnt++;
      }
    }
  }

  cout << cnt << endl;
}