#include <iostream>

using namespace std;

int n;
int ans;
int board[15];

bool check(int cdx) {
  for (int i = 0; i < cdx; i++) {
    if (board[i] == board[cdx] || abs(board[i] - board[cdx]) == cdx - i)
      return false;
  }
  return true;
}

void nQueen(int cdx) {
  if (cdx == n) {
    ans++;
    return;
  }
  for (int i = 0; i < n; i++) {
    board[cdx] = i;
    if (check(cdx))
      nQueen(cdx + 1);
  }
}

int main() {
  cin >> n;
  nQueen(0);
  cout << ans << endl;
}