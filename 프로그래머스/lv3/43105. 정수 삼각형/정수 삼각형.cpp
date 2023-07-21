#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
  int mytri[500][500];
  int answer = 0;
  mytri[0][0] = triangle[0][0];
  for (int i = 1; i < triangle.size(); i++) {
    mytri[i][0] = triangle[i][0] + mytri[i - 1][0];
    for (int j = 1; j < i; j++) {
      mytri[i][j] = max(mytri[i - 1][j], mytri[i - 1][j - 1]) + triangle[i][j];
    }
    mytri[i][i] = triangle[i][i] + mytri[i - 1][i - 1];
  }
  for (int i = 0; i < triangle.size(); i++) {
    if (mytri[triangle.size() - 1][i] > answer)
      answer = mytri[triangle.size() - 1][i];
  }
  return answer;
}