class Solution {
public:
  vector<int> spiralOrder(vector<vector<int>> &matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    vector<int> answer = vector<int>();
    pair<int, int> now = {0, 0};
    int nowd = 0;
    vector<pair<int, int>> d = vector<pair<int, int>>();
    d.emplace_back(0, 1);
    d.emplace_back(1, 0);
    d.emplace_back(0, -1);
    d.emplace_back(-1, 0);
    vector<vector<bool>> visited(m, vector<bool>(n, false));

    for (int i = 0; i < m * n; i++) {
      answer.push_back(matrix[now.first][now.second]);
      visited[now.first][now.second] = true;
      int next1 = now.first + d[nowd].first;
      int next2 = now.second + d[nowd].second;
      if (!(0 <= next1 && next1 < m) || !(0 <= next2 && next2 < n)) {
        nowd = (nowd + 1) % 4;
      } else if (visited[next1][next2]) {
        nowd = (nowd + 1) % 4;
      }
      now.first += d[nowd].first;
      now.second += d[nowd].second;
    }
    return answer;
  }
};