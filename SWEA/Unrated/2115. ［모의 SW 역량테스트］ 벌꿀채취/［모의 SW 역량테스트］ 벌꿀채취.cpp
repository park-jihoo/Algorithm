
#include <cstdio>
#include <iostream>
using namespace std;
int N, M, C, res;
int honey[10][10];
int max(int a, int b) {
  if (a >= b) {
    return a;
  } else {
    return b;
  }
}
void getmaxprice(int x, int y, int cnt, int sum, int price) {
  if (sum > C)
    return;
  res = max(res, price);
  if (cnt == M)
    return;
  getmaxprice(x, y + 1, cnt + 1, sum + honey[x][y],
              price + honey[x][y] * honey[x][y]);
  getmaxprice(x, y + 1, cnt + 1, sum, price);
}
int solve(int x, int y) {
  res = 0;
  getmaxprice(x, y, 0, 0, 0);
  int priceA = res;
  int priceB = 0;
  int j = y + M;
  for (int i = x; i < N; i++, j = 0) {
    for (; j < N - M + 1; j++) {
      res = 0;
      getmaxprice(i, j, 0, 0, 0);
      priceB = max(res, priceB);
    }
  }
  return priceA + priceB;
}
int main(int argc, char **argv) {
  int test_case;
  int T;
  cin >> T;
  for (test_case = 1; test_case <= T; ++test_case) {
    int maxprice = 0;
    cin >> N;
    cin >> M;
    cin >> C;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cin >> honey[i][j];
      }
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N - M + 1; j++) {
        maxprice = max(solve(i, j), maxprice);
      }
    }
    printf("#%d %d\n", test_case, maxprice);
  }
  return 0; //정상종료시 반드시 0을 리턴해야합니다.
}