#include <cstdio>
int N, M, H, mincnt = 999999;
int D[31][11];
bool isladder() {
  for (int i = 1, pos; i <= N; i++) {
    pos = i;
    for (int j = 1; j <= H; j++) {
      if (D[j][pos] == 1)
        pos++;
      else if (D[j][pos - 1] == 1)
        pos--;
    }
    if (i != pos)
      return false;
  }
  return true;
}
void func(int cnt, int x, int y) {
  if (cnt >= mincnt)
    return;
  if (isladder()) {
    mincnt = cnt;
    return;
  }
  if (cnt == 3)
    return;
  for (int i = y; i <= H; i++, x = 1)
    for (int j = x; j < N; j++) {
      if (D[i][j]) {
        j++;
        continue;
      }
      D[i][j] = 1;
      func(cnt + 1, j + 2, i);
      D[i][j] = 0;
    }
}
int main() {
  scanf("%d %d %d", &N, &M, &H);
  for (int i = 0, a, b; i < M; i++) {
    scanf("%d %d", &a, &b);
    D[a][b] = 1;
  }
  func(0, 1, 1);
  if (mincnt > 3) {
    printf("-1");
  } else {
    printf("%d", mincnt);
  }
  return 0;
}