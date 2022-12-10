#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int scc[10010];
vector<vector<int>> graph;
vector<vector<int>> grapht;
vector<bool> visited;
stack<int> p;

void dfs(int x) {
    visited[x] = true;
    for (int next: graph[x]) {
        if (!visited[next])
            dfs(next);
    }
    p.push(x);
}

void dfs2(int k, int x) {

    visited[x] = true;
    scc[x] = k;
    for (int next: grapht[x]) {
        if (!visited[next])
            dfs2(k, next);
    }
}

int main() {
    int v, e;
    int s = 0;
    cin >> v >> e;
    graph.assign(v + 1, vector<int>(0, 0));
    grapht.assign(v + 1, vector<int>(0, 0));
    visited.assign(v + 1, false);
    for (int i = 0; i < e; i++) {
        int start, end;
        cin >> start >> end;
        graph[start].emplace_back(end);
        grapht[end].emplace_back(start);
    }

    for (int i = 1; i <= v; i++) {
        if (!visited[i])
            dfs(i);
    }

    visited.assign(v + 1, false);

    while (!p.empty()) {
        int c = p.top();
        p.pop();
        if (visited[c])
            continue;

        dfs2(++s, c);
    }

    cout << s << endl;
    for (int i = 1; i <= v; i++) {
        if (scc[i] == -1)
            continue;
        cout << i << " ";
        for (int j = i + 1; j <= v; j++) {
            if (scc[j] == scc[i]) {
                cout << j << " ";
                scc[j] = -1;
            }
        }
        cout << -1 << endl;
    }
    return 0;
}