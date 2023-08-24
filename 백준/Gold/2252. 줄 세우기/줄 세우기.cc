#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> order;
vector<bool> visited;
vector<int> p;

void dfs(int x) {
  visited[x] = true;
  for (int next : order[x]) {
    if (!visited[next])
      dfs(next);
  }
  p.push_back(x);
}

int main() {
  int n, m;
  cin >> n >> m;
  order.assign(n + 1, vector<int>(0, 0));
  visited.assign(n + 1, false);
  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    order[a].emplace_back(b);
  }

  for (int i = 1; i <= n; i++) {
    if (!visited[i])
      dfs(i);
  }
  for (int i = p.size() - 1; i >= 0; i--) {
    cout << p[i] << " ";
  }
  cout << endl;
}