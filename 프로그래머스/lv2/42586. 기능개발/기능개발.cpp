// 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어,
// 과거의 코드는 동작하지 않을 수 있습니다. 새로운 함수 구성을 적용하려면 [코드
// 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는
// 사라집니다.
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
  vector<int> finish;
  vector<int> answer;
  for (int i = 0; i < progresses.size(); i++) {
    int left = 100 - progresses[i];
    if (left % speeds[i] == 0)
      finish.push_back(left / speeds[i]);
    else
      finish.push_back(left / speeds[i] + 1);
    if (finish[i] < finish[i - 1])
      finish[i] = finish[i - 1];
  }
  answer.push_back(1);
  for (int i = 1; i < finish.size(); i++) {
    if (finish[i] == finish[i - 1])
      answer[answer.size() - 1] = answer[answer.size() - 1] + 1;
    else
      answer.push_back(1);
  }
  return answer;
}