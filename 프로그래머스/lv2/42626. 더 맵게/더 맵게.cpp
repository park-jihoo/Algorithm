#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

int solution(vector<int> scoville, int K) {
  int answer = 0;
  priority_queue<int, vector<int>, greater<int>> scovilleq;
  for (int i = 0; i < scoville.size(); i++)
    scovilleq.push(scoville[i]);
  while (scovilleq.top() < K) {
    int a, b;
    if (scovilleq.size() == 1)
      return -1;
    a = scovilleq.top();
    scovilleq.pop();
    b = scovilleq.top();
    scovilleq.pop();
    scovilleq.push(a + b * 2);
    answer++;
  }
  return answer;
}