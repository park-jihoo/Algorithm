#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> v;
  for (int i = 0; i < n; i++) {
    int val;
    cin >> val;
    v.push_back(val);
  }

  // bubble sort
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (v[j] > v[j + 1]) {
        int tmp = v[j];
        v[j] = v[j + 1];
        v[j + 1] = tmp;
      }
    }
  }

  for (int i = 0; i < n; i++) {
    cout << v[i] << endl;
  }
}