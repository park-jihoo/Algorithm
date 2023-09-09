#include <iostream>
#include <string>

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;
  int ans = b.length();
  for (int i = 0; i <= b.length() - a.length(); i++) {
    int cnt = 0;
    for (int j = 0; j < a.length(); j++) {
      if (a[j] != b[i + j])
        cnt++;
    }
    if (ans > cnt)
      ans = cnt;
  }

  cout << ans << endl;
  return 0;
}