#include <iostream>
#include <vector>

using namespace std;
vector<vector<char> > map(100, vector<char>(100, ' '));
vector<vector<bool> > visited(100, vector<bool>(100, false));
vector<vector<bool> > visited_rg(100, vector<bool>(100, false));

bool rg_same(char a, char b){
    if(a == 'R' && b == 'G') return true;
    if(a == 'G' && b == 'R') return true;
    return a == b;
}

void bfs(int i, int j, char color, bool is_rg = false) {
    vector<pair<int, int> > need_visit;
    need_visit.push_back(make_pair(i, j));
    while (!need_visit.empty()) {
        int x = need_visit.back().first;
        int y = need_visit.back().second;
        need_visit.pop_back();
        if (!is_rg && !visited[x][y]) {
            visited[x][y] = true;
                if (x - 1 >= 0 && map[x - 1][y] == color) {
                    need_visit.push_back(make_pair(x - 1, y));
                }
                if (x + 1 < map.size() && map[x + 1][y] == color) {
                    need_visit.push_back(make_pair(x + 1, y));
                }
                if (y - 1 >= 0 && map[x][y - 1] == color) {
                    need_visit.push_back(make_pair(x, y - 1));
                }
                if (y + 1 < map.size() && map[x][y + 1] == color) {
                    need_visit.push_back(make_pair(x, y + 1));
                }
        }else if(is_rg && !visited_rg[x][y]){
            visited_rg[x][y] = true;
                if (x - 1 >= 0 && rg_same(map[x - 1][y], color)) {
                    need_visit.push_back(make_pair(x - 1, y));
                }
                if (x + 1 < map.size() && rg_same(map[x + 1][y], color)) {
                    need_visit.push_back(make_pair(x + 1, y));
                }
                if (y - 1 >= 0 && rg_same(map[x][y - 1], color)) {
                    need_visit.push_back(make_pair(x, y - 1));
                }
                if (y + 1 < map.size() && rg_same(map[x][y + 1], color)) {
                    need_visit.push_back(make_pair(x, y + 1));
                }
        }
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            map[i][j] = s[j];
        }
    }

    int normal, rg;
    normal = rg = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j]) {
                normal++;
                bfs(i, j, map[i][j]);
            }
            if (!visited_rg[i][j]) {
                rg++;
                bfs(i, j, map[i][j], true);
            }
        }
    }

    cout << normal << " " << rg << endl;
}