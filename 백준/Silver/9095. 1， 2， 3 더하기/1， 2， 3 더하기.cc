#include <iostream>
#include <vector>
using namespace std;
int main(void) {
  int T, cnt;
  cin >> T;
  vector<int> ans;
  int ways[11];
  for (int i = 0; i < T; i++) {
    int num;
    cin >> num;
    ans.push_back(num);
  }
  ways[0] = 1;
  ways[1] = 2;
  ways[2] = 4;
  for (int i = 3; i < 11; i++) {
    ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3];
  }
  for (int i = 0; i < T; i++) {
    cout << ways[ans[i] - 1] << endl;
  }
}