#include <iostream>
#include <vector>
#include <queue>
#include <list>

#define INF 10000000

using namespace std;

int main() {
    //Minimum Spanning Tree
    int n, m;
    cin >> n;
    cin >> m;

    vector<vector<pair<int, int>>> adj(n + 1, vector<pair<int, int>>());
    for (int i = 0; i < m; i++) {
        int start, end, weight;
        cin >> start >> end >> weight;
        adj[start].emplace_back(weight, end);
        adj[end].emplace_back(weight, start);
    }
    //prim's algorithm(start:1)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    int s = 1;
    vector<int> key(n + 1, INF);
    vector<bool> visited(n + 1, false);
    vector<int> parent(n + 1, -1);
    pq.emplace(0, s);
    key[s] = 0;
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();
        if (visited[u]) {
            continue;
        }
        visited[u] = true;

        for (auto a: adj[u]) {

            int v = a.second;
            int weight = a.first;
            if (!visited[v] && key[v] > weight) {
                key[v] = weight;
                pq.emplace(key[v], v);
                parent[v] = u;
            }
        }
    }
    int answer = 0;
    for (int i = 2; i <= n; i++) {
        answer += key[i];
    }

    cout << answer << endl;

    return 0;

    //prim's algorithm
}