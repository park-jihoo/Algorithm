#include <cstdio>
#include <iostream>
using namespace std;

int n;
int f(int n) {
  if (n == 1)
    return 1;
  if (n == 0)
    return 0;
  else
    return f(n - 1) + f(n - 2);
}
int main() {
  cin >> n;
  cout << f(n);
  return 0;
}