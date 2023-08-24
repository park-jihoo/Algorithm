#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int V, E;
  cin >> V >> E;

  vector<bool> visited(V + 1, false);
  vector<vector<pair<int, int>>> Elist(V + 1);
  priority_queue<pair<int, int>, vector<pair<int, int>>,
                 greater<pair<int, int>>>
      heap;
  heap.push(make_pair(0, 1));

  for (int i = 0; i < E; ++i) {
    int s, e, w;
    cin >> s >> e >> w;
    Elist[s].emplace_back(w, e);
    Elist[e].emplace_back(w, s);
  }

  int answer = 0, cnt = 0;

  while (!heap.empty()) {
    if (cnt == V) {
      break;
    }
    int w = heap.top().first;
    int s = heap.top().second;
    heap.pop();
    if (!visited[s]) {
      visited[s] = true;
      answer += w;
      ++cnt;
      for (const auto &i : Elist[s]) {
        heap.push(i);
      }
    }
  }

  cout << answer << endl;

  return 0;
}