#include <iostream>

using namespace std;

int main() {
  int n;
  cin >> n;
  int min = 1000001;
  int max = -10000001;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    if (x > max) {
      max = x;
    }
    if (x < min) {
      min = x;
    }
  }

  cout << min << " " << max << endl;
}