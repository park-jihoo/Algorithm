#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> citations) {
  int answer = 0;
  sort(citations.begin(), citations.end());
  for (answer = 0; answer < citations.size(); answer++) {
    if (citations[citations.size() - answer] < answer)
      return answer - 1;
  }
}