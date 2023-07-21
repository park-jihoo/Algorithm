#include <iostream>
#include <vector>

using namespace std;

#define INF 1000000

int d[101][101];

int main() {
  int n, m;
  cin >> n >> m;

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      if (i == j)
        d[i][j] = 0;
      else
        d[i][j] = INF;
    }
  }

  for (int i = 0; i < m; i++) {
    int start, end;
    cin >> start >> end;
    d[start][end] = 1;
    d[end][start] = 1;
  }

  for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
      }
    }
  }

  int minimum = INF;
  int answer = 0;

  for (int i = 1; i <= n; i++) {
    int sum = 0;
    for (int j = 1; j <= n; j++) {
      sum += d[i][j];
    }
    if (minimum > sum) {
      minimum = sum;
      answer = i;
    }
  }

  cout << answer << endl;

  // Floyd-Warshall
  return 0;
}