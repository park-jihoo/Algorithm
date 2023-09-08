class Solution {
public:
  vector<vector<int>> generate(int numRows) {
    vector<vector<int>> answer;
    if (numRows == 0)
      return answer;
    if (numRows == 1) {
      answer.push_back({1});
      return answer;
    }
    answer = generate(numRows - 1);
    vector<int> line(1, 1);
    for (int i = 1; i < numRows - 1; i++) {
      line.push_back(answer[numRows - 2][i] + answer[numRows - 2][i - 1]);
    }
    line.push_back(1);
    answer.push_back(line);
    return answer;
  }
};