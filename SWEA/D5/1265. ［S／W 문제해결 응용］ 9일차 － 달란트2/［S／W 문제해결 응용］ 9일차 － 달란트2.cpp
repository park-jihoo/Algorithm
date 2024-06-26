#include <iostream>
using namespace std;

int main(int argc, char **argv) {
  int test_case;
  int T;

  cin >> T;

  for (test_case = 1; test_case <= T; ++test_case) {
    int amount, num;
    long long ans = 1;
    cin >> amount;
    cin >> num;
    for (int i = 0; i < num; i++) {
      if (i < amount % num)
        ans = ans * (amount / num + 1);
      else
        ans = ans * (amount / num);
    }
    cout << "#" << test_case << " " << ans << endl;
  }
  return 0; //정상종료시 반드시 0을 리턴해야합니다.
}