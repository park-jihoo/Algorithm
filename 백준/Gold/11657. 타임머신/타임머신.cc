#include <iostream>
#include <vector>

using namespace std;
#define INF 10000000

long long dist[INF];

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> edges;
  // Initialize-Single-Sources
  for (int i = 1; i <= n; i++) {
    dist[i] = INF;
  }

  for (int i = 0; i < m; i++) {
    int from, to, time;
    cin >> from >> to >> time;
    vector<int> edge = {from, to, time};
    edges.push_back(edge);
  }

  dist[1] = 0;

  // Relaxation
  for (int i = 1; i <= n - 1; i++) {
    for (auto &edge : edges) {
      int from = edge[0];
      int to = edge[1];
      int cost = edge[2];
      if (dist[from] == INF)
        continue;
      if (dist[to] > dist[from] + cost)
        dist[to] = dist[from] + cost;
    }
  }

  // for edge in G.E
  for (auto edge : edges) {
    int from = edge[0];
    int to = edge[1];
    int cost = edge[2];
    if (dist[from] == INF)
      continue;
    if (dist[to] > dist[from] + cost) {
      cout << -1 << endl;
      return 0;
    }
  }

  for (int i = 2; i <= n; i++) {
    if (dist[i] == INF)
      cout << -1 << endl;
    else
      cout << dist[i] << endl;
  }
}