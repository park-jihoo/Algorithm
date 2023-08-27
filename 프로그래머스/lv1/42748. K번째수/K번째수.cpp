#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
  vector<int> answer;
  for (int i = 0; i < commands.size(); i++) {
    vector<int> newarr;
    for (int j = commands[i][0]; j <= commands[i][1]; j++) {
      newarr.push_back(array[j - 1]);
    }
    sort(newarr.begin(), newarr.end());
    answer.push_back(newarr[commands[i][2] - 1]);
  }
  return answer;
}