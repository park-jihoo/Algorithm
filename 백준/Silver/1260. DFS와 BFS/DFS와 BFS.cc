#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> dfs(const map<int, vector<int>>& board, int v) {
    vector<int> visited, need_visited;
    need_visited.push_back(v);
    while (!need_visited.empty()) {
        int node = need_visited.back();
        need_visited.pop_back();
        if (find(visited.begin(), visited.end(), node) == visited.end()) {
            visited.push_back(node);
            if (board.count(node)) {
                vector<int> neighbors = board.at(node);
                sort(neighbors.rbegin(), neighbors.rend());
                need_visited.insert(need_visited.end(), neighbors.begin(), neighbors.end());
            }
        }
    }
    return visited;
}

vector<int> bfs(const map<int, vector<int>>& board, int v) {
    vector<int> visited, need_visited;
    need_visited.push_back(v);
    while (!need_visited.empty()) {
        int node = need_visited.front();
        need_visited.erase(need_visited.begin());
        if (find(visited.begin(), visited.end(), node) == visited.end()) {
            visited.push_back(node);
            if (board.count(node)) {
                vector<int> neighbors = board.at(node);
                sort(neighbors.begin(), neighbors.end());
                need_visited.insert(need_visited.end(), neighbors.begin(), neighbors.end());
            }
        }
    }
    return visited;
}

int main() {
    int n, m, v;
    cin >> n >> m >> v;

    map<int, vector<int>> board;

    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        board[x].push_back(y);
        board[y].push_back(x);
    }

    vector<int> dfsResult = dfs(board, v);
    vector<int> bfsResult = bfs(board, v);

    for (int i : dfsResult) {
        cout << i << " ";
    }
    cout << endl;

    for (int i : bfsResult) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}