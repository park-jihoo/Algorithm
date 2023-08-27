#include <iostream>
using namespace std;
int main(void) {
  int x, l = 1, a = 1, b = 1;
  cin >> x;
  while (true) {
    if (x <= l * (l + 1) / 2)
      break;
    else
      l++;
  }
  b = x - l * (l - 1) / 2;
  a = l - b + 1;
  if (l % 2 == 0) {
    int temp = a;
    a = b;
    b = temp;
  }
  cout << a << "/" << b;
}
