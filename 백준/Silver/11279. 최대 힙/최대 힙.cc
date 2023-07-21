#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int n, x;
  scanf("%d", &n);
  vector<int> result;
  priority_queue<int> pq;
  for (int i = 0; i < n; i++) {
    scanf("%d", &x);
    if (x == 0) {
      if (pq.empty()) {
        result.push_back(0);
      } else {
        result.push_back(pq.top());
        pq.pop();
      }
    } else {
      pq.push(x);
    }
  }

  for (int i : result) {
    printf("%d\n", i);
  }
}