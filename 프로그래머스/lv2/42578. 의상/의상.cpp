#include <map>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<string>> clothes) {
  int answer = 1;
  map<string, int> cases;
  map<string, int>::iterator p;
  for (int i = 0; i < clothes.size(); i++) {
    if (cases.find(clothes[i][1]) == cases.end())
      cases[clothes[i][1]] = 1;
    else
      cases[clothes[i][1]]++;
  }
  for (p = cases.begin(); p != cases.end(); p++) {
    answer = answer * (p->second + 1);
  }
  answer = answer - 1;
  return answer;
}