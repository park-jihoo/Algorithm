#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string a, b;
  cin >> a;
  cin >> b;
  int m = a.size();
  int n = b.size();
  vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
  for (int i = 1; i < m + 1; i++) {
    for (int j = 1; j < n + 1; j++) {
      if (a[i - 1] == b[j - 1])
        dp[i][j] = dp[i - 1][j - 1] + 1;
      else if (dp[i][j - 1] > dp[i - 1][j])
        dp[i][j] = dp[i][j - 1];
      else
        dp[i][j] = dp[i - 1][j];
    }
  }

  cout << dp[m][n] << endl;
}